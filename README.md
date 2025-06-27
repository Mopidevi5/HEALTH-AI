 🩺**HealthAI: Intelligent Healthcare Assistant using IBM Granite**
**HealthAI** is a smart, AI-powered virtual healthcare assistant designed to help users monitor their health, predict diseases, access treatment plans, analyze trends, and promote eco-friendly practices—all from one user-friendly platform.

**Team Members**
- **Battulla Mohana Sampati Nagamani**
- **Mopidevi Deepthi Priya**
- **Gitthadappa Gari Venu**
- **Kunapareddy Lalitha Prasanna**
Students of **DMSSVH College of Engineering**
**Project Overview**
HealthAI integrates conversational AI, machine learning, and health analytics to support users in understanding and managing their health more effectively. Users can chat with the AI to report symptoms, get predicted diseases, receive treatment suggestions, and access eco-health tips.
**Technologies Used**
- **IBM Granite 13B Instruct v2** – For natural language processing and intelligent response generation
- **IBM Watson Machine Learning** – For disease prediction based on symptoms
- **Python** – Core language for backend logic and processing
- **Streamlit** – Framework for building the interactive web UI
- **Pandas** – For handling and analyzing structured data
- **Matplotlib / Plotly** – For data visualization in the analytics module
- **CSV Files** – For local storage of user inputs and analytics data
## Project Structure
healthai/
│
├── components/
│   ├── analytics\_page.py
│   ├── chat\_page.py
│   ├── dashboard\_page.py
│   ├── disease\_prediction\_page.py
│   ├── eco\_tips\_page.py
│   └── treatment\_page.py
│
├── data/
│   └── analytics\_data.csv
│
├── main.py
├── requirements.txt
└── README.md
##  Application Features

### Summary Dashboard
Gives users an overview of interactions and health metrics like symptom frequency and prediction counts.

###  Analytics
Visualizes trends in health data, showing symptom frequency across regions using charts and graphs.

### Patient Chat
Allows users to interact with the AI using natural language. The assistant understands symptoms and responds with advice or direction.

### Disease Prediction
Predicts diseases based on user-reported symptoms using IBM Watson ML, allowing early health intervention.

### Treatment Plans
Provides AI-generated suggestions including medication, home remedies, lifestyle advice, and dietary tips.

### Eco-Friendly Tips
Promotes sustainable living by sharing eco-conscious healthcare tips, such as reducing plastic and using herbal alternatives.
###  Input
- Users enter symptoms or ask health questions via the chat or form.
- Example: "I have headache and nausea" or "What to do for low blood pressure?"

### Processing
- IBM Watson predicts the disease based on symptoms.
- IBM Granite generates responses and treatment suggestions.

### Output
- Predicted disease name
- Suggested treatment plan
- Visual health analytics
- Eco-health tips
- Friendly, contextual chatbot response

##  Future Improvements

* Add voice-based assistant feature
* Store data securely on the cloud
* Integrate electronic health records (EHR)
* Multi-language support for regional users
## License
This project is for academic and demonstration purposes. All rights reserved to the authors.
##  Acknowledgments
* **IBM** for providing access to Granite and Watson ML
* **Streamlit** community for documentation and open-source support
