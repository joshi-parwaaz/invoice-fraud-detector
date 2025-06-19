import streamlit as st
import torch
import torch.nn as nn
from torchvision import transforms
from torchvision.models import resnet18
from PIL import Image

# Title and description
st.title("🧾 Invoice Tampering Detector")
st.markdown("Upload an invoice image to check if it’s **tampered** or **real**.")

# Load model
@st.cache_resource
def load_model():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = resnet18(weights=None)
    model.fc = nn.Linear(model.fc.in_features, 1)
    model.load_state_dict(torch.load("outputs/resnet_invoice.pt", map_location=device))
    model.to(device)
    model.eval()
    return model, device

model, device = load_model()

# Preprocessing
transform = transforms.Compose([
    transforms.Resize((256, 256)),
    transforms.ToTensor()
])

# Upload image
uploaded_file = st.file_uploader("Upload Invoice", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Invoice", use_container_width=True)

    # Predict
    tensor = transform(image).unsqueeze(0).to(device)
    with torch.no_grad():
        output = model(tensor)
        prob = torch.sigmoid(output).item()
        pred = 1 if prob > 0.5 else 0

    label = "Tampered ❌" if pred == 1 else "Real ✅"
    st.subheader(f"📢 Prediction: {label}")
    st.write(f"Confidence: `{prob:.4f}`")
