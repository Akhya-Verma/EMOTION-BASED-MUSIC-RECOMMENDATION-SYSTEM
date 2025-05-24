import cv2
import streamlit as st
from deepface import DeepFace
from googleapiclient.discovery import build
import os
from dotenv import load_dotenv
load_dotenv()


# Load API key from .env
# load_dotenv()
api_key = os.getenv("YOUTUBE_API_KEY")

# Emotion to music search query mapping
emotion_to_music = {
    "happy": "happy upbeat songs",
    "sad": "sad emotional songs",
    "angry": "calm soothing music",
    "surprise": "fun energetic songs",
    "fear": "motivational songs",
    "disgust": "positive vibe music",
    "neutral": "chill background music"
}
def detect_emotion_from_face():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()

    if not ret:
        st.error("❌ Failed to capture image from webcam.")
        return None

    # Convert BGR to RGB for Streamlit and DeepFace
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Display the captured frame in Streamlit
    st.image(rgb_frame, caption="📸 Captured Image", use_column_width=True)

    # Analyze emotion using DeepFace
    result = DeepFace.analyze(rgb_frame, actions=['emotion'], enforce_detection=False)
    dominant_emotion = result[0]['dominant_emotion']
    return dominant_emotion

# def detect_emotion_from_face():
#     cap = cv2.VideoCapture(0)
#     print("Press 'q' to capture your face and detect emotion")

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             st.error("Failed to grab frame")
#             break
#         cv2.imshow("Webcam - Press 'q' to analyze", frame)

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()

#     # Analyze emotion
#     result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
#     dominant_emotion = result[0]['dominant_emotion']
#     return dominant_emotion









def search_youtube_music(query, max_results=5):
    # api_key = "AIzaSyActV2CfHdSPmM2VImviPfE5TxfpBGgS4k"  # Replace with your API Key
    # api_key = os.getenv("YOUTUBE_API_KEY")
    youtube = build("youtube", "v3", developerKey=api_key)

    request = youtube.search().list(
        q=query,
        part="snippet",
        type="video",
        maxResults=max_results
    )
    response = request.execute()

    results = []
    for item in response['items']:
        title = item['snippet']['title']
        url = f"https://www.youtube.com/watch?v={item['id']['videoId']}"
        results.append((title, url))
    return results

# def recommend_music_from_face():
#     print("Starting emotion detection from your face...")
#     emotion = detect_emotion_from_face()
#     print(f"Detected Emotion: {emotion}")

#     query = emotion_to_music.get(emotion.lower(), "feel good music")
#     print(f"Searching YouTube for: {query}")

#     recommendations = search_youtube_music(query)
#     print("\n🎧 Here are your music recommendations:\n")
#     for i, (title, url) in enumerate(recommendations, 1):
#         print(f"{i}. {title}\n   {url}")

# if __name__ == "__main__":
#     recommend_music_from_face()

def main():
    st.title("🎵 Emotion-Based Music Recommender")
    if st.button("Capture Emotion from Face"):
        emotion = detect_emotion_from_face()
        if emotion:
            st.success(f"😊 Detected Emotion: **{emotion}**")
            query = emotion_to_music.get(emotion.lower(), "feel good music")
            st.write(f"🔍 Searching YouTube for: **{query}**")
            recommendations = search_youtube_music(query)
            for i, (title, url) in enumerate(recommendations, 1):
                st.markdown(f"**{i}. {title}**  \n[▶️ Watch on YouTube]({url})")
        # st.success(f"Detected Emotion: {emotion}")

        # query = emotion_to_music.get(emotion.lower(), "feel good music")
        # st.write(f"🔍 Searching YouTube for: **{query}**")

        # recommendations = search_youtube_music(query)
        # for i, (title, url) in enumerate(recommendations, 1):
        #     st.markdown(f"**{i}. {title}**\n\n[Watch on YouTube]({url})")

if __name__ == "__main__":
    main()