"""
Disease Detection page for CropCare AI
This file exists to allow users to upload or capture images for disease detection.
It uses the predict.py module to make predictions and displays results.
It imports from utils.py for translation and history management.
"""

import streamlit as st
import numpy as np
from PIL import Image
import plotly.express as px
import time
import os

# Import project modules
from predict import predict_disease
from utils import (
    translate_text, 
    get_disease_info, 
    save_prediction_history, 
    format_disease_name
)
from config import MODEL_PATH, DATASET_PATH

# Get current language
language = st.session_state.language
lang_code = "en" if language == "English" else "hi"

# Page title
st.markdown("""
# 🌿 AI Crop Disease Detection

Upload a clear image of a plant leaf and let our AI identify the disease within seconds.

""")
st.markdown("---")

st.info("📸 Upload a leaf image and click **Analyze**.")

st.markdown("---")

# Image input section
col1, col2 = st.columns(2)

with col1:
    st.markdown("### " + translate_text("Input Image", lang_code))
    
    # File uploader
    uploaded_file = st.file_uploader(
        translate_text("Upload an image", lang_code), 
        type=["jpg", "jpeg", "png"],
        key="file_uploader"
    )
    
    # Camera input
    camera_image = st.camera_input(
        translate_text("Or capture an image using your camera", lang_code),
        key="camera_input"
    )
    
    # Determine which image to use
    image_to_analyze = None
    image_name = ""
    
    if uploaded_file is not None:
        image_to_analyze = uploaded_file
        image_name = uploaded_file.name
        st.image(uploaded_file, caption=translate_text("Uploaded Image", lang_code), width="stretch")
    elif camera_image is not None:
        image_to_analyze = camera_image
        image_name = f"camera_capture_{int(time.time())}.jpg"
        st.image(camera_image, caption=translate_text("Captured Image", lang_code),width="stretch")

with col2:
    st.markdown("### " + translate_text("Analysis", lang_code))
    
    # Analyze button
    analyze_button = st.button(
        translate_text("🔍 Analyze", lang_code), 
        type="primary",
        disabled=image_to_analyze is None
    )
    
    # Results container
    results_container = st.container()

# Process analysis
if analyze_button and image_to_analyze is not None:
    with results_container:
        with st.spinner(translate_text("Analyzing image...", lang_code)):
            try:
                # Load model if not already loaded
                if not st.session_state.model_loaded:
                    from train import check_and_train_model
                    with st.spinner(translate_text("Loading model (this may take a moment on first run)...", lang_code)):
                        st.session_state.model, st.session_state.class_names = check_and_train_model(DATASET_PATH, MODEL_PATH)
                        st.session_state.model_loaded = True
                
                # Make prediction
                disease_name, confidence, all_predictions = predict_disease(
                    image_to_analyze, 
                    st.session_state.model, 
                    st.session_state.class_names
                )
                
                # Format disease name for display
                formatted_disease_name = format_disease_name(disease_name)
                
                # Save to history
                save_prediction_history(disease_name, confidence, image_name)
                
                # Display results
                st.markdown("---")
                st.markdown("## " + translate_text("Detection Results", lang_code))
                
                # Disease name and confidence
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown(f"### {translate_text('Detected Disease', lang_code)}")
                    st.markdown(f"## {formatted_disease_name}")
                
                with col2:
                    st.markdown(f"### {translate_text('Confidence', lang_code)}")
                    
                    # Determine confidence color
                    if confidence >= 80:
                        conf_color = "green"
                    elif confidence >= 60:
                        conf_color = "orange"
                    else:
                        conf_color = "red"
                    
                    st.markdown(f"## :{conf_color}[{confidence:.2f}%]")
                
                # Confidence bar
                 
                
                st.markdown("---")
                
                # Top predictions chart
                st.markdown("### " + translate_text("Top Predictions", lang_code))
                
                # Prepare data for chart
                top_predictions = list(all_predictions.items())[:5]
                pred_df = {
                    "Disease": [format_disease_name(d) for d, _ in top_predictions],
                    "Confidence": [c for _, c in top_predictions]
                }
                
                # Create bar chart
                fig = px.bar(
                    pred_df, 
                    x="Confidence", 
                    y="Disease",
                    orientation='h',
                    color="Confidence",
                    color_continuous_scale=px.colors.sequential.Greens,
                    title=translate_text("Top 5 Predictions", lang_code)
                )
                
                fig.update_layout(yaxis={'categoryorder': 'total ascending'})
                st.plotly_chart(fig, use_container_width=True)
                
                st.markdown("---")
                
                # Disease information
                st.markdown("## " + translate_text("Disease Information", lang_code))
                
                # Get disease information
                disease_info = get_disease_info(disease_name, lang_code)
                
                # Display disease information in tabs
                tab1, tab2, tab3, tab4 = st.tabs([
                    translate_text("Symptoms", lang_code),
                    translate_text("Treatment", lang_code),
                    translate_text("Prevention", lang_code),
                    translate_text("Recovery", lang_code)
                ])
                
                with tab1:
                    st.markdown(f"### {translate_text('Symptoms', lang_code)}")
                    st.markdown(disease_info["symptoms"])
                    st.markdown(f"### {translate_text('Cause', lang_code)}")
                    st.markdown(disease_info["cause"])
                
                with tab2:
                    st.markdown(f"### {translate_text('General Treatment', lang_code)}")
                    st.markdown(disease_info["treatment"])
                    st.markdown(f"### {translate_text('Organic Treatment', lang_code)}")
                    st.markdown(disease_info["organic_treatment"])
                    st.markdown(f"### {translate_text('Chemical Treatment', lang_code)}")
                    st.markdown(disease_info["chemical_treatment"])
                    st.markdown(f"### {translate_text('Suitable Fertilizer', lang_code)}")
                    st.markdown(disease_info["fertilizer"])
                    st.markdown(f"### {translate_text('Suitable Pesticide', lang_code)}")
                    st.markdown(disease_info["pesticide"])
                
                with tab3:
                    st.markdown(f"### {translate_text('Preventive Measures', lang_code)}")
                    st.markdown(disease_info["preventive_measures"])
                
                with tab4:
                    st.markdown(f"### {translate_text('Estimated Recovery Time', lang_code)}")
                    st.markdown(disease_info["recovery"])
                
                st.success(translate_text("Analysis completed successfully!", lang_code))
                
                
            except Exception as e:
                st.error(f"{translate_text('Error analyzing image:', lang_code)} {str(e)}")