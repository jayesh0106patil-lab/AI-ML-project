# AI-ML-project



# 🧠 AI Image Classifier Web App

A modern **Flask + TensorFlow** web application that classifies uploaded images into animals, objects, and many more categories using a pre-trained **MobileNetV2** deep learning model.

This project allows users to upload an image through a beautiful web interface and get **Top 3 Predictions with Confidence Scores** instantly.

---

# 🚀 Features

- Upload image from device
- Detect animals, objects, vehicles, electronics, and more
- Uses powerful pre-trained MobileNetV2 model
- Displays uploaded image preview
- Shows Top 3 predictions with confidence %
- Attractive responsive UI
- Fast and lightweight performance

---

# 📸 Example Predictions

| Uploaded Image | Output |
|---------------|--------|
| Dog Image | Golden Retriever - 94% |
| Cat Image | Persian Cat - 96% |
| Car Image | Sports Car - 91% |
| Laptop Image | Notebook Computer - 93% |
| Bird Image | Parrot - 89% |

---

# 🛠️ Tech Stack

## Frontend
- HTML5
- CSS3
- Jinja2 Templates

## Backend
- Python
- Flask

## AI / Machine Learning
- TensorFlow
- MobileNetV2
- ImageNet Labels

## Image Processing
- Pillow
- NumPy

---

# 📁 Project Structure

```bash
image_classifier/
│
├── app.py
├── requirements.txt
├── README.md
├── static/
│   └── uploaded images
└── templates/
    └── index.html
