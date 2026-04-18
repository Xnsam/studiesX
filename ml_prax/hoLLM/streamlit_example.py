import time

import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.messages import SystemMessage


st.set_page_config(page_title="Langchain chatbot", page_icon="🤖")
st.title("🤖 Chatbot")

msgs = StreamlitChatMessageHistory(key="chat_messages")
model_name = "mlx-community/Qwen2.5-1.5B-Instruct-4bit"
# Point to your local MLX server
llm = ChatOpenAI(
    base_url="http://localhost:8080/v1",
    api_key="not-needed",
    # Change "local-model" to the exact name shown in your server logs
    model=model_name, 
    temperature=0.7
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant"),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{question}")
])


def get_windowed_history(session_id: str):
    # This simulates "ConversationBufferWindowMemory"
    # It only keeps the last 'k' * 2 messages (Human + AI pairs)
    if len(msgs.messages) > k * 2:
        msgs.messages = msgs.messages[-(k * 2):]
    return msgs

def get_summarized_history(history):
    """Summarizes history if it exceeds a length threshold."""
    if len(history) > 6:
        summary = llm.invoke(f"Summarize: {str(history[:-2])}")
        return [SystemMessage(content=f"Summary: {summary.content}")] + history[-2:]
    return history


def get_session_history(session_id: str):
    """
    Retrieves the chat history for a specific session.
    In Streamlit, we use the session_id to define the key in st.session_state.
    """
    # Each session_id gets its own isolated history in session_state
    history = StreamlitChatMessageHistory(key=f"chat_history_{session_id}")
    
    # Optional: Add a welcome message if the history is brand new
    if len(history.messages) == 0:
        history.add_ai_message("Hello! I'm your session-aware assistant. How can I help you?")
        
    return history


chain = (
    {"history": lambda x: get_summarized_history(x["history"]), "question": lambda x: x["question"]} 
    | prompt | llm
)
chain_with_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="question",
    history_messages_key="history",
)

with st.sidebar:
    k = st.slider("Memory Window (k)", min_value=1, max_value=20, value=5)
    if st.button("Clear Chat History"):
        msgs.clear()
        st.rerun()

if len(msgs.messages) == 0:
    msgs.add_ai_message("Hello! I'm your AI assistant. How can I help you today?")

for msg in msgs.messages:
    st.chat_message(msg.type).write(msg.content)

if question := st.chat_input("Your input"):
    st.chat_message("human").write(question)


with st.chat_message("ai"):
    config = {"configurable": {"session_id": "any"}}
    
    # 1. Get the raw stream from LangChain
    raw_stream = chain_with_history.stream({"question": question}, config=config)

    # 2. Define a generator to add "Typing" delay
    def speed_controlled_generator(stream):
        for chunk in stream:
            # Most LLMs return 'AIMessageChunk' objects, extract the text
            content = getattr(chunk, "content", str(chunk))
            
            # Split content into words or small chunks to simulate typing
            for word in content.split(" "):
                yield word + " "
                # ADJUST SPEED HERE (0.05 = 20 words per second)
                time.sleep(0.05) 

    # 3. Pass the custom generator to st.write_stream
    response_text = st.write_stream(speed_controlled_generator(raw_stream))
