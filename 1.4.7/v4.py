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
    
def bottom_text(original_image, text = 'Default Text'):
    '''
    This function takes two arguments, original_image and text.
    Original image is a filepath, while text is a string. Original image is the 
    image that text gets pasted on to. Through the modify() script, you can choose
    what text you would like to display on the top of the image. It also scales 
    the text appropriately based on the image, so that the text is neither too 
    big or too small. 
    
    Based on the image color, the text is either black or white, depending on the
    brighteness of the pixels in the top. 
    
    This function returns the modified version of the original image, with the 
    text chosen pasted onto the top, centered and scaled.
    '''
    # Creates a drawing layer
    original_image_draw = PIL.ImageDraw.Draw(original_image) 
    fontsize = 1
    imageFontSize = .5
    text_color = (0,0,0) # Standard text color is black
    colors = {
        "black": (0, 0, 0),
        "white": (255, 255, 255),
       #"purple": (255, 0, 255),
        #"green": (0, 0, 255),
        #"blue": (0, 255, 0),
        #"red": (255, 0, 0),
        #"teal": (0, 255, 255),
        #"yellow": (255, 0, 255)
        "gray": (127, 127, 127)
    }
    numpyImage = numpy.array(original_image) # convert to numpy array
    columns = len(numpyImage[0])
    rows = len(numpyImage)
    pixelCount = 1
    red_average = 0 # running total of the average intensities
    green_average = 0
    blue_average = 0
    red = ""
    blue = ""
    green = ""
    # Go through the bottom 1/8th to determine what color to use
    for row in range(int(((rows / 8) * 7)), rows): 
        for column in range(columns):
            red_average += numpyImage[row][column][0]
            green_average += numpyImage[row][column][1]
            blue_average += numpyImage[row][column][2]
            pixelCount += 1
    red_average = red_average / pixelCount
    blue_average = blue_average / pixelCount
    green_average = green_average / pixelCount
    """
    Simple checking of the averages to see what color to set the text to for 
    maximum contrast, choosing between white, gray, and black, with 27 conditions
    possible. 
    """
    if red_average >= 0 and red_average <= 63:
        red = "low"
    elif red_average >= 63 and red_average <= 190:
        red = "med"
    elif red_average >= 190 and red_average <= 255:
        red = "high"
    if green_average >= 0 and green_average <= 63:
        green = "low"
    elif green_average >= 63 and green_average <= 190:
        green = "med"
    elif green_average >= 190 and green_average <= 255:
        green = "high"
    if blue_average >= 0 and blue_average <= 63:
        blue = "low"
    elif blue_average >= 63 and blue_average <= 190:
        blue = "med"
    elif blue_average >= 190 and blue_average <= 255:
        blue = "high"
    if red == "low" and green == "low" and blue == "low":
        text_color = colors["white"]
    elif red == "low" and green == "low" and blue == "med":
        text_color = colors["white"]
    elif red == "low" and green == "low" and blue == "high":
        text_color = colors["white"]
    elif red == "low" and green == "med" and blue == "low":
        text_color = colors["white"]
    elif red == "low" and green == "med" and blue == "med":
        text_color = colors["gray"]
    elif red == "low" and green == "med" and blue == "high":
        text_color = colors["gray"]
    elif red == "low" and green == "high" and blue == "low":
        text_color = colors["white"]
    elif red == "low" and green == "high" and blue == "med":
        text_color = colors["gray"]
    elif red == "low" and green == "high" and blue == "high":
        text_color = colors["black"]
    elif red == "med" and green == "low" and blue == "low":
        text_color = colors["white"]
    elif red == "med" and green == "low" and blue == "med":
        text_color = colors["gray"]
    elif red == "med" and green == "low" and blue == "high":
        text_color = colors["gray"]
    elif red == "med" and green == "med" and blue == "low":
        text_color = colors["gray"]
    elif red == "med" and green == "med" and blue == "med":
        text_color = colors["gray"]
    elif red == "med" and green == "med" and blue == "high":
        text_color = colors["gray"]
    elif red == "med" and green == "high" and blue == "low":
        text_color = colors["gray"]
    elif red == "med" and green == "high" and blue == "med":
        text_color = colors["gray"]
    elif red == "med" and green == "high" and blue == "high":
        text_color = colors["black"]
    elif red == "high" and green == "low" and blue == "low":
        text_color = colors["white"]
    elif red == "high" and green == "low" and blue == "med":
        text_color = colors["gray"]
    elif red == "high" and green == "low" and blue == "high":
        text_color = colors["black"]
    elif red == "high" and green == "med" and blue == "low":
        text_color = colors["gray"]
    elif red == "high" and green == "med" and blue == "med":
        text_color = colors["gray"]
    elif red == "high" and green == "med" and blue == "high":
        text_color = colors["black"]
    elif red == "high" and green == "high" and blue == "low":
        text_color = colors["black"]
    elif red == "high" and green == "high" and blue == "med":
        text_color = colors["black"]
    elif red == "high" and green == "high" and blue == "high":
        text_color = colors["black"]
    
    font = ImageFont.truetype("../OpenSans-Regular.ttf", fontsize)
    # Scales the text based on the width values given
    while font.getsize(text)[0] < imageFontSize * original_image.size[0]: 
        fontsize += 1
        font = ImageFont.truetype("../OpenSans-Regular.ttf", fontsize)
    # centers the text
    textX_placement = (original_image.size[0] / 2) - (original_image_draw.textsize(text, font)[0] / 2) 
    textY_placement = original_image.size[1] - (2 * original_image_draw.textsize(text, font)[1])  
    original_image_draw.text((textX_placement, textY_placement), text, fill = text_color, font = font)
    #print (red, green, blue)
    #print (red_average, green_average, blue_average)
    return original_image

def top_text(original_image, text = 'Default Text'):
    '''
    This function takes two arguments, original_image and text.
    Original image is a filepath, while text is a string. Original image is the 
    image that text gets pasted on to. Through the modify() script, you can choose
    what text you would like to display on the bottom of the image. It also scales 
    the text appropriately based on the image, so that the text is neither too 
    big or too small. 
    
    Based on the image color, the text is either black or white, depending on the
    brighteness of the pixels in the bottom. 
    
    This function returns the modified version of the original image, with the 
    text chosen pasted onto the bottom, centered and scaled.
    '''
    original_image_draw = PIL.ImageDraw.Draw(original_image) # create drawing layer
    fontsize = 1
    imageFontSize = .95
    text_color = (0,0,0)
    colors = {
        "black": (0, 0, 0),
        "white": (255, 255, 255),
       #"purple": (255, 0, 255),
        #"green": (0, 0, 255),
        #"blue": (0, 255, 0),
        #"red": (255, 0, 0),
        #"teal": (0, 255, 255),
        #"yellow": (255, 0, 255)
        "gray": (127, 127, 127)
    }

    numpyImage = numpy.array(original_image) # convert to numpy
    columns = len(numpyImage[0])
    rows = len(numpyImage)
    pixelCount = 1
    red_average = 0
    green_average = 0
    blue_average = 0
    red = ""
    blue = ""
    green = ""
    #print (range(rows / 8))
    #print (range(columns))
    for r in range(rows / 8): # go through top 1/8th
        for column in range(columns):
            #print(row)
            #print(column)
            red_average += numpyImage[r][column][0]
            #print (r)
            #print (column)
            green_average += numpyImage[r][column][1]
            blue_average += numpyImage[r][column][2]
            pixelCount += 1
            #print (pixelCount)
    red_average = red_average / pixelCount
    blue_average = blue_average / pixelCount
    green_average = green_average / pixelCount
    """
    Simple checking of the averages to see what color to set the text to for 
    maximum contrast, choosing between white, gray, and black, with 27 conditions
    possible. 
    """
    if red_average >= 0 and red_average <= 63:
        red = "low"
    elif red_average >= 63 and red_average <= 190:
        red = "med"
    elif red_average >= 190 and red_average <= 255:
        red = "high"
    if green_average >= 0 and green_average <= 63:
        green = "low"
    elif green_average >= 63 and green_average <= 190:
        green = "med"
    elif green_average >= 190 and green_average <= 255:
        green = "high"
    if blue_average >= 0 and blue_average <= 63:
        blue = "low"
    elif blue_average >= 63 and blue_average <= 190:
        blue = "med"
    elif blue_average >= 190 and blue_average <= 255:
        blue = "high"
    if red == "low" and green == "low" and blue == "low":
        text_color = colors["white"]
    elif red == "low" and green == "low" and blue == "med":
        text_color = colors["white"]
    elif red == "low" and green == "low" and blue == "high":
        text_color = colors["white"]
    elif red == "low" and green == "med" and blue == "low":
        text_color = colors["white"]
    elif red == "low" and green == "med" and blue == "med":
        text_color = colors["gray"]
    elif red == "low" and green == "med" and blue == "high":
        text_color = colors["gray"]
    elif red == "low" and green == "high" and blue == "low":
        text_color = colors["white"]
    elif red == "low" and green == "high" and blue == "med":
        text_color = colors["gray"]
    elif red == "low" and green == "high" and blue == "high":
        text_color = colors["black"]
    elif red == "med" and green == "low" and blue == "low":
        text_color = colors["white"]
    elif red == "med" and green == "low" and blue == "med":
        text_color = colors["gray"]
    elif red == "med" and green == "low" and blue == "high":
        text_color = colors["gray"]
    elif red == "med" and green == "med" and blue == "low":
        text_color = colors["gray"]
    elif red == "med" and green == "med" and blue == "med":
        text_color = colors["gray"]
    elif red == "med" and green == "med" and blue == "high":
        text_color = colors["gray"]
    elif red == "med" and green == "high" and blue == "low":
        text_color = colors["gray"]
    elif red == "med" and green == "high" and blue == "med":
        text_color = colors["gray"]
    elif red == "med" and green == "high" and blue == "high":
        text_color = colors["black"]
    elif red == "high" and green == "low" and blue == "low":
        text_color = colors["white"]
    elif red == "high" and green == "low" and blue == "med":
        text_color = colors["gray"]
    elif red == "high" and green == "low" and blue == "high":
        text_color = colors["black"]
    elif red == "high" and green == "med" and blue == "low":
        text_color = colors["gray"]
    elif red == "high" and green == "med" and blue == "med":
        text_color = colors["gray"]
    elif red == "high" and green == "med" and blue == "high":
        text_color = colors["black"]
    elif red == "high" and green == "high" and blue == "low":
        text_color = colors["black"]
    elif red == "high" and green == "high" and blue == "med":
        text_color = colors["black"]
    elif red == "high" and green == "high" and blue == "high":
        text_color = colors["black"]
    
    font = ImageFont.truetype("../OpenSans-Regular.ttf", fontsize)
    # scale text
    while font.getsize(text)[0] < imageFontSize * original_image.size[0]: 
        fontsize += 1
        font = ImageFont.truetype("../OpenSans-Regular.ttf", fontsize)
    # center text
    textX_placement = (original_image.size[0] / 2) - (original_image_draw.textsize(text, font)[0] / 2)
    textY_placement = 15
    original_image_draw.text((textX_placement, textY_placement), text, fill = text_color, font = font)
    #print (red, green, blue)
    #print (red_average, green_average, blue_average)
    return original_image

def draw_border(original_image, rgb_value = (0,0,0),
border_thickness = 10):
    '''
    This function takes two arguments: original_image and border_thickness.
    original_image is the image that is being modified, and the border_thickness
    is the user-defined thickness of the border that defaults at 10px.
    
    This function is called when the user wants to draw border around the image. 
    The function will create a image that is completely opaque, and then will
    paste the original image onto (border_thickness,border_thickness) as the 
    left corner.
    
    The function will return the result of the operation.
    '''
    width, height = original_image.size
    # new image the size of the image plus the border thickness all around, 
    # created as the given color
    border_image = PIL.Image.new('RGB', 
        (width+2*border_thickness,height+2*border_thickness),
        rgb_value)
    #print(border_image.size)   
    # original_image.paste(overlay_mask, (0,0), mask = overlay_mask)
    # pastes image onto border
    border_image.paste(original_image, (border_thickness,border_thickness)) 
    return border_image