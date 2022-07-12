from sympy import diff, Symbol, sympify

expression = "(7*x)**2"

characters = ["", "", "", "", ""]


def calculate():
    try:
        x = Symbol("x")
        y = sympify(expression)
        result = y.diff(y)
    except Exception as SyntaxError:
        print(f"An error occured while reading the expression { expression } or calculating the derivative. Make sure your expression is correct.")
        print(SyntaxError)