# import the necessary packages
import argparse
import cv2

# contruct the arugment parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="adrian.png", help="path to the input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
print(dir(image), type(image))  # type - numpy.ndarray
# noinspection PyUnresolvedReferences
print(image.shape)  # (450, 600, 3)
h,w = image.shape[:2]

print(f"Height : {h}, Width : {w}")
cv2.imshow("Original", image)
cv2.waitKey(0)

# images are simply Numpy arrays --with the origin (0, 0) located at
# the top-lefft of the image
(b, g, r) = image[0,0]
print(f"b -> {b}, g -> {g}, r-> {r}")

(b, g, r) = image[7,5]
print(f"b -> {b}, g -> {g}, r-> {r}")

# access the pixel located at x=50, y=20
(b, g, r) = image[20, 50]
print(f"Pixel at (50, 20) - Red : {r}, Green : {g}, Blue : {b}")

# update the pixel at (50, 20) and set it to red
image[20, 50] = (0, 0, 255)

cv2.imshow("Modified", image)
cv2.waitKey(0)

# Compute Getting and Setting Pixels
# divided by two
(cX, cY) = (w // 2, h //2)
print(f"cX => {cX}, cY => {cY}")

# since we are using Numpy arrays, we can apply array slicing to grab
# large chunks/regions of interest from the image -- here we grab the
# top-left corner of the image
t1 = image[0:cY, 0:cX]
cv2.imshow("Top-Left Corner Cropped Image", t1)
cv2.waitKey(0)

# In a similiar fashion, we can crop the top-right , bottom-right , and
# bottom-left corners of the image and then displayed them to our
# screen
top_right = image[0:cY, cX: w]
btm_right = image[cY:h, cX: w]
btm_left = image[cY:h, 0:cX]

cv2.imshow("Top-Right Corner", top_right)
cv2.waitKey(0)
cv2.imshow("Bottom-Right Corner", btm_right)
cv2.waitKey(0)
cv2.imshow("Bottom-Left Corner", btm_left)
cv2.waitKey(0)

# set the top-left corner of the original image ot be green
image[0:cY, 0:cX] = (0, 255, 0)

# Show our updated image
cv2.imshow("UPdate", image)
cv2.waitKey(0)

# Croppend Image
cv2.imshow("Cropped Image", image[cY: h, cX : w])
cv2.waitKey(0)

