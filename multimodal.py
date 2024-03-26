import sys
import random
import httpx
import asyncio
from ollama import generate

async def generate_explanation(prompt, images):
    async for response in generate('llava', prompt, images=images, stream=True):
        print(response['response'], end='', flush=True)

async def main():
    latest_response = httpx.get('https://xkcd.com/info.0.json')
    latest_response.raise_for_status()
    latest_num = latest_response.json().get('num')

    if len(sys.argv) > 1:
        comic_num = int(sys.argv[1])
    else:
        comic_num = random.randint(1, latest_num)

    comic_response = httpx.get(f'https://xkcd.com/{comic_num}/info.0.json')
    comic_response.raise_for_status()

    print(f'xkcd #{comic_response.json().get("num")}: {comic_response.json().get("alt")}')
    print(f'link: https://xkcd.com/{comic_num}')
    print('---')

    raw_response = httpx.get(comic_response.json().get('img'))
    raw_response.raise_for_status()

    await generate_explanation('explain this comic:', images=[raw_response.content])

if __name__ == "__main__":
    asyncio.run(main())
