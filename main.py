from tkinter import Tk, Label, Button

# Define the window
window = Tk()
window.title("Tkinter Advanced Calculator")
window.geometry("500x750")
window.resizable(False, False)

# Widgets
title = Label(window, text="Tkinter Calculus Calculator")
title.grid(columnspan=2)

seven = Button(window, text="7")
seven.grid(column=0, row=2)

eight = Button(window, text="8")
eight.grid(column=1, row=2)

nine = Button(window, text="9")
nine.grid(column=2, row=2)

four = Button(window, text="4")
four.grid(column=0, row=3)

five = Button(window, text="5")
five.grid(column=1, row=3)

six = Button(window, text="6")
six.grid(column=2, row=3)

one = Button(window, text="1")
one.grid(column=0, row=4)

two = Button(window, text="2")
two.grid(column=1, row=4)

three = Button(window, text="3")
three.grid(column=2, row=4)

calculate_result = Button(window, text="Calc")
calculate_result.grid(row=8, column=2)

# Main loop (displays the program all the time)
window.mainloop()
