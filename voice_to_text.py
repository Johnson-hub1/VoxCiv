# voice_to_text.py

import speech_recognition as sr

def listen_and_convert():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("🎙️ Please speak now...")
        recognizer.adjust_for_ambient_noise(source)
        audio_data = recognizer.listen(source)

        try:
            # Recognize speech using Google Web Speech API
            print("⏳ Converting speech to text...")
            text = recognizer.recognize_google(audio_data)
            print(f"📝 You said: {text}")
            return text
        except sr.UnknownValueError:
            print("❌ Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"❌ Could not request results; {e}")

# Run the voice-to-text function
if __name__ == "__main__":
    listen_and_convert()
