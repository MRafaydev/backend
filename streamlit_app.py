import streamlit as st
import requests

# Streamlit layout setup
st.title("Video Transcription")
video_url = st.text_input("Enter YouTube Video URL:")
submit_button = st.button("Transcribe")

# FastAPI API endpoint
api_endpoint = "http://127.0.0.1:8000/api/v1/transcribe"

# Function to transcribe video
def transcribe_video(url):
    response = requests.post(api_endpoint, params={"url": url})
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error processing video. Status code: {response.status_code}, Detail: {response.text}")
        return None


if submit_button and video_url:
    st.info("Transcribing... Please wait.")
    transcript_data = transcribe_video(video_url)
    if transcript_data:
        st.header("Video Transcript")
        transcript_text = "\n".join([f"**Timestamp:** {entry['timestamp']:.2f}s\n**Text:** {entry['text']}\n" for entry in transcript_data])
        st.markdown(f"<div style='overflow:auto; border: 1px solid #ccc; border-radius: 5px; max-height: 400px;'>{transcript_text}</div>", unsafe_allow_html=True)
        st.success("Transcription complete!")
