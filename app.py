import database
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import font


def clear_frame():
    for widget in root.winfo_children():
        widget.destroy()


def prompt_add_album():
    name = album_name_entry.get()
    top_songs = top_songs_entry.get()
    rating = rating_entry.get()

    if name and top_songs and rating:
        try:
            rating = int(rating)
            if 0 <= rating <= 100:
                database.add_album(connection, name, top_songs, rating)
                status_label.config(text=f"Album '{name}' added successfully!")
                prompt_clear_entries()
            else:
                status_label.config(text="Rating must be between 0 and 100.")
        except ValueError:
            status_label.config(text="Rating must be an integer.")
    else:
        status_label.config(text="All fields must be filled.")


def prompt_see_all_albums():
    albums = database.get_all_albums(connection)
    result_text = "\n".join([f"{album[1]} ({album[2]}) - {album[3]}/100" for album in albums])
    result_display.config(state=NORMAL)
    result_display.delete(1.0, END)
    result_display.insert(INSERT, result_text)
    result_display.config(state=DISABLED)


def prompt_find_album():
    name = album_name_entry.get()
    albums = database.get_albums_by_name(connection, name)
    result_text = "\n".join([f"{album[1]} ({album[2]}) - {album[3]}/100" for album in albums])
    result_display.config(state=NORMAL)
    result_display.delete(1.0, END)
    result_display.insert(INSERT, result_text)
    result_display.config(state=DISABLED)


def prompt_find_top_songs():
    name = album_name_entry.get()
    top_songs = database.get_top_songs_of_album(connection, name)
    result_text = "\n".join([f"Top Songs: {song[2]}" for song in top_songs])
    result_display.config(state=NORMAL)
    result_display.delete(1.0, END)
    result_display.insert(INSERT, result_text)
    result_display.config(state=DISABLED)


def prompt_remove_album():
    name = album_name_entry.get()
    if database.remove_album(connection, name):
        status_label.config(text=f"Album '{name}' removed successfully!")
    else:
        status_label.config(text=f"Album '{name}' not found.")


def prompt_order_album_by_name():
    albums = database.order_album(connection)
    result_text = "\n".join([f"{album[1]} ({album[2]}) - {album[3]}/100" for album in albums])
    result_display.config(state=NORMAL)
    result_display.delete(1.0, END)
    result_display.insert(INSERT, result_text)
    result_display.config(state=DISABLED)


def prompt_clear_entries():
    album_name_entry.delete(0, END)
    top_songs_entry.delete(0, END)
    rating_entry.delete(0, END)


def update_font(*args):
    selected_font = font_var.get()
    label.config(font=(selected_font, 16))
    for button in buttons:
        button.config(font=(selected_font, 10))


# Initialize database connection
connection = database.connect()
database.create_tables(connection)

# Set up Tkinter window

root = tk.Tk()
root.title("Rock and Metal Album's App")
root.geometry('700x800')

fonts = list(font.families())
# Create and place widget

Label(root, text="&Rock And Metal Albums&", font=16).pack(pady=10),
Label(root, text="Album Name And Artist:").pack(pady=5)
album_name_entry = Entry(root, width=50)
album_name_entry.pack(pady=5)


Label(root, text="Top 5 Songs (comma separated):").pack(pady=5)
top_songs_entry = Entry(root, width=50)
top_songs_entry.pack(pady=5)


Label(root, text="Rating (0-100):").pack(pady=5)
rating_entry = Entry(root, width=50)
rating_entry.pack(pady=5)


# fonts = list(font.families())
font_var = tk.StringVar(value=fonts[0])

buttons = [
    Button(root, text="Add Album", command=prompt_add_album, font=(fonts[0], 10)),
    Button(root, text="See All Albums", command=prompt_see_all_albums, font=(fonts[0], 10)),
    Button(root, text="Find Album", command=prompt_find_album, font=(fonts[0], 10)),
    Button(root, text="Find Top Songs", command=prompt_find_top_songs, font=(fonts[0], 10)),
    Button(root, text="Remove Album", command=prompt_remove_album, font=(fonts[0], 10)),
    Button(root, text="Order Albums by Name", command=prompt_order_album_by_name, font=(fonts[0], 10)),
]

for button in buttons:
    button.pack(pady=5)

label = tk.Label(root, text="Sample Text", font=(fonts[0], 16))
label.pack(pady=20)
font_menu = tk.OptionMenu(root, font_var, *fonts)
font_menu.pack()
font_var.trace("w", update_font)

status_label = Label(root, text="", fg="red")
status_label.pack(pady=5)

result_display = Text(root, width=60, height=10, wrap=WORD, state=DISABLED)
result_display.pack(pady=10)

# Start Tkinter event loop
root.mainloop()
