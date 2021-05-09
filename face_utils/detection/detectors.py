#!/usr/bin/env python3

"""detectors.py: contains face detectors modules."""

__author__ = "Ahmed Hermas"
__copyright__ = "Copyright 2021, © Digified "
__license__ = "MIT"
__version__ = "0.1.0"
__email__ = "a7medhermas@gmail.com"

from cv2 import cv2
import numpy as np
import math
import os
import logging
from .settings import MODELS_CONFIG

class Detector ():
    def __init__(self,model_name):
        
        self.model_name = model_name
        #calling the laoder function of the spicified model name
        self.model = getattr(self,MODELS_CONFIG[self.model_name]['loader'])()
    
    #Models Loaders 
    def _hog_cnn_loader(self):
        """ hog and cnn detector model
        Returns:
            None
        """
        global face_locations
        from face_recognition import face_locations 
        return None 
    
    def _cascade_loader(self):
        """ Cascade detector model

        Returns:
            [class]: detector class object
        """
        cascadePath = os.path.join(os.path.dirname(__file__),
                                   'assets/haarcascade_frontalface_default.xml')
        detector = cv2.CascadeClassifier(cascadePath)
        
        return detector

    def _retina_loader(self):
        """ retina detector model

        Returns:
            [class]: detector class object
        """
        #loading model paths
        caffemodel =os.path.join(os.path.dirname(__file__),
                                 "assets/Widerface-RetinaFace.caffemodel") 
        deploy = os.path.join(os.path.dirname(__file__),
                              "assets/deploy.prototxt")
        #loading the detector
        detector = cv2.dnn.readNetFromCaffe(deploy, caffemodel)
        
        return detector

    #Models Detectors
    def _getface_hog_cnn(self,img,mode):
        """ the detection function for cnn and hog models

        Args:
            img (np array): Input Image
            mode (int): 1 (xywh) , 2 (top,right,bottom,left)

        Returns:
            [tuple]: the output faces boundries
        """
        faces = face_locations(img,number_of_times_to_upsample=1,model=self.model_name)
        if len(faces)==0:
            return None
        if mode == 1:
            out = faces[0]
        elif mode ==2 :
            top,right,bottom,left = faces[0]
            x,y,w,h = int(left), int(top), int(right-left+1), int(bottom-top+1)
            out = [x,y,w,h]
        return out
    
    def _getface_cascade(self,img,mode):
        """the detection function for the cascade model

        Args:
            img (np array): Input Image
            mode (int): 1 (xywh) , 2(top,right,bottom,left)

        Returns:
            [tuple]: the output faces boundries
        """
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = self.model.detectMultiScale(gray, 1.3, 5)
        if len(faces)==0:
            return None
        x,y,w,h = faces[0]
        top, right, bottom, left = self._change_shape(x,y,w,h)

        if mode == 1 :
            out = [x,y,w,h]
        elif mode == 2 :
            out = [top, right, bottom, left]
        return out

    def _getface_retina(self,img,mode):
        """ This is the retina face detection model implementation

        Args:
            img (np array): Input Image
            mode (int): 1 (xywh) , 2(top,right,bottom,left)

        Returns:
            [tuple]: the output faces boundries
        """
        height, width = img.shape[0], img.shape[1]
        aspect_ratio = width / height
        ####
        if img.shape[1] * img.shape[0] >= 192 * 192:
            img = cv2.resize(img,
                                (int(192 * math.sqrt(aspect_ratio)),
                                int(192 / math.sqrt(aspect_ratio))), interpolation=cv2.INTER_LINEAR)
        ####
        blob = cv2.dnn.blobFromImage(img, 1, mean=(104, 117, 123))
        self.model.setInput(blob, 'data')
        out = self.model.forward('detection_out').squeeze()
        max_conf_index = np.argmax(out[:, 2])
        if max_conf_index ==0.0:
            pass
        left, top, right, bottom = out[max_conf_index, 3]*width, out[max_conf_index, 4]*height, \
                                    out[max_conf_index, 5]*width, out[max_conf_index, 6]*height
        
        x,y,w,h = int(left), int(top), int(right-left+1), int(bottom-top+1)
        
        if mode == 1:
            out = [x,y,w,h]
        elif mode == 2:
            out = [top,right,bottom,left]
        return out
        
    def detect(self,image,mode):
        """ 
        detects faces in images and return the boundries
        Args:
            image (numpy array): the input image
            model (str): hog,cnn,cascade,retina
            mode (int): 1 (x,y,w,h) , 2 (top,right,bottom,left)

        Raises:
            ValueError: [4000]

        Returns:
            [tuple]: the output faces boundries
        """
        try:
            out =getattr(self,MODELS_CONFIG[self.model_name]['detector'])(image,mode)

        except UnboundLocalError as e :
            logging.exception("You Have entered a wrong mode number ") 
            
        return out
        
    def _change_shape(self,x,y,w,h):
        """ change output shape from xywh to top right bot left

        Args:
            x (int): [x coordinate of the top left corder]
            y (int): [y coordinate of the top left corder]
            w (int): [width of the Image]
            h (int): [height of the Image]

        Returns:
            [tuple]: new coordinates
        """
        top = y 
        left = x
        right = x + w
        bottom = y + h
        return top,right,bottom,left
