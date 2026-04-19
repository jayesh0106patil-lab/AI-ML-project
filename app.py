from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
from PIL import Image
import os

app = Flask(__name__)

# Load pre-trained model
model = tf.keras.applications.MobileNetV2(weights='imagenet')

UPLOAD_FOLDER = "static"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def preprocess_image(image_path):
    img = Image.open(image_path).resize((224,224))
    img = np.array(img)
    img = tf.keras.applications.mobilenet_v2.preprocess_input(img)
    img = np.expand_dims(img, axis=0)
    return img

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    img = preprocess_image(filepath)

    preds = model.predict(img)
    decoded = tf.keras.applications.mobilenet_v2.decode_predictions(preds, top=3)[0]

    results = [(label, round(prob*100,2)) for (_, label, prob) in decoded]

    return render_template('index.html', results=results, image=filepath)

app.run(debug=True)