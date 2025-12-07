# Vision_Assignment
Q1)
cv2.waitKey(0)
Waits forever for a key press. 
Used for static images.

cv2.waitKey(1)
Waits 1 millisecond.
Used for video frames so they keep updating.

Q2)
img_bgr = cv2.imread("image.jpg")
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

Q3)
import cv2
img = cv2.imread("image.jpg")
choice = input("Choose transformation (darken/lighten/invert): ").lower()
if choice == "darken":
    result = cv2.subtract(img, 50)
elif choice == "lighten":
    result = cv2.add(img, 50)
elif choice == "invert":
    result = 255 - img
else:
    print("Invalid choice")
    exit()
cv2.imshow("Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()

Q4)
import cv2
import numpy as np

img = cv2.imread("image.jpg", 0)  # grayscale

low = 150
high = 200

result = img.copy()
mask = cv2.inRange(img, low, high)

result[mask > 0] = 255

cv2.imshow("Selective Threshold", result)
cv2.waitKey(0)
cv2.destroyAllWindows()

Q5)
import cv2
import numpy as np

img = cv2.imread("image.jpg")

kernel = np.array([
    [0, -1, 0],
    [-1,  5, -1],
    [0, -1, 0]
])

filtered = cv2.filter2D(img, -1, kernel)

cv2.imshow("Filtered", filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()

Q6)
import cv2

img = cv2.imread("image.jpg", 0)

gauss1 = cv2.GaussianBlur(img, (5, 5), 1)
gauss2 = cv2.GaussianBlur(img, (5, 5), 2)

dog = gauss1 - gauss2

cv2.imshow("DoG", dog)
cv2.waitKey(0)
cv2.destroyAllWindows()

