# OpenCV Load Image

In this tutorial , you will learn how to use OpenCV and the `cv2.imread1 fnction to:

1. Load an input iamge from disk
2. Determine the image's width , height and number of channel
3. Display the loaded image to our screen
4. Write the image back out to disk as a different image file type

###  Load image - `cv2.imread`

How do we load images from disk with OpenCV?  We just use the `cv2.imread()` funtion.

The OpenCV `cv2.imread()` function return either of two values:

1. *A Numpy array* representing the image with the shape (`num_rows, num_cols, num_channels`)
2. A `NoneType` object, implying that the image could not be loaded.
3. OpenCV `cv2.imread()` can read a variety of image format, including JPEG TIFF, PNG and GIFF.

### Configuring your development environment

```python
PS C:\PythonProject> pip install opencv-contrib-python
Collecting opencv-contrib-python
  Downloading opencv_contrib_python-4.5.4.60-cp38-cp38-win_amd64.whl (42.0 MB)
     |████████████████████████████████| 42.0 MB 6.4 MB/s
Collecting numpy>=1.17.3
  Downloading numpy-1.21.5-cp38-cp38-win_amd64.whl (14.0 MB)
     |████████████████████████████████| 14.0 MB 6.8 MB/s
Installing collected packages: numpy, opencv-contrib-python
Successfully installed numpy-1.21.5 opencv-contrib-python-4.5.4.60
PS C:\PythonProject>
```

If you need help configuring your development environment for OpenCV 4.3+1. We highly recommend that you read [OpenCV Install Guide](https://www.pyimagesearch.com/2018/09/19/pip-install-opencv/)

The `argparse` package allows us to pass dynamic arguments to our Python script such that we do not have to hardcore parameter variables that need to be *manually changed every time* we'd like to alter their values.

If you are unfamiliar with how the `argparse` package workds, be sure to [Adrian PyImagesearch](https://www.pyimagesearch.com/2018/03/12/python-argparse-command-line-arguments/)

```python
# import the necessary package
import argparse
import cv2

# construct the argument parse and parse the arguments

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image")
ap.add_
args = vars(ap.parse_args())

# Load the image from dksl via "cv2.imread" and then grab the spatial
# dimensions, including width, heights, and number of channels.

image = cv2.imread(args["image"])
(height, width, channel) = image.shape[:3]

# display the image width, heights, and number of channels to
# our terminal
print(f"width : {width}, height : {height}, channel : {channel}")

# Show the image and wait for a keypres
cv2.imshow("LoadImage", image)  #Window name, image
cv2.waitKey(0)

# save the image back to disk(OpenCv handles converting image
# filetypes automatically.
cv2.imwrite("newimage", image)
```

Keep in mind that the number of channels will be for the three color images, representing the red, green and blue components of pixel colors.

Run this undel console the following:

```python
>>>PS C:\PythonProject\openCV\opencv-load-image> python .\load_image_opencv.py --image .\jurassic_park.png
width : 577, height : 433, channel : 3

```

If we request the image file which does not exist on your disk, what if?

```python
>>> python .\load_image_opencv.py --image .\sangseo.png
Traceback (most recent call last):
  File ".\load_image_opencv.py", line 10, in <module>
    ap.add_argument("-o", "--image")
raise ArgumentError(action, message % conflict_string)
argparse.ArgumentError: argument -o/--image: conflicting option string: --image
```

### Summary

In this tutorial , you learned how to load images using OpenCV and the `cv2.imread` function.

We created a Python script to:

1. Load an image from disk as a Numpy array using the `cv2.imread` function
2. Display the image on screen with `cv2.imshow`
3. Save the image back to disk with `cv2.imwrite`

OpenCV conveniently handles reading and writing a wide variety of image file formats (e.g., JPG, PNG, TIFF). The library also simplifies displaying an image on screen and allowing user interaction with the opened windows.

If an image cannot be read by OpenCV, you should carefully check if the input filename was given correctly, as the `cv2.imread` function returns a `NoneType` Python object upon failure. The function will fail if the file does not exist o if the image format is unsupported by OpenCV.

We have also printed the imade dimension to the terminal (width, height, and number of channels), based on the values of the underlying Numpy array shape.

OpenCV save the image to disk using the JPG format, taking advantage of OpenCV's ability to automatically convert the image to the desired file type.