import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import models, transforms
from torchvision.models import ResNet18_Weights
from zmq import device
from data.video_dataset import VideoFrameDataset
from tqdm import tqdm
import numpy as np

device  = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Define the transformation
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225])
])

# Initialize dataset and dataloader
train_dataset = VideoFrameDataset(root_dir='./dataset/WildDeepfake', split='train', transform=transform)
train_loader = DataLoader(train_dataset, batch_size=256, shuffle=True, num_workers=4)

# Initialize dataset and dataloader
test_dataset = VideoFrameDataset(root_dir='./dataset/WildDeepfake', split='test', transform=transform)
test_loader = DataLoader(test_dataset, batch_size=256, shuffle=False, num_workers=4)

print(f'Train dataset size: {len(train_dataset)}')
print(f'Test dataset size: {len(test_dataset)}')

# Define the model
model = models.resnet18(weights=ResNet18_Weights.DEFAULT)
model.fc = nn.Linear(model.fc.in_features, 2)  # Assuming binary classification (real vs fake)
model = model.to(device)

# Define loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001) # type: ignore

# Training loop
num_epochs = 2
model.train()
for epoch in range(num_epochs):
    running_loss = 0.0
    for images, labels, video_ids in tqdm(train_loader):
        optimizer.zero_grad()
        images = images.to(device)
        labels = labels.to(device)
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        running_loss += loss.item()
    print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {running_loss/len(train_loader):.4f}')

# Evaluation loop
print('Evaluating model...')
model.eval()
video_predictions = {}
with torch.no_grad():
    for images, labels, video_ids in test_loader:
        images = images.to(device)
        labels = labels.to(device)
        outputs = model(images)
        probabilities = nn.Softmax(dim=1)(outputs)[:, 1]  # Probability of being fake
        for video_id, prob in zip(video_ids, probabilities):
            if video_id not in video_predictions:
                video_predictions[video_id] = []
            video_predictions[video_id].append(prob.item())

# Aggregate predictions for each video
final_predictions = {}
for video_id, probs in video_predictions.items():
    avg_prob = np.mean(probs)
    final_predictions[video_id] = avg_prob

# Print final predictions
for video_id, avg_prob in final_predictions.items():
    print(f'Video ID: {video_id}, Average Probability of Fake: {avg_prob:.4f}')



