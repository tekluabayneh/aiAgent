import os
import sys
from dotenv import load_dotenv 
from google import genai 
from google.genai import types 
from functions.get_files_info import get_files_info, schema_get_files_info
 
load_dotenv()

def main():
    api_key = os.environ.get("GEMENI_API_KEY")
    client = genai.Client(api_key=api_key)
    system_prompt =  system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""


    
    if len(sys.argv) < 2:
        print("man you forgot to add propt add some man!")
        sys.exit(1)
        verbose_flag = False 

    if len(sys.argv) == 3 and sys.argv[2] == "--verbose": 
        verbose_flag = True 
        
    Prompt = sys.argv[1]
    messages = [
        types.Content(role="user", parts=[types.Part(text=Prompt)])
    ]
    available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
    ]
)
    config=types.GenerateContentConfig(
    tools=[available_functions], system_instruction=system_prompt
)

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=messages,
        config = config 

    )

    if response is None or response.usage_metadata is None: 
        print(f"response is malwormed")
        return 

    if response.function_calls: 
        print(response.function_calls)
        for function_call_part in response.function_calls:
            print("Calling function: {function_call_part.name}({function_call_part.args})")
    else: 
        print(response.text)

        
    # print(f"User Prompt:{Prompt}")
    # print(f"Prompt Tokens:{ response.usage_metadata.prompt_token_count}")
    # print(f"Response Tokens:{ response.usage_metadata.candidates_token_count}")
    # print("aI RESPONSE", response.text)
    # print(get_files_info("calculator", "pkg"))
    #
main()
