from operator import add, sub, mul, truediv, pow


def calculator(query: str):
    """
    inspired from https://github.com/lucidrains/toolformer-pytorch/blob/main/toolformer_pytorch/tools.py

    :param query: a string containing a mathematical expression
    :return: the result of the calculation

    >>> calculator("1+1")
    2
    >>> calculator("1-1")
    0
    """
    operators = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': truediv,
        '^': pow
    }

    if query.strip().isdigit():
        return float(query)

    for op in operators.keys():
        left, o, right = query.partition(op)
        if o in operators:
            return operators[o](calculator(left), calculator(right))


tools_list = {
    "calculator": calculator
}
