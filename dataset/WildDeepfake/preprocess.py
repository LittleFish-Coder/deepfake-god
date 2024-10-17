import tarfile
import os 
import shutil


def extract_tar_gz(input_file, output_dir):
    try:
        with tarfile.open(input_file, 'r:') as tar:
                tar.extractall(path=output_dir)
    except tarfile.ReadError:
        print(f"Error: {input_file} is not a regular tar file. Skipping.")

if __name__ == '__main__':

    input_dirs = [
                './deepfake_in_the_wild/fake_test/',
                './deepfake_in_the_wild/fake_train/', 
                './deepfake_in_the_wild/real_test/',
                './deepfake_in_the_wild/real_train/'
                ]
    output_dirs = [
                './extracted/fake_test/', 
                './extracted/fake_train/', 
                './extracted/real_test/', 
                './extracted/real_train/'
                ]
    for output_dir in output_dirs:
        os.makedirs(output_dir, exist_ok=True)

    for input_dir, output_dir in zip(input_dirs, output_dirs):
        for filename in os.listdir(input_dir):
            if filename.endswith(".tar.gz"):
                input_file = os.path.join(input_dir, filename)
                extract_tar_gz(input_file, input_dir)

        # move all files from the input folder to the output folder
        for celeb in os.listdir(input_dir):
            if not os.path.isdir(os.path.join(input_dir, celeb)):
                continue
            for label_folder in os.listdir(os.path.join(input_dir, celeb)):
                for video_id_folder in os.listdir(os.path.join(input_dir, celeb, label_folder)):
                    os.makedirs(os.path.join(output_dir, celeb), exist_ok=True)
                    # move the video_id_folder to the output_dir/celeb
                    print(f"Moving {os.path.join(input_dir, celeb, label_folder, video_id_folder)} to {output_dir}/{celeb}")
                    shutil.move(os.path.join(input_dir, celeb, label_folder, video_id_folder), os.path.join(output_dir, celeb, video_id_folder))