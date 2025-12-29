import tkinter as tk

def on_button_click(text):
    # Code that updates de img being loaded
    print("Click", text)

def add_button(root, text):
    btn = tk.Button(
            root,
            text=text,
            command=lambda: on_button_click(text)
    )
    btn.pack(padx=20, pady=5)

def list_box(root, width, height):
    # Code that detects when img is downloaded and calls add_button with the name of the file
    add_button(root, "Button")
    add_button(root, "Button2")
