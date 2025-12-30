# LangChain Streamlit Demo

A simple Streamlit application that uses LangChain and OpenAI to answer questions.

## Features

- Interactive Q&A interface using OpenAI's GPT-4o model
- Secure API key input via Streamlit sidebar
- Built with LangChain for easy LLM integration

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

2. Enter your OpenAI API key in the sidebar

3. Ask any question in the input field

## Requirements

- Python 3.x
- OpenAI API key
- See `requirements.txt` for package dependencies

