"""
Configuration file for CropCare AI
This file exists to centralize all configuration settings, making the codebase more maintainable.
It contains paths, model parameters, API keys, and other settings used throughout the project.
Other files import this to access configuration values.
"""

import os

# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Paths
MODEL_PATH = os.path.join(BASE_DIR, "models", "cropcare_model.keras")
DATASET_PATH = DATASET_PATH = os.path.join(
    BASE_DIR,
    "dataset",
    "plantdoc",
    "PlantDoc-Dataset",
    "train"
)
HISTORY_PATH = os.path.join(BASE_DIR, "prediction_history.csv")
ASSETS_PATH = os.path.join(BASE_DIR, "assets")

# Ensure directories exist
os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
os.makedirs(ASSETS_PATH, exist_ok=True)

# Model parameters
IMAGE_SIZE = (224, 224)
BATCH_SIZE = 32
EPOCHS = 15
LEARNING_RATE = 0.001
VALIDATION_SPLIT = 0.2

# Weather API
WEATHER_API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"  # Replace with your actual API key
WEATHER_BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Language settings
SUPPORTED_LANGUAGES = {
    "English": "en",
    "Hindi": "hi"
}

# Disease information dictionary
DISEASE_INFO = {
    "Apple___Healthy": {
        "symptoms": {
            "en": "No visible symptoms. The plant appears healthy with normal leaf color and structure.",
            "hi": "कोई दृश्यमान लक्षण नहीं। पौधा सामान्य पत्ती के रंग और संरचना के साथ स्वस्थ दिखता है।"
        },
        "cause": {
            "en": "No disease. The plant is in good health.",
            "hi": "कोई बीमारी नहीं। पौधा अच्छी स्वास्थ्य स्थिति में है।"
        },
        "treatment": {
            "en": "No treatment needed. Continue regular care.",
            "hi": "कोई उपचार आवश्यक नहीं। नियमित देखभाल जारी रखें।"
        },
        "organic_treatment": {
            "en": "Continue with organic fertilizers and proper watering.",
            "hi": "जैविक उर्वरकों और उचित पानी देने के साथ जारी रखें।"
        },
        "chemical_treatment": {
            "en": "No chemical treatment needed.",
            "hi": "कोई रासायनिक उपचार आवश्यक नहीं।"
        },
        "preventive_measures": {
            "en": "Maintain proper watering, fertilization, and pruning schedules.",
            "hi": "उचित पानी, उर्वरक और प्रूनिंग अनुसूची बनाए रखें।"
        },
        "recovery": {
            "en": "N/A - Plant is healthy",
            "hi": "लागू नहीं - पौधा स्वस्थ है"
        },
        "fertilizer": {
            "en": "Balanced NPK fertilizer (10-10-10) during growing season.",
            "hi": "बढ़ते मौसम के दौरान संतुलित NPK उर्वरक (10-10-10)।"
        },
        "pesticide": {
            "en": "No pesticide needed. Monitor for pests regularly.",
            "hi": "कोई कीटनाशक आवश्यक नहीं। नियमित रूप से कीटों की निगरानी करें।"
        }
    },
    "Apple___Scab": {
        "symptoms": {
            "en": "Olive-green to dark brown spots on leaves, often with a velvety texture. Leaves may curl or drop prematurely. Fruit may have corky, scab-like lesions.",
            "hi": "पत्तियों पर जैतून-हरे से गहरे भूरे रंग के धब्बे, अक्सर वेलवेटी बनावट के साथ। पत्तियां मुड़ सकती हैं या समय से पहले गिर सकती हैं। फलों पर कॉर्की, डाग जैसी घाव हो सकती हैं।"
        },
        "cause": {
            "en": "Fungal infection caused by Venturia inaequalis. Favored by cool, wet weather in spring.",
            "hi": "वेंच्यूरिया इनएक्वालिस के कारण फंगल संक्रमण। वसंत ऋतु में ठंडे, गीले मौसम के अनुकूल।"
        },
        "treatment": {
            "en": "Apply fungicides at green tip, tight cluster, pink, and petal fall stages. Remove and destroy infected leaves and fruit.",
            "hi": "हरी टिप, टाइट क्लस्टर, गुलाबी और पंखुड़ी गिरने के चरणों में कवकनाशक लगाएं। संक्रमित पत्तियों और फलों को हटा दें और नष्ट करें।"
        },
        "organic_treatment": {
            "en": "Apply sulfur-based fungicides or copper sprays. Use neem oil as a preventive measure.",
            "hi": "सल्फर-आधारित कवकनाशक या तांबा स्प्रे लगाएं। नीम का तेल एक निवारक उपाय के रूप में उपयोग करें।"
        },
        "chemical_treatment": {
            "en": "Apply myclobutanil, captan, or dodine according to label instructions.",
            "hi": "लेबल निर्देशों के अनुसार माइक्लोब्यूटेनिल, कैप्टन, या डोडिन लगाएं।"
        },
        "preventive_measures": {
            "en": "Plant resistant varieties. Ensure good air circulation. Rake and destroy fallen leaves in autumn. Apply dormant oil spray in early spring.",
            "hi": "प्रतिरोधी किस्में लगाएं। अच्छी हवा का परिसंचरण सुनिश्चित करें। शरद ऋतु में गिरी हुई पत्तियों को बुहारें और नष्ट करें। शुरुआती वसंत में डॉर्मेंट ऑयल स्प्रे लगाएं।"
        },
        "recovery": {
            "en": "2-3 weeks with proper treatment. Severe cases may take longer.",
            "hi": "उचित उपचार के साथ 2-3 सप्ताह। गंभीर मामलों में अधिक समय लग सकता है।"
        },
        "fertilizer": {
            "en": "Balanced fertilizer to promote overall plant health and resistance.",
            "hi": "समग्र पौधे के स्वास्थ्य और प्रतिरोध को बढ़ावा देने के लिए संतुलित उर्वरक।"
        },
        "pesticide": {
            "en": "Not directly effective against apple scab. Focus on fungicides.",
            "hi": "सेब के डाग के खिलाफ सीधे प्रभावी नहीं। कवकनाशक पर ध्यान केंद्रित करें।"
        }
    },
    "Corn___Rust": {
        "symptoms": {
            "en": "Small, reddish-brown to dark brown pustules on upper and lower leaf surfaces. Severe cases can lead to premature leaf death.",
            "hi": "ऊपरी और निचली पत्ती की सतहों पर छोटे, लाल-भूरे से गहरे भूरे रंग के फफोले। गंभीर मामलों में समय से पहले पत्ती की मृत्यु हो सकती है।"
        },
        "cause": {
            "en": "Fungal infection caused by Puccinia sorghi. Favored by moderate temperatures and high humidity.",
            "hi": "पुक्सिनिया सोरघी के कारण फंगल संक्रमण। मध्यम तापमान और उच्च आर्द्रता के अनुकूल।"
        },
        "treatment": {
            "en": "Apply fungicides at early infection stages. Remove and destroy infected plant debris.",
            "hi": "शुरुआती संक्रमण चरणों में कवकनाशक लगाएं। संक्रमित पौधे के मलबे को हटा दें और नष्ट करें।"
        },
        "organic_treatment": {
            "en": "Apply sulfur-based fungicides or copper sprays. Use neem oil as a preventive measure.",
            "hi": "सल्फर-आधारित कवकनाशक या तांबा स्प्रे लगाएं। नीम का तेल एक निवारक उपाय के रूप में उपयोग करें।"
        },
        "chemical_treatment": {
            "en": "Apply triazole or strobilurin fungicides according to label instructions.",
            "hi": "लेबल निर्देशों के अनुसार ट्रायज़ोल या स्ट्रोबिलुरिन कवकनाशक लगाएं।"
        },
        "preventive_measures": {
            "en": "Plant resistant corn varieties. Crop rotation. Ensure proper plant spacing for air circulation.",
            "hi": "प्रतिरोधी मक्का की किस्में लगाएं। फसल रोटेशन। हवा के परिसंचरण के लिए उचित पौधों के बीच की दूरी सुनिश्चित करें।"
        },
        "recovery": {
            "en": "2-3 weeks with proper treatment. Severe cases may have reduced yield.",
            "hi": "उचित उपचार के साथ 2-3 सप्ताह। गंभीर मामलों में उपज कम हो सकती है।"
        },
        "fertilizer": {
            "en": "Balanced fertilizer with adequate potassium to improve plant resistance.",
            "hi": "पौधे के प्रतिरोध को बेहतर बनाने के लिए पर्याप्त पोटैशियम के साथ संतुलित उर्वरक।"
        },
        "pesticide": {
            "en": "Not directly effective against corn rust. Focus on fungicides.",
            "hi": "मक्के के जंग के खिलाफ सीधे प्रभावी नहीं। कवकनाशक पर ध्यान केंद्रित करें।"
        }
    },
    "Potato___Early_Blight": {
        "symptoms": {
            "en": "Dark brown to black lesions with concentric rings (target-spot pattern) on older leaves. Lesions may coalesce, causing leaf yellowing and defoliation.",
            "hi": "पुरानी पत्तियों पर केंद्रीय छल्लों के साथ गहरे भूरे से काले रंग के घाव (लक्ष्य-स्थान पैटर्न)। घाव मिल सकते हैं, जिससे पत्ती पीली हो जाती है और पत्तियां गिर जाती हैं।"
        },
        "cause": {
            "en": "Fungal infection caused by Alternaria solani. Favored by warm temperatures, high humidity, and poor plant nutrition.",
            "hi": "अल्टरनेरिया सोलानी के कारण फंगल संक्रमण। गर्म तापमान, उच्च आर्द्रता और खराब पौधे के पोषण के अनुकूल।"
        },
        "treatment": {
            "en": "Apply fungicides at first sign of disease. Remove and destroy infected plant debris.",
            "hi": "बीमारी के पहले संकेत पर कवकनाशक लगाएं। संक्रमित पौधे के मलबे को हटा दें और नष्ट करें।"
        },
        "organic_treatment": {
            "en": "Apply copper-based fungicides or biological controls like Bacillus subtilis.",
            "hi": "तांबे-आधारित कवकनाशक या बैसिलस सबटिलिस जैसे जैविक नियंत्रण लगाएं।"
        },
        "chemical_treatment": {
            "en": "Apply chlorothalonil, mancozeb, or triazole fungicides according to label instructions.",
            "hi": "लेबल निर्देशों के अनुसार क्लोरोथालोनिल, मैनकोज़ेब, या ट्रायज़ोल कवकनाशक लगाएं।"
        },
        "preventive_measures": {
            "en": "Crop rotation. Ensure adequate plant nutrition, especially nitrogen. Maintain proper plant spacing.",
            "hi": "फसल रोटेशन। पर्याप्त पौधे के पोषण सुनिश्चित करें, विशेष रूप से नाइट्रोजन। उचित पौधों के बीच की दूरी बनाए रखें।"
        },
        "recovery": {
            "en": "2-3 weeks with proper treatment. Severe cases may have reduced yield.",
            "hi": "उचित उपचार के साथ 2-3 सप्ताह। गंभीर मामलों में उपज कम हो सकती है।"
        },
        "fertilizer": {
            "en": "Balanced fertilizer with adequate nitrogen to maintain plant vigor.",
            "hi": "पौधे की जीवनशक्ति बनाए रखने के लिए पर्याप्त नाइट्रोजन के साथ संतुलित उर्वरक।"
        },
        "pesticide": {
            "en": "Not directly effective against early blight. Focus on fungicides.",
            "hi": "शुरुआती ब्लाइट के खिलाफ सीधे प्रभावी नहीं। कवकनाशक पर ध्यान केंद्रित करें।"
        }
    },
    "Tomato___Early_Blight": {
        "symptoms": {
            "en": "Dark brown to black lesions with concentric rings on lower leaves. Lesions may coalesce, causing leaf yellowing and defoliation. Fruit may be affected near the stem end.",
            "hi": "निचली पत्तियों पर केंद्रीय छल्लों के साथ गहरे भूरे से काले रंग के घाव। घाव मिल सकते हैं, जिससे पत्ती पीली हो जाती है और पत्तियां गिर जाती हैं। फल तने के छोर के पास प्रभावित हो सकते हैं।"
        },
        "cause": {
            "en": "Fungal infection caused by Alternaria solani. Favored by warm temperatures, high humidity, and poor plant nutrition.",
            "hi": "अल्टरनेरिया सोलानी के कारण फंगल संक्रमण। गर्म तापमान, उच्च आर्द्रता और खराब पौधे के पोषण के अनुकूल।"
        },
        "treatment": {
            "en": "Apply fungicides at first sign of disease. Remove and destroy infected plant debris.",
            "hi": "बीमारी के पहले संकेत पर कवकनाशक लगाएं। संक्रमित पौधे के मलबे को हटा दें और नष्ट करें।"
        },
        "organic_treatment": {
            "en": "Apply copper-based fungicides or biological controls like Bacillus subtilis.",
            "hi": "तांबे-आधारित कवकनाशक या बैसिलस सबटिलिस जैसे जैविक नियंत्रण लगाएं।"
        },
        "chemical_treatment": {
            "en": "Apply chlorothalonil, mancozeb, or triazole fungicides according to label instructions.",
            "hi": "लेबल निर्देशों के अनुसार क्लोरोथालोनिल, मैनकोज़ेब, या ट्रायज़ोल कवकनाशक लगाएं।"
        },
        "preventive_measures": {
            "en": "Crop rotation. Ensure adequate plant nutrition, especially nitrogen. Maintain proper plant spacing. Stake or cage plants to improve air circulation.",
            "hi": "फसल रोटेशन। पर्याप्त पौधे के पोषण सुनिश्चित करें, विशेष रूप से नाइट्रोजन। उचित पौधों के बीच की दूरी बनाए रखें। हवा के परिसंचरण को बेहतर बनाने के लिए पौधों को स्टेक या केज करें।"
        },
        "recovery": {
            "en": "2-3 weeks with proper treatment. Severe cases may have reduced yield.",
            "hi": "उचित उपचार के साथ 2-3 सप्ताह। गंभीर मामलों में उपज कम हो सकती है।"
        },
        "fertilizer": {
            "en": "Balanced fertilizer with adequate nitrogen to maintain plant vigor.",
            "hi": "पौधे की जीवनशक्ति बनाए रखने के लिए पर्याप्त नाइट्रोजन के साथ संतुलित उर्वरक।"
        },
        "pesticide": {
            "en": "Not directly effective against early blight. Focus on fungicides.",
            "hi": "शुरुआती ब्लाइट के खिलाफ सीधे प्रभावी नहीं। कवकनाशक पर ध्यान केंद्रित करें।"
        }
    },
    "Tomato___Late_Blight": {
        "symptoms": {
            "en": "Water-soaked lesions on leaves, stems, and fruit that rapidly enlarge and turn brown. White fuzzy growth on the underside of leaves in humid conditions. Rapid wilting and plant death.",
            "hi": "पत्तियों, तनों और फलों पर पानी-से भीगे हुए घाव जो तेजी से बढ़ते हैं और भूरे हो जाते हैं। नमी वाली स्थितियों में पत्तियों के नीचे सफेद फजी वृद्धि। तेजी से मुरझाना और पौधे की मृत्यु।"
        },
        "cause": {
            "en": "Fungal infection caused by Phytophthora infestans. Favored by cool, moist conditions.",
            "hi": "फाइटोफ्थोरा इन्फेस्टांस के कारण फंगल संक्रमण। ठंडी, नम स्थितियों के अनुकूल।"
        },
        "treatment": {
            "en": "Apply fungicides immediately upon detection. Remove and destroy infected plants to prevent spread.",
            "hi": "पहचान पर तुरंत कवकनाशक लगाएं। फैलाव को रोकने के लिए संक्रमित पौधों को हटा दें और नष्ट करें।"
        },
        "organic_treatment": {
            "en": "Apply copper-based fungicides. Biological controls have limited effectiveness.",
            "hi": "तांबे-आधारित कवकनाशक लगाएं। जैविक नियंत्रणों की प्रभावशीलता सीमित है।"
        },
        "chemical_treatment": {
            "en": "Apply mefenoxam + chlorothalonil or cymoxanil + mancozeb according to label instructions.",
            "hi": "लेबल निर्देशों के अनुसार मेफेनोक्सम + क्लोरोथालोनिल या साइमोक्सानिल + मैनकोज़ेब लगाएं।"
        },
        "preventive_measures": {
            "en": "Plant resistant varieties. Avoid overhead irrigation. Ensure good air circulation. Remove volunteer plants.",
            "hi": "प्रतिरोधी किस्में लगाएं। ओवरहेड सिंचाई से बचें। अच्छा हवा का परिसंचरण सुनिश्चित करें। स्वयंसेवी पौधों को हटाएं।"
        },
        "recovery": {
            "en": "Difficult to recover once symptoms appear. Focus on preventing spread to healthy plants.",
            "hi": "लक्षण दिखने के बाद ठीक होना मुश्किल है। स्वस्थ पौधों में फैलाव को रोकने पर ध्यान केंद्रित करें।"
        },
        "fertilizer": {
            "en": "Balanced fertilizer to maintain plant health, but avoid excessive nitrogen which can increase susceptibility.",
            "hi": "पौधे के स्वास्थ्य को बनाए रखने के लिए संतुलित उर्वरक, लेकिन अत्यधिक नाइट्रोजन से बचें जो संवेदनशीलता बढ़ा सकता है।"
        },
        "pesticide": {
            "en": "Not directly effective against late blight. Focus on fungicides.",
            "hi": "लेट ब्लाइट के खिलाफ सीधे प्रभावी नहीं। कवकनाशक पर ध्यान केंद्रित करें।"
        }
    },
    "Grape___Black_Rot": {
        "symptoms": {
            "en": "Small, circular, reddish-brown spots on leaves that may develop tiny black fruiting bodies in the center. Berries become brown, shriveled, and covered with black pustules.",
            "hi": "पत्तियों पर छोटे, गोल, लाल-भूरे रंग के धब्बे जो केंद्र में छोटे काले फलने वाले शरीर विकसित कर सकते हैं। बेरी भूरे, सिकुड़े हुए और काले फफोलों से ढके हो जाते हैं।"
        },
        "cause": {
            "en": "Fungal infection caused by Guignardia bidwellii. Favored by warm, wet weather.",
            "hi": "गिग्नार्डिया बिडवेली के कारण फंगल संक्रमण। गर्म, गीले मौसम के अनुकूल।"
        },
        "treatment": {
            "en": "Apply fungicides from early bloom through fruit set. Remove and destroy infected mummified berries.",
            "hi": "शुरुआती खिलने से लेकर फल सेट होने तक कवकनाशक लगाएं। संक्रमित ममीफाइड बेरीज को हटा दें और नष्ट करें।"
        },
        "organic_treatment": {
            "en": "Apply sulfur-based fungicides or copper sprays. Neem oil may provide some protection.",
            "hi": "सल्फर-आधारित कवकनाशक या तांबा स्प्रे लगाएं। नीम का तेल कुछ सुरक्षा प्रदान कर सकता है।"
        },
        "chemical_treatment": {
            "en": "Apply myclobutanil, captan, or mancozeb according to label instructions.",
            "hi": "लेबल निर्देशों के अनुसार माइक्लोब्यूटेनिल, कैप्टन, या मैनकोज़ेब लगाएं।"
        },
        "preventive_measures": {
            "en": "Good air circulation through proper pruning. Remove infected debris. Avoid overhead irrigation.",
            "hi": "उचित प्रूनिंग के माध्यम से अच्छा हवा का परिसंचरण। संक्रमित मलबे को हटाएं। ओवरहेड सिंचाई से बचें।"
        },
        "recovery": {
            "en": "2-3 weeks with proper treatment. Infected berries cannot be recovered.",
            "hi": "उचित उपचार के साथ 2-3 सप्ताह। संक्रमित बेरीज को ठीक नहीं किया जा सकता।"
        },
        "fertilizer": {
            "en": "Balanced fertilizer to maintain vine health and vigor.",
            "hi": "लता के स्वास्थ्य और जीवनशक्ति को बनाए रखने के लिए संतुलित उर्वरक।"
        },
        "pesticide": {
            "en": "Not directly effective against black rot. Focus on fungicides.",
            "hi": "ब्लैक रॉट के खिलाफ सीधे प्रभावी नहीं। कवकनाशक पर ध्यान केंद्रित करें।"
        }
    },
    "Pepper___Bacterial_Spot": {
        "symptoms": {
            "en": "Small, water-soaked spots on leaves that become brown and may have yellow halos. Spots may coalesce, causing leaf drop. Fruit may have raised, scab-like spots.",
            "hi": "पत्तियों पर छोटे, पानी-से भीगे हुए धब्बे जो भूरे हो जाते हैं और उनमें पीले हैलो हो सकते हैं। धब्बे मिल सकते हैं, जिससे पत्ती गिर जाती है। फलों पर उभरे हुए, डाग जैसे धब्बे हो सकते हैं।"
        },
        "cause": {
            "en": "Bacterial infection caused by Xanthomonas campestris pv. vesicatoria. Spread by splashing water, tools, and workers.",
            "hi": "ज़ैन्थोमोनास कैम्पेस्ट्रिस पीवी वेसिकेटोरिया के कारण बैक्टीरियल संक्रमण। छिड़कते पानी, उपकरणों और श्रमिकों द्वारा फैलता है।"
        },
        "treatment": {
            "en": "Apply copper-based bactericides. Remove and destroy severely infected plants.",
            "hi": "तांबे-आधारित बैक्टीरियासाइड लगाएं। गंभीर रूप से संक्रमित पौधों को हटा दें और नष्ट करें।"
        },
        "organic_treatment": {
            "en": "Apply copper-based bactericides. Use biological controls like Bacillus subtilis.",
            "hi": "तांबे-आधारित बैक्टीरियासाइड लगाएं। बैसिलस सबटिलिस जैसे जैविक नियंत्रणों का उपयोग करें।"
        },
        "chemical_treatment": {
            "en": "Apply copper hydroxide or copper sulfate according to label instructions.",
            "hi": "लेबल निर्देशों के अनुसार कॉपर हाइड्रॉक्साइड या कॉपर सल्फेट लगाएं।"
        },
        "preventive_measures": {
            "en": "Use disease-free seeds and transplants. Avoid overhead irrigation. Disinfect tools regularly. Work in fields when dry.",
            "hi": "बीमारी-मुक्त बीज और ट्रांसप्लांट का उपयोग करें। ओवरहेड सिंचाई से बचें। नियमित रूप से उपकरणों की सफाई करें। सूखे में खेतों में काम करें।"
        },
        "recovery": {
            "en": "Difficult to cure infected plants. Focus on preventing spread to healthy plants.",
            "hi": "संक्रमित पौधों का इलाज करना मुश्किल है। स्वस्थ पौधों में फैलाव को रोकने पर ध्यान केंद्रित करें।"
        },
        "fertilizer": {
            "en": "Balanced fertilizer to maintain plant health, but avoid excessive nitrogen.",
            "hi": "पौधे के स्वास्थ्य को बनाए रखने के लिए संतुलित उर्वरक, लेकिन अत्यधिक नाइट्रोजन से बचें।"
        },
        "pesticide": {
            "en": "Not directly effective against bacterial spot. Focus on bactericides.",
            "hi": "बैक्टीरियल स्पॉट के खिलाफ सीधे प्रभावी नहीं। बैक्टीरियासाइड पर ध्यान केंद्रित करें।"
        }
    }
}

# Default disease info for unknown diseases
DEFAULT_DISEASE_INFO = {
    "symptoms": {
        "en": "Symptoms vary depending on the specific disease. Consult a plant pathologist for accurate diagnosis.",
        "hi": "लक्षण विशिष्ट बीमारी के आधार पर भिन्न होते हैं। सटीक निदान के लिए पौधे रोग विज्ञानी से परामर्श करें।"
    },
    "cause": {
        "en": "Causes vary depending on the specific disease. It could be fungal, bacterial, viral, or abiotic.",
        "hi": "कारण विशिष्ट बीमारी के आधार पर भिन्न होते हैं। यह फंगल, बैक्टीरियल, वायरल, या अजैविक हो सकता है।"
    },
    "treatment": {
        "en": "Treatment depends on accurate diagnosis. Consult agricultural extension services for specific recommendations.",
        "hi": "उपचार सटीक निदान पर निर्भर करता है। विशिष्ट सिफारिशों के लिए कृषि विस्तार सेवाओं से परामर्श करें।"
    },
    "organic_treatment": {
        "en": "Organic treatments vary by disease. Neem oil, copper sprays, and biological controls may be effective for some diseases.",
        "hi": "जैविक उपचार बीमारी के अनुसार भिन्न होते हैं। नीम का तेल, तांबा स्प्रे, और जैविक नियंत्रण कुछ बीमारियों के लिए प्रभावी हो सकते हैं।"
    },
    "chemical_treatment": {
        "en": "Chemical treatments depend on the specific disease. Consult with agricultural experts for appropriate recommendations.",
        "hi": "रासायनिक उपचार विशिष्ट बीमारी पर निर्भर करते हैं। उचित सिफारिशों के लिए कृषि विशेषज्ञों से परामर्श करें।"
    },
    "preventive_measures": {
        "en": "General preventive measures include crop rotation, proper spacing, adequate nutrition, and good sanitation practices.",
        "hi": "सामान्य निवारक उपायों में फसल रोटेशन, उचित दूरी, पर्याप्त पोषण और अच्छी सफाई प्रथाएं शामिल हैं।"
    },
    "recovery": {
        "en": "Recovery time varies depending on the disease severity and treatment effectiveness.",
        "hi": "रिकवरी का समय बीमारी की गंभीरता और उपचार की प्रभावशीलता के आधार पर भिन्न होता है।"
    },
    "fertilizer": {
        "en": "Use a balanced fertilizer appropriate for the specific crop to maintain overall plant health.",
        "hi": "समग्र पौधे के स्वास्थ्य को बनाए रखने के लिए विशिष्ट फसल के लिए उपयुक्त संतुलित उर्वरक का उपयोग करें।"
    },
    "pesticide": {
        "en": "Pesticide use depends on the specific disease and any secondary pest issues. Consult with agricultural experts.",
        "hi": "कीटनाशक का उपयोग विशिष्ट बीमारी और किसी भी माध्यमिक कीट समस्याओं पर निर्भर करता है। कृषि विशेषज्ञों से परामर्श करें।"
    }
}

# Weather advice based on conditions
WEATHER_ADVICE = {
    "Clear": {
        "en": "Good weather for most farming activities. Ensure adequate irrigation as clear skies can lead to increased evaporation. Monitor for heat stress in plants.",
        "hi": "अधिकांश कृषि गतिविधियों के लिए अच्छा मौसम। साफ आसमान से वाष्पीकरण बढ़ सकता है, इसलिए पर्याप्त सिंचाई सुनिश्चित करें। पौधों में ताप तनाव की निगरानी करें।"
    },
    "Clouds": {
        "en": "Cloudy conditions can reduce photosynthesis but may help prevent heat stress. Monitor for fungal diseases in high humidity. Good time for transplanting.",
        "hi": "बादलों वाली स्थितियां प्रकाश संश्लेषण को कम कर सकती हैं लेकिन ताप तनाव को रोकने में मदद कर सकती हैं। उच्च आर्द्रता में फंगल रोगों की निगरानी करें। ट्रांसप्लांटिंग का अच्छा समय।"
    },
    "Rain": {
        "en": "Rain provides natural irrigation but can spread diseases. Avoid working in wet fields to prevent soil compaction. Monitor for waterlogging and drainage issues.",
        "hi": "बारिश प्राकृतिक सिंचाई प्रदान करती है लेकिन बीमारियां फैला सकती है। मिट्टी के संकुचन को रोकने के लिए गीले खेतों में काम करने से बचें। जलभराव और जल निकासी की समस्याओं की निगरानी करें।"
    },
    "Drizzle": {
        "en": "Light rain is beneficial for most crops but can create conditions for fungal diseases. Good time for applying foliar fertilizers. Avoid spraying pesticides.",
        "hi": "हल्की बारिश अधिकांश फसलों के लिए फायदेमंद है लेकिन फंगल रोगों की स्थिति बना सकती है। पत्ती वाले उर्वरक लगाने का अच्छा समय। कीटनाशक छिड़कने से बचें।"
    },
    "Thunderstorm": {
        "en": "Thunderstorms can cause physical damage to crops and increase disease risk. Ensure proper staking and support for tall plants. Check drainage systems.",
        "hi": "तूफान फसलों को शारीरिक नुकसान पहुंचा सकते हैं और बीमारी के जोखिम को बढ़ा सकते हैं। लंबे पौधों के लिए उचित स्टेकिंग और समर्थन सुनिश्चित करें। जल निकासी प्रणालियों की जांच करें।"
    },
    "Snow": {
        "en": "Snow can insulate plants but heavy snow can cause breakage. Protect sensitive plants with covers. Avoid walking on frozen soil to prevent damage.",
        "hi": "बर्फ पौधों को इंसुलेट कर सकती है लेकिन भारी बर्फ टूटने का कारण बन सकती है। कवर के साथ संवेदनशील पौधों की रक्षा करें। नुकसान को रोकने के लिए जमी हुई मिट्टी पर चलने से बचें।"
    },
    "Mist": {
        "en": "Misty conditions increase humidity and can promote fungal diseases. Ensure good air circulation. Good time for transplanting seedlings.",
        "hi": "धुंधली स्थितियां आर्द्रता बढ़ाती हैं और फंगल रोगों को बढ़ावा दे सकती हैं। अच्छा हवा का परिसंचरण सुनिश्चित करें। सीडलिंग्स को ट्रांसप्लांट करने का अच्छा समय।"
    },
    "Fog": {
        "en": "Foggy conditions increase humidity and disease risk. Delay spraying operations. Ensure proper ventilation in greenhouses.",
        "hi": "धुंधली स्थितियां आर्द्रता और बीमारी के जोखिम को बढ़ाती हैं। स्प्रेइंग ऑपरेशन में देरी करें। ग्रीनहाउस में उचित वेंटिलेशन सुनिश्चित करें।"
    },
    "Haze": {
        "en": "Hazy conditions can reduce sunlight and photosynthesis. Monitor for any air pollution effects on plants. Ensure adequate irrigation.",
        "hi": "धुंधली स्थितियां धूप और प्रकाश संश्लेषण को कम कर सकती हैं। पौधों पर वायु प्रदूषण के प्रभावों की निगरानी करें। पर्याप्त सिंचाई सुनिश्चित करें।"
    }
}

# Temperature-based advice
TEMPERATURE_ADVICE = {
    "hot": {
        "en": "High temperatures can cause heat stress. Increase irrigation frequency. Provide shade for sensitive plants. Avoid transplanting during peak heat.",
        "hi": "उच्च तापमान ताप तनाव का कारण बन सकता है। सिंचाई की आवृत्ति बढ़ाएं। संवेदनशील पौधों के लिए छाया प्रदान करें। चरम गर्मी में ट्रांसप्लांटिंग से बचें।"
    },
    "warm": {
        "en": "Warm temperatures are ideal for most crops. Monitor for pests that thrive in warm weather. Ensure adequate watering.",
        "hi": "गर्म तापमान अधिकांश फसलों के लिए आदर्श है। गर्म मौसम में पनपने वाले कीटों की निगरानी करें। पर्याप्त पानी देना सुनिश्चित करें।"
    },
    "moderate": {
        "en": "Moderate temperatures are excellent for most farming activities. Good time for planting, transplanting, and applying fertilizers.",
        "hi": "मध्यम तापमान अधिकांश कृषि गतिविधियों के लिए उत्कृष्ट है। लगाने, ट्रांसप्लांटिंग और उर्वरक लगाने का अच्छा समय।"
    },
    "cool": {
        "en": "Cool temperatures can slow growth. Protect sensitive plants with row covers. Delay planting warm-season crops.",
        "hi": "ठंडे तापमान से वृद्धि धीमी हो सकती है। पंक्ति कवर के साथ संवेदनशील पौधों की रक्षा करें। गर्म मौसम की फसलों की लगाने में देरी करें।"
    },
    "cold": {
        "en": "Cold temperatures can damage or kill sensitive plants. Provide frost protection. Avoid watering in the evening to prevent frost damage.",
        "hi": "ठंडे तापमान से संवेदनशील पौधों को नुकसान हो सकता है या वे मर सकते हैं। ठहराव से सुरक्षा प्रदान करें। ठहराव के नुकसान को रोकने के लिए शाम को पानी देने से बचें।"
    },
    "freezing": {
        "en": "Freezing temperatures are dangerous for most crops. Provide heavy frost protection. Harvest any mature crops immediately. Avoid any planting activities.",
        "hi": "जमाने वाले तापमान अधिकांश फसलों के लिए खतरनाक हैं। भारी ठहराव से सुरक्षा प्रदान करें। किसी भी परिपक्व फसल की तुरंत कटाई करें। कोई भी लगाने की गतिविधियों से बचें।"
    }
}

# Humidity-based advice
HUMIDITY_ADVICE = {
    "low": {
        "en": "Low humidity increases water loss from plants. Increase irrigation frequency. Consider misting for humidity-loving plants. Watch for spider mites.",
        "hi": "कम आर्द्रता पौधों से पानी के नुकसान को बढ़ाती है। सिंचाई की आवृत्ति बढ़ाएं। आर्द्रता-प्रेमी पौधों के लिए मिस्टिंग पर विचार करें। स्पाइडर माइट्स पर नजर रखें।"
    },
    "moderate": {
        "en": "Moderate humidity is ideal for most crops. Continue regular watering schedule. Good time for most farming activities.",
        "hi": "मध्यम आर्द्रता अधिकांश फसलों के लिए आदर्श है। नियमित पानी देने की अनुसूची जारी रखें। अधिकांश कृषि गतिविधियों के लिए अच्छा समय।"
    },
    "high": {
        "en": "High humidity increases disease risk, especially fungal diseases. Improve air circulation. Avoid overhead watering. Apply preventive fungicides if necessary.",
        "hi": "उच्च आर्द्रता बीमारी के जोखिम को बढ़ाती है, विशेष रूप से फंगल रोगों। हवा का परिसंचरण बेहतर करें। ओवरहेड वाटरिंग से बचें। आवश्यकता हो तो निवारक कवकनाशक लगाएं।"
    },
    "very_high": {
        "en": "Very high humidity creates ideal conditions for many diseases. Maximize air circulation. Consider using dehumidifiers in greenhouses. Delay planting until conditions improve.",
        "hi": "बहुत उच्च आर्द्रता कई बीमारियों के लिए आदर्श स्थितियां बनाती है। हवा के परिसंचरण को अधिकतम करें। ग्रीनहाउस में डीह्यूमिडिफायर का उपयोग करने पर विचार करें। स्थितियां सुधरने तक लगाने में देरी करें।"
    }
}

# UI colors and styling
UI_COLORS = {
    "primary": "#2E7D32",  # Green
    "secondary": "#81C784",  # Light green
    "accent": "#FFC107",  # Amber
    "background": "#F1F8E9",  # Very light green
    "card_background": "#FFFFFF",
    "text": "#212121",
    "text_secondary": "#757575",
    "success": "#4CAF50",
    "warning": "#FF9800",
    "error": "#F44336",
    "info": "#2196F3"
}