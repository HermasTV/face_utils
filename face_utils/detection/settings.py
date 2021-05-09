#!/usr/bin/env python3

"""settings.py: detection module settings file """

__author__ = "Ahmed Hermas"
__copyright__ = "Copyright 2021, © Digified "
__license__ = "MIT"
__version__ = "0.1.0"
__email__ = "a7medhermas@gmail.com"

MODELS_CONFIG = {
    'hog' : 
        {'loader':'_hog_cnn_loader',
         'detector':'_getface_hog_cnn'},
    'cnn':
        {'loader':'_hog_cnn_loader',
         'detector':'_getface_hog_cnn'},
    'retina':
        {'loader':'_retina_loader',
         'detector':'_getface_retina'},
    'cascade':
        {'loader':'_cascade_loader',
         'detector':'_getface_cascade'},
    
}