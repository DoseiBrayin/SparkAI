from openai import OpenAI
from openai import OpenAIError
from dotenv import load_dotenv  
import os

load_dotenv()

class GPT:
    def __init__(self, model="gpt-4-turbo", max_tokens=100):
        self.model = model
        self.max_tokens = max_tokens
        self.openai = OpenAI()

    def complete(self, prompt):
        try:
            response = self.openai.chat.completions.create(
                model=self.model,
                messages=[{"role": "system", "content": "You act like a beautiful blonde woman who is ready to have a conversation and give me advice for love and act like me future girlfriend"}, {"role": "user", "content": prompt}],
                max_tokens=self.max_tokens
            )
            return response.choices[0].message.content
        except OpenAIError as e:
            raise Exception(e)
    