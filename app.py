import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="WhatsApp Clone",
    page_icon="💬",
    layout="wide"
)

# ---------------- FIREBASE SETUP ----------------
if not firebase_admin._apps:

    cred = credentials.Certificate(
        "firebase-key.json"
    )

    firebase_admin.initialize_app(
        cred,
        {
           firebase_config = {
    "databaseURL": "https://mughaliyaa-chatting-default-rtdb.firebaseio.com/"
}
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
    width: fit-content;
    max-width: 70%;
    color: white;
    font-size: 16px;
}

.user-box {
    background-color: #005c4b;
    padding: 12px;
    border-radius: 12px;
    margin-left: auto;
    margin-bottom: 10px;
    width: fit-content;
    max-width: 70%;
    color: white;
    font-size: 16px;
}

.title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    color: #25D366;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.title("💬 Real Chat App")

username = st.sidebar.text_input("Your Name")
chat_with = st.sidebar.text_input("Chat With")

# ---------------- MAIN TITLE ----------------
st.markdown(
    '<p class="title">💬 WhatsApp Clone</p>',
    unsafe_allow_html=True
)

# ---------------- CHAT SYSTEM ----------------
if username and chat_with:

    room_id = "_".join(
        sorted([username, chat_with])
    )

    st.write(f"### Chat with {chat_with}")

    ref = db.reference(f"chats/{room_id}")

    messages = ref.get()

    # ---------------- SHOW MESSAGES ----------------
    if messages:

        for key, value in messages.items():

            if value["sender"] == username:

                st.markdown(
                    f"""
                    <div class="user-box">
                    {value['message']}
                    <br>
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
    message = st.text_input("Type Message")

    if st.button("Send 📤"):

        if message:

            ref.push({
                "sender": username,
                "message": message,
                "time": str(datetime.now())
            })

            st.rerun()
