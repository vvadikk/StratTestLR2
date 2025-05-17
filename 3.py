import re

def percent_to_decimal(e):
    return re.sub(r'(\d+(\.\d+)?)%', r'(\1 / 100)', e)
def evaluate(expression):
    return eval(percent_to_decimal(expression))
print(evaluate('3 ** 10'))
print(evaluate('55% + 1.5'))
print(evaluate('9 ** 3 + 66%'))
