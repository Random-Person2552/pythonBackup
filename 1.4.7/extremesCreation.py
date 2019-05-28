from __future__ import print_function
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path  
import PIL
import PIL.ImageDraw      

big_vertical = PIL.Image.new('RGB', (200, 1000), (37, 91, 178))
big_vertical.save('big_vertical.jpg')
big_horizontal = PIL.Image.new('RGB', (1000, 200), (36, 178, 41))
big_horizontal.save('big_horizontal.jpg')