# DeepFake Dataset Download

## Label

We uniformly use the following labels for all datasets:

- `0`: Real
- `1`: Fake

## Dataset
| Dataset | Official Site | Download Link | Size |
| --- | --- | --- | --- |
| FaceForensics++ | [GitHub](https://github.com/ondyari/FaceForensics) | [Link](https://kaldir.vc.in.tum.de/faceforensics_download_v4.py) | --- |
| DFDC | [Meta](https://ai.meta.com/datasets/dfdc/) | [Link](https://ai.meta.com/datasets/dfdc/) | --- |
| Celeb-DF | [GitHub](https://github.com/yuezunli/celeb-deepfakeforensics) | [Link](https://drive.google.com/uc?id=1iLx76wsbi9itnkxSqz9BVBl4ZvnbIazj) | 10G |
| WildDeepfake | [GitHub](https://github.com/OpenTAI/wild-deepfake) | [Link](https://drive.google.com/drive/folders/1Cb_OqksBU3x7HFIo8EvDTigU6IjM7tmp) | 13G |

## Remind

change the `MAX_NUMBER_FILES = 1000000` in `gdown.download_folder` to maximize the number of files to download.