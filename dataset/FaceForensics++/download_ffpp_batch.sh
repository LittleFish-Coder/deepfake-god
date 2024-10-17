#!/bin/bash

# The FaceForensics++ dataset consists of the following manipulated datasets:
ALL_DATASETS=("original" "DeepFakeDetection_original" "Deepfakes" 
              "DeepFakeDetection" "Face2Face" "FaceShifter" "FaceSwap" 
              "NeuralTextures")

# Compression levels for the videos
# c23(hq original sequence images/videos)
# c40(lq original sequence images/videos)
COMPRESSION=("c23", "c40")

# Run the faceforensics_download_v4.py script with the specified parameters

## Download 'original' dataset
echo "Downloading 'original' dataset"
echo "" | python faceforensics_download_v4.py ./ -d original -c c23 -t videos --server EU2

## Download 'Deepfakes' dataset
echo "Downloading 'Deepfakes' dataset"
echo "" | python faceforensics_download_v4.py ./ -d Deepfakes -c c23 -t videos --server EU2

## Download 'Face2Face' dataset
echo "Downloading 'Face2Face' dataset"
echo "" | python faceforensics_download_v4.py ./ -d Face2Face -c c23 -t videos --server EU2

## Download 'FaceSwap' dataset
echo "Downloading 'FaceSwap' dataset"
echo "" | python faceforensics_download_v4.py ./ -d FaceSwap -c c23 -t videos --server EU2

## Download 'NeuralTextures' dataset
echo "Downloading 'NeuralTextures' dataset"
echo "" | python faceforensics_download_v4.py ./ -d NeuralTextures -c c23 -t videos --server EU2

# ================================================================================================= #
# Below datasets are not mentioned in the FF++ Dataset paper, but are available for download
# "DeepFakeDetection_original", "DeepFakeDetection", "FaceShifter"
# ================================================================================================= #
# You can download them by uncommenting the below lines

## Download 'DeepFakeDetection_original' dataset
# echo "Downloading 'DeepFakeDetection_original' dataset"
# echo "" | python faceforensics_download_v4.py ./ -d DeepFakeDetection_original -c c23 -t videos --server EU2

## Download 'DeepFakeDetection' dataset
# echo "Downloading 'DeepFakeDetection' dataset"
# echo "" | python faceforensics_download_v4.py ./ -d DeepFakeDetection -c c23 -t videos --server EU2

## Download 'FaceShifter' dataset
# echo "Downloading 'FaceShifter' dataset"
# echo "" | python faceforensics_download_v4.py ./ -d FaceShifter -c c23 -t videos --server EU2
