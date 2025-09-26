import streamlit as st
from utils.api import ask_question

def render_chat():
    st.subheader("Medical Assistant Chat")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    #render chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    #input and response
    user_input = st.chat_input("Ask a medical question...")
    if user_input:
        st.chat_message("user").markdown(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})

        response = ask_question(user_input) 
        if response.status_code == 200:
            data = response.json()
            answer = data["response"]
            sources = data.get("sources", [])
            st.chat_message("assistant").markdown(answer)
            # if sources:
            #     st.markdown("**Sources:**")
            #     for source in sources:
            #         st.markdown(f"- {source}")
            st.session_state.messages.append({"role": "assistant", "content": answer})
        else:
            st.error(f"Error :{response.text}")

