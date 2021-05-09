# face utils
> this is an opensource wrapper library for the most common face detection models. 

It also provides multiple face utilities such as face cropping.

## Supported detection models
- face_recognition (hog and cnn)
- retina face model
- haar cascade face detection  

more to be added in the next releases

## Installation

OS X & Linux using PIP :

```sh
pip install face-utils
```


## Features

### Face Detection 

By creating an object of the face detection model you want you can use it to detect the faces in images.  
I have also implemented outputs forms such as
1 : (x,y,w,h) and  2 : (top,right,bottom,left )


### Face cropping 
ability to crop the  face from the image given the detector result  
You can also zoom in and out from the face.  

## Example 


```python 
import cv2
from face_utils.detection import Detector
from face_utils.cropping import cropping
imgPath = "files/Obama.jpg"
img = cv2.imread(imgPath)
img= np.array(img)
model = Detector("hog")
bbox = model.detect(img,2) #using (x,y,w,h) return mode
face = cropping.crop(img,bbox,1,80,80)
```


input :  
<img src="https://i.ibb.co/HKRFmSJ/President-Barack-Obama-is-photographed-during-a-presidential-portrait-sitting-for-an-official-photo.jpg" width="240" height="300">


output :  
<img src="https://i.ibb.co/HHd37KT/obama-out.png">

## TODO::  

-  add images loading function (opencv and PIL)
-  add multiple faces detection for retina face model
-  add x1,y1,x2,y2 for detection module
-  add encoding feature
-  add shape drawing around faces 
-  add test scripts


## Release History

* 0.1.0
    * three detection models with one simple cropping module

## License 

MIT

## COPYRIGHT 

© Digified 2021