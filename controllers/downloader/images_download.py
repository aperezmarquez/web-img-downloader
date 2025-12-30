import os
import aiohttp
import asyncio
import cairosvg
from urllib.parse import urlparse
from controllers.downloader.get_web_images import get_web_images

def filename_from_url(url):
    return os.path.basename(urlparse(url).path).split(".")[0] or "image"

async def download(session, url, filename):
    async with session.get(url) as response:
        if response.status != 200:
            return
        
        data = await response.read()

        if url.lower().endswith(".svg"):
            cairosvg.svg2png(bytestring=data, write_to=f"assets/{filename}.png")
            return
        
        with open(f"assets/{filename}.png", "wb") as f:
            f.write(data)

async def download_images(image_urls, image_alts):
    print("URLs", image_urls)
    print("Alts", image_alts)

    async with aiohttp.ClientSession() as session:
        tasks = []
        for i, url in enumerate(image_urls):
            if image_alts[i] is None or len(image_alts[i]) == 0 or len(image_alts[i]) > 10:
                image_alts[i] = filename_from_url(url)

            image_alts[i] = image_alts[i].replace(" ", "-")
            tasks.append(asyncio.create_task(download(session, url, image_alts[i])))

        await asyncio.gather(*tasks)

    return image_alts

async def download_url(url):
    urls, alts = await get_web_images(url)
    alts = await download_images(urls, alts)

    return alts
