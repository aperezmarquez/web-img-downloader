import tkinter as tk

def box(root, width, height):
    entry = tk.Entry(root, width=width)
    entry.pack(padx=int(width*0.3), pady=10)
    entry.insert(0, "Inserte la url de la web")
    
    def placeholder(event):
        entry.delete(0, tk.END)

        entry.unbind('<Button-1>', click)


    click = entry.bind('<Button-1>', placeholder)
