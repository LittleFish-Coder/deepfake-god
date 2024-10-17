# Download FaceForensics++ Dataset

Run the following command to download the dataset in the background:

```bash
nohup bash download_ffpp_batch.sh &
```

or directly download the dataset from official python script:

```bash
python faceforensics_download_v4.py ./ -d original -c c23 -t videos --server EU2
```

## Subdatasets to download
In FF++ paper, the below subdatasets are used (Must be downloaded):

`original`, `Deepfakes`, `Face2Face`, `FaceSwap`, `NeuralTextures`

but there exists more subdatasets in the dataset (optional):

`DeepFakeDetection_original`, `DeepFakeDetection`, `FaceShifter`

## Arguments
- `-h:` help
- `-d:` dataset version ['original', 'DeepFakeDetection_original', 'Deepfakes', 'DeepFakeDetection', 'Face2Face', 'FaceShifter', 'FaceSwap', 'NeuralTextures']
- `-c:` compression level ['raw', 'c23', 'c40']
- `-t:` data type ['videos', 'masks', 'models']
- `--server:` server location ['EU', 'EU2', 'CA']
