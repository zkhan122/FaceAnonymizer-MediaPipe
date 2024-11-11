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

Example:

### Before



https://github.com/user-attachments/assets/d8f1572b-49b8-492d-99fc-c0fda22b75a1


### After


https://github.com/user-attachments/assets/8e4249b4-0c7b-410c-b66d-89562c12e93c




notes: currently only tested jpeg image formats and mp4, mkv, mov video formats


to do:
- more exception handling
- check for other image extension types
- add gpu acceleration 
- documentation

