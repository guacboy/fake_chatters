from tkinter import *

BACKGROUND_COLOR = "#18181a"
FONT_COLOR = "#ffffff"
FONT_TYPE = "Roobert"

class Util:
    # default format for text box
    def create_text(window):
        return Text(window,
                    height=1000,
                    width=1000,
                    padx=20,
                    pady=20,
                    bg=BACKGROUND_COLOR,
                    fg=FONT_COLOR,
                    font=FONT_TYPE,
                    spacing3=10,
                    wrap=WORD)

    # default format for label
    def create_label(window):
        return Label(window,
                     bg=BACKGROUND_COLOR,
                     fg=FONT_COLOR,
                     font=FONT_TYPE)
    
    # default format for scale
    def create_scale(window):
        return Scale(window,
                     bg=BACKGROUND_COLOR,
                     troughcolor=BACKGROUND_COLOR,
                     highlightbackground=BACKGROUND_COLOR,
                     highlightcolor=BACKGROUND_COLOR,
                     fg=FONT_COLOR,
                     font=FONT_TYPE,
                     length=300,
                     orient=HORIZONTAL)
    
    # default format for frame
    def create_frame(window):
        return Frame(window,
                     bg=BACKGROUND_COLOR)
    
    # default format for button
    def create_button(window):
        return Button(window,
                      bg=BACKGROUND_COLOR,
                      activebackground=BACKGROUND_COLOR,
                      bd=0,
                      relief=FLAT,
                      compound=CENTER)