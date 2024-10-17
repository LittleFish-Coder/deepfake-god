from ast import arg
import dlib
import cv2
import os
import argparse

from numpy import argsort

# Load the pre-trained Dlib face detector model
detector = dlib.get_frontal_face_detector()

def process_video(video_path, size):
    output_dir = video_path.split('.')[0]
    file_name = output_dir.split('/')[-1]

    if os.path.exists(output_dir):
        print(f'Output directory {output_dir} already exists. Skipping processing of video: {video_path}')
        return
    else:
        os.makedirs(output_dir)

    print(f'Processing video: {video_path}')
    print(f'Create directory: {output_dir}')

    # Open the video file
    video_capture = cv2.VideoCapture(f"{video_path}")

    # Loop through each frame in the video
    counter = 0
    while video_capture.isOpened():
        # Capture frame-by-frame
        ret, frame = video_capture.read()
        
        if not ret:
            break  # End of video

        # Convert the frame to grayscale (Dlib works better with grayscale images)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = detector(gray)

        # Save the detected faces as 299x299 images
        for face in faces:
            try: 
                x, y, w, h = face.left(), face.top(), face.width(), face.height()
                face_image = frame[y:y+h, x:x+w]
                face_image_resized = cv2.resize(face_image, (size, size))
                cv2.imwrite(f'./{output_dir}/{file_name}_{counter}.jpg', face_image_resized)
                counter += 1
            except Exception as e:
                print(f'Error: {e}')
                print(f'skipping frame')

        if counter > 200:
            break

    # Release the video capture object and close any OpenCV windows
    video_capture.release()

if __name__ == '__main__':

    # add argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', type=str, default='Celeb-real', help='Directory containing the videos')
    parser.add_argument('--size', type=int, default=256, help='Size of the cropped image')
    args = parser.parse_args()

    dir = args.dir
    size = args.size
    print(os.listdir(dir))

    # iterate over all the videos
    for video in os.listdir(dir):
        # load the video
        video_path = f'{dir}/{video}'
        process_video(video_path, size)
