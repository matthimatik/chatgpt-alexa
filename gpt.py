import os
from typing import Protocol

from openai import OpenAI


class ChatBot(Protocol):
    def chat(self, message: str) -> str:
        ...

class GPTChatBot:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.messages = [
            {"role": "system", "content": "You are an intelligent assistant."}
        ]

    def call_openai_api(self):
        chat = self.client.chat.completions.create(
            model="gpt-3.5-turbo", messages=self.messages
        )
        reply = chat.choices[0].message.content
        return reply

    def chat(self, message):
        if message:
            self.messages.append({"role": "user", "content": message})
            reply = self.call_openai_api()
            print(f"ChatGPT: {reply}")
            self.messages.append({"role": "assistant", "content": reply})
        return reply


def main():
    bot = GPTChatBot()
    bot.chat("hello")


if __name__ == "__main__":
    main()
