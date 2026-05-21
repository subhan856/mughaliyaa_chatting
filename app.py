import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
import os
from datetime import datetime

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Real Chat App",
    page_icon="💬",
    layout="wide"
)

# ---------------- FIREBASE SETUP ----------------

firebase_config = {
    "type": "service_account",
    "project_id": "YOUR_PROJECT_ID",
    "private_key_id": "YOUR_PRIVATE_KEY_ID",
    "private_key": "YOUR_PRIVATE_KEY",
    "client_email": "YOUR_CLIENT_EMAIL",
    "client_id": "YOUR_CLIENT_ID",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url":
    "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "YOUR_CERT_URL"
}

if not firebase_admin._apps:

    cred = credentials.Certificate(firebase_config)

    firebase_admin.initialize_app(
        cred,
        {
            "databaseURL":
            "YOUR_FIREBASE_DATABASE_URL"
        }
    )

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.main {
    background-color: #0b141a;
    color: white;
}

[data-testid="stSidebar"] {
    background-color: #202c33;
}

.chat-box {
    background-color: #202c33;
    padding: 12px;
    border-radius: 12px;
    margin-bottom: 10px;
    color: white;
}

.user-box {
    background-color: #005c4b;
    padding: 12px;
    border-radius: 12px;
    margin-bottom: 10px;
    margin-left: auto;
    width: fit-content;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# ---------------- LOGIN ----------------
st.sidebar.title("💬 Real Chat App")

username = st.sidebar.text_input("Enter Your Name")

chat_with = st.sidebar.text_input("Chat With")

# ---------------- CHAT ROOM ----------------
if username and chat_with:

    room_id = "_".join(
        sorted([username, chat_with])
    )

    st.title(f"💬 Chat: {chat_with}")

    ref = db.reference(f"chats/{room_id}")

    messages = ref.get()

    if messages:

        for key, value in messages.items():

            if value["sender"] == username:

                st.markdown(
                    f"""
                    <div class="user-box">
                    {value['message']}<br>
                    <small>✓ Seen</small>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            else:

                st.markdown(
                    f"""
                    <div class="chat-box">
                    <b>{value['sender']}:</b>
                    {value['message']}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    # ---------------- SEND MESSAGE ----------------
    msg = st.text_input("Type Message")

    if st.button("Send"):

        if msg:

            ref.push({
                "sender": username,
                "message": msg,
                "time": str(datetime.now())
            })

            st.rerun()
