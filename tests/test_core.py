from reason_action import parse


def test_parse():
    response = """think: The question involve a calculation, so I have to use calculator for this task.
action: My money is calculator(5000 - 3000) rupiah left.
observation: There is no calculation left, so my answer is final.
final_answer: My money is 2000 rupiah left.
    """

    think, action, observation, final_answer = parse(response)

    assert think == "The question involve a calculation, so I have to use calculator for this task."
    assert action == "My money is calculator(5000 - 3000) rupiah left."
    assert observation == "There is no calculation left, so my answer is final."
    assert final_answer == "My money is 2000 rupiah left."
