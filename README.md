# LangChain Streamlit Demo

An enhanced Streamlit application that uses LangChain and OpenAI for interactive AI conversations.

## 🚀 Live Demo

**[Try it live here →](https://joeest.streamlit.app/)**

> 💡 **Note**: You'll need your own OpenAI API key to use the app. Enter it in the sidebar when you visit the link.

## Features

- 💬 **Chat Interface**: Full conversation history with chat-style UI
- 🤖 **Multiple Models**: Support for GPT-4o, GPT-4o-mini, GPT-4-turbo, and GPT-3.5-turbo
- ⚙️ **Customizable**: Adjustable temperature for response creativity
- 🔐 **Secure**: API key input with environment variable support
- 💾 **Session Memory**: Maintains conversation context throughout the session
- 🎨 **Modern UI**: Clean, user-friendly interface with emojis and better UX
- ⚡ **Error Handling**: Robust error handling and user feedback

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run streamlit_demo.py
   ```

2. Enter your OpenAI API key in the sidebar (or set `OPENAI_API_KEY` environment variable)

3. Select your preferred model and adjust temperature if needed

4. Start chatting! Your conversation history will be maintained during the session

## Deployment

**Live App**: [https://joeest.streamlit.app/](https://joeest.streamlit.app/)

This app is deployed on **Streamlit Community Cloud** (free):
- Connect your GitHub repository
- Deploy automatically on every push
- Share the public URL with anyone
- **Completely free** for public and private apps

## Environment Variables

You can set your API key as an environment variable:
```bash
export OPENAI_API_KEY="your-api-key-here"  # Linux/Mac
set OPENAI_API_KEY=your-api-key-here       # Windows
```

## Requirements

- Python 3.x
- OpenAI API key
- See `requirements.txt` for package dependencies

