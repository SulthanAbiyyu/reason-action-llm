from src import LLM
from src import prompt_calculator

def test_prompt_calculator():
    llm = LLM()
    QUERY = "My money is 5000 rupiah. I want to buy a car that costs 2000 rupiah. How much money do I have left?"
    llm.run(
            QUERY,
            template=prompt_calculator
        )

    assert "calculator(5000-2000)" in llm.get_answer()
