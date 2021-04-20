from cv2 import cv2
import numpy as np
import math
import os
from face_recognition import face_landmarks,face_locations
from .cropping import crop

def _change_shape(x,y,w,h):
    ''' takes xywh return top right bottom left'''
    top = y 
    left = x
    right = x + w
    bottom = y + h
    return top,right,bottom,left

def _getface_hog_cnn(img,model,mode):

    faces = face_locations(img,number_of_times_to_upsample=1,model=model)
    
    if mode == 1:
        out = faces[0]
    elif mode ==2 :
        top,right,bottom,left = faces[0]
        x,y,w,h = int(left), int(top), int(right-left+1), int(bottom-top+1)
        out = [x,y,w,h]
    return out

def _getface_cascade(img,mode):
    cascadePath = os.path.join(os.path.dirname(__file__),'assets/haarcascade_frontalface_default.xml')
    face_cascade = cv2.CascadeClassifier(cascadePath)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    x,y,w,h = faces[0]
    top, right, bottom, left = _change_shape(x,y,w,h)

    if mode == 1 :
        out = [x,y,w,h]
    elif mode == 2 :
        out = [top, right, bottom, left]
    return out

def _getface_retina(img,mode):
    caffemodel =os.path.join(os.path.dirname(__file__), "assets/Widerface-RetinaFace.caffemodel") 
    deploy = os.path.join(os.path.dirname(__file__),"assets/deploy.prototxt")
    detector = cv2.dnn.readNetFromCaffe(deploy, caffemodel)
    height, width = img.shape[0], img.shape[1]
    aspect_ratio = width / height
    if img.shape[1] * img.shape[0] >= 192 * 192:
        img = cv2.resize(img,
                            (int(192 * math.sqrt(aspect_ratio)),
                            int(192 / math.sqrt(aspect_ratio))), interpolation=cv2.INTER_LINEAR)

    blob = cv2.dnn.blobFromImage(img, 1, mean=(104, 117, 123))
    detector.setInput(blob, 'data')
    out = detector.forward('detection_out').squeeze()
    max_conf_index = np.argmax(out[:, 2])
    left, top, right, bottom = out[max_conf_index, 3]*width, out[max_conf_index, 4]*height, \
                                out[max_conf_index, 5]*width, out[max_conf_index, 6]*height
    x,y,w,h = int(left), int(top), int(right-left+1), int(bottom-top+1)
    
    if mode == 1:
        out = [x,y,w,h]
    elif mode == 2:
        out = [top,right,bottom,left]
    return out

def extract_face_boudries(img,model,mode):
    if model in ['hog','cnn']:
        out =_getface_hog_cnn(img,model,mode)
    elif model == 'cascade':
        out =_getface_cascade(img,mode)
    elif 'retina' :
        out =_getface_retina(img,mode)
    else : 
        raise ValueError('E4000')
    return out

def extract_face(img,model):
    bbox = extract_face_boudries(img,model,1)
    outImg = crop(img,bbox,2.7,80,80)
    return outImg