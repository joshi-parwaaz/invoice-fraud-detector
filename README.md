### 📦 Dataset Attribution

This project uses the **FUTURA Synthetic Invoices Dataset**, publicly available via Zenodo:

> **FUTURA - Synthetic Invoices Dataset for Document Analysis**  
> Authors: Dimosthenis Karatzas, Fei Chen, Davide Fichera, Diego Marchetti  
> License: [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)  
> DOI: [https://doi.org/10.5281/zenodo.10371464](https://doi.org/10.5281/zenodo.10371464)  
> Accessed via Zenodo. Redistribution and derivative works must credit the original authors.


# 🧾 Invoice Tampering Detection using CNN

Detect tampered or fake invoice images using a Convolutional Neural Network (CNN) trained on a custom dataset of real and synthetically altered invoices.
Check deployed web application here:
https://invoice-fraud-detector-ce58ouovow9hboanjvunul.streamlit.app/

---

## 🚀 Project Overview

This project applies computer vision and deep learning to detect whether an invoice has been **tampered** with. It includes:

- Custom dataset with **10,000 real** + **600 tampered** invoices
- Image preprocessing, EDA, and synthetic tamper generation
- A fine-tuned **ResNet18** model trained using PyTorch
- Deployment-ready inference script + Streamlit frontend

---

## 🗂️ Directory Structure

cnn-invoice-fraud-detector/
│
├── data/ # Raw and processed invoice data
│ ├── real/ # Real invoice images
│ ├── tampered/ # Synthetic tampered invoices
│ └── processed/ # Memory-efficient .npy files
│
├── notebooks/ # Step-by-step notebooks
│ ├── 01_eda_preprocessing.ipynb
│ ├── 02_train_model.ipynb
│ ├── 03_evaluation.ipynb
│ └── 04_inference.ipynb
│
├── outputs/ # Model and visual outputs
│ ├── resnet_invoice.pt # Trained model weights
│ └── tampered_examples/ # Example visual comparisons
│
├── src/ # Supporting Python scripts
│ ├── infer.py # CLI inference
│ ├── tamper_generator.py # Script to generate tampered invoices
│
├── app.py # Streamlit web app
├── requirements.txt # Dependencies
├── .gitignore
└── README.md # Project overview

---

## 🧠 Model

- **Architecture**: Pretrained `ResNet18` (fine-tuned final FC layer)
- **Input Size**: 256×256 RGB images
- **Loss Function**: Binary Cross Entropy with Logits
- **Optimizer**: Adam (`lr=1e-4`)

---

## 📊 Evaluation

- **Accuracy**: ~98%
- **Precision**: ~83%
- **Recall**: ~87%
- **AUC**: 0.93  
- Full metrics and ROC/Confusion Matrix available in `03_evaluation.ipynb`.

---

## 🖥️ Streamlit App

Run locally with:

```bash
streamlit run app.py
```

Then open http://localhost:8501 to use the web interface.

## 🔍 Inference from CLI

```bash
python src/infer.py "data/tampered/tampered_6.jpg"
```

## 🔗 Deployment Link
https://invoice-fraud-detector-ce58ouovow9hboanjvunul.streamlit.app/

## 📚 What I Learned
- CNNs and transfer learning with ResNet18
- Data augmentation and class balancing
- Evaluation metrics and visualizations (ROC, confusion matrix)
- Creating real-world ML tools with Python
- Deployment using Streamlit

## 📎 License
MIT License – feel free to use and
