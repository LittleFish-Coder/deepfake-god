import dlib
import cv2
import os
import random

# Load the pre-trained Dlib face detector model
detector = dlib.get_frontal_face_detector()

def find_face_loop(total_frames , video_capture , output_dir , counter ):
    found_face = False
    while not found_face:
        random_frame_index = random.randint(0, total_frames - 1)
        video_capture.set(cv2.CAP_PROP_POS_FRAMES, random_frame_index)
        ret, random_frame = video_capture.read()
        if ret:
            # Convert the random frame to grayscale for face detection
            gray_random_frame = cv2.cvtColor(random_frame, cv2.COLOR_BGR2GRAY)
            faces_random = detector(gray_random_frame)

            if faces_random:
                # Save the randomly selected frame with a detected face
                x, y, w, h = faces_random[0].left(), faces_random[0].top(), faces_random[0].width(), faces_random[0].height()
                face_image_random = random_frame[y:y+h, x:x+w]
                if face_image_random.size > 0:
                    face_image_resized_random = cv2.resize(face_image_random, (size, size))
                    cv2.imwrite(f'{output_dir}/{counter}.jpg', face_image_resized_random)
                    counter += 1
                    found_face = True  # Exit the loop once a face is found
    return counter

def process_video(input_file, size , output_dir):

    counter = 0
    current_counter = 0
    for filename in os.listdir(output_dir):
        current_counter += 1
    if current_counter < 200 :
        counter = current_counter
    else :
        return 

    # Open the video file
    video_capture = cv2.VideoCapture(input_file)

    total_frames = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = video_capture.get(cv2.CAP_PROP_FPS)

    # Calculate total duration in seconds
    total_duration = total_frames / fps

    # Calculate interval duration to capture 200 frames
    interval_duration = total_duration / 200

    while video_capture.isOpened() and counter < 200:

        time_to_capture = counter * interval_duration
        video_capture.set(cv2.CAP_PROP_POS_MSEC, time_to_capture * 1000)
        ret, frame = video_capture.read()
        
        if not ret:
            break  # End of video

        # Convert the frame to grayscale (Dlib works better with grayscale images)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = detector(gray)
        # Save the detected faces as size*size images
        if faces :
            try: 
                x, y, w, h = faces[0].left(), faces[0].top(), faces[0].width(), faces[0].height()
                face_image = frame[y:y+h, x:x+w]
                if face_image.size > 0:  # Check if the face image is not empty
                    face_image_resized = cv2.resize(face_image, (size, size))
                    cv2.imwrite(f'{output_dir}/{counter}.jpg', face_image_resized)
                    counter += 1
                else :
                    counter = find_face_loop(total_frames , video_capture , output_dir , counter)
            except Exception as e:
                print(f'Error: {e}')
                print(f'skipping frame')
        else:
            counter = find_face_loop(total_frames , video_capture , output_dir , counter)
            

    # Release the video capture object and close any OpenCV windows
    video_capture.release()

if __name__ == '__main__':

    size = 224

    input_dirs = [
        './original_sequences/youtube/c23/videos/',
        './manipulated_sequences/Deepfakes/c23/videos',
        './manipulated_sequences/Face2Face/c23/videos',
        './manipulated_sequences/FaceSwap/c23/videos',
        './manipulated_sequences/NeuralTextures/c23/videos'
    ]

    output_dirs = [
        './result/true/original_sequences/',
        './result/fake/Deepfakes/',
        './result/fake/Face2Face/',
        './result/fake/FaceSwap/',
        './result/fake/NeuralTextures/'
    ]

    for output_dir in output_dirs:
        os.makedirs(output_dir, exist_ok=True)

    for input_dir, output_dir in zip(input_dirs, output_dirs):
        for filename in os.listdir(input_dir):
            if filename.endswith(".mp4"):
                input_file = os.path.join(input_dir, filename)
                print(input_file)
                output_dir_name = os.path.splitext(os.path.splitext(filename)[0])[0]
                final_output_dir = os.path.join(output_dir, output_dir_name)
                os.makedirs(final_output_dir, exist_ok=True)
                process_video(input_file,size,final_output_dir)

