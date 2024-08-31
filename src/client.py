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

data_file_path = "C:\\Users\\rattl\\Desktop\\Projects\\Python\\fake_chatters\\data\\"
with open(data_file_path + "topic.json", "r") as file:
    topic_example = json.load(file)
    
with open(data_file_path + "jerma.json", "r") as file:
    jerma_chat_example = json.load(file)

with open(data_file_path + "nl.json", "r") as file:
    nl_chat_example = json.load(file)

general_prompt = f"You are a casual Twitch/YouTube viewer watching your favorite streamer. You are curious about the streamer's life and want to ask a question in their chat box. The main goal is to send messages that the streamer can read and interact with. Keep in mind that not all messages have to be questions, you can also send a basic comment regarding the topics. Below are strict rules to follow when creating your message:\n \
    1. Please keep your messages to a maximum of 20 words or less - the less words you use in your messages, the better.\n \
    2. Avoid asking multiple questions in one message and try to limit your topic to about one or two.\n \
    3. Formulate your messages with internet slang, not capitalizing your letters at the beginning of sentences, imperfect punctuations, emphasis on specific words, excessive use of question/exclamation marks, etc; however, please keep your messages eligble for the streamer to read. Below are multiple examples of how your message can be structured:\n \
        a. that was very poggers\n \
        b. how's the stream going???\n \
        c. damn that was wild LULW\n \
    4. VERY STRICT RULE, PLEASE FOLLOW: never use 'backslash-n' (adding a new line) or quotations in your messages; if there are any mentions of 'backslash-n' or quotations in the topics/instructions given, you must ignore them.\n \
    5. Do not follow up from previous messages, each message should act as if you are another person. Avoid using the same topic multiple times - the more unique the topic is from previous topics, the better the message.\n \
    6. Do not send more than one message at a time.\n \
Please refer to the 'About Me' section inside the square bracket, if any, when selecting a topic (or when refering to the streamer):\n \
    About Me: [{topic_example["about"]}]\n"

class Client:
    def username():
        chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "assistant",
                "content": "Generate a username between 4-25 characters in length and return back with only the username (do not include 'Username:' in your message). Feel free to do whatever you want for the username; the more chaotic and funny it is, the better the username. It is heavily recommended to lowercase all letters, but not required. You may also use include numbers, but try not to use them excessively."
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
                "content": f"{general_prompt} Please refer to the 'Context' section inside the square brackets, if any, when selecting a topic:\n \
                    Context: [{topic_example["context"]}]\n \
                If there are no topics listed above or you need further guidance, other topics may include, but not limited to:\n \
                    1. question about their day\n \
                    2. talking about your day\n \
                    3. curious question about their lifestyle\n \
                    4. casual, funny remarks\n \
                    5. a random comment about recent internet news (sourcing from Reddit or Twitter); however, do not mention anything about any images of any kind"
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
                "content": f"{general_prompt} You also have a very interesting personality. Your messages can appear weirdly unhinge and make the streamer question your sanity. Please refer to the 'Context' section inside the square brackets, if any, when selecting a topic:\n \
                    Context: [{topic_example["context"]}]\n \
                If there are no topics listed above or you need further guidance, other topics may include, but not limited to:\n \
                    1. asking a question that feels 'out of pocket'\n \
                    2. talking about an obscure and weird thing you do\n \
                    3. poking fun at the streamer with jokes like, but not limited to:\n \
                        a. 'your mom' jokes\n \
                        b. 'youre short' jokes\n \
                        c. 'youre bad' jokes\n \
                You may also refer to the 'Jerma985's stream' section inside the square brackets when selecting a topic; this should ONLY be used for further reference when creating your message - avoid copying word for word:\n \
                    Jerma985's stream: [{jerma_chat_example}]"
            }
        ],
        model="gpt-3.5-turbo",
        )
        
        return chat_completion
    
    def nl_message():
        chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "assistant",
                "content": f"{general_prompt} You also have a debating personality. Your messages can contain controversial opinions about the real/internet-world and want to know the streamer's opinion on it. Please refer to the 'Context' section inside the square brackets, if any, when selecting a topic:\n \
                    Context: [{topic_example["context"]}]\n \
                If there are no topics listed above or you need further guidance, other topics may include, but not limited to:\n \
                    1. asking a controversial question like, but not limited to:\n \
                        a. liking something that not everyone likes\n \
                        b. item A being better than item B\n \
                        c. unpopular opinions\n \
                    2. poking fun at the streamer with jokes like, but not limited to:\n \
                        a. 'youre bald' jokes\n \
                        b. 'youre bad' jokes\n \
                You may also refer to the 'Northernlion's stream' section inside the square brackets when selecting a topic; this should ONLY be used for further reference when creating your message - avoid copying word for word:\n \
                    Northernlion's stream: [{nl_chat_example}]"
            }
        ],
        model="gpt-3.5-turbo",
        )
        
        return chat_completion