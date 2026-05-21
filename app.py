import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="WhatsApp Clone Pro",
    page_icon="💬",
    layout="wide"
)

# ---------------- SESSION STATE ----------------
if "contacts" not in st.session_state:
    st.session_state.contacts = [
        {"name": "Ali", "number": "+92 300 1111111"},
        {"name": "Ahmed", "number": "+92 301 2222222"},
    ]

if "messages" not in st.session_state:
    st.session_state.messages = {
        "Ali": ["Hello 👋", "How are you?"],
        "Ahmed": ["Welcome to WhatsApp Clone 🚀"]
    }

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

.title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    color: #25D366;
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

.contact-card {
    background-color: #111b21;
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 8px;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.title("💬 WhatsApp Clone")

st.sidebar.subheader("➕ Add New Contact")

new_name = st.sidebar.text_input("Contact Name")
new_number = st.sidebar.text_input("Phone Number")

if st.sidebar.button("Add Contact"):

    if new_name and new_number:

        # Add Contact
        st.session_state.contacts.append({
            "name": new_name,
            "number": new_number
        })

        # Create Empty Chat
        st.session_state.messages[new_name] = []

        st.sidebar.success("Contact Added ✅")

# ---------------- CONTACT LIST ----------------
st.sidebar.subheader("📱 Your Contacts")

contact_names = [c["name"] for c in st.session_state.contacts]

selected_contact = st.sidebar.radio(
    "Select Chat",
    contact_names
)

# ---------------- MAIN TITLE ----------------
st.markdown(
    '<p class="title">💬 WhatsApp Clone Pro</p>',
    unsafe_allow_html=True
)

# ---------------- SHOW CONTACT INFO ----------------
selected_data = next(
    c for c in st.session_state.contacts
    if c["name"] == selected_contact
)

st.write(f"### 👤 {selected_data['name']}")
st.write(f"📞 {selected_data['number']}")

st.divider()

# ---------------- CHAT AREA ----------------
for msg in st.session_state.messages[selected_contact]:

    st.markdown(
        f'<div class="chat-box">{msg}</div>',
        unsafe_allow_html=True
    )

# ---------------- SEND MESSAGE ----------------
message = st.text_input("Type your message")

if st.button("Send 📤"):

    if message:

        st.session_state.messages[selected_contact].append(message)

        st.rerun()
       
