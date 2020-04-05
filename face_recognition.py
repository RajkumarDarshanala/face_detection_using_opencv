import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def detect(gray,frame):
    faces =face_cascade.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]
        eyes=eye_cascade.detectMultiScale(roi_gray,1.1,3)
        for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    return frame 
#if we want to detect faces in the live camera output
#    inside video capture can use videocapture(1) if external camera is used;
vid_capture = cv2.VideoCapture(0)
while True:
    _,frame=vid_capture.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    result=detect(gray,frame)
    cv2.imshow('Video',result)
    if cv2.waitKey(1) & 0xFF == ord('q'):  #line to make a command 'q' to quit the process
        break
vid_capture.release()
cv2.destroyAllWindows()


#if want to detect faces in a image


img=cv2.imread('image_file_name.jpg')
gray=cv.cvtCOLOR(img,cv2.COLOR_BGR2GRAY)
result=detect(gray,img)
cv2.imshow('Image',result)
