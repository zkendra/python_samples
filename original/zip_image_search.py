##Intro code--import libraries and modules, load face detection classifier, import the small file to with which to practice,
##and then open the zip file and create a list of the files inside


#     file_name_str = 'readonly/small_img.zip'
#     face_cascade_str = 'readonly/haarcascade_frontalface_default.xml'

def main (name_str, file_name_str, face_cascade_str):
    
    import zipfile

    from PIL import Image
    from PIL import ImageDraw
    import pytesseract
    import cv2 as cv
    import numpy as np

    file_name_str = file_name_str
    face_cascade_str = face_cascade_str
    
    search_name_return_faces (name_str, file_name_str, face_cascade_str)

#this function accepts a zipfile as a string and returns a list of the files, in this case, image files
def create_list_unzipped_files(file_name_str):
    print ("Starting to create_list_unzipped_files")
   
    # specifying the zip file name 
    file_name = file_name_str
  
    # opening the zip file in READ mode 
    with zipfile.ZipFile(file_name, 'r') as zip: 
        # printing all the contents of the zip file 
#         zip.printdir() 
  
        # extracting all the files 
        print("Extracting all the files now...") 
        zip.extractall()
    
    #create a list of the files within the ZipFile
    list_unzipped_files = zip.namelist()
   
    print (("Number of files in zip folder is: ") + (str(len(zip.namelist()))))
    
    display (list_unzipped_files)
    
    return list_unzipped_files

    print ("Done with create_list_unzipped_files!")

# #this function takes a list [(x,y,w,h),...] and returns [(x1, y1, x2, y2),....] which is more usable for creating a 
# bounding_box by which the image is cropped and the resulting images are saved to a list 
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
        
        single_face=pil_img.crop(bounding_box)
        
        #display(single_face)
    
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
def create_dictionary_of_thmbnls_text (file_name_str, face_cascade_str):
    
    list_unzipped_files = create_list_unzipped_files (file_name_str)
    
    print ("Starting to create_dictionary_of_thmbnls_text")
    
    # loading the face detection classifier
    face_cascade = cv.CascadeClassifier(face_cascade_str)
    
    #iterate through image files and create arrays
    dictionary = { }
    
    for img in list_unzipped_files:
        img_name = img
        img = cv.imread(img)
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        array_faces = face_cascade.detectMultiScale(gray, 1.15, 5)
        array_faces_list = array_faces.tolist()
        
        text = pytesseract.image_to_string(img)
        
        dictionary [img_name] = [create_list_face_thmbnl_imgs(gray, array_faces_list)] + [text] 
        
    # check to see that the dictionary was created correctly
#     display (dictionary)
    
    print ('Done with create_dictionary_of_thmbnls_text!')   
    
    return (dictionary)


def search_name_return_faces (name_str, file_name_str, face_cascade_str):
    
    name_dictionary = create_dictionary_of_thmbnls_text (file_name_str, face_cascade_str)
    
    print ("Starting to search_name_return_faces")
    
    for key in name_dictionary:
        text = name_dictionary[key][-1]
        if (text.find(name_str)) != -1:
            print ("{} in {} = true".format(name_str, key))
             #  #create contact sheet from list of images (not perfect, needs work, and the height and width is hard-coded with 5 and 4.
             # #will need to determine the number of files in a list and probably update the sizes of the thmbnls)
            count = len(name_dictionary[key][0])
            
            ##create a contact sheet from images##
            display(type(name_dictionary[key][0][0]))
            first_image=name_dictionary[key][0][0]
            first_image_copy = first_image.copy()
            first_image_copy = first_image_copy.thumbnail ([100,100])
#             first_image.open().show()
            columns = int(count / 2)
            rows = int (count / columns)
            contact_sheet=Image.new(first_image.mode, (first_image.width*columns ,first_image.height*rows))
            x=0
            y=0

            # read image(s) and convert to RGB
            for img in name_dictionary[key][0]:
                img_copy = img.copy()
                img_copy = img.thumbnail([100,100])
            # Lets paste the current image into the contact sheet
#                 img = Image.open(img)
                contact_sheet.paste(img, (x,y))

            # Now we update our X position. If it is going to be the width of the image, then we set it to 0
            # and update Y as well to point to the next "line" of the contact sheet.
                if x+ first_image.width == contact_sheet.width:
                    x=0
                    y= y + first_image.height
                else:
                    x = x + first_image.width

            # resize and display the contact sheet
#           contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
            contact_sheet.save("contact_sheet.jpg")
            display(contact_sheet)   
            
        else:
            print ("{} in {} = false".format(name_str, key))
            


main ('Snyder','readonly/small_img.zip','readonly/haarcascade_frontalface_default.xml')
