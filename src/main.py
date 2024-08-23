from client import Client
from tkinter import *
import random

# starting menu - where you can customize what type of messages to expect
root = Tk()
root.geometry("480x440")

is_general_button_on = True
is_jerma_button_on = False

off_image = PhotoImage(file="C:\\Users\\rattl\\Desktop\\Projects\\Python\\fake_chatters\\assets\\off-button.png")
on_image = PhotoImage(file="C:\\Users\\rattl\\Desktop\\Projects\\Python\\fake_chatters\\assets\\on-button.png")
start_image = PhotoImage(file="C:\\Users\\rattl\\Desktop\\Projects\\Python\\fake_chatters\\assets\\start-button.png")

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

def create_button(button_image):
    button = Button(root,
                    relief=FLAT,
                    image=button_image,
                    compound=CENTER)
    return button

# toggles the on/off image of the button
def toggle_button(button,
                  button_state):
    if button_state:
        button.config(image=off_image)
    else:
        button.config(image=on_image)

# General Mode
def general_button_function(general_button) -> bool:
    global is_general_button_on
    
    print("Toggling general mode.")
    toggle_button(general_button,
                  is_general_button_on)
    is_general_button_on = not is_general_button_on
    
# creates the toggle button for general mode
general_button = create_button(on_image)
general_button.config(command=lambda: general_button_function(general_button))
general_button.pack()

# Jerma Mode
def jerma_button_function(jerma_button) -> bool:
    global is_jerma_button_on
    
    print("Toggling 'Jerma' mode.")
    toggle_button(jerma_button,
                  is_jerma_button_on)
    is_jerma_button_on = not is_jerma_button_on
    
# creates the toggle button for "Jerma" mode
jerma_button = create_button(off_image)
jerma_button.config(command=lambda: jerma_button_function(jerma_button))
jerma_button.pack()

# creates a new window where the chat messages will appear
def start_button_function():
    # chat window - where you can view your chat's messages
    chat_window = Toplevel(root)
    chat_window.geometry("480x840")
    
    chat_message = create_text(chat_window)
    chat_message.pack()
    display_chat(chat_window, chat_message)

start_button = create_button(start_image)
start_button.config(command=lambda: start_button_function())
start_button.pack()

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
        root.after(20000, display_chat, chat_window, chat_message)

if __name__ == "__main__":
    root.mainloop()