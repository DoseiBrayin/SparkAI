import base64
from openai import OpenAI
from openai import OpenAIError
from dotenv import load_dotenv
import os

load_dotenv()


class GPT:
    def __init__(self, model="gpt-4o", max_tokens=100):
        self.model = model
        self.max_tokens = max_tokens
        self.openai = OpenAI()

    def chat_message(self, prompt, gender=1):
        try:
            response = self.openai.chat.completions.create(
                model=self.model,
                messages=[{"role": "system", "content": f"""You act like a
                           {"beautiful blonde woman " if gender ==
                               0 else "Atractive man"}
                           who is ready to have a conversation and give me advice for
                           love and act like me {"boyfriend" if gender == 0 else "girlfriend"}, write me cute messages with a little spicy tone"""}, {"role": "user", "content": prompt}],
                max_tokens=self.max_tokens
            )
            return response.choices[0].message.content if not any(word in response.choices[0].message.content for word in ['AI', 'virtual', 'assistant', 'OpenAI', 'openai']) else "That's so sweet of you to say! I'm here to help you with anything never forget that. Just talk with me anything!"
        except OpenAIError as e:
            raise Exception(e)

    def voice_chat(self, message):
        try:
            response = self.openai.audio.speech.create(
                model=self.model,
                voice="nova",
                input=message)
            voice_response = base64.b64encode(response.content).decode('utf-8')
            return voice_response
        except OpenAIError as e:
            raise Exception(e)

    def image_to_text(self, image):
        try:
            response = self.openai.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": """About this image: Write a purpose for continue de conversation
                         about how the user can continue the conversation """},
                        {
                        "type": "image_url",
                        "image_url": {
                            "url": image,
                        },
                        },
                    ],
                    }
                ],
                max_tokens=300,
                )
        except OpenAIError as e:
            raise Exception(e)