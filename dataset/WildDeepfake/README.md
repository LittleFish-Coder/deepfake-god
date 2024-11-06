# WildDeepfake

1. Download Dataset
```bash
python download_WildDeepfake.py
```

2. Preprocess Dataset

This will extract the zip files and export to a new folder
```bash
python preprocess.py
```

3. Reorganize Dataset

This will reorganize the dataset better for PyTorch Dataset Structure
```bash
python reorganize_dataset.py
```