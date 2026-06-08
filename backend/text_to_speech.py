from gtts import gTTS

def generate_voice(text, language="en", output_file="story.mp3"):

    tts = gTTS(
        text=text,
        lang=language
    )

    tts.save(output_file)

    return output_file