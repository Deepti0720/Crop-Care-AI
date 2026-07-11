"""
Model evaluation functions for CropCare AI
This file exists to evaluate the performance of the trained model.
It can be used to assess model accuracy, precision, recall, and other metrics.
It is not directly used by the main app but can be run standalone for evaluation.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns
import os

# Import project modules
from preprocessing import load_dataset_images
from predict import predict_disease
from config import MODEL_PATH, DATASET_PATH, IMAGE_SIZE

def evaluate_model(model_path=MODEL_PATH, dataset_path=DATASET_PATH):
    """
    Evaluate the model on the dataset.
    
    Args:
        model_path (str): Path to the model file
        dataset_path (str): Path to dataset directory
        
    Returns:
        dict: Evaluation metrics
    """
    try:
        # Load model
        from model import load_model
        model = load_model(model_path)
        
        # Get class names
        class_names_path = os.path.join(os.path.dirname(model_path), "class_names.txt")
        if os.path.exists(class_names_path):
            with open(class_names_path, "r") as f:
                class_names = [line.strip() for line in f.readlines()]
        else:
            from train import get_class_names
            class_names = get_class_names(dataset_path)
        
        # Load dataset (without augmentation for evaluation)
        images, labels, _ = load_dataset_images(dataset_path, augment=False)
        
        if len(images) == 0:
            raise ValueError("No images found in the dataset directory")
        
        # Make predictions for all images
        y_true = labels
        y_pred = []
        
        for i, image in enumerate(images):
            # Preprocess image (add batch dimension and normalize)
            img = np.expand_dims(image, axis=0)
            
            # Make prediction
            predictions = model.predict(img)
            pred_idx = np.argmax(predictions[0])
            y_pred.append(pred_idx)
            
            # Print progress
            if (i + 1) % 100 == 0 or i == len(images) - 1:
                print(f"Processed {i + 1}/{len(images)} images")
        
        # Calculate metrics
        report = classification_report(y_true, y_pred, target_names=class_names, output_dict=True)
        cm = confusion_matrix(y_true, y_pred)
        
        # Plot confusion matrix
        plt.figure(figsize=(12, 10))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=class_names, yticklabels=class_names)
        plt.title('Confusion Matrix')
        plt.ylabel('True Label')
        plt.xlabel('Predicted Label')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        
        # Save confusion matrix plot
        cm_path = os.path.join(os.path.dirname(model_path), "confusion_matrix.png")
        plt.savefig(cm_path)
        plt.close()
        
        print(f"Confusion matrix saved to {cm_path}")
        
        # Return evaluation metrics
        return {
            "classification_report": report,
            "confusion_matrix": cm,
            "accuracy": report["accuracy"],
            "macro_avg_precision": report["macro avg"]["precision"],
            "macro_avg_recall": report["macro avg"]["recall"],
            "macro_avg_f1": report["macro avg"]["f1-score"],
            "weighted_avg_precision": report["weighted avg"]["precision"],
            "weighted_avg_recall": report["weighted avg"]["recall"],
            "weighted_avg_f1": report["weighted avg"]["f1-score"]
        }
    except Exception as e:
        raise ValueError(f"Error evaluating model: {e}")

# This allows the script to be run standalone for evaluation
if __name__ == "__main__":
    try:
        # Check if model exists
        if not os.path.exists(MODEL_PATH):
            raise ValueError(f"Model not found at {MODEL_PATH}. Please train the model first.")
            
        # Check if dataset exists
        if not os.path.exists(DATASET_PATH):
            raise ValueError(f"Dataset directory not found at {DATASET_PATH}")
            
        # Evaluate the model
        metrics = evaluate_model()
        
        # Print evaluation results
        print("\nModel Evaluation Results:")
        print(f"Accuracy: {metrics['accuracy']:.4f}")
        print(f"Macro Avg Precision: {metrics['macro_avg_precision']:.4f}")
        print(f"Macro Avg Recall: {metrics['macro_avg_recall']:.4f}")
        print(f"Macro Avg F1-Score: {metrics['macro_avg_f1']:.4f}")
        print(f"Weighted Avg Precision: {metrics['weighted_avg_precision']:.4f}")
        print(f"Weighted Avg Recall: {metrics['weighted_avg_recall']:.4f}")
        print(f"Weighted Avg F1-Score: {metrics['weighted_avg_f1']:.4f}")
        
        # Print per-class metrics
        print("\nPer-Class Metrics:")
        for class_name in metrics["classification_report"].keys():
            if class_name in ["accuracy", "macro avg", "weighted avg"]:
                continue
            class_metrics = metrics["classification_report"][class_name]
            print(f"{class_name}:")
            print(f"  Precision: {class_metrics['precision']:.4f}")
            print(f"  Recall: {class_metrics['recall']:.4f}")
            print(f"  F1-Score: {class_metrics['f1-score']:.4f}")
            print(f"  Support: {class_metrics['support']}")
    except Exception as e:
        print(f"Error: {e}")
        print("Please make sure the model is trained and the dataset is properly structured.")