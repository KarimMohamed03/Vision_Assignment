import cv2
import numpy as np

# Start webcam
cap = cv2.VideoCapture(0)

# Default smoothing sigma
sigma = 1

print("[INFO] Controls:")
print("o = original frame")
print("x = Sobel X")
print("y = Sobel Y")
print("m = Sobel magnitude")
print("s = Sobel + threshold (bonus)")
print("l = Laplacian of Gaussian (LoG)")
print("+ / - = increase or decrease sigma")
print("q = quit")

mode = 'o'   # start with original

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur with sigma
    ksize = int(6 * sigma + 1)
    if ksize % 2 == 0:
        ksize += 1   # must be odd

    blurred = cv2.GaussianBlur(gray, (ksize, ksize), sigma)

    # Apply selected mode
    if mode == 'o':
        output = frame

    elif mode == 'x':
        sobel_x = cv2.Sobel(blurred, cv2.CV_64F, 1, 0)
        output = cv2.convertScaleAbs(sobel_x)

    elif mode == 'y':
        sobel_y = cv2.Sobel(blurred, cv2.CV_64F, 0, 1)
        output = cv2.convertScaleAbs(sobel_y)

    elif mode == 'm':
        sobel_x = cv2.Sobel(blurred, cv2.CV_64F, 1, 0)
        sobel_y = cv2.Sobel(blurred, cv2.CV_64F, 0, 1)
        magnitude = np.sqrt(sobel_x**2 + sobel_y**2)
        output = cv2.convertScaleAbs(magnitude)

    elif mode == 's':  # Sobel + threshold (Bonus)
        sobel = cv2.Sobel(blurred, cv2.CV_64F, 1, 1)
        sobel_abs = cv2.convertScaleAbs(sobel)
        _, thresholded = cv2.threshold(sobel_abs, 50, 255, cv2.THRESH_BINARY)
        output = thresholded

    elif mode == 'l':  # Laplacian of Gaussian
        log = cv2.Laplacian(blurred, cv2.CV_64F)
        output = cv2.convertScaleAbs(log)

    else:
        output = frame

    cv2.imshow("Webcam Edge Detection", output)

    # Handle key presses
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break
    elif key == ord('o'):
        mode = 'o'
    elif key == ord('x'):
        mode = 'x'
    elif key == ord('y'):
        mode = 'y'
    elif key == ord('m'):
        mode = 'm'
    elif key == ord('s'):
        mode = 's'
    elif key == ord('l'):
        mode = 'l'
    elif key == ord('+'):
        sigma += 0.5
        print("Sigma:", sigma)
    elif key == ord('-') and sigma > 0.5:
        sigma -= 0.5
        print("Sigma:", sigma)

cap.release()
cv2.destroyAllWindows()
