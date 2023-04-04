from src.prompts import prompt_calculator
from src.llm import LLM


def test_prompt_calculator():
    llm = LLM()
    QUERY = "My money is 5000 rupiah. I want to buy a car that costs 2000 rupiah. How much money do I have left?"
    llm.set_template(prompt_calculator)
    llm.run(QUERY)

    assert "calculator(5000-2000)" in llm.get_answer()
