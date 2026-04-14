import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image

# Load model
model = tf.keras.models.load_model('C:/Users/DELL XPS/OneDrive/Desktop/AIML/project_4/app.py/garbage_model.keras')

classes = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']

# ---------------- UI ---------------- #
st.set_page_config(page_title="Waste Classifier", layout="centered")

st.title("♻️  Garbage Classification System Using Deep Learning")
st.markdown("### 🌍 Smart Waste Segregation for a Cleaner Future")

st.markdown(
"""
💡 **Upload an image of waste and let AI classify it instantly!**

This system uses deep learning to identify waste types and helps improve recycling efficiency.
"""
)

# Sidebar
st.sidebar.title("🌿 About Project")
st.sidebar.info(
"""
This project uses **MobileNetV2 (Transfer Learning)** to classify garbage images.

🚀 Built with:
- Deep Learning
- TensorFlow
- Streamlit
"""
)

st.sidebar.markdown("### 🔧 Features")
st.sidebar.write("✔ Image Upload")
st.sidebar.write("✔ Instant Prediction")
st.sidebar.write("✔ Confidence Score")
st.sidebar.write("✔ Top-3 Predictions")

# ---------------- Upload ---------------- #
st.info("📌 Upload a clear waste image for best results")

file = st.file_uploader("📤 Upload Image", type=["jpg","png","jpeg"])

if file:
    st.success("✅ Image uploaded successfully!")

    img = Image.open(file).resize((224,224))
    st.image(img, caption="🖼️ Uploaded Image", use_column_width=True)

    st.write("🔍 **Analyzing image... Please wait**")

    # Preprocess
    img_array = np.array(img)/255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Prediction
    pred = model.predict(img_array)
    predicted_index = np.argmax(pred)
    confidence = np.max(pred)

    # ---------------- Result ---------------- #
    st.markdown("---")
    st.success(f"♻️ **Predicted Waste Type: {classes[predicted_index].upper()}**")
    st.write(f"📊 Confidence Score: **{confidence:.2f}**")

    # Progress bar
    st.subheader("📈 Confidence Level")
    st.progress(int(confidence * 100))

    # Top 3 Predictions
    st.subheader("🏆 Top 3 Predictions")
    top3 = pred[0].argsort()[-3:][::-1]

    for i in top3:
        st.write(f"👉 {classes[i]} : {pred[0][i]:.2f}")

    # Environmental message
    st.markdown("---")
    st.markdown(
    "🌱 **Did you know?** Proper waste segregation can significantly reduce pollution and improve recycling efficiency!"
    )

# ---------------- Extra Info Section ---------------- #
st.markdown("---")

st.subheader("📚 Project Overview")

st.markdown("""
### 🎯 Objectives
- Build an automated waste classification system  
- Use deep learning for image recognition  
- Improve accuracy using augmentation  
- Deploy using Streamlit  

### ❗ Problem
Manual waste sorting is slow, inefficient, and error-prone.

### 💡 Solution
An AI-powered system that classifies waste images instantly.

### 🚀 Outcome
- Faster waste segregation  
- Reduced human effort  
- Better environmental impact 🌍  
""")

# Footer
st.markdown("---")
st.caption("💻 Developed using Streamlit | ♻️ Smart Waste Management System")