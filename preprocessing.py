"""
Image preprocessing functions for CropCare AI
This file exists to handle all image preprocessing operations needed before model prediction.
It contains functions for loading, resizing, and normalizing images.
The predict.py file imports this to preprocess images before prediction.
"""

import os
import cv2
import numpy as np
from PIL import Image
import io

# Import configuration
from config import IMAGE_SIZE

def preprocess_image(image, target_size=IMAGE_SIZE):
    """
    Preprocess an image for model prediction.
    
    Args:
        image: Input image (can be file path, PIL Image, or numpy array)
        target_size (tuple): Target size for resizing (height, width)
        
    Returns:
        numpy.ndarray: Preprocessed image ready for model input
    """
    try:
        # Handle different input types
        if isinstance(image, str):
            # File path
            img = cv2.imread(image)
            if img is None:
                raise ValueError(f"Could not read image from path: {image}")
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        elif isinstance(image, Image.Image):
            # PIL Image
            img = np.array(image)
            if len(img.shape) == 2:  # Grayscale
                img = np.stack([img] * 3, axis=-1)
            elif img.shape[2] == 4:  # RGBA
                img = img[:, :, :3]  # Remove alpha channel
        elif isinstance(image, np.ndarray):
            # Numpy array
            if len(image.shape) == 2:  # Grayscale
                img = np.stack([image] * 3, axis=-1)
            elif image.shape[2] == 4:  # RGBA
                img = image[:, :, :3]  # Remove alpha channel
            else:
                img = image
        elif hasattr(image, 'read'):  # File-like object (e.g., from Streamlit)
            # Read bytes and convert to PIL Image
            img_bytes = image.read()
            pil_img = Image.open(io.BytesIO(img_bytes))
            img = np.array(pil_img)
            if len(img.shape) == 2:  # Grayscale
                img = np.stack([img] * 3, axis=-1)
            elif img.shape[2] == 4:  # RGBA
                img = img[:, :, :3]  # Remove alpha channel
        else:
            raise ValueError(f"Unsupported image type: {type(image)}")
        
        # Resize image
        img = cv2.resize(img, (target_size[1], target_size[0]))
        
        # Normalize pixel values to [0, 1]
        img = img.astype(np.float32) / 255.0
        
        # Add batch dimension
        img = np.expand_dims(img, axis=0)
        
        return img
    except Exception as e:
        raise ValueError(f"Error preprocessing image: {e}")

def augment_image(image):
    """
    Apply data augmentation to an image.
    
    Args:
        image: Input image (numpy array)
        
    Returns:
        numpy.ndarray: Augmented image
    """
    try:
        # Convert to numpy array if needed
        if isinstance(image, Image.Image):
            img = np.array(image)
        else:
            img = image.copy()
        
        # Random horizontal flip
        if np.random.random() > 0.5:
            img = cv2.flip(img, 1)
        
        # Random rotation (0-20 degrees)
        angle = np.random.uniform(-20, 20)
        h, w = img.shape[:2]
        M = cv2.getRotationMatrix2D((w/2, h/2), angle, 1)
        img = cv2.warpAffine(img, M, (w, h))
        
        # Random brightness adjustment
        brightness = np.random.uniform(0.8, 1.2)
        img = img * brightness
        img = np.clip(img, 0, 255).astype(np.uint8)
        
        return img
    except Exception as e:
        print(f"Error augmenting image: {e}")
        return image

def load_dataset_images(dataset_path, target_size=IMAGE_SIZE, augment=False):
    """
    Load and preprocess images from dataset directory.
    
    Args:
        dataset_path (str): Path to dataset directory
        target_size (tuple): Target size for resizing (height, width)
        augment (bool): Whether to apply data augmentation
        
    Returns:
        tuple: (images, labels, class_names)
    """
    try:
        images = []
        labels = []
        class_names = []
        
        # Get class names from directory structure
        if os.path.exists(dataset_path):
            class_names = [d for d in os.listdir(dataset_path) 
                          if os.path.isdir(os.path.join(dataset_path, d))]
            class_names = sorted(class_names)
            
            # Create class index mapping
            class_indices = {name: index for index, name in enumerate(class_names)}
            
            # Load images from each class directory
            for class_name in class_names:
                class_dir = os.path.join(dataset_path, class_name)
                print("Reading:", class_dir)
                
                for img_name in os.listdir(class_dir):
                    if not img_name.lower().endswith((".jpg", ".jpeg", ".png")):
                        continue
                    img_path = os.path.join(class_dir, img_name)
                    
                    try:
                        # Read image
                        img = cv2.imread(img_path)
                        if img is None:
                            continue
                            
                        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                        
                        # Apply augmentation if requested
                        if augment:
                            img = augment_image(img)
                        
                        # Resize and normalize
                        img = cv2.resize(img, (target_size[1], target_size[0]))
                        img = img.astype(np.float32) / 255.0
                        
                        images.append(img)
                        labels.append(class_indices[class_name])
                        
                        # Add augmented versions if requested
                        if augment:
                            for _ in range(2):  # Add 2 augmented versions
                                aug_img = augment_image(cv2.imread(img_path))
                                aug_img = cv2.cvtColor(aug_img, cv2.COLOR_BGR2RGB)
                                aug_img = cv2.resize(aug_img, (target_size[1], target_size[0]))
                                aug_img = aug_img.astype(np.float32) / 255.0
                                images.append(aug_img)
                                labels.append(class_indices[class_name])
                    except Exception as e:
                        print(f"Error loading image {img_path}: {e}")
                        continue
            
            # Convert to numpy arrays
            images = np.array(images)
            labels = np.array(labels)
            
            return images, labels, class_names
        else:
            raise ValueError(f"Dataset directory not found: {dataset_path}")
    except Exception as e:
        raise ValueError(f"Error loading dataset: {e}")