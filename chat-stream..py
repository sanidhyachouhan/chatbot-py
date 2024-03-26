from ollama import AsyncClient

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
        print(response_content, end='', flush=True)

    # End with a newline
    print()

if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
