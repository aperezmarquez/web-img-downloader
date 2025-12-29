import tkinter as tk
from ui.text_box import box
from ui.list import list_box
from ui.image import image_loader

def window():
    WIDTH=1400
    HEIGHT=900

    root = tk.Tk()
    root.geometry(f"{WIDTH}x{HEIGHT}")
    root.title("Descargador de imagenes por URL")

    # Text box to insert the url
    box(root, width=WIDTH, height=HEIGHT)

    # Images downloaded frame
    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH)
    list_box(frame, width=WIDTH, height=HEIGHT)
    image_loader(frame, width=WIDTH, height=HEIGHT)

    root.mainloop()
