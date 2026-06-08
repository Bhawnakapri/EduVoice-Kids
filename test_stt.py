from backend.speech_to_text import transcribe_audio

audio_path = "test.wav"  # we will add this file next

result = transcribe_audio(audio_path)

print("Transcription:", result)