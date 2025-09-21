import streamlit as st
from components.upload import render_file_upload
from components.history_downloads import render_history_downloads
from components.chatUI import render_chat



st.set_page_config(page_title="Medical Assistant", page_icon=":hospital:", layout="wide")
st.title("AI Medical Chatbot")

render_file_upload()
render_chat()
render_history_downloads()
