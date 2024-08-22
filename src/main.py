# from client import Client
from tkinter import *

root = Tk()
root.geometry("480x440")
# root.geometry("480x840")

is_jerma_button_on = False

off_image = PhotoImage(file="C:\\Users\\rattl\\Desktop\\Projects\\Python\\fake_chatters\\assets\\off-button.png")
on_image = PhotoImage(file="C:\\Users\\rattl\\Desktop\\Projects\\Python\\fake_chatters\\assets\\on-button.png")

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

# Jerma Mode
def jerma_button_function(jerma_button) -> bool:
    global is_jerma_button_on
    
    toggle_button(jerma_button,
                  is_jerma_button_on)
    is_jerma_button_on = not is_jerma_button_on
    
# creates the toggle button for "Jerma Mode"
jerma_button = create_button(off_image)
jerma_button.config(command=lambda: jerma_button_function(jerma_button))
jerma_button.pack(anchor=CENTER)

if __name__ == "__main__":
    root.mainloop()