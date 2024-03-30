import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        # Check if model file exists
        model_path = os.path.join("model", "model.h5")
        if not os.path.exists(model_path):
            print("Model file not found.")
            return None

        # Load model
        model = load_model(model_path)

        # Load and preprocess image
        try:
            test_image = image.load_img(self.filename, target_size=(224, 224))
            test_image = image.img_to_array(test_image)
            test_image = np.expand_dims(test_image, axis=0)
            test_image = test_image / 255.0  # Normalize pixel values
        except Exception as e:
            print(f"Error loading or preprocessing image: {e}")
            return None

        # Make prediction
        try:
            result = model.predict(test_image)
            prediction = "Normal" if result[0][0] < 0.5 else "Adenocarcinoma Cancer"
            return [{ "image" : prediction}]
        except Exception as e:
            print(f"Error making prediction: {e}")
            return None
