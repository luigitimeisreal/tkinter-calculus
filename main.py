from tkinter import Tk, Label, Button
from sympy import Symbol, diff, sympify
from math import pi


def calculate(expression="0"):
    try:
        x = Symbol("x")
        result = diff(sympify(expression))
        print_result = Label(window, text=f"{ result }", font=("Arial", 14))
        print_result.grid(row=11)
    except Exception as SyntaxErrorException:
        error = Label(window, text="An error occured, is your expression correct?")
        error.grid(row=10, columnspan=2)
        print(f"An error occured while reading the expression { expression } "
              f"or calculating the derivative. "
              f"Make sure your expression is correct.")
        print(SyntaxErrorException)


def press(button_text: str):
    global equation
    if button_text == "D":
        equation = equation[:-1]
    else:
        equation += button_text
    display_equation = Label(window, text=f"{ equation }", font=("Arial", 14))
    display_equation.grid(row=10)


# Define the window
window = Tk()
window.title("Tkinter Calculus Calculator")
window.geometry("500x700")
window.resizable(False, False)

# Define equation
equation = ""
print(equation)

# Widgets
title = Label(window, text="Tkinter Calculus Calculator", font=("Arial", 25))
title.grid(row=0, columnspan=2)

current_expression = Label(window, font=("Arial", 25))
current_expression.grid(row=1, columnspan=2)

seven = Button(window, text="7", font=("Arial", 25), command=lambda: press("7"))
seven.grid(column=0, row=2)

eight = Button(window, text="8", font=("Arial", 25), command=lambda: press("8"))
eight.grid(column=1, row=2)

nine = Button(window, text="9", font=("Arial", 25), command=lambda: press("9"))
nine.grid(column=2, row=2)

four = Button(window, text="4", font=("Arial", 25), command=lambda: press("4"))
four.grid(column=0, row=3)

five = Button(window, text="5", font=("Arial", 25), command=lambda: press("5"))
five.grid(column=1, row=3)

six = Button(window, text="6", font=("Arial", 25), command=lambda: press("6"))
six.grid(column=2, row=3)

one = Button(window, text="1", font=("Arial", 25), command=lambda: press("1"))
one.grid(column=0, row=4)

two = Button(window, text="2", font=("Arial", 25), command=lambda: press("2"))
two.grid(column=1, row=4)

three = Button(window, text="3", font=("Arial", 25), command=lambda: press("3"))
three.grid(column=2, row=4)

plus = Button(window, text="+", font=("Arial", 25), command=lambda: press("+"))
plus.grid(column=0, row=5)

minus = Button(window, text="-", font=("Arial", 25), command=lambda: press("-"))
minus.grid(column=1, row=5)

by = Button(window, text="*", font=("Arial", 25), command=lambda: press("*"))
by.grid(column=2, row=5)

divide = Button(window, text="/", font=("Arial", 25), command=lambda: press("/"))
divide.grid(column=0, row=6)

power = Button(window, text="^", font=("Arial", 25), command=lambda: press("**"))
power.grid(column=1, row=6)

sqrt = Button(window, text="√", font=("Arial", 25), command=lambda: press("√"))
sqrt.grid(column=2, row=6)

phi = Button(window, text="π", font=("Arial", 25), command=lambda: press("pi"))
phi.grid(column=0, row=7)

parenthesis1 = Button(window, text="(", font=("Arial", 25), command=lambda: press("("))
parenthesis1.grid(column=1, row=7)

parenthesis2 = Button(window, text=")", font=("Arial", 25), command=lambda: press(")"))
parenthesis2.grid(column=2, row=7)

zero = Button(window, text="0", font=("Arial", 25), command=lambda: press("0"))
zero.grid(column=0, row=8)

floating = Button(window, text="DEL", font=("Arial", 25), command=lambda: press("D"))
floating.grid(column=1, row=8)

variable = Button(window, text="x", font=("Arial", 25), command=lambda: press("x"))
variable.grid(column=2, row=8)

calculate_result = Button(window, text="Calculate!", font=("Arial", 22), command=lambda: calculate(equation))
calculate_result.grid(row=9, column=1)

# Main loop (displays the program all the time)
window.mainloop()
