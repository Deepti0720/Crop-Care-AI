import streamlit as st

# ---------------- PAGE ---------------- #

st.title("🌱 CropCare AI")
st.markdown("### AI Powered Crop Disease Detection & Smart Farming Assistant")

st.write(
    """
Detect crop diseases instantly using Artificial Intelligence.
Upload a leaf image, identify diseases, receive treatment recommendations,
and improve crop health with smart farming support.
"""
)

st.markdown("---")

# ---------------- HERO IMAGE ---------------- #

st.image(
    "https://images.unsplash.com/photo-1500937386664-56d1dfef3854?w=1200",
    use_container_width=500
)

st.markdown("---")

# ---------------- FEATURES ---------------- #

st.markdown("## 🚀 Key Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("""
### 📷 Disease Detection

✔ Upload Crop Leaf

✔ AI Disease Prediction

✔ Confidence Score
""")

with col2:
    st.info("""
### 🌦 Weather Advisor

✔ Live Weather

✔ Farming Advice

✔ Crop Protection Tips
""")

with col3:
    st.warning("""
### 🎤 Voice Assistant

✔ English Support

✔ Hindi Support

✔ Smart Farming Help
""")

st.markdown("---")

# ---------------- WHY CHOOSE ---------------- #

st.markdown("## 🌾 Why CropCare AI?")

c1, c2, c3 = st.columns(3)

c1.metric("Model Accuracy", "95%+")

c2.metric("Diseases Covered", "38+")

c3.metric("Languages", "2")

st.markdown("---")

# ---------------- ABOUT ---------------- #

st.markdown("## 📖 About")

st.write("""
CropCare AI is a deep learning based crop disease detection system built
using **TensorFlow, MobileNetV2 and Streamlit**.

The system allows farmers to upload crop images and instantly receive:

- 🌱 Disease Detection
- 💊 Treatment Recommendation
- 🌦 Weather-based Advice
- 🎤 Voice Assistance

The goal of CropCare AI is to reduce crop loss and help farmers make better decisions using Artificial Intelligence.
""")

st.markdown("---")

st.markdown(
"""
<center>

### 🌿 Made with ❤️ for Smart Agriculture

TensorFlow • Streamlit • MobileNetV2 • OpenCV

</center>
""",
unsafe_allow_html=True
)