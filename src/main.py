from client import Client
from tkinter import *
import random
import json

# starting menu - where you can customize what type of messages to expect
root = Tk()
root.geometry("480x440")

data_file_path = "C:\\Users\\rattl\\Desktop\\Projects\\Python\\fake_chatters\\data\\"
assets_file_path = "C:\\Users\\rattl\\Desktop\\Projects\\Python\\fake_chatters\\assets\\"

off_image = PhotoImage(file=assets_file_path + "off-button.png")
on_image = PhotoImage(file=assets_file_path + "on-button.png")
start_image = PhotoImage(file=assets_file_path + "start-button.png")

is_general_button_on = True
is_jerma_button_on = False

class App:
    # default format for text box
    def create_text(window):
        text = Text(window,
                    height=1000,
                    width=1000,
                    padx=20,
                    pady=20,
                    bg="#18181a",
                    fg="#ffffff",
                    font="Roobert",
                    spacing3=10,
                    wrap=WORD)
        return text
    
    # default format for button
    def create_button(window):
        button = Button(window,
                        relief=FLAT,
                        compound=CENTER)
        return button

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
        if button_name == "jerma_button":
            is_jerma_button_on = not is_jerma_button_on
    
    # creates a new window for inserting personal topics
    def create_topic_window():
        topic_window = Toplevel(root)
        topic_window.geometry("480x440")
        
        topic_entry = App.create_text(topic_window)
        # restores any previous saved data
        with open(data_file_path + "topic.json", "r") as file:
            topic_example = json.load(file)
        topic_entry.insert(END, "<Ctrl + S> to close window and save.\n" + "".join([word for word in topic_example.values()]))
        topic_entry.bind("<Control-s>", lambda e: App.add_topic(topic_entry,
                                                                topic_window))
        topic_entry.pack()
    
    # adds the inserted topics into topic.json
    def add_topic(topic_entry,
                  topic_window):
        with open(data_file_path + "topic.json", "r") as file:
            topic_example = json.load(file)
            
        topic_example["topic"] = topic_entry.get("2.0", END)
        
        with open(data_file_path + "topic.json", "w") as file:
            json.dump(topic_example, file)
        
        topic_window.destroy()
            
    # creates a new window where the chat messages will appear
    def create_chat_window():
        # chat window - where you can view your chat's messages
        chat_window = Toplevel(root)
        chat_window.geometry("480x840")
        
        chat_message = App.create_text(chat_window)
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
            if random_trait == "jerma":
                print("Generating a 'Jerma' message.")
                message = Client.jerma_message().choices[0].message.content
            
            random_username = Client.username().choices[0].message.content
            chat_message.insert(END, random_username + ": " + message + "\n")
            
            # generates a random color into hex format
            random_font_color, random_tag_name = "", ""
            while True:
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
            
            root.after(60000, App.display_chat, chat_window, chat_message)
   
# creates the toggle button for general mode
general_button = App.create_button(root)
general_button.config(image=on_image,
                      command=lambda: App.toggle_button("general_button",
                                                        general_button,
                                                        is_general_button_on))
general_button.pack()
    
# creates the toggle button for "Jerma" mode
jerma_button = App.create_button(root)
jerma_button.config(image=off_image,
                    command=lambda: App.toggle_button("jerma_button",
                                                      jerma_button,
                                                      is_jerma_button_on))
jerma_button.pack()

# creates the "add personal topic" button
topic_button = App.create_button(root)
topic_button.config(text="add topic",
                    command=lambda: App.create_topic_window())
topic_button.pack()

# creates the start button
start_button = App.create_button(root)
start_button.config(image=start_image,
                    command=lambda: App.create_chat_window())
start_button.pack()

if __name__ == "__main__":
    root.mainloop()