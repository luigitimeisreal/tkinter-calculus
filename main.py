from tkinter import Tk, Label, Button




def press(button_text: str):
    print(button_text)


def calculate():
    print("Calculation in process. . .")


# Define the window
window = Tk()
window.title("Tkinter Advanced Calculator")
window.geometry("500x650")
window.resizable(False, False)

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

by = Button(window, text="·", font=("Arial", 25), command=lambda: press("·"))
by.grid(column=2, row=5)

divide = Button(window, text="/", font=("Arial", 25), command=lambda: press("/"))
divide.grid(column=0, row=6)

power = Button(window, text="^", font=("Arial", 25), command=lambda: press("^"))
power.grid(column=1, row=6)

sqrt = Button(window, text="√", font=("Arial", 25), command=lambda: press("√"))
sqrt.grid(column=2, row=6)

phi = Button(window, text="π", font=("Arial", 25), command=lambda: press("π"))
phi.grid(column=0, row=7)

parenthesis1 = Button(window, text="(", font=("Arial", 25), command=lambda: press("("))
parenthesis1.grid(column=1, row=7)

parenthesis2 = Button(window, text=")", font=("Arial", 25), command=lambda: press(")"))
parenthesis2.grid(column=2, row=7)

zero = Button(window, text="0", font=("Arial", 25), command=lambda: press("0"))
zero.grid(column=0, row=8)

floating = Button(window, text=".", font=("Arial", 25), command=lambda: press("."))
floating.grid(column=1, row=8)

calculate_result = Button(window, text="Calc", font=("Arial", 22), command=calculate)
calculate_result.grid(row=8, column=2)

# Main loop (displays the program all the time)
window.mainloop()
