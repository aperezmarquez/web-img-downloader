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

def add_scrollbar(root, box):
    scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    box.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=box.yview)

def list_box(root, width, height):
    box_frame = tk.Frame(root)
    box_frame.pack(side=tk.LEFT, padx=10, pady=10)

    box = tk.Listbox(box_frame, width=50, height=50)
    box.pack(side=tk.LEFT)

    # Scrollbar for the list, in case there are too many imgs
    add_scrollbar(box_frame, box)

    # Code that detects when img is downloaded and calls add_button with the name of the file
    add_button(root, box, "Button")
    add_button(root, box, "Button2")
    add_button(root, box, "Button3")

    box.bind("<<ListboxSelect>>", on_select)
