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