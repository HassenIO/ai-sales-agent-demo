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

## Online demo

The application was deployed online for testing.

First, download the following [sample sales audio call](https://github.com/HassenIO/ai-sales-agent-demo/raw/refs/heads/master/dataset/sample_call.mp3).

The sample audio was truncated at the moment the customer raises an concern. **The goal is to see if the AI Coach provides the suitable salesperson response**.

> NOTA: To access the full untruncated example, head to the [following YouTube video](https://www.youtube.com/watch?v=4ostqJD3Psc).

Once you have the sample locally, access the Streamlit application through this link: [https://ai-sales-call-coach.streamlit.app](https://ai-sales-call-coach.streamlit.app/).

Use the sample audio to test the application:

![AI Sales Call Analyzer demo page](/assets/ai-sales-call-analyzer.png)

## Final Notes

This project serves as a demonstration concept to showcase the potential of AI in sales coaching. It is intended for learning and exploration purposes, providing insights into how AI can assist in analyzing and improving sales conversations.

If you have any questions, suggestions, or would like to discuss this concept further, please feel free to reach out to me. I'm always interested in exploring innovative applications of AI in business contexts, as well as being in touch with AI enthusiats.

You can contact me through:

- GitHub Issues on this repository
- LinkedIn: https://linkedin.com/in/htaidirt

2025 - Hassen Taidirt
