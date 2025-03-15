# AI Sales Coach demo

This is a simple "Hello World" demo about how an AI agent can be a sales coach.

It consists of a simple AI that reads an audio about a sales conversation, transcribes it, then runs sentiment analysis on on it and finally provides feedback.

## Limitations

It is important to remember this is a simple demo and proof of concept. Thus it has the following limitations:

- Not production ready: This demo is missing all critical parts of a production application
- Too general: The LLM used was not finetuned on specific sales data and scenario, thus accuracy is limited
- Off-line usage limited: The application is designed to handle offline audio files, thus the conversation has finished. Realtime equivalent should use a differennt paradigm (using audio streams) and much capable and fast models, to provide real-time feedbacks

So use this as a demo only.

## Technology

This is a Python only project:

- Using `uv` to install and manage python environments
- Using OpenAI `whisper` model for TTS conversion
- Using OpenAI `gpt-4o-mini` which is simple and cheap for the purpose of this demo
- Using `Streamlit` for the UI

## Dataset

To test the application, we provide some sample audio data located in `/dataset` folder.

## Running the application locally

- Clone the repository
- Ensure to have `uv` installed
- Create an environment and install packages using `uv sync`
- Run the application using `make run`
