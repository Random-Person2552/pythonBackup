'''earthEyes demonstrates PIL.Image.paste()
Unpublished work (c)2013 Project Lead The Way
CSE Activity 1.3.7 PIL API
Version 9/10/2013 '''

from __future__ import print_function
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import PIL
import os.path              

# Open the files in the same directory as the Python script
directory = os.path.dirname(os.path.abspath(__file__))  
student_file = os.path.join(directory, 'student.jpg')

# Open and show the student image in a new Figure window
student_img = PIL.Image.open(student_file)
fig, axes = plt.subplots(1, 2)
axes[0].imshow(student_img, interpolation='none')

# Display student in second axes and set window to the right eye
axes[1].imshow(student_img, interpolation='none')
axes[1].set_xticks(range(1050, 1410, 100))
axes[1].set_xlim(1050, 1400) #coordinates measured in plt, and tried in iPython
axes[1].set_ylim(1100, 850)
fig.savefig('girl')

# Open, resize, and display earth
earth_file = os.path.join(directory, 'earth.png')
earth_img = PIL.Image.open(earth_file)
earth_small = earth_img.resize((89, 87)) #eye width and height measured in plt
fig2, axes2 = plt.subplots(1, 2)
axes2[0].imshow(earth_img)
axes2[1].imshow(earth_small)
fig2.savefig('resize_earth')

# Paste earth into right eye and display
# Uses alpha from mask
student_img.paste(earth_small, (1162, 966), mask=earth_small) 
student_img.paste(earth_small, (700, 940), mask=earth_small) 
# Display
fig3, axes3 = plt.subplots(1, 2)
axes3[0].imshow(student_img, interpolation='none')
axes3[1].imshow(student_img, interpolation='none')
axes3[1].set_xlim(500, 1500)
axes3[1].set_ylim(1130, 850)
fig3.savefig('earth_as_eyes')


#13 
# MatPlotLib allows you to create subplots of images, which can then be manipulated
# Numpy is used to create arrays, which can be changed to represent images
# PIL is used to manipulate images, using methods.

#15
# A Line 19 calls the function subplots() from the plt library. The function is 
# being called with 2 arguments, 1 and 2. The function returns 2 objects, which 
# are being assigned to fig and ax.

# B Line 23 calls imshow() on axes[1]
# Line 24 calls setx_ticks() on axes[1]
# Line 25 calls set_xlim() on axes[1]
# Line 26 calls set_ylim() on axes[1]
# Line 27 calls savefig() on fig

# C The coordinates are (1162, 966)

# 16 Upper Left: (700, 940), bottom right: (790, 1025) Width: 90, Height: 85

# 17 
# A Line 30 uses the join() method from the os.path module. It is being passed 
# 2 arguments. The value it returns is being assigned to the variable earth_flie.

# B In line 31 the open() function of the PIL.Image module returns a new PIL.Image 
# object, which is being assigned to the variable earth_img.

# C There are two sets of parentheses because one set belongs to the method, 
# while the other set belongs to the tuple being used for height and width.

# D The (89, 87) argument resizes the earth to be the same size as the bounding
# box of the eye, which in turn is the size of the eye, ensuring the earth is a 
# perfect fit over the eye.

# E Line 33 calls the function subplots() from the library plt with 2 arguments, 
# 1 and 2. The function returns two objects, which are being assigned to fig2 and
# axes2.
# Line 34 calls the method imshow() on the object axes2[0] with 1 argument, earth_img.
# Line 35 calls the method imshow() on the object axes2[1] with 1 argument, earth_small.
# Line 36 calls the method savefig() on the object fig2 with 1 argument, 'resize_earth'.

# F An additional argument that can be passed to resize() is filter, which if 
# ommitted is set to NEAREST.
# ANTIALIAS is the recommended filter for downsampling, unless you prefer speed. 

# G The size attribute is the image's size in pixels represented by a tuple.

# H The output is the size of the two images in pixels, while the last output
# is the second value of the size tuple of the earth image. 

# I You can tell that the two images contain a different number of image pixels
# because the increments of the axis are different, which are representations of
# the image pixels. 

# 18 The code most likely averages out the colors of the three to four bytes in
# a group of pixels, then depending on what the resized image size is, will
# continue to do this until is has enough to fill a row/column. 

# 19 
# A Student_img uses 15667200 bytes, while earth_small uses 30972 bytes

# C Student.jpg uses 206000 bytes, while smallEarth uses 18300 bytes. 

# D These discrepancies might be due to cloud9 compressing images, or the fact 
# that the images might have been downsized to be a smaller size.

# E When a color is used as the paste, the area that is specified is filled with 
# a single color instead of an image. 

# F If the image modes don't match, the pasted image is changed to the mode of
# the image being pasted on.

# G earth_small is the image to be pasted, the tuple represents where to paste
# the image, being the upper left corner and the bottom right corner to create 
# a box. mask = earth_small uses earth_small as a mask of where to paste the image,
# so that when there is transparency around the earth, that is not pasted onto the
# eye. 

###############################################################################
# CONCLUSION

# 1
'''The classes used in this code include image from PIL, of which the methods are 
open(), used to open images, resize(), used to resize the images, paste() which 
is used to paste images onto other images, imshow(), being used to show the final
image on the subplots. Some other methods are setx_lim and sety_lim, which are 
being used to set the limits of the x and y axes to show where to display the
image. There aren't any attributes used specifically in the code, but they are 
referenced, such as the earth size being set to the size of the girl's eye.
'''

# 2 
''' A complex task performed in this activity was pasting the earth onto the 
girl's eye. Through abstraction, we are able to simply use the paste() method,
specifying where and how we want the image to be pasted onto the girl. This allows
us to do this task much simpler, as we do not have to go through the process of
adding the earth to the girl pixel by pixel, since the computer does it for us. 
'''