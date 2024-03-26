from tqdm import tqdm
from ollama import pull
import asyncio

async def pull_and_track_progress(model):
    current_digest, bars = '', {}
    async for progress in pull(model, stream=True):
        digest = progress.get('digest', '')

        if digest != current_digest and current_digest in bars:
            bars[current_digest].close()

        if not digest:
            print(progress.get('status'))
            continue

        if digest not in bars and (total := progress.get('total')):
            bars[digest] = tqdm(total=total, desc=f'pulling {digest[7:19]}', unit='B', unit_scale=True)

        if completed := progress.get('completed'):
            bars[digest].update(completed - bars[digest].n)

        current_digest = digest

async def main():
    model = 'mistral'

    try:
        await pull_and_track_progress(model)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        for bar in bars.values():
            bar.close()

if __name__ == "__main__":
    asyncio.run(main())
