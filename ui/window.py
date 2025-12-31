import asyncio
import tkinter as tk
from ui.text_box import box
from ui.list import list_box
from ui.image import image_loader
from controllers.observables.image_selection import ImageSubject
from controllers.downloader.images_download import download_url

async def send_url(url):
    alts_obs = await download_url(url)

def window():
    WIDTH=1400
    HEIGHT=900
    img_sub = ImageSubject("assets/placeholder.png")

    root = tk.Tk()
    root.geometry(f"{WIDTH}x{HEIGHT}")
    root.title("Descargador de imagenes por URL")

    # Text box to insert the url
    text_box = box(root, width=WIDTH, height=HEIGHT)
    btn = tk.Button(root, text="Descargar imgs", command=lambda: asyncio.run(send_url(text_box.get())))
    btn.pack(pady=10)

    # Images downloaded frame
    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH)
    list_box(frame, img_sub, width=WIDTH, height=HEIGHT)
    image_loader(frame, img_sub, width=WIDTH, height=HEIGHT)

    root.mainloop()
