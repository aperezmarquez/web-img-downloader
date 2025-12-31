import tkinter as tk
from PIL import Image, ImageTk

def update_image(image_canvas, img):
    print(img)
    new_image = Image.open(img)
    
    new_image.thumbnail((image_canvas.winfo_width(), image_canvas.winfo_height()))

    new_photo = ImageTk.PhotoImage(new_image)

    image_canvas.create_image(0, 0, anchor=tk.NW, image=new_photo)
    image_canvas.image = new_photo

def image_loader(root, subject, width, height):
    loader_frame = tk.Frame(root)
    loader_frame.pack(side=tk.RIGHT, padx=10, pady=10)
    
    image = Image.open("assets/placeholder.png")
    photo = ImageTk.PhotoImage(image)

    image_canvas = tk.Canvas(loader_frame, width=width-70, height=height)
    image_canvas.pack()

    image_canvas.create_image(width/2, height/2, anchor=tk.SE, image=photo)
    image_canvas.image = photo

    # We subscribe to the subject, here every time we select another img it updates
    subject.subscribe(lambda img: update_image(image_canvas, img))
