import tkinter as tk
from PIL import Image, ImageTk

# UPDATE THE CANVAS IMAGE
# - Params:
#   - image_canvas: the canvas to update
#   - img: the new image to show
# - Return: None
# - Description: Using the new image, updates the canvas image
def update_image(image_canvas, img):    
    new_image = img.copy()
    new_image.thumbnail((image_canvas.winfo_width(), image_canvas.winfo_height()))
    new_photo = ImageTk.PhotoImage(new_image)

    image_canvas.create_image(0, 0, anchor=tk.NW, image=new_photo)
    image_canvas.image = new_photo

# IMAGE LOADER
# - Params:
#   - root: the window root
#   - subject: the image subject that notifies when the image is changed
#   - width: the width of the window
#   - height: the height of the window
# - Return: None
# - Description: Creates a frame with a canvas to show the selected image with a fixed size
def image_loader(root, subject, width, height):
    loader_frame = tk.Frame(root)
    loader_frame.pack(side=tk.RIGHT, padx=10, pady=10)
    
    image = Image.open("assets/placeholder.png")
    photo = ImageTk.PhotoImage(image)

    image_canvas = tk.Canvas(loader_frame, width=width-70, height=height)
    image_canvas.pack()

    image_canvas.create_image(width/2, height/2, anchor=tk.SE, image=photo)
    image_canvas.image = photo

    # Every time a new image is selected in the list it updates the canvas img
    subject.subscribe(lambda img: update_image(image_canvas, img))
