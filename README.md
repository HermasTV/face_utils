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
pip install face_utils
```


## Features

### Face Detection 

```python 
import cv2
from face_utils import Detector
imgPath = "path_to_image" 
img = cv2.imread(imgPath)
model = Detector("retina")
model.detect(img,2)
```

### Face cropping 



## TODO::  

- [ ] add images loading function (opencv and PIL)
- [ ] add multiple faces detection for retina face model
- [ ] add x1,y1,x2,y2 for detection module
- [ ] add encoding feature
- [ ] add shape drawing around faces 


## Release History

* 0.0.1
    * minimal workable features



