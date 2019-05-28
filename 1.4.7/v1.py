from __future__ import print_function
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path  
import PIL
import ImageDraw      
import ImageFont
import ImageOps
import numpy

directory = os.path.dirname(os.path.abspath(__file__))

# USED FOR TESTING PURPOSES
#earth_test = os.path.join(directory, 'Project_Images/sulfur.JPG')
#earth_image = PIL.Image.open(earth_test)

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

def grapefruit_in_corner(original_image, logo_image):
    
    '''
    This function takes the arguments "original_image" and "logo_image".
    Both arguments are in the form of filepaths to the image.
    
    The function is called when the user wants to create an icon
    placed in the corner of the original image. The coordinates that the 
    icon is placed on are determined by the height and width of the
    original image.
    
    Original Image is the original image to paste the logo_image on. Logo_image 
    is chosen by the user in the modify() script, allowing them to place a square
    version of the image in the bottom right corner. 
    
    This function returns the modified version of the original image, with
    the logo in the bottom right.
    '''
    
    image_width, image_height = original_image.size
    resize_width = image_width / 8 # 1/8 of the image size
    resize_height = image_height / 8
    # New mask image
    overlay_mask = PIL.Image.new('RGBA', (image_width, image_height), (0, 0, 0, 0)) 
    #Find the file
    grapefruit_file = os.path.join(directory, 'Project_Images/' + logo_image) 
    grapefruit = PIL.Image.open(grapefruit_file)
    # Use the lowest value, so as to have a square
    if resize_height > resize_width: 
        grapefruit = grapefruit.resize((resize_width, resize_width))
    elif resize_width > resize_height:
        grapefruit = grapefruit.resize((resize_height, resize_height))
    else:
        grapefruit = grapefruit.resize((resize_width, resize_height))
    grapefruit.convert('RGBA')
    overlay_mask.paste(grapefruit, ((image_width - grapefruit.size[0]), (image_height - grapefruit.size[1])))
    #paste the image
    original_image.paste(overlay_mask, (0,0), mask = overlay_mask)
    return original_image