#!/usr/bin/env python3

"""cropping.py: the image cropping module."""

__author__ = "Ahmed Hermas"
__copyright__ = "Copyright 2021, © Digified "
__license__ = "MIT"
__version__ = "0.1.0"
__email__ = "a7medhermas@gmail.com"

from cv2 import cv2
import numpy as np


def _get_new_box(src_w, src_h, bbox, scale):
    """ change the new face boundries into based on the zoomout scale

        Args:
            src_w (int): Original Image width
            src_h (int): Original Image height
            bbox (tuple): face boundries in (xywh) format 
            scale (float): the zoomout scale

        Returns:
            [tuple]: the new face boundries
        """
    x = bbox[0]
    y = bbox[1]
    box_w = bbox[2]
    box_h = bbox[3]

    scale = min((src_h-1)/box_h, min((src_w-1)/box_w, scale))

    new_width = box_w * scale
    new_height = box_h * scale
    center_x, center_y = box_w/2+x, box_h/2+y

    left_top_x = center_x-new_width/2
    left_top_y = center_y-new_height/2
    right_bottom_x = center_x+new_width/2
    right_bottom_y = center_y+new_height/2

    if left_top_x < 0:
        right_bottom_x -= left_top_x
        left_top_x = 0

    if left_top_y < 0:
        right_bottom_y -= left_top_y
        left_top_y = 0

    if right_bottom_x > src_w-1:
        left_top_x -= right_bottom_x-src_w+1
        right_bottom_x = src_w-1

    if right_bottom_y > src_h-1:
        left_top_y -= right_bottom_y-src_h+1
        right_bottom_y = src_h-1

    return int(left_top_x), int(left_top_y),\
            int(right_bottom_x), int(right_bottom_y)

def crop(org_img, bbox, zoom_out, out_w=None, out_h=None):
    """ face cropping function,takes an image and return face cropped image

        Args:
            org_img (np array): Original Image
            bbox (tuple): face boundries in (xywh) format
            zoom_out (float): How zoomed out the face, 
            out_w (int): the output image width
            out_h (int): the output image height

        Returns:
            [np array]: the output face image
        """
    #get the shape of the image
    src_h, src_w, _ = np.shape(org_img)
    # get the new face boundries
    left_top_x, left_top_y, \
        right_bottom_x, right_bottom_y = _get_new_box(src_w, src_h, bbox, scale)
    #crop the image based on thge new boundries
    dst_img = org_img[left_top_y: right_bottom_y+1,
                    left_top_x: right_bottom_x+1]
    # check if you need to change the output image shape
    if out_w and out_h :
        
        dst_img = cv2.resize(img, (out_w, out_h))
    
    return dst_img