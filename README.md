

## 🌿 CropCare AI
# AI-Powered Smart Crop Disease Detection and Treatment Recommendation System
Python
TensorFlow
Streamlit
Theme
Status

[Artificial Intelligence in Agriculture]

Features • Workflow • Installation • Demo • Future Scope

</div>

📖 Project Overview
CropCare AI is an end-to-end intelligent farming assistant designed to bridge the gap between complex agricultural pathology and grassroots farmers. By leveraging cutting-edge MobileNetV2 Transfer Learning, the application can instantly diagnose crop diseases from leaf images captured via a smartphone camera.

Beyond simple detection, CropCare AI acts as a comprehensive agronomist in your pocket—providing detailed symptomatic analysis, organic and chemical treatment pathways, preventive measures, and real-time weather-adaptive farming advice. Engineered with a focus on accessibility, it features bilingual support (English & Hindi) and an offline-capable AI core to function seamlessly in low-connectivity rural environments.

⚠️ Problem Statement
Agriculture is the backbone of developing economies, yet millions of farmers face catastrophic crop losses annually due to late detection of plant diseases. The current agricultural landscape suffers from several critical inefficiencies:

1.Lack of Expert Guidance: Agricultural extension workers are severely outnumbered by farmers. By the time an expert diagnoses a disease, it is often too late to save the crop.
2.Inability to Identify Diseases: Farmers frequently misidentify fungal, bacterial, or viral infections, leading to the application of wrong pesticides, wasting resources and poisoning the soil.
3.Delayed Treatment: Diseases like Late Blight can destroy a tomato field in 48 hours. Manual identification is inherently too slow.
4.Severe Crop Losses: Undiagnosed diseases lead to an estimated 20-40% reduction in global crop yields annually, directly impacting food security and farmer livelihoods.
5.The Digital Divide (Poor Internet): Most sophisticated AI solutions rely on cloud computing. Rural farmlands notoriously suffer from poor 4G/5G connectivity, rendering cloud-dependent applications useless.
6.Language Barriers: Existing digital tools are predominantly in English, alienating non-English speaking farmers in rural demographics.


# 💡 Our Solution
CropCare AI directly addresses these bottlenecks through a localized, intelligent, and highly accessible architecture:

Instant AI Diagnosis: Replaces human lag with sub-second Deep Learning inference, identifying diseases at early, treatable stages.
Actionable Intelligence: Does not just say "Disease Found." It provides exact fertilizer names, pesticide dosages, and organic alternatives.
Edge Computing (Offline AI): The TensorFlow model runs entirely on the local machine. The core disease detection feature works flawlessly with zero internet connectivity.
Multilingual & Voice-First: Supports Hindi and English, integrating a Voice Assistant so illiterate or visually impaired farmers can simply speak their queries.
Contextual Awareness: Integrates real-time weather APIs to dynamically alter treatment advice (e.g., warning against chemical sprays if rain is imminent).

✨ Key Features
| Feature | Description | Impact |
| :--- | :--- | :--- |
| 📷 **Image Ingestion** | Upload from gallery or capture directly via device camera. | Easy, intuitive data collection. |
| 🧠 **AI Detection** | MobileNetV2 Transfer Learning with high-accuracy classification. | Fast, reliable disease identification. |
| 📊 **Confidence Scoring** | Provides a precise percentage probability of the prediction. | Builds user trust in the AI. |
| 🩺 **Symptom & Cause Analysis** | Detailed text explaining what is happening to the plant and why. | Educates the farmer on pathology. |
| 💊 **Dual Treatment Paths** | Separate, detailed recommendations for Organic and Chemical treatments. | Empowers choice based on budget/farming style. |
| 🛡️ **Preventive Measures** | Actionable steps to stop the disease from spreading to healthy crops. | Mitigates future crop loss. |
| 🌦️ **Weather Advisory** | Location-specific weather fetching with dynamic agricultural advice. | Prevents weather-induced treatment failures. |
| 🎙️ **Voice Assistant** | Speak questions in Hindi/English; receive spoken audio responses. | Breaks literacy and language barriers. |
| 📱 **QR Scanner** | Scan seed bags/fertilizer packets for instant digital information. | Modernizes input management. |
| 🌐 **Multi-Language UI** | Entire interface dynamically switches between English and Hindi. | Maximizes rural adoption. |
| 📜 **Prediction History** | Local CSV logging of all past scans with dates and confidence. | Tracks crop health over time. |
| 📴 **Offline Core AI** | Disease prediction engine requires no internet connection. | Functionality in remote farmlands. |

🔄 Workflow
The following diagram illustrates the end-to-end user journey from image capture to actionable treatment:
graph TD
    A[📷 User Uploads/Captures Leaf Image] --> B[⚙️ Image Preprocessing & Resizing]
    B --> C[🧠 MobileNetV2 AI Model Inference]
    C --> D[📈 Confidence Score Calculation]
    D --> E{🟢 Confidence > 60%?}
    E -- Yes --> F[🔍 Disease Identified]
    E -- No --> G[⚠️ Low Confidence: Request Better Image]
    F --> H[📋 Retrieve Disease Database]
    H --> I[💊 Display Treatment & Prevention]
    I --> J[🌤️ Fetch Weather Context]
    J --> K[📝 Generate Comprehensive Report]
    K --> L[💾 Save to History & Download]

🗺️ Application Routing
CropCare AI is built on a robust Streamlit multi-page architecture, ensuring clean separation of concerns:

🏠 Home (1_Home.py): The central dashboard. Displays project statistics, feature highlights, and quick-start steps.
🔍 Disease Detection (2_Disease_Detection.py): The core engine. Handles file uploads, camera input, triggers the TensorFlow model, and renders the detailed treatment UI.
🌤️ Weather (3_Weather.py): Connects to OpenWeatherMap API, parses JSON, calculates rain probability, and renders context-aware farming advice.
📱 QR Scanner (4_QR_Scanner.py): Utilizes OpenCV and PyZbar to decode QR codes from uploaded images or camera feeds.
🎙️ Voice Assistant (5_Voice_Assistant.py): Interfaces with SpeechRecognition for STT and gTTS for TTS, routing through a localized NLP keyword matcher.
📊 History (6_History.py): Reads the local prediction_history.csv using Pandas and renders a clean, sortable data table.
ℹ️ About (7_About.py): Project documentation, tech stack details, and future roadmap.

🖥️ Prototype Functionality
Initiation: The user opens the app and is greeted by a localized dashboard.
Data Input: The user navigates to "Disease Detection" and selects the camera tab. They snap a photo of a diseased leaf.
Processing: The image is instantly resized to 
224×224
 pixels, normalized to 
[0,1]
, and passed to the .keras model.
Inference: The model outputs a softmax probability array (e.g., [0.05, 0.92, 0.03]).
Presentation: The UI maps the highest probability (92%) to Tomato___Late_Blight. A matplotlib confidence bar chart is rendered.
Enrichment: The app queries the local config.py dictionary for "Tomato Late Blight" and populates tabs for Symptoms, Organic Treatment (e.g., Copper spray), and Chemical Treatment (e.g., Mandipropamid).
Logging: The result, timestamp, and image name are automatically appended to prediction_history.csv.

🛠️ Tech Stack
| Technology | Purpose in CropCare AI |
| :--- | :--- |
| **Python** | Core programming language. |
| **Streamlit** | Rapid frontend deployment, UI components, and multi-page routing. |
| **TensorFlow / Keras** | Model building, training, and local inference engine. |
| **MobileNetV2** | Pre-trained base model for Transfer Learning (optimized for edge/mobile). |
| **OpenCV** | Image processing, array manipulation, and QR code matrix reading. |
| **Pillow** | Image format handling and validation. |
| **NumPy** | High-performance mathematical array operations for pixel manipulation. |
| **Pandas** | Data structuring for reading and displaying prediction history CSVs. |
| **Matplotlib** | Generating static confidence percentage bar charts. |
| **SpeechRecognition** | Converting user voice audio (WAV) to text strings. |
| **gTTS** | Converting text treatment responses back to MP3 audio. |
| **PyZbar** | Decoding QR codes from image arrays. |
| **Deep Translator** | Fallback translation engine for dynamic strings. |
| **Requests** | HTTP GET requests to the OpenWeatherMap API. |

🧠 Machine Learning Pipeline
Our ML pipeline is engineered for high accuracy on limited hardware, avoiding the need for expensive GPU cloud hosting.
Technical Details:

Base Model: MobileNetV2 (ImageNet weights, without top layers).
Freezing: All base layers are frozen initially to retain pre-trained feature extraction.
Classifier Head: Custom Sequential layers added: GlobalAveragePooling2D -> Dense(512, ReLU) -> BatchNormalization -> Dropout(0.5) -> Dense(num_classes, Softmax).
Augmentation: Random rotations (20%), width/height shifts (20%), shear (20%), and horizontal flips to prevent overfitting on the relatively small PlantDoc dataset.
Loss Function: Categorical Crossentropy.
Optimizer: Adam with a learning rate of 
0.0001
.
Callbacks: EarlyStopping (patience=5) and ReduceLROnPlateau to ensure optimal convergence.


📁 Folder Structure
CropCareAI/
├── app.py                  # Main entry point, session state, CSS, routing
├── config.py               # Constants, API keys, translations, disease DB
├── utils.py                # Helper functions (QR, Voice, CSV, Charts)
├── model.py                # MobileNetV2 architecture definition
├── preprocessing.py        # Image resizing, normalization, data generators
├── train.py                # Model training script with callbacks
├── evaluation.py           # Confusion matrix, classification reports
├── predict.py              # Inference logic, model loading, prediction output
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── models/                 # Directory containing cropcare_model.keras
├── dataset/                # Training data (PlantDoc structure)
│   ├── Apple___Healthy/
│   ├── Apple___Scab/
│   ├── Corn___Rust/
│   └── ...
├── assets/                 # Static files
├── prediction_history.csv  # Auto-generated user history log
└── pages/                  # Streamlit multipage modules
    ├── __init__.py
    ├── 1_Home.py
    ├── 2_Disease_Detection.py
    ├── 3_Weather.py
    ├── 4_QR_Scanner.py
    ├── 5_Voice_Assistant.py
    ├── 6_History.py
    └── 7_About.py


## 
# Future Improvements: In future versions, we plan to expand CropCare AI by supporting all major Indian languages, making the application accessible to farmers across every region of the country. This multilingual support will enable users to interact with the application, understand disease diagnoses, and receive treatment recommendations in their preferred language, helping bridge language barriers and making AI-powered agricultural assistance more inclusive, user-friendly, and impactful.


🚀 Installation Guide
Ensure you have Python 3.9+ installed on your system.

1. Clone the Repository
git clone https://github.com/your-username/CropCareAI.git
cd CropCareAI

2. Create a Virtual Environment (Recommended)
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt
Note: For QR Scanning (pyzbar), you may need system-level ZBar libraries:

Ubuntu: sudo apt-get install libzbar0
Windows: Install via conda: conda install -c conda-forge pyzbar

4. Setup Dataset

Download the PlantDoc Dataset.
Extract images into the dataset/ folder following the ClassName/Image.jpg hierarchy.


5. Run the Application
streamlit run app.py



🎯 Key Use Cases
For Farmers: Instantly identify unknown leaf blights in the field without waiting for an agricultural officer. Get immediate instructions on which chemical to buy.
For Students/Researchers: A plug-and-play baseline model for agricultural computer vision research, complete with data augmentation and evaluation pipelines.
For Agriculture Departments: Can be deployed as a centralized kiosk system in rural areas to crowdsource disease outbreak data via the prediction_history.csv logs.
For Agri-Shops: Customers can scan diseased leaves in the store, allowing shopkeepers to recommend the exact pesticide required.

📴 Offline Capability
One of the most critical engineering decisions in CropCare AI is Edge AI Deployment.
The entire TensorFlow model is saved as a .keras file locally. When a user uploads an image, the inference is computed entirely on the CPU/GPU of the local machine using TensorFlow's C++ backend. No data is sent to external cloud servers for prediction. This ensures:

Sub-second response times regardless of network latency.
100% functionality in remote farmlands with zero connectivity.
Complete privacy of farmer data and location.
(Note: The Weather and Voice features require internet for API calls and STT processing, but the core disease detection remains offline).

🔮 Future Scope
Mobile App Deployment: Convert the TensorFlow model to TensorFlow Lite (.tflite) and wrap the UI in Flutter/React Native for Android/iOS.
IoT Sensor Integration: Connect with soil moisture, NPK, and humidity sensors for automated, holistic crop health monitoring.
Drain Integration: Pair with agricultural drones to capture field-wide imagery and geo-tag disease outbreaks.
Advanced Soil Analysis: Allow users to upload soil report PDFs, using NLP to extract data and suggest crop-specific rotations.
Expanded Voice NLP: Integrate local LLMs (like Llama-3-8B) via Ollama for conversational, context-aware farming assistants in regional languages.
Market Price Prediction: Integrate mandi (market) APIs to advise farmers on the best time to harvest and sell based on current disease state and market trends.
Government Scheme Integration: Auto-suggest applicable government subsidies for crop loss based on the diagnosed disease severity.
⚠️ Limitations
Dataset Dependency: The model is only as good as the PlantDoc dataset. It may struggle with highly localized or newly mutated plant pathogens not present in the training data.
Lighting Conditions: Like most computer vision models, extreme overexposure or very dark images can degrade prediction confidence.
Multiple Diseases: The current architecture is trained primarily for single-disease classification. It may not accurately diagnose leaves simultaneously suffering from two distinct pathogens.
Language Coverage: Currently limited to English and Hindi. Expanding to other regional languages (e.g., Tamil, Marathi, Bengali) requires translation dataset expansion.
💡 Innovation
Traditional disease detection systems stop at classification (e.g., "It is Scab"). CropCare AI is an action-engine, not just a classification engine.
It bridges the gap between raw AI probabilities and actionable agronomy by pairing the model with a deeply structured, multilingual relational database of treatments, causes, and preventive measures. Furthermore, the integration of localized text-to-speech, offline edge inference, and real-time weather contextualization transforms it from a standard GitHub tutorial project into a production-ready agricultural tool.

🧪 Demo Instructions (For Judges)
To effectively evaluate this project, please follow these steps:

Start the App: Run streamlit run app.py.
Test Language Toggle: Switch the language to "Hindi" in the sidebar. Observe the entire UI translate instantly.
Test Core AI:
Go to "Disease Detection".
Upload a clear picture of a diseased leaf (e.g., Tomato Late Blight or Apple Scab).
Observe the confidence score and the detailed treatment tabs that appear.
Test Camera: Use the "Capture Image" tab to take a live photo and run prediction.
Test History: Return to the "History" page to see your previous scan logged with timestamps.
Test Weather: Go to "Weather", enter a city (e.g., "Mumbai"), and observe the dynamic farming advice generated based on the current humidity and temperature.
Test Voice: Go to "Voice Assistant", grant microphone permissions, speak "What is good for yellow leaves?", and listen to the generated audio response.

📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgements
PlantDoc Dataset: Special thanks to Pratik Kayal for curating the real-world plant disease dataset.
TensorFlow & Keras: For providing accessible, state-of-the-art deep learning tools.
Streamlit: For revolutionizing Python-based data app deployment.
OpenWeatherMap: For providing the weather data API.
<div align="center">

🌾 Final Conclusion
Crop yields should not be left to chance, and expert agricultural advice should not be a luxury reserved for large-scale commercial farms. CropCare AI represents a paradigm shift in grassroots agriculture. By putting a highly accurate, offline-capable AI diagnostic tool directly into the hands of smallholder farmers, we are not just detecting diseases—we are preventing crop loss, reducing chemical waste, and securing livelihoods.

This project proves that with the right application of Deep Learning and thoughtful, user-centric design, technology can be demystified and translated into tangible, life-changing impact for the people who feed the world.

Built with 🌿 for the farmers of tomorrow.

</div>
