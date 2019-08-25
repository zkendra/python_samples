##Intro code--import libraries and modules, load face detection classifier, import the small file to with which to practice,
##and then open the zip file and create a list of the files inside
import zipfile

from PIL import Image
from PIL import ImageDraw
import pytesseract
import cv2 as cv
import numpy as np

def main (name_str, file_name_str, face_cascade_str):
	name_dictionary = setup_dictionary(file_name_str, face_cascade_str)
    
    print ("Starting to search_name_return_faces")
    
    for name in name_dictionary:
        text = name_dictionary[key][-1]
        if (text.find(name_str) == -1):
        	print ("{} in {} = false".format(name_str, name))
        	continue
        print ("{} in {} = true".format(name_str, name))
        # create contact sheet from list of images (not perfect, needs work, and the height and width is hard-coded with 5 and 4.
        # will need to determine the number of files in a list and probably update the sizes of the thmbnls)
        count = len(name_dictionary[name][0])
            
        # create a contact sheet from images##
        display(type(name_dictionary[name][0][0]))
        first_image=name_dictionary[name][0][0]
        first_image_copy = first_image.copy()
        first_image_copy = first_image_copy.thumbnail ([100,100])

        columns = int(count / 2)
        rows = int(count / columns)
        contact_sheet_width = first_image.width*columns
        contact_sheet_height = first_image.height*rows
        
        contact_sheet=Image.new(first_image.mode, (contact_sheet_width, contact_sheet_height))
        x=0
        y=0

        # read image(s) and convert to RGB
        for img in name_dictionary[name][0]:
            # Lets paste the current image into the contact sheet
            contact_sheet.paste(img, (x,y))

            # Update our X position. If it is going to be the width of the image, then we set it to 0
            if x+ first_image.width == contact_sheet.width:
                x=0
                # Update Y to point to the next "line" of the contact sheet.
                y= y + first_image.height
            else:
                x = x + first_image.width

        # display the contact sheet
        contact_sheet.save("contact_sheet.jpg")
        display(contact_sheet)   

# Function accepts a zipfile as a string 
# Returns a list of the files, in this case, image files
def get_files(file_name_str):
    print ("Starting to create_list_unzipped_files")
   
    # specifying the zip file name 
    file_name = file_name_str
  
    # opening the zip file in READ mode 
    with zipfile.ZipFile(file_name, 'r') as zip: 
        # extracting all the files 
        print("Extracting all the files now...") 
        zip.extractall()
    
    #create a list of the files within the ZipFile
    files = zip.namelist()
   
    print (("Number of files in zip folder is: ") + str(len(files)))
    display (files)
    return files

# Function takes a list [(x,y,w,h),...]
# Returns [(x1, y1, x2, y2),....] 
# Which is more usable for creating a bounding_box by which the image is cropped
# The resulting images are saved to a list 
def create_list_face_thmbnl_imgs(array_name, list_name):
    print ("Starting to create_list_face_thmbnl_imgs")

    # Lets create a PIL image object
    pil_img=Image.fromarray(array_name,mode="L")
    
    # And lets create our drawing context
    drawing=ImageDraw.Draw(pil_img)
    
    list_thmbnl_images = [ ]
    
    num = 0 
    
    for xywh in list_name:
        num = num + 1

        # Now we just draw a rectangle around the bounds
        x1 = xywh[0]
        y1 = xywh[1]
        x2 = xywh[0]+xywh[2]
        y2 = xywh[1]+xywh[3]

        bounding_box = (x1, y1, x2, y2)
        single_face = pil_img.crop(bounding_box)
        single_face_copy = single_face.copy()
        
        single_face_copy.save('single_face_copy_thmbnl_{}.jpg'.format(num))
        
        list_thmbnl_images.append(single_face_copy)

    print ('Done with create_list_face_thmbnl_imgs!')    
    return list_thmbnl_images


#this function calls the create_list_unzipped_files function and returns the list of files, in this case, images, from which 
#we iterate through and detect the faces as a tuple (x1, y1, w, h).
#It accepts the following parameters: zip file name as file_name_str, and the haar cascade as face_cascade_str
# It stores the tuples in a key dictionary, the key = img_name, and the value = list of tuples
#This function takes a LOOOONG time to run :(
def setup_dictionary (file_name_str, face_cascade_str):
    
    files = get_files (file_name_str)
    
    print ("Starting to create_dictionary_of_thmbnls_text")
    
    # loading the face detection classifier
    face_cascade = cv.CascadeClassifier(face_cascade_str)
    dictionary = { }
    
    # Iterate through image files and create arrays
    for img in files:
        img_name = img
        img = cv.imread(img)
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        array_faces = face_cascade.detectMultiScale(gray, 1.15, 5)
        array_faces_list = array_faces.tolist()
        
        text = pytesseract.image_to_string(img)
        
        dictionary[img_name] = [create_list_face_thmbnl_imgs(gray, array_faces_list)] + [text] 
    
    print ('Done with create_dictionary_of_thmbnls_text!')   
    
    return (dictionary)
    
    
main ('Snyder','readonly/small_img.zip','readonly/haarcascade_frontalface_default.xml')