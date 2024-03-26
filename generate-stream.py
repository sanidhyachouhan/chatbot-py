from ollama import generate
import asyncio

async def generate_response(model, prompt):
    async for part in generate(model, prompt, stream=True):
        yield part['response']

async def main():
    model = 'mistral'
    prompt = 'Why is the sky blue?'

    try:
        async for response_part in generate_response(model, prompt):
            print(response_part, end='', flush=True)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(main())
