# ♻️ AI-Based Garbage Classification System

## 🌍 Overview
This project is a Deep Learning-based web application that classifies garbage images into categories such as cardboard, glass, metal, paper, plastic, and organic.  
It helps in automating waste segregation and promotes efficient recycling.

---

## 🎯 Objectives
- Build an automated waste classification system  
- Use Deep Learning (CNN & Transfer Learning)  
- Improve accuracy using preprocessing & augmentation  
- Deploy using Streamlit for real-time predictions  

---

## ❗ Problem Statement
Improper waste segregation leads to environmental pollution and inefficient recycling.  
Manual classification is time-consuming and error-prone.

---

## 💡 Solution
This system uses a **MobileNetV2-based deep learning model** to classify waste images.  
Users can upload an image through a Streamlit web app and get instant predictions.

---

## 🛠️ Tech Stack
- Python  
- TensorFlow / Keras  
- NumPy  
- Streamlit  
- PIL (Image Processing)  
- Scikit-learn  

---

## 📂 Dataset
- Garbage Classification Dataset (Kaggle)  
- Classes:
  - Cardboard  
  - Glass  
  - Metal  
  - Paper  
  - Plastic  
  - Trash  

---

## ⚙️ Workflow
1. Data Collection  
2. Data Preprocessing (Resize, Normalize, Augmentation)  
3. Model Training (MobileNetV2)  
4. Model Evaluation (Accuracy, Precision, Recall, F1-score)  
5. Model Saving  
6. Streamlit App Development  
7. User Image Upload → Prediction → Result Display  

---

## 🧠 Model Details
- Transfer Learning: MobileNetV2  
- Input Size: 224x224  
- Output: 6 Classes  
- Activation: Softmax  

---

## 📊 Features
- Upload garbage images  
- Predict waste category  
- Show confidence score  
- Top-3 predictions (optional)  
- Simple and user-friendly interface  

---
## FlowChart
        ┌──────────────────────┐
        │   Start              │
        └─────────┬────────────┘
                  │
                  ▼
        ┌──────────────────────┐
        │ Load Dataset         │
        │ (TrashNet/Kaggle)    │
        └─────────┬────────────┘
                  │
                  ▼
        ┌──────────────────────┐
        │ Data Preprocessing   │
        │ - Resize (224x224)   │
        │ - Normalize          │
        │ - Augmentation       │
        └─────────┬────────────┘
                  │
                  ▼
        ┌──────────────────────┐
        │ Split Data           │
        │ Train / Validation   │
        └─────────┬────────────┘
                  │
                  ▼
        ┌──────────────────────┐
        │ Model Building       │
        │ (MobileNetV2)        │
        └─────────┬────────────┘
                  │
                  ▼
        ┌──────────────────────┐
        │ Model Training       │
        │ (Fit model)          │
        └─────────┬────────────┘
                  │
                  ▼
        ┌──────────────────────┐
        │ Model Evaluation     │
        │ Accuracy, F1 Score   │
        └─────────┬────────────┘
                  │
                  ▼
        ┌──────────────────────┐
        │ Save Model (.keras)  │
        └─────────┬────────────┘
                  │
                  ▼
        ┌──────────────────────┐
        │ Streamlit App        │
        │ - Upload Image       │
        │ - Preprocess Image   │
        └─────────┬────────────┘
                  │
                  ▼
        ┌──────────────────────┐
        │ Model Prediction     │
        │ (Class + Confidence) │
        └─────────┬────────────┘
                  │
                  ▼
        ┌──────────────────────┐
        │ Display Result       │
        │ in UI                │
        └─────────┬────────────┘
                  │
                  ▼
        ┌──────────────────────┐
        │         End          │
        └──────────────────────┘
cd waste-classification
