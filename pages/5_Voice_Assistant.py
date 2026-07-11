"""
Voice Assistant page for CropCare AI
This file exists to provide a voice-based interface for asking questions about crop diseases.
It uses SpeechRecognition for voice input and gTTS for voice output.
It imports from utils.py for translation functions.
"""

import streamlit as st
import os
import tempfile
import base64
from io import BytesIO

# Import project modules
from utils import translate_text, get_disease_info, format_disease_name
from config import DISEASE_INFO, SUPPORTED_LANGUAGES

# Get current language
language = st.session_state.language
lang_code = "en" if language == "English" else "hi"

# Page title
st.title("🎤 " + translate_text("Voice Assistant", lang_code))
st.markdown("---")

# Instructions
st.markdown("### " + translate_text("Instructions", lang_code))
st.markdown(translate_text("""
1. Click the microphone button to start recording
2. Ask a question about crop diseases, treatments, or farming practices
3. The assistant will provide a spoken and text response
""", lang_code))

st.markdown("---")

# Voice input section
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### " + translate_text("Voice Input", lang_code))
    
    # Language for voice recognition
    voice_lang = st.selectbox(
        translate_text("Voice Language", lang_code),
        ["en-US", "hi-IN"],
        index=0 if language == "English" else 1,
        format_func=lambda x: "English" if x == "en-US" else "Hindi"
    )
    
    # Record button
    record_button = st.button(
        translate_text("🎙️ Record Question", lang_code),
        type="primary"
    )

with col2:
    st.markdown("### " + translate_text("Assistant Response", lang_code))
    
    # Response container
    response_container = st.container()

# Process voice input
if record_button:
    with response_container:
        try:
            import speech_recognition as sr
            
            with st.spinner(translate_text("Listening...", lang_code)):
                # Initialize recognizer
                recognizer = sr.Recognizer()
                
                # Create a temporary file for audio recording
                with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio:
                    temp_audio_path = temp_audio.name
                
                try:
                    # Use the microphone
                    with sr.Microphone() as source:
                        # Adjust for ambient noise
                        recognizer.adjust_for_ambient_noise(source, duration=1)
                        
                        # Record audio
                        st.info(translate_text("Speak now...", lang_code))
                        audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
                        
                        # Save audio to temporary file
                        with open(temp_audio_path, "wb") as f:
                            f.write(audio.get_wav_data())
                        
                        # Recognize speech
                        try:
                            question = recognizer.recognize_google(audio, language=voice_lang)
                            st.markdown(f"**{translate_text('You asked', lang_code)}:** {question}")
                            
                            # Process the question
                            response = process_question(question, lang_code)
                            
                            # Display response
                            st.markdown(f"**{translate_text('Assistant', lang_code)}:**")
                            st.markdown(response)
                            
                            # Generate audio response
                            with st.spinner(translate_text("Generating audio response...", lang_code)):
                                generate_audio_response(response, lang_code)
                            
                        except sr.UnknownValueError:
                            st.warning(translate_text("Could not understand audio. Please try again.", lang_code))
                        except sr.RequestError as e:
                            st.error(f"{translate_text('Could not request results', lang_code)}; {e}")
                
                finally:
                    # Clean up temporary file
                    if os.path.exists(temp_audio_path):
                        os.remove(temp_audio_path)
        
        except ImportError:
            st.error(translate_text(
                "SpeechRecognition package is not installed. Please install it using 'pip install SpeechRecognition'.",
                lang_code
            ))
        except Exception as e:
            st.error(f"{translate_text('Error with voice recognition:', lang_code)} {str(e)}")
            st.info(translate_text(
                "If you're having issues with microphone access, try using a text-based query instead.",
                lang_code
            ))

# Text-based fallback
st.markdown("---")
st.markdown("## " + translate_text("Text-Based Query (Alternative)", lang_code))
st.markdown(translate_text(
    "If you're having issues with voice recognition, you can type your question here:",
    lang_code
))

text_query = st.text_input(
    translate_text("Type your question about crop diseases", lang_code),
    placeholder=translate_text("e.g., What is the treatment for tomato early blight?", lang_code)
)

if text_query:
    response = process_question(text_query, lang_code)
    st.markdown(f"**{translate_text('Assistant', lang_code)}:**")
    st.markdown(response)
    
    # Generate audio response
    with st.spinner(translate_text("Generating audio response...", lang_code)):
        generate_audio_response(response, lang_code)

def process_question(question, lang_code):
    """
    Process a question about crop diseases and generate a response.
    
    Args:
        question (str): User's question
        lang_code (str): Language code (en, hi)
        
    Returns:
        str: Response to the question
    """
    question_lower = question.lower()
    
    # Check for disease-specific questions
    for disease_name in DISEASE_INFO.keys():
        formatted_name = format_disease_name(disease_name).lower()
        
        if formatted_name in question_lower:
            # Get disease information
            disease_info = get_disease_info(disease_name, lang_code)
            
            # Check what specific information is being asked
            if any(word in question_lower for word in ["symptom", "sign", "look like"]):
                return disease_info["symptoms"]
            elif any(word in question_lower for word in ["treatment", "cure", "medicine", "how to treat"]):
                return f"{disease_info['treatment']} {disease_info['organic_treatment']}"
            elif any(word in question_lower for word in ["prevent", "avoid", "stop"]):
                return disease_info["preventive_measures"]
            elif any(word in question_lower for word in ["cause", "reason", "why", "how does"]):
                return disease_info["cause"]
            elif any(word in question_lower for word in ["recover", "how long", "time"]):
                return disease_info["recovery"]
            elif any(word in question_lower for word in ["fertilizer", "nutrient"]):
                return disease_info["fertilizer"]
            elif any(word in question_lower for word in ["pesticide", "chemical", "spray"]):
                return disease_info["pesticide"]
            else:
                # General information about the disease
                return f"{disease_info['symptoms']} {disease_info['treatment']}"
    
    # Check for general questions
    if any(word in question_lower for word in ["what is", "what are", "tell me about", "explain"]):
        if any(word in question_lower for word in ["crop", "plant", "disease"]):
            return translate_text(
                "Crop diseases are caused by pathogens such as fungi, bacteria, viruses, and nematodes. "
                "They can affect various parts of the plant including leaves, stems, roots, and fruits. "
                "Early detection and proper treatment are crucial for managing crop diseases.",
                lang_code
            )
    
    if any(word in question_lower for word in ["how", "prevent", "avoid", "stop"]):
        if any(word in question_lower for word in ["disease", "infection"]):
            return translate_text(
                "To prevent crop diseases: 1) Use disease-resistant varieties, 2) Practice crop rotation, "
                "3) Maintain proper plant spacing for air circulation, 4) Avoid overhead watering, "
                "5) Keep the garden clean of debris, 6) Monitor plants regularly for early signs of disease, "
                "7) Apply preventive fungicides when conditions favor disease development.",
                lang_code
            )
    
    if any(word in question_lower for word in ["organic", "natural"]):
        if any(word in question_lower for word in ["treatment", "control", "manage"]):
            return translate_text(
                "Organic disease control methods include: 1) Neem oil spray for fungal diseases and pests, "
                "2) Copper-based fungicides, 3) Bacillus thuringiensis (Bt) for certain pests, "
                "4) Compost tea to boost plant immunity, 5) Proper crop rotation, "
                "6) Companion planting to deter pests, 7) Biological controls like beneficial insects.",
                lang_code
            )
    
    # Default response
    return translate_text(
        "I'm not sure I understand your question. Could you be more specific about which crop disease "
        "you're asking about? You can ask about symptoms, treatments, prevention methods, or causes "
        "of specific diseases like 'tomato early blight' or 'apple scab'.",
        lang_code
    )

def generate_audio_response(text, lang_code):
    """
    Generate an audio response using gTTS.
    
    Args:
        text (str): Text to convert to speech
        lang_code (str): Language code (en, hi)
    """
    try:
        from gtts import gTTS
        
        # Create a temporary file for audio
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_audio:
            temp_audio_path = temp_audio.name
        
        try:
            # Generate speech
            tts = gTTS(text=text, lang=lang_code, slow=False)
            tts.save(temp_audio_path)
            
            # Read the audio file
            with open(temp_audio_path, "rb") as audio_file:
                audio_bytes = audio_file.read()
            
            # Create a download button for the audio
            st.download_button(
                label=translate_text("🔊 Listen to Response", lang_code),
                data=audio_bytes,
                file_name="cropcare_response.mp3",
                mime="audio/mp3"
            )
            
            # Try to play audio using HTML5 audio player
            try:
                audio_base64 = base64.b64encode(audio_bytes).decode()
                audio_html = f"""
                <audio controls>
                    <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
                    Your browser does not support the audio element.
                </audio>
                """
                st.markdown(audio_html, unsafe_allow_html=True)
            except:
                pass  # Fallback to download button if audio player fails
        
        finally:
            # Clean up temporary file
            if os.path.exists(temp_audio_path):
                os.remove(temp_audio_path)
    
    except ImportError:
        st.warning(translate_text(
            "gTTS package is not installed. Text response only.",
            lang_code
        ))
    except Exception as e:
        st.warning(f"{translate_text('Error generating audio response:', lang_code)} {str(e)}")