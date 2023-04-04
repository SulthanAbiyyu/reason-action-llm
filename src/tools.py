from operator import add, sub, mul, truediv, mod, pow


def calculator(query: str):
    """
    inspired from https://github.com/lucidrains/toolformer-pytorch/blob/main/toolformer_pytorch/tools.py

    :param query: a string containing a mathematical expression
    :return: the result of the calculation

    >>> calculator("1+1")
    2
    >>> calculator("1-1")
    0

    query should only contains one operation.
    """
    operation = {
        "^": pow,
        "*": mul,
        "/": truediv,
        "%": mod,
        "+": add,
        "-": sub,
    }

    if query.isdigit():
        return float(query)

    for op in operation.keys():
        left, o, right = query.partition(op)
        print(o)
        if o in operation:
            return operation[o](calculator(left), calculator(right))
