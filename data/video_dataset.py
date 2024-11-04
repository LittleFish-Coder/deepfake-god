import os
from PIL import Image
from torch.utils.data import Dataset

class VideoFrameDataset(Dataset):
    def __init__(self, root_dir, transform=None):
        self.root_dir = root_dir
        self.transform = transform
        self.image_paths = self._get_image_paths()

    def _get_image_paths(self):
        image_paths = []
        for split in ['train', 'val', 'test']:
            for label in ['real', 'fake']:
                label_dir = os.path.join(self.root_dir, split, label)
                for video_id in os.listdir(label_dir):
                    video_path = os.path.join(label_dir, video_id)
                    for img_file in os.listdir(video_path):
                        if img_file.endswith(('.png', '.jpg', '.jpeg')):
                            image_paths.append((os.path.join(video_path, img_file), label))
        return image_paths

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, idx):
        img_path, label = self.image_paths[idx]
        image = Image.open(img_path).convert("RGB")
        
        if self.transform:
            image = self.transform(image)

        return image, label  # Return image and its label (real or fake)