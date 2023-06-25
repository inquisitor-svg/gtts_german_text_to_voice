from gtts import gTTS
import time


def generate_audio(text):
    tts = gTTS(text, lang='de')
    filename = f'audio_{int(time.time())}.mp3'
    tts.save(filename)
    print(f"Audio file generated: {filename}")


txt = input("Tell me your text(only work for German)")


generate_audio(txt)
