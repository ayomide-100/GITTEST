import cv2 as cv #lesson 2----to display video using while loop and terminate the loop after 20 secs or by pressing D
                 #            the while loop reads each frame of the video and and displays it

capture= cv.VideoCapture('Videos/galaxy.mp4')
while True:
	isTrue, frame = capture.read()   #while loop is used in displaying video frame by frame
	cv.imshow('Video',frame)

	if cv.waitKey(20) & 0xFF==ord('d'):  #line 9 means 20secs till video is closed or terminate when d is pressed
		break
capture.release()   #line 11 is to terminate the capture method
cv.destroyAllWindows()  #line 12 is to close all open windows

cv.waitKey(0)







import cv2 #lesson 1----to display a picture, rotate the image,set a new resolution to the image

img=cv2.imread('Photos/lion.jpeg', 1)
r.img=cv2.resize(img,(720,1600))   #line 25 is for resizing image by specifying the resolution
ro.img=cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE) #line 26 is for rotating pictures to a degree and a direction
cv2.imwrite('new_lion.jpeg',img) #to name new image gottenafter resizing and rotating
cv2.imshow('Lion', img)  
cv2.waitKey(0) 
cv2.destroyAllWindows() 

import cv2 as cv #lesson 3----to resize or rescale a video



#img= cv.imread('Photos/car.jpeg')
#cv.imshow('Car' , img)
def rescaleFrame(frame, scale=0.25):  #line 38 is to set new scale to 25% of the original video
	width=int(frame.shape[1]*scale)  #to define the width and set to new scale
	height=int(frame.shape[0]*scale)  #to define the height and set to new scale
	dimensions = (width,height)
	return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
	


capture= cv.VideoCapture('Videos/galaxy.mp4')
while True:
	isTrue, frame = capture.read()  

	frame_resized=rescaleFrame(frame)

	cv.imshow('Video',frame)
	cv.imshow('Video Resized', frame_resized)

	if cv.waitKey(20) & 0xFF==ord('d'):  
		break
capture.release()   
cv.destroyAllWindows()  

cv.waitKey(0)




import cv2 as cv  #lesson 4-----to resize images with method similar to resizing video


img= cv.imread('Photos/car.jpeg')
cv.imshow('Car' , img)
def rescaleFrame(frame, scale=0.25):
	width=int(frame.shape[1]*scale)
	height=int(frame.shape[0]*scale)
	dimensions = (width,height)
	return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
resized_image=rescaleFrame(img)	
cv.imshow('Image' , resized_image)


cv.waitKey(0)






import cv2 as cv  #lesson 5----rescale frame method can be used for vids, pics and lives vids
# while the chage res method works only for live feed


#img= cv.imread('Photos/car.jpeg')
#cv.imshow('Car' , img)
def rescaleFrame(frame, scale=0.25):  #this method will work for images, videos and live videos
	width=int(frame.shape[1]*scale)
	height=int(frame.shape[0]*scale)
	dimensions = (width,height)
	return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
#resized_image=rescaleFrame(img)	
#cv.imshow('Image' , resized_image)


def changeRes(width,height):  #this method only works for live video from a webcam or conneted camera 
	capture.set(3,width)
	capture.set(4,height)


capture= cv.VideoCapture('Videos/galaxy.mp4')
while True:
	isTrue, frame = capture.read()  

	frame_resized=rescaleFrame(frame)

	cv.imshow('Video',frame)
	cv.imshow('Video Resized', frame_resized)

	if cv.waitKey(20) & 0xFF==ord('d'):  
		break
capture.release()   
cv.destroyAllWindows()  

cv.waitKey(0)




#lesson 6 to draw on blank image or any image and use choose colour to use in drawing
import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3),dtype='uint8')# to get a blank picture with only only

#blank[200:400 , 300:400]=0,0,255   #to paint image in a certain way, this give a square painting with colour red



cv.imshow('Blank',blank)

rec=cv.rectangle(blank, (0,0),(blank.shape[1]//1, blank.shape[0]//2), (0,255,0), thickness=-1) #to draw a rectangle over an image which we used blank
                                                                     #to fill image completly, thickness will be equal to cv.FILLED or -1(negative one)
                                                                       #to edit image, instead of using img.shape[1 or 0] which represents the height 
                                                                       #and width and using //2 or 1 to scale it, use the coordinates such as (250,500) or (300,400)

cv.imshow('Rectangle', blank)


cv.waitKey(0)





import cv2 as   #lesson 7....creating a blank image and editing it in different manners
import numpy as np

blank=np.zeros((500,500,3),dtype='uint8')# to get a blank picture with only only

#blank[200:400 , 300:400]=0,0,255   #to paint image in a certain way, this give a square painting with colour red



cv.imshow('Blank',blank)

rec=cv.rectangle(blank, (0,0),(blank.shape[1]//1, blank.shape[0]//2), (0,255,0), thickness=-1) #to draw a rectangle over an image which we used blank
                                                                     #to fill image completly, thickness will be equal to cv.FILLED or -1(negative one)
                                                                       #to edit image, instead of using img.shape[1 or 0] which represents the height 
                                                                       #and width and using //2 or 1 to scale it, use the coordinates such as (250,500) or (300,400)

cv.imshow('Rectangle', blank)     #function to display rectangle
#cv.circle(blank,(250,250)) #or
cv.circle(blank,(blank.shape[1]//2, blank.shape[0]//2), 50, (0,0,255),thickness=-1) #to create a circle using the blank.shape[] method
                                                                                     #for height or width and filled thickness
                                                                                     #


cv.imshow('Circle', blank)      #function to display circle
 

#cv.line(blank, (250,500),(blank.shape[1]//1, blank.shape[0]//2), (255,255,255), thickness=11)
cv.line(blank,(0,250),(500,250), (255,255,255), thickness=10)   #to draw line with coordinates and thicknessand colour...white
cv.imshow('Line', blank)      #function to display line

cv.putText(blank,'Life Is Good', (125,250,), cv.FONT_HERSHEY_TRIPLEX,1.0,(255,0,0))  #to with text'life is good' in hershey triplex font and scale it using that '1'
                                                                                     #and is colour blue

cv.imshow('Text', blank)   #function to display text
cv.waitKey(0)






import cv2 as cv   #lesson 8.....various methods used in image editing



img=cv.imread('Photos/lion.jpeg')
cv.imshow('Lion', img)

gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)   # to make image greyscale
cv.imshow('Gray',gray)


blur=cv.GaussianBlur(img,(9,9),cv.BORDER_DEFAULT)  #to blur an image, the (3,3) reps the kernel size with must be an odd number
cv.imshow('Blur',blur)


canny= cv.Canny(img,125,175)  #to make image canny i.e to know the number of edges in the imagw
cv.imshow('Canny Edges',canny)


dilated= cv.dilate(canny,(7,7), iterations=3)   #to dilate image
cv.imshow('Dilated',dilated)



eroded=cv.erode(dilated, (3,3), iterations=1)  #to erode image
cv.imshow('Eroded', eroded)


#the dilate and erode methods are methods used to edit the image


resized= cv.resize(img,(500,500), interpolation=cv.INTER_AREA)#the cv.INTER_AREA is ore suitable for resizing images to a smaller scale
                                                              #to resize to bigger scales, cv.INTER_LINEAR or cv.INTER_CUBIC
                                                              #the cv.INTER_CUBIC is slower, but the resulting image is of more quality
                                                              #method is to resize image by defining the boundary lenght and width

cv.imshow('Resized', resized)



cropped=img[50:200,200:400]  #to crop out a specifc part of the image by state the boundary coordinate of the image
cv.imshow('Cropped', cropped)


cv.waitKey(0)