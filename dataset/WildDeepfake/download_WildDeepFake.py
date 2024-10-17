import gdown

# WildDeepFake dataset googlde drive link
gdrive_folder_link = 'https://drive.google.com/drive/folders/1Cb_OqksBU3x7HFIo8EvDTigU6IjM7tmp'

gdown.download_folder(gdrive_folder_link, quiet=True)

# if error occurs, try to download the dataset manually from the link above