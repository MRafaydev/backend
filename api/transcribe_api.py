from fastapi import FastAPI, Depends, HTTPException, status
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi
from models.public_url import VideoUrl

app = FastAPI()

@app.post('/api/v1/transcribe')
async def transcript(form_data: VideoUrl = Depends()):
    try:
        video_url = YouTube(form_data.url)
        video_path = video_url.streams.get_audio_only().download()
        print(video_path)
        transcripts_list = YouTubeTranscriptApi.list_transcripts(
            video_url.video_id)
        print(transcripts_list)
        transcript_list = YouTubeTranscriptApi.get_transcript(
            video_url.video_id)
        transcript = [{'timestamp': line['start'], 'text': line['text']}
                      for line in transcript_list]
        return transcript

    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error processing video")
