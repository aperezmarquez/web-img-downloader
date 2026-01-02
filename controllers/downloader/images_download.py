import os
import aiohttp
import asyncio
import cairosvg
from urllib.parse import urlparse
from io import BytesIO
from PIL import Image
from controllers.downloader.get_web_images import get_web_images
from controllers.observables.alts import AltsSubject
from controllers.observables.progress_download import ProgressSubject
from ui.list import update_subject
from ui.progress_bar import update_progress_sub
from utils.image_memory import add_image

alts_obs = AltsSubject()
session = None
pending_downloads = 0
progress_sub = None

# CREATES A SESSION IF THERE IS NONE
# - Params: None
# - Return: None
# - Description: Ensures there is a session so the code can proceed correctly
async def ensure_session():
    global session
    if session is None:
        session = aiohttp.ClientSession()

# SESSION CLOSING
# - Params: None
# - Return: None
# - Description: Close the aiohttp sessio if there are no pending downloads
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
# - Description: In case there is no alt given, gets the img name from the url
def filename_from_url(url):
    return os.path.basename(urlparse(url).path).split(".")[0] or "image"

# IMAGE DOWNLOADER
# - Params: 
#   - url: the url of the image
#   - filename: the name of the image
# - Return: None
# - Description: Using an aiohttp session downloads the image and saves it in memory using BytesIO to show them in the TkInter app
async def download(url, filename):
    global session, alts_obs, pending_downloads, memory_images, progress_sub

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
    progress_sub.update_progress(pending_downloads)
    
    await maybe_close_session()

# CALLS TO DOWNLOAD EACH IMAGE
# - Params:
#   - image_urls: the urls for every image in the given url
#   - image_alts: the list with the names of the images
# - Return:
#   - image_alts: the list with the names of the images
# - Description: Using the image names, downloads and saves each img in memory calling download()
async def download_images(image_urls, image_alts):
    global pending_downloads
    
    # Updates the observable object being used by the list to show the names of each image
    update_subject(alts_obs)
    # Creates a session to execute all the downloads
    await ensure_session()

    for i, url in enumerate(image_urls):
        if not url:
            continue
        
        # Gets a name for the image to save it in memory
        if not image_alts[i]:
            image_alts[i] = filename_from_url(url)

        image_alts[i] = image_alts[i].replace(" ", "-") # Prepares the name to download it locally with no problems
        
        # Creates an asyncio task to download the images inside of the loop created in the main file
        asyncio.create_task(download(url, image_alts[i]))
        pending_downloads += 1

    return image_alts

# MAIN FUNCTION
# - Params:
#   - url: the url given by the user
# - Return:
#   - alts: the list with the names of the images in memory
# - Description: Gets the images from the url and calls a function to download them and get their names (alts)
async def download_url(url):
    global progress_sub
    urls, alts = await get_web_images(url)
    progress_sub = ProgressSubject(len(urls))
    update_progress_sub(progress_sub)

    alts = await download_images(urls, alts)

    return alts
