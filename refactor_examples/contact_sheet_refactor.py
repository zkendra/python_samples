import PIL
import numpy as np
from PIL import Image
from PIL import ImageColor
from PIL import ImageEnhance
from PIL import ImageOps
from PIL import ImageDraw
from PIL import ImageFont
import sys

# define channels
RED = 0
GREEN = 1
BLUE = 2

def main():

  channels = [RED, GREEN, BLUE]
  intensities = [0.1, 0.5, 0.8]

  # not sure if I should be using rgb_image or image for things like .width
  image = Image.open('readonly/msi_recruitment.gif')
  rgb_image = im.convert('RGB')

  # setup final image
  thumbprint_image = PIL.Image.new(rgb_image.mode, (rgb_image.width*3,rgb_image.height*3))
  
  x = 0
  y = 0

  # start the conversion
  for channel in channels:
    for intensity in intensities:

      updated_image = update_image(rgb_image, channel, intensity)
      thumbprint_image.paste(updated_image, (x,y))

      # handle moving x and y to correct next image location
      x = x+rgb_img.width % thumbprint_image.width
      if x == 0: # if we are on the left move down to next row
        y = y + rgb_img.height

  thumbprint_image = thumbprint_image.resize((int(thumbprint_image.width/2),int(thumbprint_image.height/2) ))

  # TODO: because we are calling display, I'm not confident we need to save first
  thumbprint_image.save("contact_sheet.jpg")
  display(thumbprint_image)

# return a copy of pixels with the color transformation applied, and text with border
def update_image(img, channel, intensity):
  print("update_image")
  pixels = np.asarray(img.convert('RGB')).copy()
  img = apply_color_filter(pixels, channel, intensity, img.width, img.height)
  img = add_bottom_border(img)
  img = write_text(img, "Channel "+channel+", Intensity "+intensity)
  return img

# set the color filter on the pixels provided (channels expected are RGB)
def apply_color_filter(pixels, channel, intensity, width, height):
  print("apply_color_filter (channel='%s', intensity='%s', width='%s', height='%s'" % (channel, intensity, width, height))
  # color the existing image
  # I'm doing this because its more efficient
  for i in range(width): #image.width
    for j in range(height): # image.height
        new_pixel = pixels[i,j][channel]*intensity
        pixels.itemset((i,j,channel),(new_pixel))

  return Image.fromarray(pixels)

#  Add a bottom border on  the provided pixelspixels
def add_bottom_border(img):
  print('bottom_border')
  img = ImageOps.expand(img, border=border)
  return img

# add text to the bottom of the image
def write_text(img, text):
  print("write_text (text='%s')" % (text) )
  draw = ImageDraw.Draw(img)
  font = ImageFont.truetype('readonly/fanwood-webfont.ttf', 40)

  # to do, allow choosing of text writing location
  draw.text((10, 460), text, (128, 255, 255, 255), font=font)

  return img

# start the program
main()

