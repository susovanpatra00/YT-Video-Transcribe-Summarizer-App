from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi, VideoUnavailable, NoTranscriptFound, TranscriptsDisabled
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

input_prompt = """
                You are a Youtube Video Summarizer.
                You will be given the youtube video
                transcript text as input and you need to 
                give a brief summary of that as detailed notes 
                in pointwise manner within 
                300-500 words.  

               """

## getting gemini response as summary of transcript based on prompt
def get_gemini_response(transcript_text, input_prompt):
    model = genai.GenerativeModel(model_name="gemini-pro")
    response = model.generate_content([transcript_text, input_prompt])
    return response.text

## fetching the transcript from youtube api
def fetch_transcript_details(url):
    try:
        video_id = url.split("=")[1]
        transcript_data = YouTubeTranscriptApi.get_transcript(video_id)
        
        transcript_text = ""
        for chunks in transcript_data:
            transcript_text += " " + chunks['text']
        
        return transcript_text
    except VideoUnavailable:
        return "Video is unavailable."
    except NoTranscriptFound:
        return "No transcript found for this video."
    except TranscriptsDisabled:
        return "Transcripts are disabled for this video."
    except Exception as e:
        return f"An error occurred: {str(e)}"

## Initialize streamlit app
st.title("Youtube Transcript to Detailed Notes Converter")
url = st.text_input("Enter Youtube Video Link")

if url:
    try:
        video_id = url.split("=")[1]
        st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)
    except IndexError:
        st.error("Invalid YouTube URL. Please check and try again.")

if st.button("Get Detailed Notes"):
    with st.spinner('Fetching transcript and generating summary...'):
        transcript_text = fetch_transcript_details(url)
        if "An error occurred" in transcript_text or "Video is unavailable" in transcript_text or "No transcript found" in transcript_text or "Transcripts are disabled" in transcript_text:
            st.error(transcript_text)
        else:
            summary = get_gemini_response(transcript_text, input_prompt)
            st.markdown("## Detailed Notes:\n")
            st.write(summary)
