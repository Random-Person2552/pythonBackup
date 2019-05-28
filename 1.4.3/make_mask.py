import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import numpy as np
import PIL
import math

def make_mask(rows, columns, stripe_width):
    '''An example mask generator
    Makes slanted stripes of width stripe_width
    image
    returns an ndarray of an RGBA image rows by columns
    '''
    
    img = PIL.Image.new('RGBA', (columns, rows))
    image = np.array(img)
    '''
    for row in range(rows):
        for column in range(columns):
            if (row**column*30)/stripe_width % 2 == 0: 
                image[row][column] = [0, 255, 0, 255] # green, alpha=255
            else:
                # Odd stripe
                image[row][column] = [0, 0, 255, 255] # blue, alpha=255
                '''
#WEIRD CHRISTMAS PATTERN THING            
    for row in range(rows):
        for column in range(columns):
            if (row**column*30)/stripe_width % 2 == 0: 
                image[row][column] = [0, 255, 0, 255] # green, alpha=255
            else:
                # Odd stripe
                image[row][column] = [0, 0, 255, 255] # blue, alpha=255
                '''
    for row in range(rows):
        for column in range(columns):
            if ((column**columns) - (row ** rows))/stripe_width % 2 == 0: 
                image[row][column] = [0, 255, 0, 255] # green, alpha=255
            else:
                # Odd stripe
                image[row][column] = [0, 0, 255, 255] # blue, alpha=255
                '''
    '''for row in range(rows):
        for column in range(columns):
            if (row+column)/stripe_width % 2 == 1: 
                #(r+c)/w says how many stripes above/below line y=x
                # The % 2 says whether it is an even or odd stripe
                
                # Even stripe
                image[row][column] = [0, 255, 0, 255] # green, alpha=255
            
            else:
                # Odd stripe
                image[row][column] = [0, 0, 255, 255] # blue, alpha=255'''
    return image
    
if __name__ == "__main__":
    image = make_mask(100,100,20)
    
    fig, ax = plt.subplots(1, 1)
    ax.imshow(image)
    fig.savefig('mask')