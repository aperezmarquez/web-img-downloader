import tkinter as tk
from text_box import box
from list import list_box
from image import image_loader

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
