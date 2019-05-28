import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path
import numpy as np      # 'as' lets us use standard abbreviation

'''Part 1: Working With a File System'''
#5 The absolute file name is C:/Users/Student Login/Desktop/nice.jpg
#5 ../Student Login/Desktop/nice.jpg
#6 This is an absolute file name, as it stars with C:. You do not have to be in
# a particular working directory for this to make sense.
# Cloud 9 runs on linux, so when you pwd, it starts with u'/home/ubuntu, instead
# of u'/C:/Windows

'''Part 2: Rendering an image on-screen'''
'''
#7 ONE SUBPLOT

#Read the image data
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, \'cat1-a.gif\')
# Read the image data into an array
img = plt.imread(filename)

#Show the image data
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation=\'none\')
# Show the figure on the screen
# fig.show()
fig.savefig(\'cat_plot\')
'''

#7 The new code does not work at first, as it still throws the error. You have to 
# reset the terminal before executin gthe new code to ge the proper result.
# 7a the x,y of the woman's nose is 275, 400.
# 7b the x,y of the cat's nose is 60, 40

'''Part 3: Objects and methods'''
#8 fig is an instance of the class Figure, and ax is an instance of AxesSubplot
# In line 25, the method savefig() is called on object fig. That method is being
# given the 'cat_plot' arguments. That method is a method of the class Figure.
# Comments explain what each line does, such as showing the figure on screen
# or building an absolute file-path.

'''Part 4: Arrays of Objects'''
#9a the method imshow is being called on the object ax[0]
'''
#9 TWO SUBPLOTS

#Read the image data
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, \'woman.jpg\')
# Read the image data into an array
img = plt.imread(filename)

# Create a 1x2 grid of subplots
# fig is the Figure, and ax is an ndarray of AxesSubplots
# ax[0] and ax[1] are the two Axes Subplots
fig, ax = plt.subplots(1, 2)
# Show the image data in the first subplot
ax[0].imshow(img, interpolation=\'none\')
# Show the image data in the second subplot
ax[1].imshow(img, interpolation=\'none\')
# Show the figure on the screen
# fig.show()
fig.savefig(\'two_women\')
'''
'''
#9b FIVE SUBPLOTS

#Read the image data
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'cat1-a.gif')
# Read the image data into an array
img = plt.imread(filename)

# Create a 1x2 grid of subplots
# fig is the Figure, and ax is an ndarray of AxesSubplots
# ax[0] and ax[1] are the two Axes Subplots
fig, ax = plt.subplots(1, 5)
# Show the image data in the first subplot
ax[0].imshow(img, interpolation='none')
# Show the image data in the second subplot
ax[1].imshow(img, interpolation='none')
# Show the image data in the first subplot
ax[2].imshow(img, interpolation='none')
# Show the image data in the second subplot
ax[3].imshow(img, interpolation='none')
# Show the image data in the first subplot
ax[4].imshow(img, interpolation='none')
# Show the figure on the screen
# fig.show()
fig.savefig('five_cats')
'''

'''Part 5: Keyword = Value pairs'''
'''
#10 LEAF EARING INTERPOLATION

#Read the image data
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, \'woman.jpg\')
# Read the image data into an array
img = plt.imread(filename)

# Create figure with 2 subplots
fig, ax = plt.subplots(1, 2)
# Show the image data in the first subplot
ax[0].imshow(img, interpolation=\'none\') # Override the default
ax[1].imshow(img)
ax[0].set_xlim(135, 165)
ax[0].set_ylim(470, 420)
ax[1].set_xlim(135, 165)
ax[1].set_ylim(470, 420)
# Show the figure on the screen
# fig.show()
fig.savefig(\'leaf_earing\')
'''

#10 Interpolation is when you put something in between the range of two other 
# points. Here, interpolation is putting colors between pixels, and is specified
# through the interpolation argument, which is whether or not you want interpolation
# to occur. The code has one instance of interpolation, which causes it to look 
# smoother. 
'''
#11a LEAF EARING EXPERIMENT

# Read the image data
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

# Create figure with 2 subplots
fig, ax = plt.subplots(1, 2)
# Show the image data in the first subplot
ax[0].imshow(img, interpolation='none') # Override the default
ax[1].imshow(img)
ax[0].set_xlim(135, 165)
ax[0].set_ylim(470, 420)
ax[1].set_xlim(135, 165)
ax[1].set_ylim(470, 420)
ax[1].minorticks_on()
ax[1].set_title('experiment')
ax[1].set_xlabel('X Label')
ax[1].set_ylabel('Y Label')
# Show the figure on the screen
# fig.show()
fig.savefig('experiment')
'''
'''
#11b THREE CLOSEUP

#Read the image data
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, \'woman.jpg\')
# Read the image data into an array
img = plt.imread(filename)

# Create figure with 2 subplots
fig, ax = plt.subplots(1, 3)
# Show the image data in the first subplot
ax[0].imshow(img, interpolation=\'none\') # Override the default
ax[1].imshow(img)
ax[2].imshow(img)
ax[0].set_xlim(125, 275)
ax[0].set_ylim(400, 250)
ax[1].set_xlim(300, 450)
ax[1].set_ylim(400, 250)
ax[2].set_xlim(250, 270)
ax[2].set_ylim(810, 780)
# Show the figure on the screen
# fig.show()
fig.savefig(\'three_closeup\')
'''
#12 axes.legend(), lets you place a legend on the axes, and takes the arguments
# handles and labels, which are used when you need finer control over what is 
# placed in the legend. 

#13 PLOT CRAZY MICE

#Read the image data
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'PCWmice1.jpg')
# Read the image data into an array
img = plt.imread(filename)

# Create a 1x2 grid of subplots
# fig is the Figure, and ax is an ndarray of AxesSubplots
# ax[0] and ax[1] are the two Axes Subplots
fig, ax = plt.subplots(1, 2)
# Show the image data in the first subplot
ax[0].imshow(img, interpolation='none')
# Show the image data in the second subplot
ax[1].imshow(img, interpolation='none')
ax[1].plot(38, 45, 'ro')
ax[1].plot(117, 43, 'ro')
ax[1].plot(138, 43, 'ro')
# Show the figure on the screen
# fig.show()
fig.savefig('crazy_mice')

'''CONCLUSION'''
#1 Absolute filenames start at the root directory, wherewas relative filenames
# start at the working directory that you are currently in. 
#2 An object is an instance of a class that you have instantiated
#3 methods are functions that you can call on an object, and will change the way 
# the object looks. Properties are attributes that are associated with objects, 
# and will ususally describe an object
#4 Python will check the class for the method, and will run the associated method
# with the name of what you called. This can modify an object, changing attributes,
# or do something else with a different object. 