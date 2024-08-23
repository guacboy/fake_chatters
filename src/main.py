from client import Client
from tkinter import *
import random

# starting menu - where you can customize what type of messages to expect
root = Tk()
root.geometry("480x440")

off_image = PhotoImage(file="C:\\Users\\rattl\\Desktop\\Projects\\Python\\fake_chatters\\assets\\off-button.png")
on_image = PhotoImage(file="C:\\Users\\rattl\\Desktop\\Projects\\Python\\fake_chatters\\assets\\on-button.png")
start_image = PhotoImage(file="C:\\Users\\rattl\\Desktop\\Projects\\Python\\fake_chatters\\assets\\start-button.png")

is_general_button_on = True
is_jerma_button_on = False

class App:
    # default format for text box
    def create_text(window):
        text = Text(window,
                    height=400,
                    width=800,
                    padx=20,
                    pady=20,
                    bg="#18181a",
                    fg="#ffffff",
                    font="Roobert",
                    spacing3=10,
                    wrap=WORD)
        return text
    
    # default format for button
    def create_button():
        button = Button(root,
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
            
    # creates a new window where the chat messages will appear
    def create_chat_window():
        # chat window - where you can view your chat's messages
        chat_window = Toplevel(root)
        chat_window.geometry("480x840")
        
        chat_message = App.create_text(chat_window)
        chat_message.pack()
        App.display_chat(chat_window, chat_message)
        
    # opens a new window where the chat messages will be displayed
    def display_chat(chat_window, chat_message):
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
            
            chat_message.insert(END, message + "\n")
            root.after(60000, App.display_chat, chat_window, chat_message)
   
# creates the toggle button for general mode
general_button = App.create_button()
general_button.config(image=on_image,
                      command=lambda: App.toggle_button("general_button",
                                                        general_button,
                                                        is_general_button_on))
general_button.pack()
    
# creates the toggle button for "Jerma" mode
jerma_button = App.create_button()
jerma_button.config(image=off_image,
                    command=lambda: App.toggle_button("jerma_button",
                                                      jerma_button,
                                                      is_jerma_button_on))
jerma_button.pack()

# creates the start button
start_button = App.create_button()
start_button.config(image=start_image,
                    command=lambda: App.create_chat_window())
start_button.pack()

if __name__ == "__main__":
    root.mainloop()