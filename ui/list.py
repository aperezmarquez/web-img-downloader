import tkinter as tk

box = None
img_sub = None

def update_subject(new_sub):
    new_sub.subscribe(lambda x: add_button(x))

def on_select(event):
    global img_sub
    widget = event.widget
    selection = widget.curselection()

    value = widget.get(selection) if selection else None

    if value and img_sub:
        filename = ("assets/" + str(value) + ".png")
        img_sub.change_img(filename)

def add_button(text):
    global box
    box.insert(tk.END, text)

def add_scrollbar(root):
    global box
    scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    box.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=box.yview)

def list_box(root, subject, width, height):
    global img_sub, box
    img_sub = subject

    box_frame = tk.Frame(root)
    box_frame.pack(side=tk.LEFT, padx=80, pady=10)

    box = tk.Listbox(box_frame, width=50, height=50)
    box.pack(side=tk.LEFT)

    # Scrollbar for the list, in case there are too many imgs
    add_scrollbar(box_frame)

    box.bind("<<ListboxSelect>>", on_select)
