import streamlit as st
import requests

import os

API_URL = os.getenv("API_URL", "http://127.0.0.1:8000/ask")


st.set_page_config(page_title="Enterprise RAG Assistant", layout="wide", page_icon="🏢")

# ── Full Dark Theme CSS ──────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

/* ════════════════════════════════════════
   FORCE DARK EVERYWHERE — every element
   ════════════════════════════════════════ */
html, body,
.stApp,
.stApp > div,
[data-testid="stAppViewContainer"],
[data-testid="stAppViewBlockContainer"],
[data-testid="stMain"],
[data-testid="stBottom"],
[data-testid="stBottomBlockContainer"],
[data-testid="stChatInputContainer"],
section.main,
.block-container,
.main .block-container,
footer,
header {
    background: #0F1117 !important;
    background-color: #0F1117 !important;
    font-family: 'Inter', sans-serif !important;
}

/* Chat input sticky footer wrapper */
[data-testid="stBottom"],
[data-testid="stBottomBlockContainer"],
.stChatFloatingInputContainer,
div[class*="InputContainer"],
div[class*="chatInputContainer"],
div[class*="bottom"] {
    background: #1A1D2E !important;
    background-color: #1A1D2E !important;
    border-top: 1px solid rgba(79,70,229,0.20) !important;
}

/* ════════════════════════════════════════
   TITLE
   ════════════════════════════════════════ */
h1 {
    font-size: 2rem !important;
    font-weight: 800 !important;
    background: linear-gradient(135deg, #4F46E5 0%, #7C3AED 50%, #06B6D4 100%) !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    background-clip: text !important;
    letter-spacing: -0.03em !important;
    margin-bottom: 0 !important;
}

h1::after {
    content: '';
    display: block;
    height: 3px;
    width: 72px;
    background: linear-gradient(90deg, #4F46E5, #06B6D4);
    border-radius: 2px;
    margin-top: 6px;
}

/* ════════════════════════════════════════
   SUBTITLE
   ════════════════════════════════════════ */
.stApp p {
    color: #94A3B8 !important;
    font-size: 0.93rem !important;
}

/* ════════════════════════════════════════
   CHAT MESSAGES
   ════════════════════════════════════════ */
[data-testid="stChatMessage"] {
    background: #1A1D2E !important;
    border: 1px solid rgba(255,255,255,0.07) !important;
    border-radius: 16px !important;
    box-shadow: 0 4px 24px rgba(0,0,0,0.4) !important;
    padding: 1rem 1.25rem !important;
    margin-bottom: 0.8rem !important;
}

/* User bubble */
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {
    background: linear-gradient(135deg,
        rgba(79,70,229,0.20) 0%,
        rgba(124,58,237,0.12) 100%) !important;
    border: 1px solid rgba(79,70,229,0.38) !important;
    border-left: 3px solid #4F46E5 !important;
}

/* Assistant bubble */
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) {
    background: linear-gradient(135deg,
        rgba(13,148,136,0.16) 0%,
        rgba(6,182,212,0.10) 100%) !important;
    border: 1px solid rgba(6,182,212,0.30) !important;
    border-left: 3px solid #0D9488 !important;
}

/* Message text */
[data-testid="stChatMessage"] p,
[data-testid="stChatMessage"] li,
[data-testid="stChatMessage"] div,
[data-testid="stChatMessage"] span {
    color: #FFFFFF !important;
}

/* ════════════════════════════════════════
   CHAT INPUT — fully dark
   ════════════════════════════════════════ */
[data-testid="stChatInput"],
.stChatInput,
.stChatInput > div,
[data-testid="stChatInputContainer"] > div {
    background: #1A1D2E !important;
    background-color: #1A1D2E !important;
    border: 1.5px solid rgba(79,70,229,0.45) !important;
    border-radius: 14px !important;
    box-shadow: 0 0 24px rgba(79,70,229,0.20) !important;
}

[data-testid="stChatInput"] textarea,
.stChatInput textarea,
[data-testid="stChatInput"] input,
.stChatInput input {
    background: transparent !important;
    background-color: transparent !important;
    color: #FFFFFF !important;
    caret-color: #FFFFFF !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.96rem !important;
    font-weight: 500 !important;
    border: none !important;
    box-shadow: none !important;
}

[data-testid="stChatInput"] textarea::placeholder,
.stChatInput textarea::placeholder {
    color: #64748B !important;
    font-weight: 400 !important;
}

/* Send button */
[data-testid="stChatInput"] button,
.stChatInput button {
    background: linear-gradient(135deg, #4F46E5, #06B6D4) !important;
    border: none !important;
    border-radius: 10px !important;
    color: #fff !important;
    transition: opacity 0.2s, transform 0.15s;
}
[data-testid="stChatInput"] button:hover,
.stChatInput button:hover {
    opacity: 0.88 !important;
    transform: scale(1.05) !important;
}

/* ════════════════════════════════════════
   EXPANDER (Sources)
   ════════════════════════════════════════ */
.streamlit-expanderHeader {
    background: #1E2235 !important;
    border: 1px solid rgba(6,182,212,0.30) !important;
    border-radius: 10px !important;
    color: #06B6D4 !important;
    font-weight: 600 !important;
    font-size: 0.85rem !important;
}

.streamlit-expanderContent {
    background: #1A1D2E !important;
    border: 1px solid rgba(6,182,212,0.20) !important;
    border-top: none !important;
    border-radius: 0 0 10px 10px !important;
    color: #94A3B8 !important;
    font-size: 0.875rem !important;
    padding: 0.75rem 1rem !important;
}

/* ════════════════════════════════════════
   ALERT / ERROR
   ════════════════════════════════════════ */
[data-testid="stAlert"] {
    background: rgba(225,29,72,0.12) !important;
    border: 1px solid rgba(225,29,72,0.35) !important;
    border-radius: 10px !important;
    color: #FCA5A5 !important;
}

/* ════════════════════════════════════════
   SPINNER
   ════════════════════════════════════════ */
.stSpinner > div {
    border-top-color: #4F46E5 !important;
}

/* ════════════════════════════════════════
   SCROLLBAR
   ════════════════════════════════════════ */
::-webkit-scrollbar        { width: 5px; }
::-webkit-scrollbar-track  { background: #0F1117; }
::-webkit-scrollbar-thumb  { background: #4F46E5; border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: #7C3AED; }

/* ════════════════════════════════════════
   HIDE STREAMLIT CHROME
   ════════════════════════════════════════ */
#MainMenu, footer               { visibility: hidden; }
header[data-testid="stHeader"]  { background: #0F1117 !important; }
</style>
""", unsafe_allow_html=True)

# ── App Header ───────────────────────────────────────────────────────────────
st.title("🏢 Enterprise SOP & Policy Assistant")
st.write("Ask questions about HR, SOP, and compliance documents.")

# ── Session State ────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []

# ── Render history ───────────────────────────────────────────────────────────
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ── Chat Input ───────────────────────────────────────────────────────────────
if prompt := st.chat_input("Ask your question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.write(prompt)

    try:
        with st.spinner("Thinking..."):
            response = requests.post(API_URL, json={"question": prompt})
            data = response.json()

        answer = data.get("answer", "No response")
        sources = data.get("sources", [])

        with st.chat_message("assistant"):
            st.write(answer)

            if sources:
                with st.expander("Sources"):
                    for s in sources:
                        st.write(f"{s['file']} (Page {s['page']})")

        st.session_state.messages.append({"role": "assistant", "content": answer})

    except Exception as e:
        st.error(f"Backend not connected: {e}")
