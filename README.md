# DeepFake Graph-Oriented Detector (DeepFake GOD)

## Dataset
| Dataset | Official Site | Download Link | Size |
| --- | --- | --- | --- |
| FaceForensics++ | [GitHub](https://github.com/ondyari/FaceForensics) | [Link](https://kaldir.vc.in.tum.de/faceforensics_download_v4.py) | --- |
| DFDC | [Meta](https://ai.meta.com/datasets/dfdc/) | [Link](https://ai.meta.com/datasets/dfdc/) | --- |
| Celeb-DF | [GitHub](https://github.com/yuezunli/celeb-deepfakeforensics) | [Link](https://drive.google.com/uc?id=1iLx76wsbi9itnkxSqz9BVBl4ZvnbIazj) | 10G |
| WildDeepfake | [GitHub](https://github.com/OpenTAI/wild-deepfake) | [Link](https://drive.google.com/drive/folders/1Cb_OqksBU3x7HFIo8EvDTigU6IjM7tmp) | 13G |

## Installation

0. Create a new conda environment

```bash
conda create -n deepfake-god python=3.12
conda activate deepfake-god
```

1. Install PyTorch (with CUDA 12.1) [(Official Doc)](https://pytorch.org/get-started/locally/)

```bash
conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia
```

2. Install PyTorch Geometric [(Official Doc)](https://pytorch-geometric.readthedocs.io/en/latest/install/installation.html)

```bash
pip install torch-geometric
```

3. Install Additional Libraries for GNN (Based on your environment)

```bash
pip install pyg_lib torch_scatter torch_sparse torch_cluster torch_spline_conv -f https://data.pyg.org/whl/torch-2.4.0+cu121.html
```

4. Install Other Packages

```bash
pip install -r requirements.txt
```