import tkinter as tk
from PIL import Image, ImageTk

def update_image(image_canvas):
    # Code to get notify of a change (new image selected)
    image_canvas.delete("all")

    new_image = Image.open("../assets/placeholder.png") # Change this with the url of the new selected img
    new_photo = ImageTk.PhotoImage(new_image)

    image_canvas.create_image(0, 0, anchor=tk.NW, image=new_photo)
    image_canvas.image = new_photo

def image_loader(root, width, height):
    loader_frame = tk.Frame(root)
    loader_frame.pack(side=tk.RIGHT, padx=10, pady=10)
    
    image = Image.open("../assets/placeholder.png")
    photo = ImageTk.PhotoImage(image)

    image_canvas = tk.Canvas(loader_frame, width=width-70, height=height)
    image_canvas.pack()

    image_canvas.create_image(width/2, height/2, anchor=tk.SE, image=photo)
    image_canvas.image = photo
