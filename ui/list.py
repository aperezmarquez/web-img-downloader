import tkinter as tk

def on_select(event):
    widget = event.widget
    selection = widget.curselection()
    if selection:
        value = widget.get(selection)
        print(value)

    # Code that updates the img being loaded
    

def add_button(root, box, text):
    box.insert(tk.END, text)

def list_box(root, width, height):
    box = tk.Listbox(root, width=width, height=height)
    box.pack(padx=10, pady=10)

    # Code that detects when img is downloaded and calls add_button with the name of the file
    add_button(root, box, "Button")
    add_button(root, box, "Button2")
