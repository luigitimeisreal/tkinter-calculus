from tkinter import Tk, Label, Button

# Define the window
window = Tk()
window.title("Tkinter Advanced Calculator")
window.geometry("500x750")
window.resizable(False, False)

# Widgets
title = Label(window, text="Tkinter Advanced Calculator")
title.grid(columnspan=3)

calculate_result = Button(window, text="Calculate")
calculate_result.grid(row=1, column=0)

# Main loop (displays the program all the time)
window.mainloop()
