from .llm import LLM
from .tools import *
from .prompts import *

import re
from typing import Tuple, Union


def builder():
    return LLM()


def parse(response: str) -> Tuple[str, str, str, Union[str, None]]:
    think = re.search(r"(?<=think: ).*", response).group(0)
    action = re.search(r"(?<=action: ).*", response).group(0)
    observation = re.search(r"(?<=observation: ).*", response).group(0)

    if "final_answer" in response:
        final_answer = re.search(r"(?<=final_answer: ).*", response).group(0)
    else:
        final_answer = None

    return think, action, observation, final_answer


def action_handler(action: str) -> str:
    for tool in tools_list.keys():
        if tool in action:
            api_calls = re.findall(rf"(?<={tool}\().*?(?=\))", action)
            for api_call in api_calls:
                result = tools_list[tool](api_call)
                action = re.sub(rf"{tool}\({api_call}\)", str(result), action)

    return action


