import sys
import asyncio
from ollama import create

async def create_model(model_name, file_path):
    modelfile = f"FROM {file_path}"
    async for response in create(model=model_name, modelfile=modelfile, stream=True):
        print(response['status'])

async def main():
    args = sys.argv[1:]
    if len(args) != 2:
        print('Usage: python main.py <name> <filepath>')
        sys.exit(1)

    model_name, file_path = args

    try:
        await create_model(model_name, file_path)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(main())
