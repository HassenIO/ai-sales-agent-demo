import streamlit as st
import whisper
import os
from openai import OpenAI
from pydub import AudioSegment
import dotenv

dotenv.load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError(
        "Missing OPENAI_API_KEY in your environment variables or local .env file"
    )

whisper_model = whisper.load_model("base")


def convert_audio(file_path):
    """Convert audio file to WAV format if it's not already."""
    if file_path.endswith(".wav"):
        return file_path  # No conversion needed

    audio = AudioSegment.from_file(file_path)
    wav_path = file_path.rsplit(".", 1)[0] + ".wav"
    audio.export(wav_path, format="wav")
    return wav_path


def transcribe_audio(file_path):
    """Transcribes an audio file into text using Whisper."""
    result = whisper_model.transcribe(file_path)
    return result["text"]


def structure_conversation(text):
    """Structures raw transcription into a formatted conversation."""
    client = OpenAI()

    prompt = f"""
    Convert this raw transcription into a structured conversation format.
    Identify the speakers and format their dialogue as:

    SPEAKER NAME:
    Their dialogue text

    Raw Transcription:
    {text}

    Format each speaker's parts clearly separated by newlines.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are an expert at converting raw transcriptions into clearly structured conversations. Identify speakers and format their dialogue cleanly.",
            },
            {"role": "user", "content": prompt},
        ],
    )

    return response.choices[0].message.content


def analyze_sales_conversation(text):
    """Sends transcribed conversation to OpenAI's gpt-x for analysis."""
    client = OpenAI()

    prompt = f"""
    Analyze the following sales conversation, using the following 6 sales dimensions:
    - Solution
    - Price
    - Decision makers
    - Competition
    - Planning
    - Legal
    Then identify key risks and provide recommended actions with expected outcomes if the actions are well implemented.
    
    Sales Call Transcript:
    {text}

    Output should be structured as:
    - Sales Analysis
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


if __name__ == "__main__":
    st.title("🎙 AI Sales Call Analyzer")
    st.info(
        "[GitHub Source Code](https://github.com/HassenIO/ai-sales-agent-demo) • Created by [Hassen Taidirt](https://linkedin.com/in/htaidirt)"
    )
    st.write(
        "Upload an MP3 sales call, and our AI Coach will transcribe it and provide recommendations."
    )

    uploaded_file = st.file_uploader(
        "Upload an MP3, WAV or M4A file", type=["mp3", "wav", "m4a"]
    )

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

        # Structure the conversation
        with st.spinner("Structuring conversation..."):
            structured_transcript = structure_conversation(transcript)
        st.subheader("📝 Structured Conversation")
        st.text_area("Structured Conversation:", structured_transcript, height=300)

        # Analyze conversation
        with st.spinner("Analyzing sales call..."):
            analysis = analyze_sales_conversation(
                structured_transcript
            )  # Note: Now using structured transcript
        st.subheader("📊 AI Sales Insights")
        st.write(analysis)

        # Cleanup
        os.remove(file_path)
