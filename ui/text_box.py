import tkinter as tk

# TKINTER TEXT BOX ENTRY
# - Params:
#   - root: the window root
#   - width: the width of the window
#   - height: the height of the window
# - Return:
#   - entry: the entry widget
# - Description: Creates the text box entry with a placeholder
def box(root, width, height):
    entry = tk.Entry(root, width=width)
    entry.pack(padx=int(width*0.3), pady=10)
    entry.insert(0, "Inserte la url de la web")
    
    # Placeholder that automaticly removes when selected
    def placeholder(event):
        entry.delete(0, tk.END)

        entry.unbind('<Button-1>', click)


    click = entry.bind('<Button-1>', placeholder)

    return entry
