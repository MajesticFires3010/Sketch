import time

import cv2  # To Perform All the Image Operations
from termcolor import cprint, colored   # For Style ;-)
from pyfiglet import figlet_format      # For Style ;-)
import os   # To Open the Saved Image

def img_sketch(img) :
    global a

    image = cv2.imread(img) # loads an image from the specified file

    # convert an image from one color space to another
    grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # GreyScale Conversion
    invert = cv2.bitwise_not(grey_img)                  # Inverting Colors # helps in masking of the image

    # sharp edges in images are smoothed while minimizing too much blurring
    blur = cv2.GaussianBlur(grey_img, (21, 21), 0)        # Gaussian Blur
    invertedblur = cv2.bitwise_not(blur)                # Negligible

    sketch = cv2.divide(grey_img, blur, scale = 256.0)

    name = input("Enter Name to be Saved : ")
    a = str(str(os.getcwd()) + '\\' + name + ".jpg")
    cv2.imwrite(a, sketch) # converted image is saved as mentioned name

def img_open(img) :
    img = "start " + img
    os.system(a)

f3 = figlet_format("Sketcher", font="doh", width = 200)
print(colored(f3, "green"))
image = input("Enter Image Address : ")
img_sketch(image)
print("Image Rendered Successfully ;-)")
time.sleep(1)
img_open(a)