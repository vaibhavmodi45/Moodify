import streamlit as st

# Page configuration
st.set_page_config(page_title="Moodify - AI Chatbot", page_icon="🧠", layout="wide")

# Custom styling
st.markdown(
    """
    <style>
        body { background-color: #0E1621; }
        .chat-container { max-width: 700px; margin: auto; padding: 20px; padding-bottom: 60px; }
        .chat-header { font-size: 28px; font-weight: bold; margin-top: 10px; color: #ffffff; text-align: left; }
        .chat-tagline { font-size: 18px; color: #b0b0b0; margin-bottom: 20px; text-align: left; }
        .message { padding: 10px; margin: 5px 0; border-radius: 10px; display: inline-block; }
        .user-message { background-color: #0078ff; color: white; text-align: right; margin-left: auto; }
        .bot-message { background-color: #444; color: white; text-align: left; margin-right: auto; }
        .input-container { position: fixed; bottom: 0; width: 100%; background-color: #fff; padding: 10px; box-shadow: 0 -2px 5px rgba(0,0,0,0.1); }
        .stTextInput > div > div > input { border-radius: 20px; padding: 10px; width: 100%; }
    </style>
    """,
    unsafe_allow_html=True
)

def intro():
    st.markdown("<div class='chat-header'>Moodify</div>", unsafe_allow_html=True)
    st.markdown("<div class='chat-tagline'>Revolutionizing Therapy using AI</div>", unsafe_allow_html=True)
    st.write("# Welcome to Moodify! 👋")
    st.sidebar.success("Select a page above.")

    st.markdown(
        """
        Moodify is an AI-based chatbot designed to provide mental calmness and support.

        **👈 Select a page from the sidebar** to see some examples
        of what Moodify can do!

        ### Want to learn more?

        - Check out [our website](https://moodify.ai)
        - Jump into our [documentation](https://docs.moodify.ai)
        - Ask a question in our [community forums](https://discuss.moodify.ai)

        ### See more complex demos

        - Use a neural net to [analyze mental health data](https://github.com/moodify/demo-mental-health)
        - Explore a [dataset of mental health conversations](https://github.com/moodify/demo-conversations)
    """
    )

def chat():
    st.markdown("<div class='chat-header'>Moodify Chat 💬</div>", unsafe_allow_html=True)
    st.markdown("<div class='chat-tagline'>Your AI companion for mental calmness</div>", unsafe_allow_html=True)

    # Chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    st.markdown('<div class="chat-container">', unsafe_allow_html=True)

    for msg in st.session_state.messages:
        css_class = "user-message" if msg["is_user"] else "bot-message"
        st.markdown(f'<div class="message {css_class}">{msg["content"]}</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # User input
    st.markdown('<div class="input-container">', unsafe_allow_html=True)
    user_input = st.text_input("Type your message...", "", key="chat_input")

    if user_input:
        st.session_state.messages.append({"content": user_input, "is_user": True})
        # Here you would add the logic to get the bot's response
        bot_reply = "I'm here to help! How can I assist you today?"
        st.session_state.messages.append({"content": bot_reply, "is_user": False})
        st.experimental_rerun()

    st.markdown('</div>', unsafe_allow_html=True)

def resources():
    st.markdown("<div class='chat-header'>Resources 📃</div>", unsafe_allow_html=True)
    st.markdown("<div class='chat-tagline'>Helpful resources for mental calmness</div>", unsafe_allow_html=True)
    st.write("### Here are some resources to help you stay calm and relaxed:")
    st.markdown(
        """
        - [Meditation Techniques](https://www.mindful.org/how-to-meditate/)
        - [Breathing Exercises](https://www.healthline.com/health/breathing-exercise)
        - [Mental Health Support](https://www.mentalhealth.gov/get-help)
        - [Stress Management Tips](https://www.apa.org/topics/stress)
    """
    )

# Sidebar navigation
st.sidebar.markdown("Moodify 🧠")
st.sidebar.write("Moodify 🧠")
page = st.sidebar.radio("Navigation", ["Home 🏠", "Chat 💬", "Resources 📃"])

# Render selected page
if page == "Home 🏠":
    intro()
elif page == "Chat 💬":
    chat()
elif page == "Resources 📃":
    resources()