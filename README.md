# FaceAnonymizer-MediaPipe
face anonymization of an image or video using MediaPipe

part of my journey of understanding opencv

to use:
- clone repository
- run `pip install -r requirements.txt` to install required modules (preferably in a virtual environment)
- put the image or video files you want to anonymize inside the `data` folder
- for images -> run command 
    `python anonymizer.py image --filepath {path_to_image}`
- for videos -> run command
    `python anonymizer.py video --filepath {path_to_video}`
- media with added anonymization will be added to the  `output-dir` folder


notes: currently only tested .jpg image formats and mp4, mkv and mov video formats


to do:
- more exception handling
- check for other image extension types
- add gpu acceleration 
- documentation

