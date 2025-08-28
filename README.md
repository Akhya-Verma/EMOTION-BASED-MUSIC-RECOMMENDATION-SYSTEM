# Emotion-Based Music Recommendation System 🎶

This project recommends music based on real-time facial emotion detection using **DeepFace** and the **YouTube API**.  
It captures the user's face, detects emotions, and fetches relevant songs from YouTube accordingly.

---

## 🚀 Features
- Real-time emotion detection using **OpenCV** and **DeepFace**  
- Emotion-to-music mapping (e.g., happy → upbeat songs, sad → emotional songs)  
- Fetches **top YouTube songs** based on detected emotion  
- Simple UI built with **Streamlit**  

---

## 🛠️ Tech Stack
- **Python**  
- **OpenCV** – for capturing webcam input  
- **DeepFace** – for emotion recognition  
- **Google API (YouTube Data API v3)** – for fetching music  
- **Streamlit** – for building the web interface  
- **dotenv** – for API key management  

---

## 📂 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/emotion-music-recommender.git
   cd emotion-music-recommender
2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Mac/Linux
   venv\Scripts\activate      # On Windows
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
4. **Set up YouTube API Key**
- Create a .env file in the project root
- Add your API key:
  ```bash
   YOUTUBE_API_KEY=your_api_key_here
--- 
## ▶️ Run the Application
    ```bash
    streamlit run app.py



---

## 🎯 How It Works

1. The app captures your facial expression using OpenCV.
2. DeepFace analyzes your face and predicts your current emotion.
3. The emotion is mapped to a specific music query.
4. The YouTube API fetches the top songs based on that query.
5. The songs are displayed in the Streamlit interface.

---


## 🔮 Future Enhancements

- Support for multiple languages in song recommendations
- Integration with Spotify API
- Advanced personalization using user history



