import aiohttp 
import asyncio 
from bs4 import BeautifulSoup

async def get_web_images(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            
            soup = BeautifulSoup(html, "html.parser")
            images = soup.find_all('img')
            image_urls = [img.get('src') for img in images]
            image_alts = [img.get('alt') for img in images]

            return image_urls, image_alts
