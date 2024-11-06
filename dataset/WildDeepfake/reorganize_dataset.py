import os
import shutil
from glob import glob
from pathlib import Path

def create_directory_structure(base_path):
    """Create the required directory structure"""
    for split in ['train', 'test']:
        for label in ['real', 'fake']:
            os.makedirs(os.path.join(base_path, split, label), exist_ok=True)

def organize_dataset(source_path, dest_path):
    """
    Organize dataset from extracted folder structure into train/test splits
    
    Args:
        source_path: Path to source 'extracted' folder
        dest_path: Path to destination dataset
    """
    # Create directory structure
    create_directory_structure(dest_path)
    
    # Process each source folder
    source_folders = {
        ('train', 'fake'): os.path.join(source_path, 'fake_train'),
        ('train', 'real'): os.path.join(source_path, 'real_train'),
        ('test', 'fake'): os.path.join(source_path, 'fake_test'),
        ('test', 'real'): os.path.join(source_path, 'real_test')
    }
    
    video_counter = {
        ('train', 'fake'): 1,
        ('train', 'real'): 1,
        ('test', 'fake'): 1,
        ('test', 'real'): 1
    }
    
    for (split, label), folder_path in source_folders.items():
        if not os.path.exists(folder_path):
            print(f"Warning: {folder_path} does not exist, skipping...")
            continue
            
        # Walk through all subfolders
        for root, _, files in os.walk(folder_path):
            if not files:  # Skip empty directories
                continue
                
            # Only process PNG files
            png_files = [f for f in files if f.endswith('.png')]
            if not png_files:
                continue
                
            # Create new video folder
            video_folder = f'video_{video_counter[(split, label)]:03d}'
            dest_video_path = os.path.join(dest_path, split, label, video_folder)
            os.makedirs(dest_video_path, exist_ok=True)
            
            # Copy all PNG files from this folder with renamed frames
            for idx, png_file in enumerate(sorted(png_files), 1):
                src_path = os.path.join(root, png_file)
                dest_frame = f'frame_{idx:03d}.jpg'
                dest_path_full = os.path.join(dest_video_path, dest_frame)
                shutil.copy2(src_path, dest_path_full)
            
            video_counter[(split, label)] += 1
            
            # Print progress
            print(f"Processed {video_folder} in {split}/{label}")

if __name__ == '__main__':
    source_path = './extracted'  # Path to your extracted folder
    dest_path = './'            # Path where you want the organized dataset
    
    # Create and organize dataset
    organize_dataset(source_path, dest_path)
    print("Dataset reorganization complete!")
    
    # Print summary
    for split in ['train', 'test']:
        for label in ['real', 'fake']:
            path = os.path.join(dest_path, split, label)
            num_videos = len(os.listdir(path))
            print(f"{split}/{label}: {num_videos} videos")