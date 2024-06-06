class Prompt:
    def __init__(self, prompt: str,gender: int, personality: str):
        self.prompt = prompt
        self.gender = gender
        self.personality = personality
    
    def __str__(self):
        return f"""{self.prompt} you are a {
            "beutiful woman" if self.gender == 0 else "attractive man"
        } with this personality: {self.personality}"""
    
    def to_dict(self):
        return {
            "prompt": self.__str__(),
        }