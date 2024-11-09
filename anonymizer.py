import os
import cv2
import mediapipe as mp
import argparse
from pathlib import Path


def process_img(image, face_detection):
    IMAGE_HEIGHT, IMAGE_WIDTH, _ = image.shape # 3-dimensionsal image (height, width and depth)
    img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    output = face_detection.process(img_rgb)

    print(output.detections) # prints the bounding box as well as keypoints (facial landmarks)

    # checking to see if the detection output is not None (if no human face is detected in the images)
    if output.detections is not None:
        for detection in output.detections:
            location_data = detection.location_data
            bounding_box = location_data.relative_bounding_box
            x1, y1, w, h = bounding_box.xmin, bounding_box.ymin, bounding_box.width, bounding_box.height # grabbing the bounding box

            x1 = int(x1 * IMAGE_WIDTH) # make the values relative to bounding box
            y1 = int(y1 * IMAGE_HEIGHT)
            w = int(w * IMAGE_WIDTH)
            h = int(h * IMAGE_HEIGHT)

            # image_bounded = cv2.rectangle(image, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 10)
            # image = image_bounded
            # blurring the face
            image[y1:y1+h, x1:x1+w, :] = cv2.blur(src=image[y1:y1+h, x1:x1+w, :], ksize=(30, 30)) # kernel size is the amount of blur applied (transformation matrix applied)

            # cv2.imshow("img", image)

    return image

def main():
    args = argparse.ArgumentParser()

    required = args.add_argument_group("required arguments")
    required.add_argument("mode", help=["image | video"])
    args.add_argument("--filepath", default=None)
    args = args.parse_args()

    if not Path(args.filepath).is_file():
        print("\nNO SUCH FILE EXISTS FOR PATH SPECIFIED")
        raise SystemExit(0)


    OUTPUT_DIR = "./output-dir"
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    mp_face_detection = mp.solutions.face_detection
    
    filename, file_extension = os.path.splitext(os.path.basename(args.filepath))


    # print(mp_face_detection)

    # https://mediapipe.readthedocs.io/en/latest/solutions/face_detection.html -> only works for human faces else ERROR
    with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection: # creating new mediapipe object params=(0 for faces close to camera), CI thresold = 96&

        if args.mode == "image":
            image = cv2.imread(args.filepath)
            image = process_img(image, face_detection=face_detection)
            # saving the image
            cv2.imwrite(filename=os.path.join(OUTPUT_DIR, os.path.splitext(os.path.basename(args.filepath))[0] + "-anon.jpg"), img=image)   

        elif args.mode == "video":

            if file_extension == ".mp4" or ".mov" or ".mkv":

                capture = cv2.VideoCapture(args.filepath)
                ret, frame = capture.read()

                output_video = cv2.VideoWriter(os.path.join(OUTPUT_DIR, os.path.splitext(os.path.basename(args.filepath))[0] + "-anon" + file_extension), 
                                        cv2.VideoWriter_fourcc(*"MP4V"),
                                        30,
                                        (frame.shape[1], frame.shape[0])) # specifying 30 fps for anonymized video

                while ret & capture.isOpened():
                    ret, frame = capture.read()

                    # check for if video ends or reads
                    if ret is None or frame is None:
                        break

                    frame = process_img(frame, face_detection=face_detection) # each frame can be seen as a 3 dimensional image 
                    cv2.imshow("Video", frame)
                    output_video.write(frame)

                    if cv2.waitKey(1) & 0xFF == ord("q"):
                        break

                print("\nMedia has finished processing. Anonymization process complete.")

                capture.release()
                output_video.release()
                cv2.destroyAllWindows
            
             # cv2.waitKey(0)
        else:
            print("Check you are specifying the correct mode and file extension")

if __name__== "__main__":
    main()