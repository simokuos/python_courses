import tkinter as tk
from tkinter import messagebox as mb

def convert_click():
    input_temp = input_text.get('1.0','end')
    try:
        integer = int(input_temp)
        assert integer >= 0
    except ValueError:
        mb.showerror(title="alert", message="input is not a whole number")
        return
    except:
        mb.showerror(title="alert", message="input is negative, year should be possitive number")
        return
    mb.showinfo(title="year", message=input_temp)

window = tk.Tk()
window.geometry("200x70")

label_frame = tk.Frame()
label_frame.pack(side=tk.TOP)

text_and_button = tk.Frame()
text_and_button.pack()

text_input_title = tk.Label(
    master = label_frame,
    text="What year it is?",
    font = ("Arial", 16 )
    )
text_input_title.pack(side=tk.LEFT, padx=(0,0))

input_text = tk.Text(
    master=text_and_button,
    height = 1,
    width = 10,
    font = ("Arial", 16 )
    )
input_text.pack(side=tk.LEFT, padx = (0,0))

answer_button = tk.Button(
    master = text_and_button,
    command = convert_click,
    text = "answer",
    width = 5,
    height = 1,
    bg = "black",
    fg = "white"
    )
answer_button.pack(side=tk.RIGHT, padx=(0,0))

window.mainloop()