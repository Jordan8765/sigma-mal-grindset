import tkinter as tk
from tkinter import messagebox

# Function to be called when an option is selected
def option_selected(selected_option):
    messagebox.showinfo("Selected Option", f"You selected: {selected_option}")

# Create the main window
root = tk.Tk()
root.title("Dropdown Menu Example")

# Options for the dropdown
options = ["Option 1", "Option 2", "Option 3"]

# Variable to hold the selected option
selected_option = tk.StringVar(root)
selected_option.set(options[0])  # Set default option

# Create the dropdown (OptionMenu)
dropdown = tk.OptionMenu(root, selected_option, *options, command=option_selected)
dropdown.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()