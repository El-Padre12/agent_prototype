from openai import OpenAI
import os
from dotenv import load_dotenv

# load enviorment variables
load_dotenv()

# create an instance of openai
openai_client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# function that generates text based on prompt, ai model, and system prompt
def generate_text_basic(prompt: str, model = 'ai-model', system_prompt: str='You are a helpful AI assistant'):
    response = openai_client.chat.completions.create(
        model=model,
        messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': prompt}
            ]
        )
    
    return response.choices[0].message.content