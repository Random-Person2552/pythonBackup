from __future__ import print_function
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path  
import PIL
import PIL.ImageDraw            

def round_corners_one_image(original_image, percent_of_side=.3):
    """ Rounds the corner of a PIL.Image
    
    original_image must be a PIL.Image
    Returns a new PIL.Image with rounded corners, where
    0 < percent_of_side < 1
    is the corner radius as a portion of the shorter dimension of original_image
    """
    #set the radius of the rounded corners
    width, height = original_image.size
    radius = int(percent_of_side * min(width, height)) # radius in pixels
    
    ###
    #create a mask
    ###
    
    #start with transparent mask
    rounded_mask = PIL.Image.new('RGBA', (width, height), (127,0,127,0))
    drawing_layer = PIL.ImageDraw.Draw(rounded_mask)
    border_mask = PIL.Image.new('RGBA', (width+10, height+10), (127,0,127,0))
    drawing_layer2 = PIL.ImageDraw.Draw(border_mask)
    overlay_mask = PIL.Image.new('RGBA', (width, height), (127,0,127,0))
    overlay_drawing = PIL.ImageDraw.Draw(overlay_mask)
    
    drawing_layer2.polygon([(0,0),(10, 0), (10, height), (0,height)], fill = (0, 0, 0, 255))
    drawing_layer2.polygon([(0,0),(0, 10), (width, 10), (width, 0)], fill = (0, 0, 0, 255))
    drawing_layer2.polygon([(width,0),(width-10, 0), (width-10, height), (width,height)], fill = (0, 0, 0, 255))
    drawing_layer2.polygon([(0,height),(width, height), (width, height-10), (10,height-10)], fill = (0, 0, 0, 255))
    
    overlay_drawing.polygon([(0,0),(width, 0), (width, height), (0, height)], fill = (127, 0, 127, 127))
    overlay_drawing.text((10,10), 'TEST STRING OVERLAY', fill = (0, 0, 0))
    overlay_mask.resize((width *2, height * 2))
    # Overwrite the RGBA values with A=255.
    # The 127 for RGB values was used merely for visualizing the mask
    
    # Draw two rectangles to fill interior with opaqueness
    drawing_layer.polygon([(radius,0),(width-radius,0),
                            (width-radius,height),(radius,height)],
                            fill=(127,0,127,255))
    drawing_layer.polygon([(0,radius),(width,radius),
                            (width,height-radius),(0,height-radius)],
                            fill=(127,0,127,255))

    #Draw four filled circles of opaqueness
    drawing_layer.ellipse((0,0, 2*radius, 2*radius), 
                            fill=(0,127,127,255)) #top left
    drawing_layer.ellipse((width-2*radius, 0, width,2*radius), 
                            fill=(0,127,127,255)) #top right
    drawing_layer.ellipse((0,height-2*radius,  2*radius,height), 
                            fill=(0,127,127,255)) #bottom left
    drawing_layer.ellipse((width-2*radius, height-2*radius, width, height), 
                            fill=(0,127,127,255)) #bottom right
                         
    # Uncomment the following line to show the mask
    #plt.imshow(rounded_mask)
    
    # Make the new image, starting with all transparent
    result = PIL.Image.new('RGBA', original_image.size, (0,0,0,0))
    result.paste(original_image, (0,0), mask=rounded_mask)
    result.paste(border_mask, (0,0), mask=border_mask)
    result.paste(overlay_mask, (0,0), mask=overlay_mask)
    #result.save('test.png')
    return result
    
def get_images(directory=None):
    """ Returns PIL.Image objects for all the images in directory.
    
    If directory is not specified, uses current directory.
    Returns a 2-tuple containing 
    a list with a  PIL.Image object for each image file in root_directory, and
    a list with a string filename for each image file in root_directory
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    image_list = [] # Initialize aggregaotrs
    file_list = []
    
    directory_list = os.listdir(directory) # Get list of files
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass # do nothing with errors tying to open non-images
    return image_list, file_list

def round_corners_of_all_images(directory=None):
    """ Saves a modfied version of each image in directory.
    
    Uses current directory if no directory is specified. 
    Places images in subdirectory 'modified', creating it if it does not exist.
    New image files are of type PNG and have transparent rounded corners.
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    # Create a new directory 'modified'
    new_directory = os.path.join(directory, 'modified')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed  
    
    # Load all the images
    image_list, file_list = get_images(directory)  

    # Go through the images and save modified versions
    for n in range(len(image_list)):
        # Parse the filename
        print(n)
        filename, filetype = os.path.splitext(file_list[n])
        
        # Round the corners with default percent of radius
        curr_image = image_list[n]
        new_image = round_corners_one_image(curr_image) 
        
        # Save the altered image, suing PNG to retain transparency
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)
        
'''directory = os.path.dirname(os.path.abspath(__file__))  
neil_degrasse_tyson = os.path.join(directory, '1.4.5_Images/Neil_deGrasse_Tyson.jpg')
neil_degrasse_tyson_image = PIL.Image.open(neil_degrasse_tyson)
round_corners_one_image(neil_degrasse_tyson_image)
'''
round_corners_of_all_images()

#5 The names of the three functions are round_corners_one_image(), get_images, 
# and round_corners_of_all_images()

#6 It creates a new folder titled modified, and places all images into this folder
# after rounding all of the corners of each image in the original folder.

#7 
# A Round_corners_one_image() takes two arguments. Argument 1 is PIL.image image. 
# Argument 2 is a float between 0 and 1 representing the radius of the rounding.
# The function returns a new PIL.image with rounded corners. 

# B The image created is a magenta color. 

# C The object created in line 26 is called rounded_mask, while the object in 
# line 27 is drawing_layer.

# D You would want the values of the mask to be 255. 

# E Lines 33-38 create the second image of two rectangles, while 41-48 creates the
# 4 circles in the corners. 

# F The image is initialized to black, as the RGBA values are 0, 0, 0, 0.

# G The corners are white, but they have an alpha value of 0, so the color doesn't
# matter.

# 8 
# A get_images() can be passed either 0 or 1 argument. 

# B Returns 2 objects that are both lists representing directories.

# C os.getcwd(), os.listdir and os.path.join()

# D Return a list containing the names of the entries in the directory given by 
# path.

# E This program uses try-except because it does not want to terminate the 
# program when an error is thrown, but continue running the rest of the program. 
# An advantage of this is that the program can continue running when an error 
# occurs, but disadvantages are that errors are not reported, so you would not
# be able to traceback to what caused the error. 

# F Opens every image in a directory until an error is thrown, causing the except
# to trip and the rest of the code to execute. 

# 9
# A If the program is unable to create a new directory called modified, it is 
# going to throw and error and cause the entire program to stop running, which 
# is what we don't want to happen. The directory could also already exist, in 
# which case the images could just be dumped into the directory.

# B The number of images in the directory, represented by a list.

# C The current image on the specified iteration of the list, used to grab the 
# actual image and perform the rounding on. 

'''Conclusion'''
# 1 Transparency and the alpha channel allow the space behind the icon to be shown,
# and not just a white background.

# 2 When you wanted to round the image, you sinmply had to call the function 
# already defined to round one image, and perform that function on every image 
# in a list, created by get_images()

# 3 Alice is clost to correct, as technically no image is truly originial, as the
# brain has to process each image and fill in blindspots. However, some images
# could be considered original, as the image you take on a camera might not 
# be modified to fit the screen, as that might be its actual size.

# 4 I believe that all images are yours to use if they are published somwehere,
# however they cannot be used for personal gain or anything involving monetary value.
# If you were to take an image off the web, and display it in your house, that 
# would not be copyright, but if you were to get that image printed from a 
# company without permission of the original owner, you could be prosecuted for 
# copyright, as the company recieved monetary value for an image that they
# are not allowed to legally sell. This is different than if an image is open
# source, which means anyone can use it for any purpose they desire. 

# 5 Our team dynamic works well together, as we both contributed ideas to the 
# conversation and each person's input is valued. I believe that there is not 
# a lot that we need to work on to make a better team dynamic. 