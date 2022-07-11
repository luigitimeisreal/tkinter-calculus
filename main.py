from tkinter import Tk, Label, Button, Entry

equation = ""


def press(button_text: str):
    print(button_text)


def calculate():
    print(equation)


# Define the window
window = Tk()
window.title("Tkinter Advanced Calculator")
window.geometry("500x650")
window.resizable(False, False)

# Widgets
title = Label(window, text="Tkinter Calculus Calculator", font=("Arial", 25))
title.grid(row=0, columnspan=2)

current_expression = Entry(window, font=("Arial", 25) ,textvariable=equation)
current_expression.grid(row=1, columnspan=2)

seven = Button(window, text="7", font=("Arial", 25), command=press("7"))
seven.grid(column=0, row=2)

eight = Button(window, text="8", font=("Arial", 25), command=press("8"))
eight.grid(column=1, row=2)

nine = Button(window, text="9", font=("Arial", 25), command=press("9"))
nine.grid(column=2, row=2)

four = Button(window, text="4", font=("Arial", 25), command=press("7"))
four.grid(column=0, row=3)

five = Button(window, text="5", font=("Arial", 25), command=press("5"))
five.grid(column=1, row=3)

six = Button(window, text="6", font=("Arial", 25), command=press("6"))
six.grid(column=2, row=3)

one = Button(window, text="1", font=("Arial", 25), command=press("1"))
one.grid(column=0, row=4)

two = Button(window, text="2", font=("Arial", 25), command=press("2"))
two.grid(column=1, row=4)

three = Button(window, text="3", font=("Arial", 25), command=press("3"))
three.grid(column=2, row=4)

plus = Button(window, text="+", font=("Arial", 25), command=press("+"))
plus.grid(column=0, row=5)

minus = Button(window, text="-", font=("Arial", 25), command=press("-"))
minus.grid(column=1, row=5)

by = Button(window, text="·", font=("Arial", 25), command=press("·"))
by.grid(column=2, row=5)

divide = Button(window, text="/", font=("Arial", 25), command=press("/"))
divide.grid(column=0, row=6)

power = Button(window, text="^", font=("Arial", 25), command=press("^"))
power.grid(column=1, row=6)

sqrt = Button(window, text="√", font=("Arial", 25), command=press("√"))
sqrt.grid(column=2, row=6)

phi = Button(window, text="π", font=("Arial", 25), command=press("π"))
phi.grid(column=0, row=7)

parenthesis1 = Button(window, text="(", font=("Arial", 25), command=press("("))
parenthesis1.grid(column=1, row=7)

parenthesis2 = Button(window, text=")", font=("Arial", 25), command=press(")"))
parenthesis2.grid(column=2, row=7)

zero = Button(window, text="0", font=("Arial", 25), command=press("0"))
zero.grid(column=0, row=8)

floating = Button(window, text=".", font=("Arial", 25), command=press("."))
floating.grid(column=1, row=8)

calculate_result = Button(window, text="Calc", font=("Arial", 22), command=calculate)
calculate_result.grid(row=8, column=2)

# Main loop (displays the program all the time)
window.mainloop()
