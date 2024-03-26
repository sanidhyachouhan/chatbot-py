from ollama import generate
import asyncio

async def generate_response(model, prompt):
    response = await generate(model, prompt)
    return response['response']

async def main():
    model = 'mistral'
    prompt = 'Why is the sky blue?'

    try:
        response = await generate_response(model, prompt)
        print(response)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(main())
