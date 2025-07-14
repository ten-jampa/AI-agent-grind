from dotenv import load_dotenv
import os

load_dotenv()

gemini_api_key = os.getenv('GEMINI_API_KEY')

if __name__ == '__main__':
    print(f'The Gemini API key is {gemini_api_key}')