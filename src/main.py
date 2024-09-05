from client import Client
from util import Util, BACKGROUND_COLOR, FONT_COLOR, FONT_TYPE
from tkinter import *
from PIL import ImageTk, Image
import random
import json

# starting menu - where you can customize what type of messages to expect
root = Tk()
root.title("Schizo-Chat")
root.geometry("480x540")
root.config(bg=BACKGROUND_COLOR)

off_image = ImageTk.PhotoImage(Image.open("assets/off-button.png"))
on_image = ImageTk.PhotoImage(Image.open("assets/on-button.png"))
context_image = ImageTk.PhotoImage(Image.open("assets/context-button.png"))
about_image = ImageTk.PhotoImage(Image.open("assets/about-button.png"))
start_image = ImageTk.PhotoImage(Image.open("assets/start-button.png"))

is_general_button_on = True
is_jerma_button_on = False

class App:    
    # toggles the on/off image of the button
    def toggle_button(button_name: str,
                      button,
                      button_state: bool):
        global is_general_button_on
        global is_jerma_button_on
        
        if button_state:
            button.config(image=off_image)
        else:
            button.config(image=on_image)
        
        if button_name == "general_button":
            is_general_button_on = not is_general_button_on
        elif button_name == "jerma_button":
            is_jerma_button_on = not is_jerma_button_on
    
    # creates a new window for inserting topics
    def create_topic_window(request: str):
        topic_window = Toplevel(root,
                                bg=BACKGROUND_COLOR)
        topic_window.geometry("480x440")
        
        topic_instruction = Util.create_label(topic_window)
        topic_instruction.config(text="<Ctrl + S> to close window and save.",
                                 pady=10)
        topic_instruction.pack(side=TOP)
        
        topic_entry = Util.create_text(topic_window)
        # restores any previous saved data
        with open("../data/topic.json", "r") as file:
            topic_example = json.load(file)
            
        topic_entry.insert(END, "".join([word for word in topic_example[request]]))
        topic_entry.bind("<Control-s>", lambda e: App.add_topic(request,
                                                                topic_entry,
                                                                topic_window))
        topic_entry.pack()
    
    # adds the inserted topic into topic.json
    def add_topic(request: str,
                  topic_entry,
                  topic_window):
        with open("../data/topic.json", "r") as file:
            topic_example = json.load(file)
        
        topic_example[request] = topic_entry.get("1.0", END)
        
        with open("../data/topic.json", "w") as file:
            json.dump(topic_example, file, indent=4, sort_keys=True)
        
        topic_window.destroy()
            
    # creates a new window where the chat messages will appear
    def create_chat_window():
        # chat window - where you can view your chat's messages
        chat_window = Toplevel(root)
        chat_window.geometry("480x840")
        
        chat_message = Util.create_text(chat_window)
        chat_message.pack()
        App.display_chat(chat_window, chat_message)
        
    # opens a new window where the chat messages will be displayed
    def display_chat(chat_window,
                     chat_message):
        trait_list = list()
        
        if chat_window.winfo_exists():
            if is_general_button_on:
                trait_list.append("general")
            if is_jerma_button_on:
                trait_list.append("jerma")
            
            random_trait = random.choice(trait_list)
            
            if random_trait == "general":
                print("Generating a general message.")
                message = Client.general_message().choices[0].message.content
            elif random_trait == "jerma":
                print("Generating a 'Jerma' message.")
                message = Client.jerma_message().choices[0].message.content
            
            random_username = Client.username().choices[0].message.content
            chat_message.insert(END, random_username + ": " + message + "\n")
            
            # generates a random color into hex format
            while True:
                random_font_color, random_tag_name = "", ""
                random_font_color = "#" + "".join([random.choice("0123456789ABCDEF") for hex in range(6)])
                random_tag_name = random_font_color
                
                if random_font_color.startswith("#f") == False and random_font_color.startswith("#1") == False:
                    break
            
            # creates a tag for the username
            idx = chat_message.index(END)
            start_idx = float(idx) - 2.0
            end_idx = (len(random_username) / 100.0) + start_idx
            chat_message.tag_add(random_tag_name, str(start_idx), str(end_idx))
            
            # changes the username to the random_font_color
            chat_message.tag_config(random_tag_name, foreground=random_font_color)
            
            root.after((time_scale.get() * 60) * 1000, App.display_chat, chat_window, chat_message)
   
# creates the toggle button for general mode
general_label = Util.create_label(root)
general_label.config(text="General Mode")
general_label.pack(pady=(20, 0))

general_button = Util.create_button(root)
general_button.config(image=on_image,
                      command=lambda: App.toggle_button("general_button",
                                                        general_button,
                                                        is_general_button_on))
general_button.pack(pady=(0, 10))
    
# creates the toggle button for "Jerma" mode
jerma_label = Util.create_label(root)
jerma_label.config(text="Jerma985 Mode")
jerma_label.pack()

jerma_button = Util.create_button(root)
jerma_button.config(image=off_image,
                    command=lambda: App.toggle_button("jerma_button",
                                                      jerma_button,
                                                      is_jerma_button_on))
jerma_button.pack(pady=(0, 10))

# creates the start button
start_button = Util.create_button(root)
start_button.config(image=start_image,
                    command=lambda: App.create_chat_window())
start_button.pack(side=BOTTOM,
                  pady=(0, 20))

# creates the time interval scale
time_scale = Util.create_scale(root)
time_scale.config(from_=5, # 5 minutes
                   to=60) # 60 minutes
time_scale.pack(side=BOTTOM,
                pady=(0, 20))

time_scale_label2 = Util.create_label(root)
time_scale_label2.config(text="Min: 5 minutes; Max: 60 minutes")
time_scale_label2.pack(side=BOTTOM)

time_scale_label1 = Util.create_label(root)
time_scale_label1.config(text="Time Interval b/w Messages (in Minutes)")
time_scale_label1.pack(side=BOTTOM)

# creates a personalized section ("add topic" and "about me" buttons)
personalize_frame = Util.create_frame(root)
personalize_frame.pack(side=BOTTOM,
                       pady=(0, 20))

personalize_label = Util.create_label(personalize_frame)
personalize_label.config(text="Additional Information")
personalize_label.pack()

context_button = Util.create_button(personalize_frame)
context_button.config(image=context_image,
                      command=lambda: App.create_topic_window("context"))
context_button.pack(side=LEFT,
                    padx=(0, 2.5))

about_button = Util.create_button(personalize_frame)
about_button.config(image=about_image,
                    command=lambda: App.create_topic_window("about"))
about_button.pack()

if __name__ == "__main__":
    root.mainloop()