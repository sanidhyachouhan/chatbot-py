from ollama import AsyncClient
import asyncio

async def chat_with_bot(model, messages):
    async with AsyncClient() as client:
        async for response in client.chat(model=model, messages=messages, stream=True):
            yield response['message']['content']

async def main():
    messages = [
        {
            'role': 'user',
            'content': 'Why is the sky blue?',
        },
    ]

    async for response_content in chat_with_bot('mistral', messages):
        print(response_content)
        # You can add more complex processing of responses here
        if "sky" in response_content.lower():
            print("Bot: The sky appears blue because of Rayleigh scattering.")
            break  # Exit after the first response

if __name__ == "__main__":
    asyncio.run(main())
