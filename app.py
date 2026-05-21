import streamlit as st
import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime

# ---------------- PAGE ----------------
st.set_page_config(page_title="WhatsApp Clone", page_icon="💬", layout="wide")

# ---------------- FIREBASE INIT ----------------
if not firebase_admin._apps:
    try:
        cred = credentials.Certificate("firebase-key.json")

        firebase_admin.initialize_app(
            cred,
            {
                "databaseURL": "https://mughaliyaa-chatting-default-rtdb.firebaseio.com/"
            }
        )
    except Exception as e:
        st.error("Firebase Error ❌ Check JSON file or Database URL")
        st.stop()

# ---------------- UI ----------------
st.title("💬 WhatsApp Clone (Firebase)")

username = st.text_input("Your Name")
chat_with = st.text_input("Chat With")

if username and chat_with:

    room_id = "_".join(sorted([username, chat_with]))
    ref = db.reference(f"chats/{room_id}")

    st.subheader(f"Chat with {chat_with}")

    messages = ref.get()

    if messages:
        for msg_id, msg in messages.items():
            if msg["sender"] == username:
                st.markdown(f"👉 **You:** {msg['message']}")
            else:
                st.markdown(f"👤 **{msg['sender']}:** {msg['message']}")

    message = st.text_input("Type message")

    if st.button("Send"):
        if message:
            ref.push({
                "sender": username,
                "message": message,
                "time": str(datetime.now())
            })
            st.rerun()
