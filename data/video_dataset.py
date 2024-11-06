import os
from PIL import Image
import torch
from torch.utils.data import Dataset
from torchvision import transforms


class VideoFrameDataset(Dataset):
    def __init__(self, root_dir, split="train", transform=transforms.Compose([transforms.ToTensor()])):
        """
        Args:
            root_dir (str): Root directory of the dataset
            split (str): 'train' or 'test'
            transform: Optional transform to be applied on images
        """
        self.root_dir = root_dir
        self.split = split
        self.transform = transform

        # Label encoding
        self.label_to_idx = {"real": 0, "fake": 1}

        # Get all image paths, labels, and video_ids
        self.image_paths = []
        self.labels = []
        self.video_ids = []
        self._load_dataset()

    def _load_dataset(self):
        """Load all image paths, labels, and video_ids for the specified split"""
        split_dir = os.path.join(self.root_dir, self.split)

        for label in ["real", "fake"]:
            label_dir = os.path.join(split_dir, label)
            if not os.path.exists(label_dir):
                continue

            # Iterate through video folders
            for video_folder in sorted(os.listdir(label_dir)):
                video_path = os.path.join(label_dir, video_folder)

                # Skip if not a directory
                if not os.path.isdir(video_path):
                    continue

                # Get all frames in the video folder
                for frame in sorted(os.listdir(video_path)):
                    if frame.endswith((".jpg", ".png", ".jpeg")):
                        frame_path = os.path.join(video_path, frame)
                        self.image_paths.append(frame_path)
                        self.labels.append(self.label_to_idx[label])
                        self.video_ids.append(video_folder)

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, idx) -> tuple:
        """
        Args:
            idx (int): Index
        Returns:
            tuple: (image, label, video_id) where label is 0 for real and 1 for fake
        """
        # Load image
        img_path = self.image_paths[idx]
        try:
            image = Image.open(img_path).convert("RGB")
        except Exception as e:
            print(f"Error loading image {img_path}: {str(e)}")
            # Return a black image in case of error
            image = Image.new("RGB", (224, 224))

        try:
            image = self.transform(image)
        except Exception as e:
            print(f"Error applying transform to {img_path}: {str(e)}")
            # Return a tensor of zeros in case of transform error
            image = torch.zeros((3, 224, 224))

        # Get label and video_id
        label = self.labels[idx]
        video_id = self.video_ids[idx]

        return image, label, video_id

    def get_labels(self):
        """Returns list of all labels"""
        return self.labels

    def get_class_weights(self):
        """Calculate class weights for imbalanced dataset"""
        label_counts = torch.bincount(torch.tensor(self.labels))
        total = len(self.labels)
        class_weights = total / (len(label_counts) * label_counts.float())
        return class_weights


if __name__ == "__main__":
    # Example usage with transforms
    transform = transforms.Compose(
        [
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ]
    )

    # Initialize dataset
    dataset = VideoFrameDataset(root_dir="../dataset/WildDeepfake", split="train", transform=transform)

    # Print dataset info
    print(f"Dataset size: {len(dataset)}")

    # Get first sample
    image, label, video_id = dataset[0]
    print(f"Image shape: {image.shape}")
    print(f"Label: {label} ({'real' if label == 0 else 'fake'})")
    print(f"Video ID: {video_id}")

    # Calculate and print class distribution
    total_samples = len(dataset)
    real_samples = sum(1 for label in dataset.get_labels() if label == 0)
    fake_samples = total_samples - real_samples

    print(f"\nClass distribution:")
    print(f"Real samples: {real_samples} ({real_samples/total_samples*100:.2f}%)")
    print(f"Fake samples: {fake_samples} ({fake_samples/total_samples*100:.2f}%)")

    # Get class weights
    class_weights = dataset.get_class_weights()
    print(f"\nClass weights:")
    print(f"Real: {class_weights[0]:.4f}")
    print(f"Fake: {class_weights[1]:.4f}")
