import tkinter as tk
from utils.image_memory import get_images

box = None
img_sub = None

# SUBJECT SUBSCRIPTION
# - Params:
#   - new_sub: the subject to subscribe
# - Return: None
# - Description: Subscribes to the new subject and calls to add a new button with the notified value
def update_subject(new_sub):
    new_sub.subscribe(lambda x: add_button(x))

# IMAGE NAME SELECTION
# - Params:
#   - event: the event triggered when an item is selected
# - Return: None
# - Description: Gets the selected value from the listbox and changes it inside the subject
def on_select(event):
    global img_sub
    widget = event.widget
    selection = widget.curselection()

    value = widget.get(selection) if selection else None

    if value and img_sub:
        img = get_images()[value]
        img_sub.change_img(img)

# BUTTON ADDER
# - Params: 
#   - text: the text shown in the button field
# - Return: None
# - Description: Adds a new button to the listbox with the given name of the img
def add_button(text):
    global box
    box.insert(tk.END, text)

# LIST SCROLLBAR
# - Params:
#   - root: the window root
# - Return: None
# - Description: Adds a scrollbar to the listbox so you can see all the names added
def add_scrollbar(root):
    global box
    scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    box.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=box.yview)

# NAMES LIST
# - Params: 
#   - root: the window root
#   - subject: the subject that notifies when an img is selected
#   - width: the width of the window
#   - height: the height of the window
# - Return: None
# - Description: Creates a frame with a listbox to show the names of the imgs downloaded into memory
def list_box(root, subject, width, height):
    global img_sub, box
    img_sub = subject

    box_frame = tk.Frame(root)
    box_frame.pack(side=tk.LEFT, padx=80, pady=10)

    box = tk.Listbox(box_frame, width=50, height=50)
    box.pack(side=tk.LEFT)

    # Scrollbar for the list, in case there are too many imgs
    add_scrollbar(box_frame)
    
    # Every time a new list item is selected it updates the img subject to show it in the canvas
    box.bind("<<ListboxSelect>>", on_select)
