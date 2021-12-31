# OpenCV Getting and Setting Pixels

You will also learn:

* What pixels are
* How the image coordinate system works in OpenCV
* How to access / get individual pixel values in an image
* How to set/Update pixels in an image
* How to use array slicing to grab regions of an image

In the first part of this tutorial, you will discover what pixels are(i.e., the building ).

We'll also review the image coodinate system in OpenCV, including the proper notation to access individual pixel values.



### What are pixels?

Pixels are the raw building blocks of an image. Every image consists of a set of pixels.

There is no finer granularity than the pixcel.

Normally, a pixel is considered the "color" or the "intensity" of light that appears in a given place in our image.

If we think of an image as a grid, each square in the grid contains a single pixel. 

Let's look at the example image in Figure1:

![adrian](https://user-images.githubusercontent.com/70785000/147831980-5f968b9a-0244-4783-a18c-3a3de3ef30ab.png)

> This image is 600 pixels wide and 450 pixel tall for a total 600 * 450 = 270,000 pixels.

Most pixels are represented in two ways:

1. Grayscale/sing channel
2. Color

In a grayscale image, each pixel has a value between 0 and 255, where o corresponds to "black" and 255 being "white". The values between 0 and 255 are varying shades of gray, where values closer to 0 are darker and values closer 255 are lighter:

![opencv_getting_setting_gradient](https://user-images.githubusercontent.com/70785000/147832133-3694c250-d791-4bed-9b98-fa9f2f80df89.png)

The grayscale gradient image in **Figure 2** demonstrates *darker pixels* on the left -hand side and progressively *lighter pixels* on the right-hand side.

Color pixels, however, are normally represented in the RGB color space - one value for the Red component, one for Green, and one for Blue leading to a total of *3 values per pixel*:

![](https://929687.smushcdn.com/2407837/wp-content/uploads/2020/12/opencv_getting_setting_rgb_cube.png?lossy=1&strip=1&webp=1)

Other color spaces exist (HSV(Hue, Saturation, Value)), but let's start with the basic and move our way up from there.

Each of the three Red, Green, and Blue colors are represented by an integer in the rnage from 0 to 255, which indicates how "much" of the color there is. 

Given that the pixel value only needs to be in the range [0, 255], we normally use an 8-bit unsigned integer to represent each color intensity.

We then combine these values into an RGB tuple in the form(red, green, blue). 

This tuple represnets our color.

To construct a white color, we would completely fill each of the red , green, and blue buckets, like this: (**255, 255, 255**) - Since white is the presence of all colors.

Then, to create a black color, we would completely empty each of the bucket:

(**0, 0, 0**) - since black is the absence of color.

To create a pure red color, we would completely fill the red bucket(and only the red bucket): (**255, 0, 0**)

![](https://929687.smushcdn.com/2407837/wp-content/uploads/2020/12/opencv_getting_setting_color_examples.png?lossy=1&strip=1&webp=1)

> Here,we have four examples of colors and the "bucket" amounts for each of the Read, Green, and Blue components, respectively.

In the *top-left* example, we have the color *white* - each of the Red, Green, and Blue buckets have been completely filled to form the white color.

And on the top-right, we have the color black - the Red, Green, and Blue buckets are now totally empty.

Given the above desciption, you can guess what other colors mean.

- Black: (0, 0, 0)
- White: (255, 255, 255)
- Red: (255, 0, 0)
- Green: (0, 255, 0)
- Blue: (0, 0, 255)
- Aqua: (0, 255, 255)
- Fuchsia: (255, 0, 255)
- Maroon: (128, 0, 0)
- Navy: (0, 0, 128)
- Olive: (128, 128, 0)
- Purple: (128, 0, 128)
- Teal: (0, 128, 128)
- Yellow: (255, 255, 0)

### **Overview of the image coordinate system in OpenCV**

As I mentioned in **Figure 1**, an image is represented as gird of pixels, Imagine our grid as a piece of graph paper. **Using this graph pager, the point(0,0) corresponnds to the top-left corner of the image(i.e., the origin).** As we move down and to the right, both the x and y-values increase.

Let's look at the image in **Figure 5** to make this point more clear:

![opencv_getting_setting_image_coordinates-e1609416591370](https://user-images.githubusercontent.com/70785000/147832626-24bb0e49-bc6a-41bc-bc46-8bf49e161c5a.png)

> Figure 5: In OpenCV, pixels are accessed by their (x, y)- coordinates. The origin (0,0) , is located at the top-left of the image. OpenCV images are zero-indexed, where the x-values go *left-to-right(column number) and y-values go top-to-bottom(row number).*

We see that we have an 8 * 8 grid with 64 total pixels.

The point at (0, 0) corresponds to the *top-left pixel* in our image, whereas the point (7,7) corresponds to the *bottom-right* corner.

**It is important to note that we are counting from zero rather than one.** 

The Python langauge is zero-indexed, meaning that we always start counting from zero.keep this in mind, and you will avoid a lot of confusion later on.

Finally, the pixel 4 columns to the *right and 5 rows down* is indexed by the point(3,4), keeping in mind that we are counting from zero rather than one.

### **Configuring your development environment**

<img width="800" alt="opencv" src="https://user-images.githubusercontent.com/70785000/147840866-765c0de2-9869-4f33-884c-8aeaf38ed825.png">

```python= 
# import the necessary packages
import argparse  # argument parser
import cv2

# contruct the arugment parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="adrian.png", help="path to the input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"]) # Image read
print(dir(image), type(image))  # type - numpy.ndarray
# noinspection PyUnresolvedReferences
print(image.shape)  # (450, 600, 3)
h,w = image.shape[:2] # 456, 600

print(f"Height : {h}, Width : {w}")
cv2.imshow("Original", image) # 
cv2.waitKey(0) # wait until user's key press action occurred.

# images are simply Numpy arrays --with the origin (0, 0) located at
# the top-lefft of the image
(b, g, r) = image[0,0]  # b -> 246, g -> 240, r-> 233
# the botto-left of the image
(b, g, r) = image[7,5] # b -> 245, g -> 239, r-> 232

# access the pixel located at x=50, y=20
(b, g, r) = image[20, 50]
print(f"Pixel at (50, 20) - Red : {r}, Green : {g}, Blue : {b}")

```

> (b, g, r) = image[0,0]  # b -> 246, g -> 240, r-> 233

**Why does OpenCV  represent images in BGR channel ordering rather than the standard RGB?**

The answer is that back when OpenCV was originall developed, BGR ordering was the standard! It was only later that the RGB order was adopted. The BGR ordering is standard in OpenCV, so get used to seeing it.

Then access the pixel located at x=50, y=20 using the array indexing of `image[20, 50]`.

But wait. Shoudln't it instead be `image[50, 20]`. since x = 50 and y = 20?

Let's consider.

Let's back up a step and consider that an image is simply a matrix with a width(number of columns) and height(number of rows). If we were to access an individual location in that matrix, we would denote it as the `x` value(column number) and `y` value(row number)

> (b, g, r) = image[20, 50]
> print(f"Pixel at (50, 20) - Red : {r}, Green : {g}, Blue : {b}")

Therefore , to access the pixel located at x = 50, y=20, you pass the y-value first (the row number) followed by the x-value (the column number), resulting in `image[y, x]`.

> **Note:** I've found that the concept of accessing individual pixels with the syntax of `image[y,x]` is what trips up many students. Take a second to convince yourself that `image[y, x]` is the correct syntax based on the fact that the x-value is your column number(i.e., width), and the y-value is your row number(i.e., height).

