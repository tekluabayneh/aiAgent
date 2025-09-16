import os
import sys
from dotenv import load_dotenv 
from google import genai 
from google.genai import types 
from functions.get_files_info import get_files_info, schema_get_files_info
from functions.get_file_content import get_file_content, schema_get_file_content 
from functions.write_file import write_file ,schema_write_file_content 
from functions.run_python import run_python_file,schema_run_python_file 

from call_function import call_function
load_dotenv()

def main():
    api_key = os.environ.get("GEMENI_API_KEY")
    client = genai.Client(api_key=api_key)

    system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan.
You can perform the following operations:

- List files and directories
- Read the content of a file
- Write a file (create or update)
- Run a python file with optional arguments

⚠️ All paths are relative to the working directory.
⚠️ You don’t need to include working_directory in your calls.
"""

    if len(sys.argv) < 2:
        print("man you forgot to add prompt add some man!")
        sys.exit(1)

    verbose_flag = False
    if len(sys.argv) == 3 and sys.argv[2] == "--verbose":
        verbose_flag = True

    user_prompt = sys.argv[1]
    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]

    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_write_file_content,
            schema_run_python_file,
            schema_get_file_content
        ]
    )

    config = types.GenerateContentConfig(
        tools=[available_functions],
        system_instruction=system_prompt
    )

    # 🔁 Loop until model gives plain text
    while True:
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=messages,
            config=config
        )

        if response is None or response.usage_metadata is None:
            print("response is malformed")
            sys.exit(1)

        if response.function_calls:
            for function_call_part in response.function_calls:
                print(f"Calling function: {function_call_part.name}({function_call_part.args})")
                result = call_function(function_call_part, verbose_flag)

                # append result back to conversation
                messages.append(
                    types.Content(role="function", parts=[types.Part(text=str(result))])
                )
        else:
            print(response.text)
            break
 
    # print(f"User Prompt:{Prompt}")
    # print(f"Prompt Tokens:{ response.usage_metadata.prompt_token_count}")
    # print(f"Response Tokens:{ response.usage_metadata.candidates_token_count}")
    # print("aI RESPONSE", response.text)
    # print(get_files_info("calculator", "pkg"))
    #
main()
