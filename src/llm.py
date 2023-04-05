import os
from typing import Optional

import openai
from dotenv import load_dotenv
from pydantic import BaseModel


class BaseLLM(BaseModel):
    model: str = "gpt-3.5-turbo"
    temperature: float = 0.5
    max_tokens: int = 100
    top_p: float = 1.0
    prompt: Optional[str] = None
    template: Optional[str] = None
    response: Optional[dict] = None

    load_dotenv(".env")
    openai.api_key = os.getenv("OPENAI_KEY")

    def get_used_tokens(self):
        return self.response["usage"]["total_tokens"]

    def get_answer(self):
        return self.response["choices"][0]["message"]["content"]


class LLM(BaseLLM):
    def run(self, prompt: str, template: str = None):

        if template is not None:
            self.template = template
            self.prompt = self.template.format(QUERY=prompt)
        else:
            self.prompt = prompt
            
        if self.model == "gpt-3.5-turbo":
            self.response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": self.prompt,
                    }
                ],
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                top_p=self.top_p,
            )
        else:
            raise NotImplementedError("Model not implemented yet.")
