import tarfile
import os 


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
                output_dir_name = os.path.splitext(os.path.splitext(filename)[0])[0]
                final_output_dir = os.path.join(output_dir, output_dir_name)
                os.makedirs(final_output_dir, exist_ok=True)
                extract_tar_gz(input_file, final_output_dir)

