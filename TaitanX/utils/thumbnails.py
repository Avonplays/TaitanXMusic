import os
import aiohttp
import aiofiles

from config import YOUTUBE_IMG_URL

async def gen_thumb(videoid):
    if os.path.isfile(f"cache/Alonex{videoid}_v4.png"): 
        return f"cache/Alonex{videoid}_v4.png"

    url = f"https://Alonexapi.tech/thumb?videoid={videoid}"
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status == 200:
                    f = await aiofiles.open(f"cache/Alonex{videoid}_4.png", mode="wb" ) 
                    await f.write(await resp.read()) 
                    await f.close()

        return f"cache/Alonex{videoid}_4.png"
    except Exception:
        return YOUTUBE_IMG_URL

