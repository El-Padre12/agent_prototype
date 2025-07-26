from openai import OpenAI # used to interact with the openai API
import os # used to get enviorment variables "os.getenv('key')
from dotenv import load_dotenv # used to read key value pairs from .env and sets them as enviorment variables

# load enviorment variables
load_dotenv()

# create an instance of openai
openai_client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


def generate_text_basic(prompt: str, model = 'gpt-4.1-nano', system_prompt: str='You are a helpful AI assistant'):
    """
    Generates text based on prompt, ai model, and system prompt.
    Notice the parameters are static, this keeps the code straight forward and scaleable.
    Args:
        prompt (str): The user's input prompt to send to the model.
        model (str, optional): The OpenAI model to use. Defaults to 'ai-model'.
        system_prompt (str, optional): The system message to set the assistant's behavior. Defaults to 'You are a helpful AI assistant'.

    Returns:
        str: The generated text response from the model.
    """

    # send the prompt and system message to the OpenAI API and get the response object-
    # containing possible completions, stored as response
    response = openai_client.chat.completions.create(
        model=model,
        messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': prompt}
            ]
        )
    
    # response.choices is a list of possible completions; we take the first one.
    return response.choices[0].message.content