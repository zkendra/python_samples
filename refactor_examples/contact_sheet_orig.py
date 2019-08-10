####THIS WORKS!!!!!#####

import PIL
import numpy as np
from PIL import Image
from PIL import ImageColor
from PIL import ImageEnhance
from PIL import ImageOps
from PIL import ImageDraw
from PIL import ImageFont
import sys

def add_border(input_image, output_image, border):
    img = Image.open(input_image)
 
    if isinstance(border, int) or isinstance(border, tuple):
        bimg = ImageOps.expand(img, border=border)
    else:
        raise RuntimeError('Border is not an integer or tuple!')
    
    bimg.save(output_image)

im = Image.open('readonly/msi_recruitment.gif')

#display(im)  #displays original image

rgb_im = im.convert('RGB') 

pixel_array = np.asarray(rgb_im)

##Helper things##
#print(pixel_array) #prints 450 rows and 800 columns worth of 3 (r, g, b) pixel values
#print(pixel_array.shape)
#display(pixel_array_copy)

##Generate a list to store the images from below##
list_pixel_array_copies = []
#print(list_pixel_array_copies)

##To make Image 1##
pixel_array_copy = pixel_array.copy()
for i in range(450):
    for j in range(800):
        pixel_r = pixel_array_copy[i,j][0]*0.1
        pixel_array_copy.itemset((i,j,0),(pixel_r))
#print(pixel_array_copy)

#create, save, and open image from pixel array
im_pixel_array_copy = Image.fromarray(pixel_array_copy)
im_pixel_array_copy.save("pixel_array_copy_1.jpg")
pixel_array_copy_1 = Image.open("pixel_array_copy_1.jpg")

#add border#
add_border("pixel_array_copy_1.jpg",
               output_image="pixel_array_copy_1_with_border.jpg",
               border=(0, 0, 0, 50))
pixel_array_copy_1_with_border = Image.open("pixel_array_copy_1_with_border.jpg")
pixel_array_copy_1_with_border.save("pixel_array_copy_1_with_border.jpg")

#put font and text on image#
img = Image.open('pixel_array_copy_1_with_border.jpg')
draw = ImageDraw.Draw(img)
font = ImageFont.truetype('readonly/fanwood-webfont.ttf', 40)
text = "Channel 0, Intensity 0.1"
draw.text((10, 460), text, (26, 255, 255, 255), font=font)
img.save("pixel_array_copy_1_with_border.jpg")

#add to list#
list_pixel_array_copies.append('pixel_array_copy_1_with_border.jpg')

#display image with new border
#display(pixel_array_copy_1_with_border)

#print(list_pixel_array_copies)

##To make Image 2##
pixel_array_copy = pixel_array.copy()
for i in range(450):
    for j in range(800):
        pixel_r = pixel_array_copy[i,j][0]*0.5
        pixel_array_copy.itemset((i,j,0),(pixel_r))
#print(pixel_array_copy)

#create, save, and open image from pixel array
im_pixel_array_copy = Image.fromarray(pixel_array_copy)
im_pixel_array_copy.save("pixel_array_copy_2.jpg")
pixel_array_copy_2 = Image.open("pixel_array_copy_2.jpg")

#add border#
add_border("pixel_array_copy_2.jpg",
               output_image="pixel_array_copy_2_with_border.jpg",
               border=(0, 0, 0, 50))
pixel_array_copy_2_with_border = Image.open("pixel_array_copy_2_with_border.jpg")
pixel_array_copy_2_with_border.save("pixel_array_copy_2_with_border.jpg")

#put font and text on image#
img = Image.open('pixel_array_copy_2_with_border.jpg')
draw = ImageDraw.Draw(img)
font = ImageFont.truetype('readonly/fanwood-webfont.ttf', 40)
text = "Channel 0, Intensity 0.5"
draw.text((10, 460), text, (128, 255, 255, 255), font=font)
img.save("pixel_array_copy_2_with_border.jpg")

#add to list#
list_pixel_array_copies.append('pixel_array_copy_2_with_border.jpg')

#display image with new border
#display(pixel_array_copy_2_with_border)

#print(list_pixel_array_copies)

##To make Image 3##
pixel_array_copy = pixel_array.copy()
for i in range(450):
    for j in range(800):
        pixel_r = pixel_array_copy[i,j][0]*0.9
        pixel_array_copy.itemset((i,j,0),(pixel_r))
#print(pixel_array_copy)

#create, save, and open image from pixel array
im_pixel_array_copy = Image.fromarray(pixel_array_copy)
im_pixel_array_copy.save("pixel_array_copy_3.jpg")
pixel_array_copy_3 = Image.open("pixel_array_copy_3.jpg")

#add border#
add_border("pixel_array_copy_3.jpg",
               output_image="pixel_array_copy_3_with_border.jpg",
               border=(0, 0, 0, 50))
pixel_array_copy_3_with_border = Image.open("pixel_array_copy_3_with_border.jpg")
pixel_array_copy_3_with_border.save("pixel_array_copy_3_with_border.jpg")

#put font and text on image#
img = Image.open('pixel_array_copy_3_with_border.jpg')
draw = ImageDraw.Draw(img)
font = ImageFont.truetype('readonly/fanwood-webfont.ttf', 40)
text = "Channel 0, Intensity 0.9"
draw.text((10, 460), text, (230, 255, 255, 255), font=font)
img.save("pixel_array_copy_3_with_border.jpg")

#add to list#
list_pixel_array_copies.append('pixel_array_copy_3_with_border.jpg')

#display image with new border
#display(pixel_array_copy_3_with border)

#print(list_pixel_array_copies)

        
##To make Image 4##
pixel_array_copy = pixel_array.copy()
for i in range(450):
    for j in range(800):
        pixel_g = pixel_array_copy[i,j][1]*0.1
        pixel_array_copy.itemset((i,j,1),(pixel_g))
#print(pixel_array_copy)

#create, save, and open image from pixel array
im_pixel_array_copy = Image.fromarray(pixel_array_copy)
im_pixel_array_copy.save("pixel_array_copy_4.jpg")
pixel_array_copy_4 = Image.open("pixel_array_copy_4.jpg")

#add border#
add_border("pixel_array_copy_4.jpg",
               output_image="pixel_array_copy_4_with_border.jpg",
               border=(0, 0, 0, 50))
pixel_array_copy_4_with_border = Image.open("pixel_array_copy_4_with_border.jpg")
pixel_array_copy_4_with_border.save("pixel_array_copy_4_with_border.jpg")

#put font and text on image#
img = Image.open('pixel_array_copy_4_with_border.jpg')
draw = ImageDraw.Draw(img)
font = ImageFont.truetype('readonly/fanwood-webfont.ttf', 40)
text = "Channel 1, Intensity 0.1"
draw.text((10, 460), text, (255, 26, 255, 255), font=font)
img.save("pixel_array_copy_4_with_border.jpg")

#add to list#
list_pixel_array_copies.append('pixel_array_copy_4_with_border.jpg')

#display image with new border
#display(pixel_array_copy_4_with border)

#print(list_pixel_array_copies)

##To make Image 5##
pixel_array_copy = pixel_array.copy()
for i in range(450):
    for j in range(800):
        pixel_g = pixel_array_copy[i,j][1]*0.5
        pixel_array_copy.itemset((i,j,1),(pixel_g))
#print(pixel_array_copy)

#create, save, and open image from pixel array
im_pixel_array_copy = Image.fromarray(pixel_array_copy)
im_pixel_array_copy.save("pixel_array_copy_5.jpg")
pixel_array_copy_2 = Image.open("pixel_array_copy_5.jpg")

#add border#
add_border("pixel_array_copy_5.jpg",
               output_image="pixel_array_copy_5_with_border.jpg",
               border=(0, 0, 0, 50))
pixel_array_copy_5_with_border = Image.open("pixel_array_copy_5_with_border.jpg")
pixel_array_copy_5_with_border.save("pixel_array_copy_5_with_border.jpg")

#put font and text on image#
img = Image.open('pixel_array_copy_5_with_border.jpg')
draw = ImageDraw.Draw(img)
font = ImageFont.truetype('readonly/fanwood-webfont.ttf', 40)
text = "Channel 1, Intensity 0.5"
draw.text((10, 460), text, (255, 128, 255, 255), font=font)
img.save("pixel_array_copy_5_with_border.jpg")

#add to list#
list_pixel_array_copies.append('pixel_array_copy_5_with_border.jpg')

#display image with new border
#display(pixel_array_copy_5_with border)

#print(list_pixel_array_copies)

##To make Image 6##
pixel_array_copy = pixel_array.copy()
for i in range(450):
    for j in range(800):
        pixel_g = pixel_array_copy[i,j][1]*0.9
        pixel_array_copy.itemset((i,j,1),(pixel_g))
#print(pixel_array_copy)

#create, save, and open image from pixel array
im_pixel_array_copy = Image.fromarray(pixel_array_copy)
im_pixel_array_copy.save("pixel_array_copy_6.jpg")
pixel_array_copy_6 = Image.open("pixel_array_copy_6.jpg")

#add border#
add_border("pixel_array_copy_6.jpg",
               output_image="pixel_array_copy_6_with_border.jpg",
               border=(0, 0, 0, 50))
pixel_array_copy_6_with_border = Image.open("pixel_array_copy_6_with_border.jpg")
pixel_array_copy_6_with_border.save("pixel_array_copy_6_with_border.jpg")

#put font and text on image#
img = Image.open('pixel_array_copy_6_with_border.jpg')
draw = ImageDraw.Draw(img)
font = ImageFont.truetype('readonly/fanwood-webfont.ttf', 40)
text = "Channel 1, Intensity 0.9"
draw.text((10, 460), text, (255, 230, 255, 255), font=font)
img.save("pixel_array_copy_6_with_border.jpg")

#add to list#
list_pixel_array_copies.append('pixel_array_copy_6_with_border.jpg')

#display image with new border
#display(pixel_array_copy_6_with border)

#print(list_pixel_array_copies)

##To make Image 7##
pixel_array_copy = pixel_array.copy()
for i in range(450):
    for j in range(800):
        pixel_b = pixel_array_copy[i,j][2]*0.1
        pixel_array_copy.itemset((i,j,2),(pixel_b))
#print(pixel_array_copy)

#create, save, and open image from pixel array
im_pixel_array_copy = Image.fromarray(pixel_array_copy)
im_pixel_array_copy.save("pixel_array_copy_7.jpg")
pixel_array_copy_7 = Image.open("pixel_array_copy_7.jpg")

#add border#
add_border("pixel_array_copy_7.jpg",
               output_image="pixel_array_copy_7_with_border.jpg",
               border=(0, 0, 0, 50))
pixel_array_copy_7_with_border = Image.open("pixel_array_copy_7_with_border.jpg")
pixel_array_copy_7_with_border.save("pixel_array_copy_7_with_border.jpg")

#put font and text on image#
img = Image.open('pixel_array_copy_7_with_border.jpg')
draw = ImageDraw.Draw(img)
font = ImageFont.truetype('readonly/fanwood-webfont.ttf', 40)
text = "Channel 2, Intensity 0.1"
draw.text((10, 460), text, (255, 255, 26, 255), font=font)
img.save("pixel_array_copy_7_with_border.jpg")

#add to list#
list_pixel_array_copies.append('pixel_array_copy_7_with_border.jpg')

#display image with new border
#display(pixel_array_copy_7_with border)

#print(list_pixel_array_copies)

##To make Image 8##
pixel_array_copy = pixel_array.copy()
for i in range(450):
    for j in range(800):
        pixel_b = pixel_array_copy[i,j][2]*0.5
        pixel_array_copy.itemset((i,j,2),(pixel_b))
#print(pixel_array_copy)

#create, save, and open image from pixel array
im_pixel_array_copy = Image.fromarray(pixel_array_copy)
im_pixel_array_copy.save("pixel_array_copy_8.jpg")
pixel_array_copy_8 = Image.open("pixel_array_copy_8.jpg")

#add border#
add_border("pixel_array_copy_8.jpg",
               output_image="pixel_array_copy_8_with_border.jpg",
               border=(0, 0, 0, 50))
pixel_array_copy_8_with_border = Image.open("pixel_array_copy_8_with_border.jpg")
pixel_array_copy_8_with_border.save("pixel_array_copy_8_with_border.jpg")

#put font and text on image#
img = Image.open('pixel_array_copy_8_with_border.jpg')
draw = ImageDraw.Draw(img)
font = ImageFont.truetype('readonly/fanwood-webfont.ttf', 40)
text = "Channel 2, Intensity 0.5"
draw.text((10, 460), text, (255, 255, 128, 255), font=font)
img.save("pixel_array_copy_8_with_border.jpg")

#add to list#
list_pixel_array_copies.append('pixel_array_copy_8_with_border.jpg')

#display image with new border
#display(pixel_array_copy_8_with border)

#print(list_pixel_array_copies)


##To make Image 9##
pixel_array_copy = pixel_array.copy()
for i in range(450):
    for j in range(800):
        pixel_b = pixel_array_copy[i,j][2]*0.9
        pixel_array_copy.itemset((i,j,2),(pixel_b))
#print(pixel_array_copy)

#create, save, and open image from pixel array
im_pixel_array_copy = Image.fromarray(pixel_array_copy)
im_pixel_array_copy.save("pixel_array_copy_9.jpg")
pixel_array_copy_9 = Image.open("pixel_array_copy_9.jpg")

#add border#
add_border("pixel_array_copy_9.jpg",
               output_image="pixel_array_copy_9_with_border.jpg",
               border=(0, 0, 0, 50))
pixel_array_copy_9_with_border = Image.open("pixel_array_copy_9_with_border.jpg")
pixel_array_copy_9_with_border.save("pixel_array_copy_9_with_border.jpg")

#put font and text on image#
img = Image.open('pixel_array_copy_9_with_border.jpg')
draw = ImageDraw.Draw(img)
font = ImageFont.truetype('readonly/fanwood-webfont.ttf', 40)
text = "Channel 2, Intensity 0.9"
draw.text((10, 460), text, (255, 255, 230, 255), font=font)
img.save("pixel_array_copy_9_with_border.jpg")

#add to list#
list_pixel_array_copies.append('pixel_array_copy_9_with_border.jpg')

#display image with new border
#display(pixel_array_copy_9_with border)

#print(list_pixel_array_copies)


##create a contact sheet from images##
first_image=Image.open(list_pixel_array_copies[0])
contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*3,first_image.height*3))
x=0
y=0

# read image(s) and convert to RGB
for img in list_pixel_array_copies:
# Lets paste the current image into the contact sheet
    img = Image.open(img)
    contact_sheet.paste(img, (x,y))

# Now we update our X position. If it is going to be the width of the image, then we set it to 0
# and update Y as well to point to the next "line" of the contact sheet.
    if x+first_image.width == contact_sheet.width:
        x=0
        y=y+first_image.height
    else:
        x=x+first_image.width

# resize and display the contact sheet
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
contact_sheet.save("contact_sheet.jpg")
display(contact_sheet)
