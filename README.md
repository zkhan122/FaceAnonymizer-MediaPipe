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

![sample-video2](https://github.com/user-attachments/assets/2bc252c3-a39c-460d-b54e-9d8d855dc73e)



### After

![sample-video2-anon](https://github.com/user-attachments/assets/1fc572b9-9af2-4ed7-a9c6-3d638c73da8b)




notes: currently only tested jpeg image formats and mp4, mkv, mov video formats


to do:
- more exception handling
- check for other image extension types
- add gpu acceleration 
- documentation

