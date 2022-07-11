from tkinter import Tk, Label, Button

# Define the window
window = Tk()
window.title("Tkinter Advanced Calculator")
window.geometry("500x650")
window.resizable(False, False)

# Widgets
title = Label(window, text="Tkinter Calculus Calculator", font=("Arial", 25))
title.grid(columnspan=2)

seven = Button(window, text="7", font=("Arial", 25))
seven.grid(column=0, row=2)

eight = Button(window, text="8", font=("Arial", 25))
eight.grid(column=1, row=2)

nine = Button(window, text="9", font=("Arial", 25))
nine.grid(column=2, row=2)

four = Button(window, text="4", font=("Arial", 25))
four.grid(column=0, row=3)

five = Button(window, text="5", font=("Arial", 25))
five.grid(column=1, row=3)

six = Button(window, text="6", font=("Arial", 25))
six.grid(column=2, row=3)

one = Button(window, text="1", font=("Arial", 25))
one.grid(column=0, row=4)

two = Button(window, text="2", font=("Arial", 25))
two.grid(column=1, row=4)

three = Button(window, text="3", font=("Arial", 25))
three.grid(column=2, row=4)

plus = Button(window, text="+", font=("Arial", 25))
plus.grid(column=0, row=5)

minus = Button(window, text="-", font=("Arial", 25))
minus.grid(column=1, row=5)

by = Button(window, text="·", font=("Arial", 25))
by.grid(column=2, row=5)

divide = Button(window, text="/", font=("Arial", 25))
divide.grid(column=0, row=6)

power = Button(window, text="^", font=("Arial", 25))
power.grid(column=1, row=6)

sqrt = Button(window, text="√", font=("Arial", 25))
sqrt.grid(column=2, row=6)

phi = Button(window, text="π", font=("Arial", 25))
phi.grid(column=0, row=7)

parenthesis1 = Button(window, text="(", font=("Arial", 25))
parenthesis1.grid(column=1, row=7)

parenthesis2 = Button(window, text=")", font=("Arial", 25))
parenthesis2.grid(column=2, row=7)

zero = Button(window, text="0", font=("Arial", 25))
zero.grid(column=0, row=8)

floating = Button(window, text=".", font=("Arial", 25))
floating.grid(column=1, row=8)

calculate_result = Button(window, text="Calc", font=("Arial", 22))
calculate_result.grid(row=8, column=2)

# Main loop (displays the program all the time)
window.mainloop()
