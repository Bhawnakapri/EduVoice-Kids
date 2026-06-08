import streamlit as st
from streamlit_mic_recorder import mic_recorder

from backend.speech_to_text import transcribe_audio
from backend.text_to_speech import generate_voice

from backend.learning_content import (
    english_stories,
    hindi_stories,
    english_alphabets,
    hindi_alphabets
)

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="EduVoice Kids",
    layout="wide"
)

# =====================================
# CUSTOM STYLING
# =====================================

st.markdown("""
<style>

body {
    background-color: #F4F9FF;
}

h1 {
    text-align: center;
    color: #1E3A8A;
    font-size: 52px !important;
}

h2, h3 {
    color: #2563EB;
}

.stButton button {

    width: 100%;
    height: 75px;

    font-size: 24px;
    font-weight: bold;

    border-radius: 18px;

    background-color: #2563EB;
    color: white;

    border: none;

    margin-top: 12px;
    margin-bottom: 12px;

    transition: 0.3s;
}

.stButton button:hover {

    background-color: #1E40AF;
    color: white;
}

.story-box {

    background-color: white;

    padding: 25px;

    border-radius: 18px;

    border: 2px solid #D6E4FF;

    font-size: 24px;

    line-height: 2;

    color: #111827;

    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
}

</style>
""", unsafe_allow_html=True)

# =====================================
# HEADER
# =====================================

st.title("🎓 EduVoice Kids")

st.success(
    "👋 Welcome! Learn with stories and alphabets using voice."
)

st.write(
    """
    EduVoice Kids is a voice-based learning assistant
    designed for visually impaired children.

    Children can listen to stories, learn alphabets,
    and interact using voice commands.
    """
)

st.divider()

# =====================================
# ENGLISH STORIES
# =====================================

st.subheader("📚 English Stories")

story_cols = st.columns(3)

with story_cols[0]:
    honesty_btn = st.button("😊 Honesty")

with story_cols[1]:
    friendship_btn = st.button("🤝 Friendship")

with story_cols[2]:
    kindness_btn = st.button("💖 Kindness")

story_cols2 = st.columns(3)

with story_cols2[0]:
    sharing_btn = st.button("🍱 Sharing")

with story_cols2[1]:
    courage_btn = st.button("🦁 Courage")

with story_cols2[2]:
    discipline_btn = st.button("📘 Discipline")

st.divider()

# =====================================
# HINDI STORIES
# =====================================

st.subheader("🇮🇳 Hindi Stories")

hindi_story_cols = st.columns(3)

with hindi_story_cols[0]:
    honesty_hi_btn = st.button("🌟 ईमानदारी")

with hindi_story_cols[1]:
    friendship_hi_btn = st.button("🤝 दोस्ती")

with hindi_story_cols[2]:
    kindness_hi_btn = st.button("💖 दया")

hindi_story_cols2 = st.columns(3)

with hindi_story_cols2[0]:
    courage_hi_btn = st.button("🦁 साहस")

with hindi_story_cols2[1]:
    discipline_hi_btn = st.button("📘 अनुशासन")

with hindi_story_cols2[2]:
    sharing_hi_btn = st.button("🍱 साझा करना")

st.divider()

# =====================================
# ALPHABET SECTION
# =====================================

st.subheader("🔤 Alphabet Learning")

alphabet_language = st.selectbox(
    "Choose Language",
    ["English", "Hindi"]
)

selected_alphabet = None

if alphabet_language == "English":

    selected_alphabet = st.selectbox(
        "Choose Alphabet",
        list(english_alphabets.keys())
    )

else:

    selected_alphabet = st.selectbox(
        "Choose Hindi Alphabet",
        list(hindi_alphabets.keys())
    )

st.divider()

# =====================================
# VOICE INPUT
# =====================================

st.subheader("🎤 Voice Interaction")

st.write(
    """
    Try speaking:
    - Tell me a story about honesty
    - Tell me about friendship
    - A for Apple
    - अ से अनार
    """
)

audio = mic_recorder(
    start_prompt="🎙 Start Recording",
    stop_prompt="🛑 Stop Recording",
    just_once=True
)

# =====================================
# CONTENT VARIABLES
# =====================================

selected_content = None
content_title = ""
language = "en"

# =====================================
# ENGLISH STORY BUTTONS
# =====================================

if honesty_btn:
    selected_content = english_stories["honesty"]
    content_title = "😊 Honesty Story"

elif friendship_btn:
    selected_content = english_stories["friendship"]
    content_title = "🤝 Friendship Story"

elif kindness_btn:
    selected_content = english_stories["kindness"]
    content_title = "💖 Kindness Story"

elif sharing_btn:
    selected_content = english_stories["sharing"]
    content_title = "🍱 Sharing Story"

elif courage_btn:
    selected_content = english_stories["courage"]
    content_title = "🦁 Courage Story"

elif discipline_btn:
    selected_content = english_stories["discipline"]
    content_title = "📘 Discipline Story"

# =====================================
# HINDI STORY BUTTONS
# =====================================

elif honesty_hi_btn:
    selected_content = hindi_stories["ईमानदारी"]
    content_title = "🌟 ईमानदारी"
    language = "hi"

elif friendship_hi_btn:
    selected_content = hindi_stories["दोस्ती"]
    content_title = "🤝 दोस्ती"
    language = "hi"

elif kindness_hi_btn:
    selected_content = hindi_stories["दया"]
    content_title = "💖 दया"
    language = "hi"

elif courage_hi_btn:
    selected_content = hindi_stories["साहस"]
    content_title = "🦁 साहस"
    language = "hi"

elif discipline_hi_btn:
    selected_content = hindi_stories["अनुशासन"]
    content_title = "📘 अनुशासन"
    language = "hi"

elif sharing_hi_btn:
    selected_content = hindi_stories["साझा करना"]
    content_title = "🍱 साझा करना"
    language = "hi"

# =====================================
# ALPHABET LOGIC
# =====================================

if selected_alphabet:

    if alphabet_language == "English":

        selected_content = english_alphabets[selected_alphabet]
        content_title = f"🔤 Alphabet {selected_alphabet.upper()}"
        language = "en"

    else:

        selected_content = hindi_alphabets[selected_alphabet]
        content_title = f"🇮🇳 अक्षर {selected_alphabet}"
        language = "hi"

# =====================================
# VOICE INTERACTION LOGIC
# =====================================

if audio:

    with open("recorded_audio.wav", "wb") as f:
        f.write(audio["bytes"])

    st.info("Recognizing speech...")

    user_text = transcribe_audio("recorded_audio.wav")

    st.success("Speech Recognized!")

    st.write("### 📝 You Said:")
    st.write(user_text)

    lower_text = user_text.lower()

    # =========================
    # ENGLISH STORIES
    # =========================

    if "honesty" in lower_text:

        selected_content = english_stories["honesty"]
        content_title = "😊 Honesty Story"
        language = "en"

    elif "friendship" in lower_text:

        selected_content = english_stories["friendship"]
        content_title = "🤝 Friendship Story"
        language = "en"

    elif "kindness" in lower_text:

        selected_content = english_stories["kindness"]
        content_title = "💖 Kindness Story"
        language = "en"

    elif "sharing" in lower_text:

        selected_content = english_stories["sharing"]
        content_title = "🍱 Sharing Story"
        language = "en"

    elif "courage" in lower_text:

        selected_content = english_stories["courage"]
        content_title = "🦁 Courage Story"
        language = "en"

    elif "discipline" in lower_text:

        selected_content = english_stories["discipline"]
        content_title = "📘 Discipline Story"
        language = "en"

    # =========================
    # HINDI STORIES
    # =========================

    elif "ईमानदारी" in user_text:

        selected_content = hindi_stories["ईमानदारी"]
        content_title = "🌟 ईमानदारी"
        language = "hi"

    elif "दोस्ती" in user_text:

        selected_content = hindi_stories["दोस्ती"]
        content_title = "🤝 दोस्ती"
        language = "hi"

    elif "दया" in user_text:

        selected_content = hindi_stories["दया"]
        content_title = "💖 दया"
        language = "hi"

    elif "साहस" in user_text:

        selected_content = hindi_stories["साहस"]
        content_title = "🦁 साहस"
        language = "hi"

    elif "अनुशासन" in user_text:

        selected_content = hindi_stories["अनुशासन"]
        content_title = "📘 अनुशासन"
        language = "hi"

    elif "साझा" in user_text:

        selected_content = hindi_stories["साझा करना"]
        content_title = "🍱 साझा करना"
        language = "hi"

    # =========================
    # ENGLISH ALPHABETS
    # =========================

    elif "letter a" in lower_text or "a for apple" in lower_text:

        selected_content = english_alphabets["a"]
        content_title = "🔤 Alphabet A"
        language = "en"

    elif "letter b" in lower_text or "b for ball" in lower_text:

        selected_content = english_alphabets["b"]
        content_title = "🔤 Alphabet B"
        language = "en"

    elif "letter c" in lower_text or "c for cat" in lower_text:

        selected_content = english_alphabets["c"]
        content_title = "🔤 Alphabet C"
        language = "en"

    elif "letter d" in lower_text or "d for dog" in lower_text:

        selected_content = english_alphabets["d"]
        content_title = "🔤 Alphabet D"
        language = "en"

    # =========================
    # HINDI ALPHABETS
    # =========================

    elif "अ से" in user_text:

        selected_content = hindi_alphabets["अ"]
        content_title = "🇮🇳 अक्षर अ"
        language = "hi"

    elif "आ से" in user_text:

        selected_content = hindi_alphabets["आ"]
        content_title = "🇮🇳 अक्षर आ"
        language = "hi"

    elif "क से" in user_text:

        selected_content = hindi_alphabets["क"]
        content_title = "🇮🇳 अक्षर क"
        language = "hi"

    elif "ख से" in user_text:

        selected_content = hindi_alphabets["ख"]
        content_title = "🇮🇳 अक्षर ख"
        language = "hi"

    else:

        st.warning(
            "Sorry, I could not understand. Please try again."
        )

# =====================================
# DISPLAY CONTENT
# =====================================

if selected_content:

    st.divider()

    st.subheader(content_title)

    st.markdown(
        f'<div class="story-box">{selected_content}</div>',
        unsafe_allow_html=True
    )

    st.info("Generating narration...")

    audio_path = generate_voice(
        selected_content,
        language=language
    )

    st.success("🔊 Narration Ready!")

    audio_file = open(audio_path, "rb")

    st.audio(audio_file.read(), format="audio/mp3")

    # Repeat button
    if st.button("🔁 Repeat Narration"):

        repeat_audio = open(audio_path, "rb")

        st.audio(repeat_audio.read(), format="audio/mp3")

    st.success(
        "😊 Great learning! Try another story or alphabet."
    )