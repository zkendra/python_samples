import PIL
import numpy as np
from PIL import Image
from PIL import ImageColor
from PIL import ImageEnhance
from PIL import ImageOps
from PIL import ImageDraw
from PIL import ImageFont
import sys

# open image
RED = 0
GREEN = 1
BLUE = 2

def main(img_path):

  channels = [RED, GREEN, BLUE]
  intensities = [0.1, 0.5, 0.8]

  # not sure if I should be using rgb_image or image for things like .width
  image = Image.open(img_path)

  # setup final image
  thumbprint_image = PIL.Image.new(image.mode, (image.width*3, image.height*3))
  
  x = 0
  y = 0

  # start the conversion
  for channel in channels:
    for intensity in intensities:

      updated_image = update_image(image, channel, intensity)
      thumbprint_image.paste(updated_image, (x,y))

      # handle moving x and y to correct next image location
      x = (x+image.width) % thumbprint_image.width
      if x == 0: # if we are on the left move down to next row
        y = y + image.height

  thumbprint_image = thumbprint_image.resize((int(thumbprint_image.width/2),int(thumbprint_image.height/2) ))

  # TODO: because we are calling display, I'm not confident we need to save first
  thumbprint_image.save("contact_sheet.png")
  display(thumbprint_image)

# return a copy of pixels with the color transformation applied, and text with border
def update_image(img, channel, intensity):
  print("update_image")
  pixels = np.asarray(img.convert('RGB')).copy()
  img = apply_color_filter(pixels, channel, intensity, img.width, img.height)
  img = add_bottom_border(img)
  txt = "Channel %s, Intensity %s" % (channel, intensity)
  img = write_text(img, txt, channel, intensity)
  return img

# set the color filter on the pixels provided (channels expected are RGB)
def apply_color_filter(pixels, channel, intensity, width, height):
  print("apply_color_filter (channel='%s', intensity='%s', width='%s', height='%s'" % (channel, intensity, width, height))
  # color the existing image
  for i in range(height): 
    for j in range(width):
        new_pixel = pixels[i,j][channel]*intensity
        pixels.itemset((i,j,channel),(new_pixel))

  return Image.fromarray(pixels)

#  Add a bottom border on  the provided pixelspixels
def add_bottom_border(img):
  print('bottom_border')
  img = ImageOps.expand(img, border=(0, 0, 0, 50))
  return img

# add text to the bottom of the image
def write_text(img, text, channel, intensity):
  txt_channels = [255,255,255]
  txt_channels[channel] = int(255*intensity)

  print("write_text (text='%s')" % (text) )
  draw = ImageDraw.Draw(img)
  font = ImageFont.load_default()
  # font = ImageFont.truetype('readonly/fanwood-webfont.ttf', 40)

  # to do, allow choosing of text writing location
  draw.text((10, 460), text, (txt_channels[RED], txt_channels[GREEN], txt_channels[BLUE], 255), font=font)

  return img

# start the program
# main('resources/happy.png')
main('resources/frog.jpg')
