import streamlit as st
from cohere import Client

from src.msecrets import COHERE_API_KEY

st.title("💬 Chatbot")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {
            "role": "assistant",
            "content": "How can I help you?"
        }
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    client = Client(api_key=COHERE_API_KEY)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    print(st.session_state.messages[-1]['content'])
    response = client.generate(
            model='command-nightly',
            prompt=st.session_state.messages[-1]['content'],
            max_tokens=300,
            temperature=0.9,
            k=0,
            p=0.75,
            stop_sequences=[],
            return_likelihoods='NONE'
        )
    print(response)
    msg = response.generations[0].text
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
