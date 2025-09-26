import streamlit as st

def render_history_downloads():
    if st.session_state.get("message"):
        chat_text="\n\n".join([f"{msg['role'].upper()}: {msg['content']}" for msg in st.session_state.message])
        st.dowlonload_button("Download Chat History", chat_text, file_name="chat_history.txt",mime="text/plain")
        st.info("No history available to download.")
        return