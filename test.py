import tkinter as tk
from tkinter import font


# Function to update the font of a label
def update_font(*args):
    selected_font = font_var.get()
    label.config(font=(selected_font, 16))  # Update font with selected value


# Create main window
root = tk.Tk()
root.title("Font Selector")


# List of available fonts
fonts = list(font.families())


# StringVar to hold the selected font
font_var = tk.StringVar(value=fonts[0])


# Create a label to display text
label = tk.Label(root, text="Sample Text", font=(fonts[0], 16))
label.pack(pady=20)


# Create OptionMenu for font selection
font_menu = tk.OptionMenu(root, font_var, *fonts)
font_menu.pack()


# Trace changes in the font selection
font_var.trace("w", update_font)


# Run the Tkinter event loop
root.mainloop()
