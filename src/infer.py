# src/infer.py

import torch
import torch.nn as nn
from torchvision import transforms
from torchvision.models import resnet18
from PIL import Image
import argparse

# --- Load model ---
def load_model(weights_path, device):
    model = resnet18(weights=None)
    model.fc = nn.Linear(model.fc.in_features, 1)
    model.load_state_dict(torch.load(weights_path, map_location=device))
    model.to(device)
    model.eval()
    return model

# --- Preprocess Image ---
def preprocess_image(image_path):
    transform = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.ToTensor()
    ])
    image = Image.open(image_path).convert("RGB")
    return transform(image).unsqueeze(0)

# --- Inference Function ---
def predict(model, image_tensor, device):
    with torch.no_grad():
        image_tensor = image_tensor.to(device)
        output = model(image_tensor)
        prob = torch.sigmoid(output).item()
        pred = 1 if prob > 0.5 else 0
    return pred, prob

# --- Main Entry Point ---
def main():
    parser = argparse.ArgumentParser(description="Invoice Fraud Detection Inference")
    parser.add_argument("image_path", type=str, help="Path to invoice image")
    parser.add_argument("--weights", type=str, default="outputs/resnet_invoice.pt", help="Path to model weights")
    args = parser.parse_args()

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = load_model(args.weights, device)
    image_tensor = preprocess_image(args.image_path)
    pred, prob = predict(model, image_tensor, device)

    label = "Tampered ❌" if pred == 1 else "Real ✅"
    print(f"\n📄 Invoice: {args.image_path}")
    print(f"📢 Prediction: {label} (Confidence: {prob:.4f})")

if __name__ == "__main__":
    main()
