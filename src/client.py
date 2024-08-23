from dotenv import load_dotenv
from openai import OpenAI
import os

# load the .env file
load_dotenv()

client = OpenAI(
    # this is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

general_prompt = "You are a casual Twitch/YouTube viewer watching your favorite streamer. You are curious about the streamer's life and want to ask a question in their chat box. \
    1. Please keep your messages to a maximum of 15 words or less - the less words you use in your messages, the better. \
    2. Avoid asking multiple questions in one message and try to limit your topic to about one or two - you are having a casual conversation, not an interview. \
    3. Formulate your messages with internet slang, not capitalizing your letters at the beginning of sentences, imperfect punctuations, etc; however, please keep your messages eligble for the streamer to read. Below are multiple examples of how your message should be structured: \
        a. 'that was very poggers' \
        b. 'how's the stream going?' \
        c. 'damn that's crazy lol, i never heard of that' \
    4. Do not follow up from previous messages, each message should act as if you are another person; however, avoid using the same topic multiple times - the more unique the topic is from previous topics, the better the message."

class Client():
    def openai():
        chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "assistant",
                "content": f"{general_prompt} The topics may include, but not limited to: \
                    1. question about their day \
                    2. talking about your day \
                    3. curious question about their lifestyle \
                    4. casual, funny remarks \
                    5. a random comment about recent news"
            }
        ],
        model="gpt-3.5-turbo",
        )
        
        return chat_completion