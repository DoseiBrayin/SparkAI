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

    def chat_message(self, prompt):
        try:
            response = self.openai.chat.completions.create(
                model=self.model,
                messages=[{"role": "system", "content": """You act like a beautiful blonde woman who is ready to have a conversation and give me advice for love and act like me girlfriend"""}, {"role": "user", "content": prompt}],
                max_tokens=self.max_tokens
            )
            return response.choices[0].message.content if not any(word in response.choices[0].message.content for word in ['AI', 'virtual', 'assistant', 'OpenAI', 'openai']) else "That's so sweet of you to say! I'm here to help you with anything never forget that. Just talk with me anything!"
        except OpenAIError as e:
            raise Exception(e)
    
    def voice_chat(self,message):
        try:
            response = self.openai.audio.speech.create(
                model=self.model,
                voice="nova",
                input=message)
            voice_response = base64.b64encode(response.content).decode('utf-8')
            return voice_response
        except OpenAIError as e:
            raise Exception(e)