"""
Model architecture for CropCare AI
This file exists to define the model architecture using MobileNetV2 with transfer learning.
It contains functions to create, compile, and save the model.
The train.py file imports this to create and train the model.
The predict.py file imports this to load the model for predictions.
"""

import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
import os

# Import configuration
from config import MODEL_PATH, IMAGE_SIZE, LEARNING_RATE, EPOCHS, BATCH_SIZE

def create_model(num_classes, input_shape=IMAGE_SIZE + (3,)):
    """
    Create a model using MobileNetV2 with transfer learning.
    
    Args:
        num_classes (int): Number of classes for classification
        input_shape (tuple): Input shape for the model (height, width, channels)
        
    Returns:
        Model: Compiled Keras model
    """
    try:
        # Load MobileNetV2 base model with pre-trained ImageNet weights
        base_model = MobileNetV2(
            weights='imagenet',
            include_top=False,
            input_shape=input_shape
        )
        
        # Freeze the base model layers
        for layer in base_model.layers:
            layer.trainable = False
        
        # Add custom classification layers on top
        x = base_model.output
        x = GlobalAveragePooling2D()(x)
        x = Dropout(0.2)(x)
        x = Dense(128, activation='relu')(x)
        x = Dropout(0.1)(x)
        predictions = Dense(num_classes, activation='softmax')(x)
        
        # Create the full model
        model = Model(inputs=base_model.input, outputs=predictions)
        
        # Compile the model
        model.compile(
            optimizer=Adam(learning_rate=LEARNING_RATE),
            loss='categorical_crossentropy',
            metrics=['accuracy']
        )
        
        return model
    except Exception as e:
        raise ValueError(f"Error creating model: {e}")

def load_model(model_path=MODEL_PATH):
    """
    Load a saved model.
    
    Args:
        model_path (str): Path to the saved model
        
    Returns:
        Model: Loaded Keras model
    """
    try:
        if os.path.exists(model_path):
            model = tf.keras.models.load_model(model_path)
            return model
        else:
            raise FileNotFoundError(f"Model file not found at {model_path}")
    except Exception as e:
        raise ValueError(f"Error loading model: {e}")

def save_model(model, model_path=MODEL_PATH):
    """
    Save the model to disk.
    
    Args:
        model (Model): Keras model to save
        model_path (str): Path to save the model
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Ensure directory exists
        os.makedirs(os.path.dirname(model_path), exist_ok=True)
        
        # Save the model
        model.save(model_path)
        return True
    except Exception as e:
        print(f"Error saving model: {e}")
        return False

def get_callbacks(model_path=MODEL_PATH):
    """
    Get callbacks for model training.
    
    Args:
        model_path (str): Path to save the best model
        
    Returns:
        list: List of Keras callbacks
    """
    try:
        # Ensure directory exists
        os.makedirs(os.path.dirname(model_path), exist_ok=True)
        
        # Early stopping callback
        early_stopping = EarlyStopping(
            monitor='val_loss',
            patience=5,
            restore_best_weights=True,
            verbose=1
        )
        
        # Model checkpoint callback
        model_checkpoint = ModelCheckpoint(
            filepath=model_path,
            monitor='val_loss',
            save_best_only=True,
            verbose=1
        )
        
        return [early_stopping, model_checkpoint]
    except Exception as e:
        print(f"Error creating callbacks: {e}")
        return []