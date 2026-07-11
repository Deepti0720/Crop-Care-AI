"""
Weather Advice page for CropCare AI
This file exists to provide farming advice based on weather conditions.
It uses the OpenWeatherMap API to fetch weather data for a user-specified city.
It imports from utils.py for translation and weather advice functions.
"""

import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# Import project modules
from utils import translate_text, get_weather_advice
from config import WEATHER_API_KEY, WEATHER_BASE_URL

# Get current language
language = st.session_state.language
lang_code = "en" if language == "English" else "hi"

# Page title
st.title("🌤️ " + translate_text("Weather-Based Farming Advice", lang_code))
st.markdown("---")

# Instructions
st.markdown("### " + translate_text("Instructions", lang_code))
st.markdown(translate_text("""
1. Enter the name of your city
2. Click 'Get Weather' to fetch current weather conditions
3. View farming advice based on the weather
""", lang_code))

st.markdown("---")

# City input section
col1, col2 = st.columns([1, 3])

with col1:
    city = st.text_input(
        translate_text("City Name", lang_code),
        placeholder=translate_text("Enter city name", lang_code)
    )
    
    get_weather_button = st.button(
        translate_text("🌤️ Get Weather", lang_code),
        type="primary",
        disabled=not city
    )

with col2:
    # Weather display container
    weather_container = st.container()

# Process weather request
if get_weather_button and city:
    with weather_container:
        with st.spinner(translate_text(f"Fetching weather for {city}...", lang_code)):
            try:
                # Check if API key is set
                if WEATHER_API_KEY == "YOUR_OPENWEATHERMAP_API_KEY":
                    st.warning(translate_text(
                        "Please set your OpenWeatherMap API key in the config.py file to use this feature. Using sample data for demonstration.",
                        lang_code
                    ))
                    
                    # Use sample data for demonstration
                    weather_data = {
                        "main": {
                            "temp": 28.5,
                            "humidity": 65
                        },
                        "weather": [
                            {
                                "main": "Clear",
                                "description": "clear sky"
                            }
                        ],
                        "name": city
                    }
                else:
                    # Make API request
                    url = f"{WEATHER_BASE_URL}?q={city}&appid={WEATHER_API_KEY}&units=metric"
                    response = requests.get(url)
                    response.raise_for_status()
                    weather_data = response.json()
                
                # Extract weather information
                temperature = weather_data["main"]["temp"]
                humidity = weather_data["main"]["humidity"]
                weather_condition = weather_data["weather"][0]["main"]
                weather_description = weather_data["weather"][0]["description"]
                city_name = weather_data["name"]
                
                # Display weather information
                st.markdown(f"## {translate_text('Current Weather in', lang_code)} {city_name}")
                
                # Weather metrics
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric(
                        translate_text("Temperature", lang_code),
                        f"{temperature:.1f}°C",
                        delta=None
                    )
                
                with col2:
                    st.metric(
                        translate_text("Humidity", lang_code),
                        f"{humidity}%",
                        delta=None
                    )
                
                with col3:
                    st.metric(
                        translate_text("Condition", lang_code),
                        translate_text(weather_condition, lang_code),
                        delta=None
                    )
                
                # Weather icon
                weather_icons = {
                    "Clear": "☀️",
                    "Clouds": "☁️",
                    "Rain": "🌧️",
                    "Drizzle": "🌦️",
                    "Thunderstorm": "⛈️",
                    "Snow": "❄️",
                    "Mist": "🌫️",
                    "Fog": "🌫️",
                    "Haze": "🌫️"
                }
                
                weather_icon = weather_icons.get(weather_condition, "🌤️")
                
                st.markdown(f"### {weather_icon} {translate_text(weather_description, lang_code)}")
                
                st.markdown("---")
                
                # Get weather-based advice
                weather_advice = get_weather_advice(weather_condition, temperature, humidity, lang_code)
                
                # Display advice
                st.markdown("## " + translate_text("Farming Advice", lang_code))
                
                tab1, tab2, tab3 = st.tabs([
                    translate_text("General Advice", lang_code),
                    translate_text("Temperature Advice", lang_code),
                    translate_text("Humidity Advice", lang_code)
                ])
                
                with tab1:
                    st.markdown(f"### {translate_text('Based on Weather Condition', lang_code)}")
                    st.markdown(weather_advice["condition_advice"])
                
                with tab2:
                    st.markdown(f"### {translate_text('Based on Temperature', lang_code)} ({temperature:.1f}°C)")
                    st.markdown(weather_advice["temperature_advice"])
                
                with tab3:
                    st.markdown(f"### {translate_text('Based on Humidity', lang_code)} ({humidity}%)")
                    st.markdown(weather_advice["humidity_advice"])
                
                # Weather suitability chart
                st.markdown("---")
                st.markdown("## " + translate_text("Weather Suitability", lang_code))
                
                # Calculate suitability scores
                temp_score = 100
                if temperature < 5 or temperature > 40:
                    temp_score = 20
                elif temperature < 10 or temperature > 35:
                    temp_score = 40
                elif temperature < 15 or temperature > 30:
                    temp_score = 70
                
                humidity_score = 100
                if humidity < 20 or humidity > 90:
                    humidity_score = 20
                elif humidity < 30 or humidity > 80:
                    humidity_score = 40
                elif humidity < 40 or humidity > 70:
                    humidity_score = 70
                
                condition_score = 100
                if weather_condition in ["Thunderstorm", "Snow"]:
                    condition_score = 20
                elif weather_condition in ["Rain", "Fog", "Haze"]:
                    condition_score = 50
                elif weather_condition in ["Drizzle", "Mist"]:
                    condition_score = 70
                
                # Create radar chart
                fig = go.Figure(data=go.Scatterpolar(
                    r=[temp_score, humidity_score, condition_score, (temp_score + humidity_score + condition_score) / 3],
                    theta=[translate_text("Temperature", lang_code), 
                           translate_text("Humidity", lang_code), 
                           translate_text("Condition", lang_code),
                           translate_text("Overall", lang_code)],
                    fill='toself',
                    fillcolor='rgba(46, 125, 50, 0.2)',
                    line=dict(color='#2E7D32')
                ))
                
                fig.update_layout(
                    polar=dict(
                        radialaxis=dict(
                            visible=True,
                            range=[0, 100]
                        )),
                    showlegend=False,
                    title=translate_text("Farming Suitability Score", lang_code)
                )
                
                st.plotly_chart(fig, use_container_width=True)
                
                # Overall suitability
                overall_score = (temp_score + humidity_score + condition_score) / 3
                
                if overall_score >= 80:
                    suitability_text = translate_text("Excellent conditions for farming activities", lang_code)
                    suitability_color = "green"
                elif overall_score >= 60:
                    suitability_text = translate_text("Good conditions for most farming activities", lang_code)
                    suitability_color = "green"
                elif overall_score >= 40:
                    suitability_text = translate_text("Moderate conditions, some activities may be limited", lang_code)
                    suitability_color = "orange"
                else:
                    suitability_text = translate_text("Poor conditions, limit farming activities", lang_code)
                    suitability_color = "red"
                
                st.markdown(f"### :{suitability_color}[" + translate_text("Overall Assessment", lang_code) + f": {overall_score:.0f}/100]")
                st.markdown(f":{suitability_color}[" + suitability_text + "]")
                
                st.success(translate_text("Weather data fetched successfully!", lang_code))
                
            except requests.exceptions.RequestException as e:
                st.error(f"{translate_text('Error fetching weather data:', lang_code)} {str(e)}")
                st.info(translate_text("Please check your internet connection and try again.", lang_code))
            except Exception as e:
                st.error(f"{translate_text('Error processing weather data:', lang_code)} {str(e)}")