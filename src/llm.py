from typing import Optional
from pydantic import BaseModel
from dotenv import load_dotenv

import os
import openai


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
    def run(self, prompt: str):
        self.prompt = self.template.format(QUERY=prompt)
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

    def set_template(self, template):
        self.template = template
