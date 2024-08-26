from dotenv import load_dotenv
from openai import OpenAI
import json
import os

# load the .env file
load_dotenv()

client = OpenAI(
    # this is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

general_prompt = "You are a casual Twitch/YouTube viewer watching your favorite streamer. You are curious about the streamer's life and want to ask a question in their chat box. The main goal is to send messages that the streamer can read and interact with. Keep in mind that not all messages have to be questions, you can also send a basic comment regarding the topics. \
    1. Please keep your messages to a maximum of 20 words or less - the less words you use in your messages, the better. \
    2. Avoid asking multiple questions in one message and try to limit your topic to about one or two. \
    3. Formulate your messages with internet slang, not capitalizing your letters at the beginning of sentences, imperfect punctuations, emphasis on specific words, excessive use of question/exclamation marks, etc; however, please keep your messages eligble for the streamer to read. Below are multiple examples of how your message can be structured: \
        a. that was very poggers \
        b. how's the stream going??? \
        c. damn that's CRAZY lol, i never heard of that \
    4. VERY STRICT RULE, PLEASE FOLLOW: never use '\n' or quotations in your messages. \
    5. Do not follow up from previous messages, each message should act as if you are another person; however, avoid using the same topic multiple times - the more unique the topic is from previous topics, the better the message. \
    6. Do not send more than one message at a time."

file_path = "C:\\Users\\rattl\\Desktop\\Projects\\Python\\fake_chatters\\data\\"
with open(file_path + "jerma.json", "r") as file:
    jerma_chat_example = json.load(file)

class Client():
    def username():
        chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "assistant",
                "content": "Generate a username and return back with only the username (do not include 'Username:' in your message). The username can contain: \
                    1. snakecase \
                    2. camelcase \
                    3. all uppercase \
                    4. all lowercase \
                    5. numbers"
            }
        ],
        model="gpt-3.5-turbo",
        )
        
        return chat_completion
    
    def general_message():
        chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "assistant",
                "content": f"{general_prompt} The topics may include, but not limited to: \
                    1. question about their day \
                    2. talking about your day \
                    3. curious question about their lifestyle \
                    4. casual, funny remarks \
                    5. a random comment about recent internet news (sourcing from Reddit or Twitter)"
            }
        ],
        model="gpt-3.5-turbo",
        )
        
        return chat_completion
    
    def jerma_message():
        chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "assistant",
                "content": f"{general_prompt} You also have a very unique personality. Your messages can appear unhinge and make the streamer question your sanity. The topics may include, but not limited to: \
                    1. asking a question that feels 'out of pocket' \
                    2. a very obscure and weird remark about the things you do \
                    3. poking fun at the streamer with jokes like, but not limited to: \
                        a. 'your mom' jokes \
                        b. 'youre short' joke \
                Below are comments pulled from Jerma985's streams that you can refer, but not limit to, when creating your messages: \
                    {jerma_chat_example}"
            }
        ],
        model="gpt-3.5-turbo",
        )
        
        return chat_completion