# Sketch

**Sketching Algorithm based on Bit Manipulation in Python3**

**Use this Easy to Use GitHub Repository to Converse in a Binary Encryption Format**

## Installation
You can install the all requirements from **requirements.txt** by using pip.

    pip install -r requirements.txt


## Explaination : 

This code allows you to convert any image into a sketch using OpenCV and save it with the name you provide.

#### How to Use:

>Run the script.

> Enter the address of the image you want to sketch (without double quotes).

> Enter the name you want to give to the sketch. The sketch will be saved in the same directory as the script.

> The script will convert the image into a sketch and save it with the name provided.

> The sketch will be opened automatically for you to view.
#### Functions

> img_sketch(img) : This function takes the image address as input and converts it into a sketch using OpenCV.

> img_open(img) : This function opens the saved sketch automatically after it has been created.

## Note
> The script uses the Gaussian blur technique to smooth the edges of the image and remove noise before converting it into a sketch.

> The img_open() function may not work on some operating systems. If that is the case, you can manually open the saved sketch.
