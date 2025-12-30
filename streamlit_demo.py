from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage
import streamlit as st
import os

# Page configuration
st.set_page_config(
    page_title="AI Chat Assistant",
    page_icon="🤖",
    layout="wide"
)

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar configuration
with st.sidebar:
    st.title("⚙️ Configuration")
    
    # API Key input with environment variable support
    OPENAI_API_KEY = st.text_input(
        "OpenAI API Key", 
        type="password",
        value=os.getenv("OPENAI_API_KEY", ""),
        help="Enter your OpenAI API key or set OPENAI_API_KEY environment variable"
    )
    
    # Model selection
    model_name = st.selectbox(
        "Select Model",
        ["gpt-4o", "gpt-4o-mini", "gpt-4-turbo", "gpt-3.5-turbo"],
        index=0,
        help="gpt-4o-mini is cheaper, gpt-4o is more capable"
    )
    
    # Temperature slider
    temperature = st.slider(
        "Temperature",
        min_value=0.0,
        max_value=2.0,
        value=0.7,
        step=0.1,
        help="Higher values make output more random, lower values more focused"
    )
    
    # Clear chat button
    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = []
        st.rerun()
    
    st.markdown("---")
    st.markdown("### 💡 Tips")
    st.info("""
    - Your API key is stored only in your session
    - Chat history is maintained during your session
    - Use gpt-4o-mini for cost-effective responses
    """)

# Check for API key
if not OPENAI_API_KEY:
    st.info("🔑 Please enter your OpenAI API key in the sidebar to continue")
    st.stop()

# Initialize LLM
try:
    llm = ChatOpenAI(
        model=model_name,
        api_key=OPENAI_API_KEY,
        temperature=temperature
    )
except Exception as e:
    st.error(f"Error initializing LLM: {str(e)}")
    st.stop()

# Main app
st.title("🤖 AI Chat Assistant")
st.markdown("Ask me anything!")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Enter your question here..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate and display assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # Convert chat history to LangChain messages
                langchain_messages = []
                for msg in st.session_state.messages:
                    if msg["role"] == "user":
                        langchain_messages.append(HumanMessage(content=msg["content"]))
                    else:
                        langchain_messages.append(AIMessage(content=msg["content"]))
                
                # Get response from LLM
                response = llm.invoke(langchain_messages)
                response_text = response.content
                
                # Display response
                st.markdown(response_text)
                
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": response_text})
                
            except Exception as e:
                error_msg = f"❌ Error: {str(e)}"
                st.error(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})