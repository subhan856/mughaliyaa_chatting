import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="WhatsApp Clone",
    page_icon="💬",
    layout="wide"
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
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 10px;
    width: fit-content;
    max-width: 70%;
    color: white;
    font-size: 16px;
}

.user-box {
    background-color: #005c4b;
    padding: 15px;
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
st.sidebar.title("💬 Chats")

users = [
    "Ali",
    "Ahmed",
    "Hamza",
    "Usman",
    "Zain"
]

selected_user = st.sidebar.radio(
    "Select User",
    users
)

# ---------------- MAIN UI ----------------
st.markdown(
    '<p class="title">WhatsApp Clone</p>',
    unsafe_allow_html=True
)

st.write(f"### Chat with {selected_user}")

# ---------------- CHAT AREA ----------------
st.markdown(
    '<div class="chat-box">Hello Bro 👋</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="user-box">Hi! How are you? 😄</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="chat-box">I am fine 🚀</div>',
    unsafe_allow_html=True
)

# ---------------- MESSAGE INPUT ----------------
message = st.text_input("Type a message")

if st.button("Send 📤"):
    if message:
        st.markdown(
            f'<div class="user-box">{message}</div>',
            unsafe_allow_html=True
        )
        st.success("Message Sent ✅")
