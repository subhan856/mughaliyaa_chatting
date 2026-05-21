import streamlit as st
import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime
import time

# ---------------- PAGE ----------------
st.set_page_config(page_title="WhatsApp Clone Pro", page_icon="💬", layout="wide")

# ---------------- FIREBASE INIT ----------------
if not firebase_admin._apps:
    cred = credentials.Certificate("firebase-key.json")

    firebase_admin.initialize_app(cred, {
        "databaseURL": "https://mughaliyaa-chatting-default-rtdb.firebaseio.com/"
    })

# ---------------- UI HEADER ----------------
st.title("💬 WhatsApp Clone PRO (Firebase Real-Time)")

# ---------------- USER INFO ----------------
username = st.text_input("Enter Your Name")
phone = st.text_input("Enter Your Phone Number (+92xxxxxxxxxx)")
chat_with = st.text_input("Chat With (Name or Number)")

# ---------------- STATUS UPDATE ----------------
def update_status(user):
    status_ref = db.reference(f"status/{user}")
    status_ref.set({
        "last_seen": str(datetime.now())
    })

# ---------------- CHAT ----------------
if username and chat_with and phone:

    room_id = "_".join(sorted([phone, chat_with]))
    chat_ref = db.reference(f"chats/{room_id}")

    st.subheader(f"Chat Room: {chat_with}")

    # show messages
    messages = chat_ref.get()

    if messages:
        for msg_id, msg in messages.items():
            if msg["sender"] == phone:
                st.markdown(f"👉 **You:** {msg['message']}  \n⏰ {msg['time']}")
            else:
                st.markdown(f"👤 **{msg['sender']}:** {msg['message']}  \n⏰ {msg['time']}")

    st.divider()

    # message input
    message = st.text_input("Type your message")

    if st.button("Send 🚀"):
        if message:
            chat_ref.push({
                "sender": phone,
                "name": username,
                "message": message,
                "time": str(datetime.now())
            })

            update_status(phone)
            st.rerun()

    # auto refresh (real-time feel)
    time.sleep(1)
    st.rerun()
