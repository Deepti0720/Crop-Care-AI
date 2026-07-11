"""
Utility functions for CropCare AI
This file exists to provide common utility functions used across multiple files.
It contains functions for translation, history management, and other helper functions.
Other files import this to access these utility functions.
"""

import os
import csv
import pandas as pd
from datetime import datetime
from deep_translator import GoogleTranslator
import json

# Import configuration
from config import HISTORY_PATH, SUPPORTED_LANGUAGES, DISEASE_INFO, DEFAULT_DISEASE_INFO

def translate_text(text, target_language="en"):
    """
    Translate text to the target language using Google Translator.
    
    Args:
        text (str): Text to translate
        target_language (str): Target language code (en, hi)
        
    Returns:
        str: Translated text
    """
    try:
        if target_language == "en":
            return text
            
        translator = GoogleTranslator(source='auto', target=target_language)
        translated = translator.translate(text)
        return translated
    except Exception as e:
        print(f"Translation error: {e}")
        return text  # Return original text if translation fails

def get_disease_info(disease_name, language="en"):
    """
    Get detailed information about a disease in the specified language.
    
    Args:
        disease_name (str): Name of the disease
        language (str): Language code (en, hi)
        
    Returns:
        dict: Disease information in the specified language
    """
    # Get disease info from config
    disease_info = DISEASE_INFO.get(disease_name, DEFAULT_DISEASE_INFO)
    
    # Get info in the requested language
    localized_info = {}
    for key, value in disease_info.items():
        if isinstance(value, dict):
            localized_info[key] = value.get(language, value.get("en", ""))
        else:
            localized_info[key] = value
            
    return localized_info

def save_prediction_history(disease_name, confidence, image_name):
    """
    Save prediction history to CSV file.
    
    Args:
        disease_name (str): Name of the predicted disease
        confidence (float): Confidence score of the prediction
        image_name (str): Name of the uploaded image
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Check if file exists to determine if we need to write headers
        file_exists = os.path.isfile(HISTORY_PATH)
        
        # Prepare data to save
        prediction_data = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "disease": disease_name,
            "confidence": f"{confidence:.2f}%",
            "image_name": image_name
        }
        
        # Write to CSV
        with open(HISTORY_PATH, 'a', newline='') as csvfile:
            fieldnames = ["date", "disease", "confidence", "image_name"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            if not file_exists:
                writer.writeheader()
                
            writer.writerow(prediction_data)
            
        return True
    except Exception as e:
        print(f"Error saving prediction history: {e}")
        return False

def get_prediction_history():
    """
    Get prediction history from CSV file.
    
    Returns:
        DataFrame: Pandas DataFrame containing prediction history
    """
    try:
        if os.path.isfile(HISTORY_PATH):
            return pd.read_csv(HISTORY_PATH)
        else:
            # Return empty DataFrame with correct columns if file doesn't exist
            return pd.DataFrame(columns=["date", "disease", "confidence", "image_name"])
    except Exception as e:
        print(f"Error reading prediction history: {e}")
        return pd.DataFrame(columns=["date", "disease", "confidence", "image_name"])

def clear_prediction_history():
    """
    Clear prediction history CSV file.
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        if os.path.isfile(HISTORY_PATH):
            os.remove(HISTORY_PATH)
        return True
    except Exception as e:
        print(f"Error clearing prediction history: {e}")
        return False

def get_weather_advice(weather_condition, temperature, humidity, language="en"):
    """
    Get farming advice based on weather conditions.
    
    Args:
        weather_condition (str): Weather condition (Clear, Rain, etc.)
        temperature (float): Temperature in Celsius
        humidity (float): Humidity percentage
        language (str): Language code (en, hi)
        
    Returns:
        dict: Weather advice in the specified language
    """
    from config import WEATHER_ADVICE, TEMPERATURE_ADVICE, HUMIDITY_ADVICE
    
    # Get weather condition advice
    condition_advice = WEATHER_ADVICE.get(weather_condition, WEATHER_ADVICE.get("Clear", {}))
    condition_text = condition_advice.get(language, condition_advice.get("en", ""))
    
    # Determine temperature category
    if temperature >= 35:
        temp_category = "hot"
    elif temperature >= 25:
        temp_category = "warm"
    elif temperature >= 15:
        temp_category = "moderate"
    elif temperature >= 5:
        temp_category = "cool"
    elif temperature >= 0:
        temp_category = "cold"
    else:
        temp_category = "freezing"
    
    # Get temperature advice
    temp_advice = TEMPERATURE_ADVICE.get(temp_category, TEMPERATURE_ADVICE.get("moderate", {}))
    temp_text = temp_advice.get(language, temp_advice.get("en", ""))
    
    # Determine humidity category
    if humidity < 30:
        humidity_category = "low"
    elif humidity < 60:
        humidity_category = "moderate"
    elif humidity < 80:
        humidity_category = "high"
    else:
        humidity_category = "very_high"
    
    # Get humidity advice
    humidity_advice = HUMIDITY_ADVICE.get(humidity_category, HUMIDITY_ADVICE.get("moderate", {}))
    humidity_text = humidity_advice.get(language, humidity_advice.get("en", ""))
    
    return {
        "condition_advice": condition_text,
        "temperature_advice": temp_text,
        "humidity_advice": humidity_text,
        "temperature_category": temp_category,
        "humidity_category": humidity_category
    }

def format_disease_name(disease_name):
    """
    Format disease name for display.
    
    Args:
        disease_name (str): Raw disease name (e.g., "Tomato___Early_Blight")
        
    Returns:
        str: Formatted disease name (e.g., "Tomato Early Blight")
    """
    return disease_name.replace("___", " ").replace("_", " ")

def get_class_names(dataset_path):
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
def get_translation(text, language="en"):
    return translate_text(text, language)