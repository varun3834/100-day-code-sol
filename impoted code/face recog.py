import cv

#Loading The Cascade File
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

#Reading the Input Image
# image= cv.imread('1.jpg')
image= cv.imread('1.png')

#Resizing the Image
img = cv.resize(image,None,fx=0.3,fy=0.3)

#Converting the image into grayscale image
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#Detecting The Faces
faces = face_cascade.detectMultiScale(imgGray, 1.2, 5)

#Pointing The Faces
for (x,y,w,h) in faces:
	cv.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)

#Displaying The Output Image
cv.imshow('img', img)
cv.waitKey()