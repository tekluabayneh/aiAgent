import os
import sys
from dotenv import load_dotenv 
from google import genai 
from google.genai import types 
from functions.get_files_info import get_files_info
load_dotenv()

def main():
    api_key = os.environ.get("GEMENI_API_KEY")
    client = genai.Client(api_key=api_key)

    
    if len(sys.argv) < 2:
        print("man you forgot to add propt add some man!")
        sys.exit(1)
        verbose_flag = False 

    if len(sys.argv) == 3 or sys.argv[2] == "--verbose": 
        verbose_flag = True 
        
    Prompt = sys.argv[1]
    messages = [
        types.Content(role="user", parts=[types.Part(text=Prompt)])
    ]
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=messages
    )

    print(f"User Prompt:{Prompt}")
    print(f"Prompt Tokens:{ response.usage_metadata.prompt_token_count}")
    print(f"Response Tokens:{ response.usage_metadata.candidates_token_count}")

    print("aI RESPONSE", response.text)

print(get_files_info("calculator", "pkg"))

# main()
