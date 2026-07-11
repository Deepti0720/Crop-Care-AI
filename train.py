"""
Training script for CropCare AI
This file exists to handle the model training process.
It uses the model architecture from model.py and preprocessing functions from preprocessing.py.
It can be run standalone to train the model or imported by app.py for on-demand training.
"""

import os
import numpy as np
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split

# Import project modules
from model import create_model, save_model, get_callbacks
from preprocessing import load_dataset_images
from config import MODEL_PATH, DATASET_PATH, EPOCHS, BATCH_SIZE, VALIDATION_SPLIT

def train_model(dataset_path=DATASET_PATH, model_path=MODEL_PATH, epochs=EPOCHS, batch_size=BATCH_SIZE, validation_split=VALIDATION_SPLIT):
    """
    Train the crop disease detection model.
    
    Args:
        dataset_path (str): Path to dataset directory
        model_path (str): Path to save the trained model
        epochs (int): Number of training epochs
        batch_size (int): Batch size for training
        validation_split (float): Fraction of data to use for validation
        
    Returns:
        tuple: (model, history) - Trained model and training history
    """
    try:
        print("Loading dataset...")
        print("Dataset Path:", dataset_path)
        images, labels, class_names = load_dataset_images(dataset_path, augment=True)
        
        if len(images) == 0:
            raise ValueError("No images found in the dataset directory")
            
        print(f"Found {len(images)} images belonging to {len(class_names)} classes")
        print(f"Classes: {class_names}")
        
        # Convert labels to one-hot encoding
        num_classes = len(class_names)
        labels_onehot = to_categorical(labels, num_classes=num_classes)
        
        # Split data into training and validation sets
        X_train, X_val, y_train, y_val = train_test_split(
            images, labels_onehot, 
            test_size=validation_split, 
            random_state=42,
            stratify=labels
        )
        
        print(f"Training samples: {len(X_train)}")
        print(f"Validation samples: {len(X_val)}")
        
        # Create model
        print("Creating model...")
        model = create_model(num_classes)
        
        # Get callbacks
        callbacks = get_callbacks(model_path)
        
        # Train model
        print("Training model...")
        history = model.fit(
            X_train, y_train,
            batch_size=batch_size,
            epochs=epochs,
            validation_data=(X_val, y_val),
            callbacks=callbacks,
            verbose=1
        )
        
        # Save class names for later use
        class_names_path = os.path.join(os.path.dirname(model_path), "class_names.txt")
        with open(class_names_path, "w") as f:
            f.write("\n".join(class_names))
        
        print(f"Model trained and saved to {model_path}")
        print(f"Class names saved to {class_names_path}")
        
        return model, history, class_names
    except Exception as e:
        raise ValueError(f"Error training model: {e}")

def check_and_train_model(dataset_path=DATASET_PATH, model_path=MODEL_PATH):
    """
    Check if a trained model exists, and if not, train a new one.
    
    Args:
        dataset_path (str): Path to dataset directory
        model_path (str): Path to the model file
        
    Returns:
        tuple: (model, class_names) - Loaded or trained model and class names
    """
    try:
        # Check if model exists
        if os.path.exists(model_path):
            print(f"Loading existing model from {model_path}")
            from model import load_model
            model = load_model(model_path)
            
            # Load class names
            class_names_path = os.path.join(os.path.dirname(model_path), "class_names.txt")
            if os.path.exists(class_names_path):
                with open(class_names_path, "r") as f:
                    class_names = [line.strip() for line in f.readlines()]
            else:
                # If class names file doesn't exist, get them from dataset
                class_names = get_class_names(dataset_path)
                
            return model, class_names
        else:
            print(f"No model found at {model_path}. Training new model...")
            model, history, class_names = train_model(dataset_path, model_path)
            return model, class_names
    except Exception as e:
        raise ValueError(f"Error in check_and_train_model: {e}")

def get_class_names(dataset_path=DATASET_PATH):
    """
    Get class names from dataset directory.
    
    Args:
        dataset_path (str): Path to dataset directory
        
    Returns:
        list: List of class names
    """
    try:
        if os.path.exists(dataset_path):
            classes = [d for d in os.listdir(dataset_path) 
                      if os.path.isdir(os.path.join(dataset_path, d))]
            return sorted(classes)
        return []
    except Exception as e:
        print(f"Error getting class names: {e}")
        return []

# This allows the script to be run standalone for training
if __name__ == "__main__":
    try:
        # Check if dataset exists
        if not os.path.exists(DATASET_PATH):
            raise ValueError(f"Dataset directory not found at {DATASET_PATH}")
            
        # Train the model
        model, history, class_names = train_model()
        
        # Print training summary
        print("\nTraining completed successfully!")
        print(f"Final training accuracy: {history.history['accuracy'][-1]:.4f}")
        print(f"Final validation accuracy: {history.history['val_accuracy'][-1]:.4f}")
    except Exception as e:
        print(f"Error: {e}")
        print("Please make sure the dataset is properly structured and all dependencies are installed.")