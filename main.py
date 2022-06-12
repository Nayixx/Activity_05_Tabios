import cv2 as cv
import numpy as np
from os import system
from time import sleep

system ('cls')

fpath = "anya.jpg"

img = cv.imread(fpath)

if len(img.shape) < 3:
    print("The image is grayscale")
    sleep(3)
    exit()


system('cls')
shapee = img.shape
print("To access a pixel")
x = int(input("Input 'x' Coordinate value (max value "+str(shapee[0])+"):"))
y = int(input("Input 'y' Coordinate value (max value "+str(shapee[1])+"):"))
chan = int(input(""" 
0 - Blue
1 - Green
2 - Red 
Select Channel: """))

axis = img.item(x,y,chan)

system('cls')
shapee = img.shape
print("Modify a Pixel")
x  = int(input("Input 'x' coordinate value (max value "+str(shapee[0])+" ) : "))
y  = int(input("Input 'y' coordinate value (max value "+str(shapee[1])+" ) : "))
blue = int(input("Input Blue channel value: "))
green = int(input("Input Green channel value: "))
red = int(input("Input Red channel value: "))

system('cls')

print("Output: ")

print("\nAccessed Pixel Value:", axis)

print("Pixel value before modify:", img[x, y])

img.itemset((x, y, 0), blue)
img.itemset((x, y, 1), green)
img.itemset((x, y, 2), red)

print("Pixel value after modified:", img[x, y],"\n")

w = 300
h = 300

if w > shapee[1] or h > shapee[0]:
    print("Set Image Dimension: Out of bounderies\n")
else:
    print("Set Image Dimension: Within the bounderies\n")

pixel = 1683001

if pixel > img.size: print("Set pixel: Higher than the pixel count\n")

elif pixel < img.size: print("Set pixel: Lower than the pixel count\n")

else: print("Set pixel: Equal to the pixel count")

print("Image Data Type:", img.dtype)