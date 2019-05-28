from __future__ import print_function
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path
import numpy as np      # 'as' lets us use standard abbreviations
import make_mask

'''Part 1: Using Arrays of Pixels'''
#4 All elements of an array are the same data type, whereas lists can mix data
# types. Arrays also can have multiple dimensions, while lists are only single
# dimensional.


'''
#Read the image data
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

#Show the image data
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation='none')
# Saves the figure
fig.savefig('women2')
print (len(img))
print (len(img[0]))
print (img[5][9][1])
print (img[4][10][2])
print (img[49][24][2])
'''
#5 image height: 943
# Image Width: 574
# Green intensity: 94
# Red intensity: 93
# Red intensity 2: 107

'''Part 2: Manipulating Pixels'''
'''
#6 MANIPULATING PIXELS

#Read the image data
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

#Show the image data
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
###
# Make a rectangle of pixels yellow
###

height = len(img)
width = len(img[0])
for row in range(200, 220):
    for column in range(50, 100):
        img[row][column] = [255, 255, 0] # red + green = yellow
ax.imshow(img, interpolation='none')
# Saves the figure
fig.savefig('women2')'''
'''
#6 MANIPULATING PIXELS

#Read the image data
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

#Show the image data
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
###
# Make a rectangle of pixels yellow
###
height = len(img)
width = len(img[0])
for row in range(420, 470):
    for column in range(135, 166):
        img[row][column] = [0, 255, 0] #Green Rectangle
ax.imshow(img, interpolation='none')
# Saves the figure
fig.savefig('green_earing')'''
'''
#7 MANIPULATING PIXELS WITH IF
#Read the image data
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

#Show the image data
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)

###
# Change a region if condition is True
###

height = len(img)
width = len(img[0])
for r in range(155):
    for c in range(width):
        if sum(img[r][c])>500: # brightness R+G+B goes up to 3*255=765
            img[r][c]=[255,0,255] # R + B = magenta
for r in range(410, 470):
    for c in range(135, 157):
        if sum(img[r][c])>500:
            img[r][c]=[0, 255, 0]

###
# Show the image data
###
# Show the image data in a subplot
ax.imshow(img, interpolation='none')
# Saves the figure
fig.savefig('woman_sky_earing')
'''
#7 For each row until 154, goes through each column and checks if the sum of the 
# rgb values is over 500, and if it is, sets it to magenta, otherwise, continues 
# to the next pixel.
'''
#9 WOMAN AND MASK

#Read the image data
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

# Create a 1x2 grid of subplots
# fig is the Figure, and ax is an ndarray of AxesSubplots
# ax[0] and ax[1] are the two Axes Subplots
fig, ax = plt.subplots(1, 2)
height = len(img)
width = len(img[0])
for r in range(155):
    for c in range(width):
        if sum(img[r][c])>500: # brightness R+G+B goes up to 3*255=765
            img[r][c]=[255,0,255] # R + B = magenta
for r in range(410, 470):
    for c in range(135, 157):
        if sum(img[r][c])>500:
            img[r][c]=[0, 255, 0]
# Show the image data in the first subplot
ax[0].imshow(img, interpolation='none')
# Show the image data in the second subplot
ax[1].imshow(make_mask.make_mask(100, 100, 20), interpolation='none')
# Show the figure on the screen
# fig.show()
fig.savefig('women_and_mask')'''

'''Conclusion'''
#1 The data in a digital image is a whole bunch of numbers representing the rgb
# values of each pixel, and when an image has been altered, theses values have 
# been changed to reflect a new color.
#2 Both cameras "write" the image, in the case of the film, it is developed later
# after the light has changed it, and with a digital image, the rgb values
# have been captured and stored to be recreated. They both can be edited
# although digital images can be edited easier.
#3 Most of the time, a simple change in a rgb value from 255 to 254 is not going
# to make a big difference, allowing you to encode letters in the picture.
# 6 bits are enough to encode 0 to 63, as 6 bits, each with an on and off, is 2**6,
# which is 64. This would barely make the image different, as the colors might
# be a little tinted, but it would be hard to notice. 
#4 Most objects are going to have the same colors, so if there is a region of 
# the same values, that is probably one object.