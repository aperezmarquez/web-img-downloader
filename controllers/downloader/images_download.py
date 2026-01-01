import os
import aiohttp
import asyncio
import cairosvg
from urllib.parse import urlparse
from io import BytesIO
from PIL import Image
from controllers.downloader.get_web_images import get_web_images
from controllers.observables.alts import AltsSubject
from ui.list import update_subject
from utils.image_memory import add_image

alts_obs = AltsSubject()
session = None
pending_downloads = 0

# CREATES A SESSION IF THERE IS NONE
# - Params: None
# - Return: None
# - Description: Ensures that there is a session, if there is none it creates one and saves it in a global variable
async def ensure_session():
    global session
    if session is None:
        session = aiohttp.ClientSession()

# SESSION CLOSING
# - Params: None
# - Return: None
# - Description: Checks if there is no pending downloads, if all the url images are downloaded, it closes the session
async def maybe_close_session():
    global session
    if pending_downloads == 0 and session:
        await session.close()
        session = None

# IMAGE FILENAME GETTER
# - Params:
#   - url: the given url
# - Return:
#   - filename: using the url gets the filename at the end of the path and splits it to get rid of the extension
def filename_from_url(url):
    return os.path.basename(urlparse(url).path).split(".")[0] or "image"

# IMAGE DOWNLOADER
# - Params: 
#   - url: the url of the image
#   - filename: the name of the image
# - Return: None
# - Description: Using an aiohttp session downloads the image and saves it in memory using BytesIO
async def download(url, filename):
    global session, alts_obs, pending_downloads, memory_images

    async with session.get(url) as response:
        if response.status != 200:
            return
        
        # Gets the image from the response and saves it in memory
        data = await response.read()
        img_bytes = BytesIO(data)
        img = Image.open(img_bytes)
        # Adds the image to the memory variable using the filename
        add_image(filename, img)

        # When the img is downloaded, we update the list of alts
        alts_obs.add_alt(filename)

    pending_downloads -= 1
    await maybe_close_session()

# CALLS TO DOWNLOAD EACH IMAGE
# - Params:
#   - image_urls: the urls for every image in the given url
#   - image_alts: the list with the names of the images
# - Return:
#   - image_alts: the list with the names of the images
# - Description: Gets the images names from the alt or the url and calls the download function for each image
async def download_images(image_urls, image_alts):
    global pending_downloads
    
    # Updates the observable object being used by the list in TkInter app
    update_subject(alts_obs)
    # CHecks for the session and creates it if needed
    await ensure_session()

    for i, url in enumerate(image_urls):
        if not url:
            continue
        
        # Gets the filename from the alt if it exists, if not it gets the name from the url
        if not image_alts[i]:
            image_alts[i] = filename_from_url(url)

        image_alts[i] = image_alts[i].replace(" ", "-") # Changes the spaces in the filename to -
        
        # Creates a task in asyncio to download each image
        asyncio.create_task(download(url, image_alts[i]))

    return image_alts

# MAIN FUNCTION
# - Params:
#   - url: the url given by the user
# - Return:
#   - alts: the list with the names of the images in memory
# - Description: Gets the images from the url and calls a function to download them and get their names (alts)
async def download_url(url):
    urls, alts = await get_web_images(url)
    alts = await download_images(urls, alts)

    return alts
