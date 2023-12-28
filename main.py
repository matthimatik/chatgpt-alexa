from gpt import ChatBot, GPTChatBot
from stt import GoogleSpeechRecognizer, SpeechRecognizer
from tts import convert_text_to_speech


def run_alexa_clone_loop(chat_bot: ChatBot, speech_recognizer: SpeechRecognizer) -> None:
    while True:
        message = speech_recognizer.recognize_speech()
        reply = chat_bot.chat(message)
        convert_text_to_speech(reply)

def main():
    run_alexa_clone_loop(GPTChatBot(), GoogleSpeechRecognizer())


if __name__ == "__main__":
    main()
