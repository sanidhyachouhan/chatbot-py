import shutil
import asyncio
import argparse

import ollama

async def speak(speaker, content):
    if speaker:
        p = await asyncio.create_subprocess_exec(speaker, content)
        await p.communicate()

async def main():
    parser = argparse.ArgumentParser(description="Enhanced Chatbot with Text-to-Speech")
    parser.add_argument('--speak', action='store_true', help="Enable text-to-speech functionality")
    parser.add_argument('--voice', default='default', choices=['default', 'male', 'female'], help="Select voice for text-to-speech")
    args = parser.parse_args()

    speaker = None
    if args.speak:
        available_engines = {
            'say': {'default': '-v Samantha', 'male': '-v Alex', 'female': '-v Samantha'},
            'espeak': {'default': '', 'male': '-ven+m3', 'female': '-ven+f3'}
        }
        for engine, options in available_engines.items():
            if engine in shutil.which(engine):
                speaker = f"{engine} {options[args.voice]}"
                break

    client = ollama.AsyncClient()

    messages = []

    try:
        while True:
            if content_in := input('>>> '):
                messages.append({'role': 'user', 'content': content_in})

                content_out = ''
                message = {'role': 'assistant', 'content': ''}
                async for response in await client.chat(model='enhanced', messages=messages, stream=True):
                    if response['done']:
                        messages.append(message)

                    content = response['message']['content']
                    print(content, end='', flush=True)

                    content_out += content
                    if content in ['.', '!', '?', '\n']:
                        await speak(speaker, content_out)
                        content_out = ''

                    message['content'] += content

                if content_out:
                    await speak(speaker, content_out)
                print()

    except (KeyboardInterrupt, EOFError):
        print("\nExiting...")

if __name__ == "__main__":
    asyncio.run(main())
