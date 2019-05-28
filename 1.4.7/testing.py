from __future__ import print_function
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path  
import PIL
import ImageFont
import ImageDraw
import ImageOps
import numpy

directory = os.path.dirname(os.path.abspath(__file__))
earth_test = os.path.join(directory, 'Project_Images/phone.jpg')
earth_image = PIL.Image.open(earth_test)
earth_draw = PIL.ImageDraw.Draw(earth_image)



#################
"""GRAPEFRUIT IN CORNER"""
#################

'''
def create_overlay(original_image):
    image_width, image_height = original_image.size
    resize_width = image_width / 8
    resize_height = image_height / 8
    overlay_mask = PIL.Image.new('RGBA', (image_width, image_height), (0, 0, 0, 0))
    grapefruit_file = os.path.join(directory, 'Project_Images/slice.png')
    grapefruit = PIL.Image.open(grapefruit_file)
    if resize_height > resize_width:
        grapefruit = grapefruit.resize((resize_width, resize_width))
    elif resize_width > resize_height:
        grapefruit = grapefruit.resize((resize_height, resize_height))
    else:
        grapefruit = grapefruit.resize((resize_width, resize_height))
    grapefruit.convert('RGBA')
    overlay_mask.paste(grapefruit, ((image_width - grapefruit.size[0]), (image_height - grapefruit.size[1])))
    original_image.paste(overlay_mask, (0,0), mask = overlay_mask)
    '''
    
#####################
"""BOTTOM TEXT SCALING"""
#####################
'''
def bottom_text(original_image):
    text = 'TESTING TEXT FOR BOTTOM TEXT'
    fontsize = 1
    imageFontSize = .5
    
    font = ImageFont.truetype("../OpenSans-Regular.ttf", fontsize)
    while font.getsize(text)[0] < imageFontSize * original_image.size[0]:
        fontsize += 1
        font = ImageFont.truetype("../OpenSans-Regular.ttf", fontsize)
        
    textX_placement = (original_image.size[0] / 2) - (earth_draw.textsize(text, font)[0] / 2)
    textY_placement = original_image.size[1] - (2 * earth_draw.textsize(text, font)[1])  
    earth_draw.text((textX_placement, textY_placement), text, fill = (255, 255, 255), font = font)
    print (fontsize)
    print (font.getsize(text))
    #print (text_placement)
'''

def border(original_image):

    original_image = ImageOps.expand(original_image, border = 45)
    original_image.save('test_overlay.png')
    

def top_text(original_image):
    original_image_draw = PIL.ImageDraw.Draw(original_image)
    text = 'The new GrapeFruit 9s Pro Max'
    fontsize = 1
    imageFontSize = .5
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
        "gray":(127, 127, 127)
    }
    rows, columns = original_image.size
    numpyImage = numpy.array(original_image)
    pixelCount = 0
    red_average = 0
    green_average = 0
    blue_average = 0
    red = ""
    blue = ""
    green = ""
    
    for row in range(rows / 8):
        for column in range(columns):
            red_average += numpyImage[row][column][0]
            green_average += numpyImage[row][column][1]
            blue_average += numpyImage[row][column][2]
            pixelCount += 1
    red_average = red_average / pixelCount
    blue_average = blue_average / pixelCount
    green_average = green_average / pixelCount
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
    while font.getsize(text)[0] < imageFontSize * original_image.size[0]:
        fontsize += 1
        font = ImageFont.truetype("../OpenSans-Regular.ttf", fontsize)
        
    textX_placement = (original_image.size[0] / 2) - (original_image_draw.textsize(text, font)[0] / 2)
    textY_placement = 15
    original_image_draw.text((textX_placement, textY_placement), text, fill = text_color, font = font)
    
    
'''
############################################
BROKEN
############################################
CODE
############################################

def draw_border_diff_color(original_image, rgb_value_left = (0,0,0), 
rgb_value_top = (255, 0, 0), rgb_value_right = (0, 255, 0), rgb_value_bottom = (0, 0, 255),
border_thickness = 10):
    
    """
    This function takes two arguments: original_image and border_thickness.
    original_image is the image that is being modified, and the border_thickness
    is the user-defined thickness of the border that defaults at 10px.
    
    This function is called when the user wants to draw border around the image. 
    The function will create a image that is completely opaque, and then will
    paste the original image onto (border_thickness,border_thickness) as the 
    left corner.
    
    The function will return the result of the operation.
    """
    
    
    width, height = original_image.size
    
    border_image = PIL.Image.new('RGB', 
        (width+2*border_thickness,height+2*border_thickness))
    print(border_image.size)
    border_draw = PIL.ImageDraw.Draw(border_image)
    border_draw.polygon([(0,0),(border_thickness, 0), (border_thickness, height), (0,height)], fill = rgb_value_left)
    border_draw.polygon([(0,0),(0, border_thickness), (width, 10), (width, 0)], fill = rgb_value_top)
    border_draw.polygon([(width,0),(width-border_thickness,  0), (width-border_thickness,  height), (width,height)], fill = rgb_value_right)
    border_draw.polygon([(0,height),(width, height), (width, height-10), (border_thickness, height-10)], fill = rgb_value_bottom)
        
    # original_image.paste(overlay_mask, (0,0), mask = overlay_mask)
    border_image.paste(original_image, (border_thickness,border_thickness))    
    border_image.save('earthBorder.png')
    return border_image
    '''

#create_overlay(earth_image)
#bottom_text(earth_image)
#border(earth_image)
top_text(earth_image)
earth_image.save('test_overlay.png')
