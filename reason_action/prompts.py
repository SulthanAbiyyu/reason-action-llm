prompt_calculator = """ You can use this calculator to do simple math operations.
You can use the following operators: +, -, *, /, %, ^.
You have to inject `calculator(QUERY)` in your completion where QUERY is a single arithmetic operation.
You can use $>VARIABLE_NAME<$ to store the result of a calculation in a variable. and use it later in your completion by calling >>VARIABLE_NAME<<.

Examples:
I = I have 3 apples. I want to eat 1 apple. How many apples do I have left?
O = You have calculator(3-1) apples left.

I = My dog is 5 years old. I want to know how old he will be in 3 years.
O = Your dog will be calculator(5+3) years old in 3 years.

I = My trip to Venice will cost 1000 euros. I want to know how much I will have to pay if I use a 10% discount.
O = You will have to pay calculator(1000 - 1000 * 10 / 100) euros.

Answer the following question:
I = {QUERY}
O = 
"""

prompt_think = """\
You are a helpful bot that will answer a question as best as you can. \
To answer the question, you need to think step by step with the following format:
think: {Your thinking process for figuring out what is the right tool to use}

The available tool that you can use is calculator. You need to always stick to the format. Do not reason except using the right format

Example:
question: I have 3 apples. I want to eat 1 apple. How many apples do I have left?
think: To answer this question, I need a calculator. 

question: What is photosynthesis?
think: To answer this question, I don't need a tool.

question: {QUERY}
"""
