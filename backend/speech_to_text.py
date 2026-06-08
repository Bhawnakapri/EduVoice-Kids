from faster_whisper import WhisperModel

# Load lightweight model
model = WhisperModel("base")

def transcribe_audio(audio_path):
    segments, _ = model.transcribe(audio_path)

    text = ""

    for segment in segments:
        text += segment.text + " "

    return text.strip()