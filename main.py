# importing open cv library and pytesseract
import cv2
import pytesseract

# giving path of executable file
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

# read image
image = cv2.imread('DEMO.png')

# pytesseract accepts only RGB values open cv is in BGR, so we need to convert before we load in pytesseract library
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

# get raw info about image
print(pytesseract.image_to_string(image)) #image -> prints converted text
print(pytesseract.image_to_boxes(image)) # prints the x,y,w,h(pixels) of bounding box of text

# Detecting characters
himg,wimg,_ = image.shape
boxes = pytesseract.image_to_boxes(image) #saving x,y,w,h(pixels) of bounding box of text in list

for b in boxes.splitlines():
    b = b.split(' ') #splitting each value based on free space and converting the data to list
    print(b)
    x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
    cv2.rectangle(image,(x,himg-y),(w,himg-h),(0,0,255),2)

    # label characters around the box
    cv2.putText(image,b[0],(x,himg-y+25),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
cv2.imshow('DISPLAY',image) #display
cv2.waitKey(0) #infinite delay

