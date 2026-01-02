import asyncio
import tkinter as tk
from ui.text_box import box
from ui.list import list_box
from ui.image import image_loader
from ui.progress_bar import progress_bar
from controllers.observables.image_selection import ImageSubject
from controllers.downloader.images_download import download_url

# DOWNLOADS THE IMAGES FROM THE URL
# - Params:
#   - url: the url given by the user
#   - loop: the asyncio event loop
# - Return: None
# - Description: Creates a task in asyncio to download the images using the loop created in main.py
async def send_url(url, loop):
    loop.create_task(download_url(url))

# APP MAIN WINDOW
# - Params:
#   - root: the main root
#   - width: the width of the window
#   - height: the height of the window
#   - loop: the asyncio event loop
# - Return: None
# - Description: Creates the app window with all the elements
def window(root, width, height, loop):
    img_sub = ImageSubject("assets/placeholder.png") 

    root.geometry(f"{width}x{height}")
    root.title("Descargador de imagenes por URL")

    # App text box element for the user to insert the url
    text_box = box(root, width=width, height=height)
    btn = tk.Button(root, text="Descargar imgs", command=lambda: asyncio.run(send_url(text_box.get(), loop)))
    btn.pack(pady=10)

    # Progress bar to show the download progress
    progress_bar(root, btn)

    # Frame to select each downloaded img and show them
    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH)
    list_box(frame, img_sub, width=width, height=height)
    image_loader(frame, img_sub, width=width, height=height)
