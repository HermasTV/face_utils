import argparse
import os
import numpy as np
from cv2 import cv2
from face_utils.detection import Detector
from face_utils.cropping import cropping


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = False, help = "Path to the input image")
ap.add_argument("-d", "--model", required = False, help = "detector model",default='hog')
ap.add_argument("-s", "--size", required = False, help = "the output size",default=128,type=int)
ap.add_argument("-o", "--out", required = True, help = "Path to out folder")
ap.add_argument("-f", "--folder", required = False, help = "Path to input folder")


args = ap.parse_args()

def detectImage(inPath,outFolder,model,size):
    
    image = cv2.imread(inPath)
    img= np.array(image)
    bbox = model.detect(img,2) #using (x,y,w,h) return mode
    outImg = cropping.crop(img,bbox,1,size,size)
    outFile = os.path.basename(inPath).split('.')[0]+"_out.jpg"
    outPath = os.path.join(outFolder,outFile)
    cv2.imwrite(outPath,outImg)
    
if __name__ == "__main__":
    
    modelName = args.model
    model = Detector(modelName)
    outFolder = args.out
    size = args.size
    
    if 'image' in args : 
        imgPath = args.image
        detectImage(imgPath,outFolder,model,size)
        
    else: 
        for file in os.listdir(args.folder):
            imgPath = os.path.join(args.folder,file)
            detectImage(imgPath,outFolder,model,size)