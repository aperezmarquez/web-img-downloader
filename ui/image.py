import tkinter as tk
from PIL import Image, ImageTk

def image_loader(root, width, height):
    loader_frame = tk.Frame(root)
    loader_frame.pack(side=tk.RIGHT, padx=10, pady=10)
    
    image = Image.open("../assets/placeholder.png")
    photo = ImageTk.PhotoImage(image)

    image_canvas = tk.Canvas(loader_frame, width=width-70, height=height)
    image_canvas.pack()

    image_canvas.create_image(width/2, height/2, anchor=tk.SE, image=photo)
    image_canvas.image = photo
