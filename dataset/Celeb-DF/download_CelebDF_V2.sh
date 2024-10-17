# command to run: bash download_CelebDF_V2.sh
# If you are unable to download the dataset using the command
# you can directly download the dataset from the following link:
# https://drive.google.com/uc?id=1iLx76wsbi9itnkxSqz9BVBl4ZvnbIazj

#!/bin/bash
FILE_ID="1iLx76wsbi9itnkxSqz9BVBl4ZvnbIazj"
FILE_NAME="Celeb-DF(v2).zip"

# Check if gdown is installed, and install it if not
if ! command -v gdown &> /dev/null
then
    echo "gdown could not be found, installing..."
    pip install gdown
else
    echo "gdown is already installed"
fi

# Check if FILE_NAME already exists
if [ -f $FILE_NAME ]; then
    echo "$FILE_NAME already exists"
    exit 0
fi

# Download the dataset
echo "Downloading Celeb-DF(v2) dataset..."
gdown $FILE_ID -O $FILE_NAME

# unzip the dataset
echo "Unzipping $FILE_NAME..."
unzip -q $FILE_NAME