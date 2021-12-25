# import the necessary package
import argparse
import cv2


# construct the argument parse and parse the arguments

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image")
args = vars(ap.parse_args())


# Load the image from dksl via "cv2.imread" and then grab the spatial
# dimensions, including width, heights, and number of channels.

image = cv2.imread(args["image"])


(height, width, channel) = image.shape[:3]

# display the image width, heights, and number of channels to
# our terminal
print(f"width : {width}, height : {height}, channel : {channel}")

# Show the image and wait for a keypres
cv2.imshow("LoadImage", image)
cv2.waitKey(0)

# save the image back to disk(OpenCv handles converting image
# filetypes automatically.

cv2.imwrite("newimage", image)