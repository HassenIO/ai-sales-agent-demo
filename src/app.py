import streamlit as st
import whisper
import os
from openai import OpenAI
from pydub import AudioSegment
import dotenv

# Load environment variables from .env
dotenv.load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("Missing OPENAI_API_KEY in your environment variables or local .env file")

# Load Whisper model
model = whisper.load_model("base")


# Function to convert audio to WAV format (if necessary)
def convert_audio(file_path):
    """Convert audio file to WAV format if it's not already."""
    if file_path.endswith(".wav"):
        return file_path  # No conversion needed

    audio = AudioSegment.from_file(file_path)
    wav_path = file_path.rsplit(".", 1)[0] + ".wav"
    audio.export(wav_path, format="wav")
    return wav_path


# Function to transcribe audio
def transcribe_audio(file_path):
    """Transcribes an audio file into text using Whisper."""
    result = model.transcribe(file_path)
    return result["text"]


# Function to analyze sales conversation
def analyze_sales_conversation(text):
    """Sends transcribed conversation to OpenAI's gpt-x for analysis."""
    client = OpenAI()

    prompt = f"""
    Analyze the following sales conversation. Identify key risks and provide recommended actions.
    
    Sales Call Transcript:
    {text}

    Output should be structured as:
    - Identified Risks
    - Recommended Actions
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are an expert sales coach analyzing sales calls and providing accurate, straight to the point and mind blowing advices.",
            },
            {"role": "user", "content": prompt},
        ],
    )

    return response.choices[0].message.content



# Streamlit UI
st.title("🎙 AI Sales Call Analyzer")
st.write(
    "Upload an MP3 sales call, and our AI Coach will transcribe it and provide recommendations."
)

uploaded_file = st.file_uploader("Upload an MP3, WAV or M4A file", type=["mp3", "wav", "m4a"])

if uploaded_file is not None:
    st.audio(uploaded_file, format="audio/mp3")

    # Save uploaded file
    file_path = f"temp/{uploaded_file.name}"
    os.makedirs("temp", exist_ok=True)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Convert if necessary
    file_path = convert_audio(file_path)

    # Transcribe the audio
    with st.spinner("Transcribing audio..."):
        transcript = transcribe_audio(file_path)
    st.subheader("📝 Transcription")
    st.text_area("Transcribed Sales Call:", transcript, height=200)

    # Analyze conversation
    with st.spinner("Analyzing sales call..."):
        analysis = analyze_sales_conversation(transcript)
    st.subheader("📊 AI Sales Insights")
    st.write(analysis)

    # Cleanup
    os.remove(file_path)
