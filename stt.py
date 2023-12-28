from typing import Protocol
import speech_recognition as sr


class SpeechRecognizer(Protocol):
    def recognize_speech(self) -> str:
        pass

class GoogleSpeechRecognizer:
    def __init__(self, language="en-US"):
        self.language = language
        self.recognizer = sr.Recognizer()

    def recognize_speech(self):
        # Capture audio
        with sr.Microphone() as source:
            print("Speak now: ")
            audio = self.recognizer.listen(source)

        # Recognize speech
        try:
            text = self.recognizer.recognize_google(audio, language=self.language)
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Request error: {0}".format(e))

def main():
    recognizer = SpeechRecognizer()
    text = recognizer.recognize_speech()
    print("You said: " + text)

if __name__ == "__main__":
    main()
