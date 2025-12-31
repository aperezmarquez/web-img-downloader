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

def get_images():
    global memory_images
    return memory_images

async def ensure_session():
    global session
    if session is None:
        session = aiohttp.ClientSession()

async def maybe_close_session():
    global session
    if pending_downloads == 0 and session:
        await session.close()
        session = None

def filename_from_url(url):
    return os.path.basename(urlparse(url).path).split(".")[0] or "image"

async def download(url, filename):
    global session, alts_obs, pending_downloads, memory_images

    async with session.get(url) as response:
        if response.status != 200:
            return
    
        data = await response.read()
        img_bytes = BytesIO(data)
        img = Image.open(img_bytes)
        add_image(filename, img)

        # When the img is downloaded, we update the list of alts
        alts_obs.add_alt(filename)

    pending_downloads -= 1
    await maybe_close_session()

async def download_images(image_urls, image_alts):
    global pending_downloads

    update_subject(alts_obs)
    
    await ensure_session()

    for i, url in enumerate(image_urls):
        if not url:
            continue

        alt = image_alts[i]
        if not alt or len(alt) > 10:
            alt = filename_from_url(url)

        alt = alt.replace(" ", "-")
        image_alts[i] = alt

        asyncio.create_task(download(url, alt))

    return image_alts

async def download_url(url):
    urls, alts = await get_web_images(url)
    alts = await download_images(urls, alts)

    return alts
