import aiohttp 
import asyncio 
from bs4 import BeautifulSoup

# WEB IMAGE DETECTOR
# - Params: 
#   - url: website url given by the user
# - Return: 
#   - image_urls: Array with the image urls
#   - image_alts: Array with the image alts
# - Description: Extracts the images html from the url.
async def get_web_images(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            
            # This library lets you convert the html text to a soup object so we can use functions as find_all or get
            soup = BeautifulSoup(html, "html.parser")
            images = soup.find_all('img')
            image_urls = [img.get('src') for img in images]
            image_alts = [img.get('alt') for img in images]

            return image_urls, image_alts
