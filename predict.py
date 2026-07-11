"""
Prediction functions for CropCare AI
This file exists to handle disease prediction from images.
It uses the model from model.py and preprocessing functions from preprocessing.py.
It is imported by the Disease Detection page to make predictions on user-uploaded images.
"""

import numpy as np
import os

# Import project modules
from model import load_model
from preprocessing import preprocess_image
from train import check_and_train_model
from config import MODEL_PATH, DATASET_PATH

def predict_disease(image, model=None, class_names=None):
    """
    Predict crop disease from an image.
    
    Args:
        image: Input image (can be file path, PIL Image, or numpy array)
        model (Model): Pre-loaded model (if None, will load or train model)
        class_names (list): List of class names (if None, will get from dataset)
        
    Returns:
        tuple: (disease_name, confidence, all_predictions) - Predicted disease, confidence, and all class predictions
    """
    try:
        # Load or train model if not provided
        if model is None:
            model, class_names = check_and_train_model(DATASET_PATH, MODEL_PATH)
        
        # Get class names if not provided
        if class_names is None:
            class_names_path = os.path.join(os.path.dirname(MODEL_PATH), "class_names.txt")
            if os.path.exists(class_names_path):
                with open(class_names_path, "r") as f:
                    class_names = [line.strip() for line in f.readlines()]
            else:
                from train import get_class_names
                class_names = get_class_names(DATASET_PATH)
        
        # Preprocess image
        preprocessed_image = preprocess_image(image)
        
        # Make prediction
        predictions = model.predict(preprocessed_image)
        
        # Get top prediction
        top_prediction_idx = np.argmax(predictions[0])
        disease_name = class_names[top_prediction_idx]
        confidence = predictions[0][top_prediction_idx] * 100
        
        # Get all predictions with class names
        all_predictions = {
            class_names[i]: float(predictions[0][i]) * 100 
            for i in range(len(class_names))
        }
        
        # Sort predictions by confidence (descending)
        all_predictions = dict(sorted(all_predictions.items(), key=lambda item: item[1], reverse=True))
        
        return disease_name, confidence, all_predictions
    except Exception as e:
        raise ValueError(f"Error predicting disease: {e}")