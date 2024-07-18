# YouTube Transcript to Detailed Notes Converter

## Overview

This application converts YouTube video transcripts into detailed notes using Google Generative AI. It fetches the transcript from a YouTube video, processes it with an AI model, and provides a summary in a pointwise manner within 300-500 words.

## Features

- **Fetch Transcript**: Retrieves the transcript of a YouTube video using the YouTube Transcript API.
- **Generate Summary**: Uses Google Generative AI (Gemini-pro) to summarize the transcript.
- **User Interface**: Built with Streamlit for a simple and interactive user experience.

## Tools and Libraries

- **Streamlit**: For creating the web application interface.
- **Google Generative AI**: For generating summaries from the transcript text.
- **YouTube Transcript API**: For fetching video transcripts from YouTube.
- **Python**: The core programming language used for this application.
- **dotenv**: For loading environment variables from a `.env` file.
- **os**: For interacting with the operating system to retrieve environment variables.

## How to Use

1. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

2. **Set Up Environment Variables**:
    - Create a `.env` file in the project root directory.
    - Add your Google API key:
      ```env
      GOOGLE_API_KEY=your_google_api_key
      ```

3. **Run the Application**:
    ```sh
    streamlit run your_script.py
    ```

4. **Enter YouTube Video URL**:
    - Input the YouTube video link in the provided text field.
    - Click on "Get Detailed Notes" to fetch the transcript and generate a summary.

## Error Handling

- Displays clear error messages for various issues such as video unavailability, no transcript found, and disabled transcripts.
- Provides feedback if the YouTube URL is invalid.


