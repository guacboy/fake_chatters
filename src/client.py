from dotenv import load_dotenv
from openai import OpenAI
import os

# load the .env file
load_dotenv()

client = OpenAI(
    # this is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

class Client():
    def openai():
        chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "assistant",
                "content": "",
            }
        ],
        model="gpt-3.5-turbo",
        )
        
        return chat_completion

print(Client.openai().choices[0].message.content)