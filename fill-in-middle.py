from ollama import generate
import asyncio

async def generate_code_with_prefix_suffix(model, prefix, suffix, options):
    prompt = f'<PRE> {prefix} <SUF>{suffix} <MID>'
    response = await generate(model=model, prompt=prompt, options=options)
    return response['response']

async def main():
    prefix = '''def remove_non_ascii(s: str) -> str:
    """ '''
    suffix = """
    return result
    """
    model = 'codellama:7b-code'
    options = {
        'num_predict': 128,
        'temperature': 0,
        'top_p': 0.9,
        'stop': ['<EOT>'],
    }

    try:
        generated_code = await generate_code_with_prefix_suffix(model, prefix, suffix, options)
        print(generated_code)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(main())
