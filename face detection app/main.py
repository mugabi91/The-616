import cv2
import os 
from random import randrange
import sys

#importing frontal face detector model

trained_face_model = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


#choosing image 
directory = "./"
images = set()
target_extension = [".png",".jpeg",".jpg",".raw"]

for filename in os.listdir(directory):
    if any(filename.endswith(ext) for ext in target_extension):
        file_path = os.path.join(directory,filename)
        images.add(filename)
        
        
def grayScale(input_media):

    grayscale_img =cv2.cvtColor(input_media, cv2.COLOR_BGR2GRAY)

    #detect faces
    face_cordinates = trained_face_model.detectMultiScale(grayscale_img)

    #draw lines on faces
    for (x,y,w,h) in face_cordinates:
        cv2.rectangle(input_media,(x, y),(x+w, y+h), [0,randrange(255),0],2)

    #show the detected face on the images 
        cv2.imshow('IMAGE1',input_media)
        cv2.waitKey(1)
    

        
        
# for image in images:
#     colour_img = cv2.imread(image)
#     grayScale(input_media=colour_img)




#### for videos


video_cam = cv2.VideoCapture(0)

def main():
    while True:
        successful_frame_capture, frame = video_cam.read()
        if successful_frame_capture:
            grayScale(input_media=frame)
        
        
        # way out of loop hold key Q
        if cv2.waitKey(1) & 0xFF == ord('q') and (sys.platform.startswith('win') or sys.stdin.isatty()):
            break

    video_cam.release()
    cv2.destroyAllWindows()
        
        
        
if __name__ == "__main__":
    main()
    print("code executed")