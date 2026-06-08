# EduVoice Kids

## AI-Powered Voice Learning Assistant for Visually Impaired Children

### 🌐 Live Demo

https://eduvoice-kids-6i8i2ajvmbgsgv7praqxuv.streamlit.app/

### 💻 GitHub Repository

https://github.com/Bhawnakapri/EduVoice-Kids

---

## Overview

EduVoice Kids is an accessibility-focused educational application designed to help visually impaired children learn through voice interaction.

The application enables children to interact using voice commands, listen to educational stories, learn English and Hindi alphabets, and receive audio narration through text-to-speech technology.

The goal of the project is to provide an inclusive and engaging learning experience for children through speech-based interaction and audio-guided learning.

---

## Problem Statement

Visually impaired children often face difficulties accessing traditional educational resources and learning materials.

EduVoice Kids addresses this challenge by providing a voice-driven learning environment where children can interact naturally using speech and receive educational content through audio narration.

---

## Features

* 🎤 Voice-based interaction
* 🗣️ Speech-to-text conversion using Faster-Whisper
* 🔊 Text-to-speech narration using gTTS
* 📖 English moral stories
* 📚 Hindi moral stories
* 🔤 English alphabet learning (A–Z)
* 🇮🇳 Hindi alphabet learning (अ–ज्ञ)
* ♿ Accessibility-focused user interface
* 🔄 Repeat narration functionality
* 🌍 Multilingual learning support

---

## Technology Stack

### Frontend

* Streamlit

### Backend

* Python

### AI & Speech Processing

* Faster-Whisper
* Speech Recognition
* Natural Language Processing (NLP)

### Text-to-Speech

* gTTS

### Version Control & Deployment

* Git
* GitHub
* Streamlit Community Cloud

---

## Project Structure

```text
EduVoice-Kids
│
├── app.py
│
├── backend/
│   ├── learning_content.py
│   ├── speech_to_text.py
│   ├── text_to_speech.py
│   ├── stories.py
│   ├── rag.py
│   └── llm.py
│
├── utils/
│   ├── pdf_loader.py
│   └── chunking.py
│
├── requirements.txt
│
└── README.md
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/Bhawnakapri/EduVoice-Kids.git
```

### Navigate to the Project Directory

```bash
cd EduVoice-Kids
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

---

## How It Works

1. The user interacts with the application using voice commands.
2. Faster-Whisper converts speech into text.
3. The system identifies the requested learning content.
4. Educational content is displayed on screen.
5. gTTS converts the content into audio narration.
6. The child can listen and learn through an accessible interface.

---

## Learning Modules

### English Learning

* English Alphabets (A–Z)
* Moral Stories
* Pronunciation Support

### Hindi Learning

* हिंदी वर्णमाला (अ–ज्ञ)
* हिंदी कहानियाँ
* हिंदी ऑडियो नैरेशन

---

## Future Enhancements

* Interactive quiz mode
* Voice-controlled navigation
* Personalized learning experience
* Progress tracking system
* Additional educational categories
* Support for more Indian languages
* AI-powered conversational learning assistant

---

## Learning Outcomes

This project demonstrates practical experience in:

* Python Development
* Artificial Intelligence Integration
* Speech Recognition
* Text-to-Speech Systems
* Accessibility-Focused Design
* Natural Language Processing
* Git & GitHub Version Control
* Cloud Deployment
* End-to-End Application Development

---

## Author

**Bhawana Kapri**

B.Tech Computer Science & Engineering (Data Science)

Galgotias University

---

## Acknowledgements

This project was developed with the aim of promoting accessible education and creating inclusive learning opportunities for visually impaired children through AI-powered voice technology.
