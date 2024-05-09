from openai import OpenAI
from openai import OpenAIError
from openai import OpenAIResponseError

class GPT:
    def __init__(self, api_key, model="gpt-4-turbo", max_tokens=100):
        self.api_key = api_key
        self.model = model
        self.max_tokens = max_tokens
        self.openai = OpenAI(api_key)

    def complete(self, prompt):
        try:
            response = self.openai.chat.completions.create(
                model=self.model,
                messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": prompt}],
                max_tokens=self.max_tokens,
                response_format="json"
            )
            return response.choices[0].message.content
        except OpenAIError as e:
            raise OpenAIResponseError(e)
    