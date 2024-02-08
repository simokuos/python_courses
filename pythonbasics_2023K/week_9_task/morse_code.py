import tkinter as tk

def convert_click():
    input = input_text.get('1.0','end')
    morse_text = ""
    morse_code_dictionary ={
        'a': '.-',
        'b': '-...',
        'c': '-.-.',
        'd': '-..',
        'e': '.',
        'f': '..-.',
        'g': '--.',
        'h': '....',
        'i': '..',
        'j': '.---',
        'k': '-.-',
        'l': '.-..',
        'm': '--',
        'n': '-.',
        'o': '---',
        'p': '.--.',
        'q': '--.-',
        'r': '.-.',
        's': '...',
        't': '-',
        'u': '..-',
        'v': '...-',
        'w': '.--',
        'x': '-..-',
        'y': '-.--',
        'z': '--..',
        '1':'.----',
        '2':'..---',
        '3':'...--',
        '4':'....-',
        '5':'.....',
        '6':'-....',
        '7':'--...',
        '8':'---..',
        '9':'----.',
        '0':'-----'
    }
    for x in input:
        temp = morse_code_dictionary.get(x)
        if(temp == None):break
        morse_text = morse_text + temp + " "
    output_text.insert(tk.END, morse_text)


window = tk.Tk()
window.geometry("700x350")

label_frame = tk.Frame()
label_frame.pack(side=tk.TOP)

text_and_button = tk.Frame()
text_and_button.pack()

label_morse = tk.Frame()
label_morse.pack(side=tk.TOP)

output_frame = tk.Frame()
output_frame.pack()


text_input_title = tk.Label(
    master = label_frame,
    text="Text:",
    font = ("Arial", 16 )
    )
text_input_title.pack(side=tk.LEFT, padx=(0,510))

#user_entry = tkinter.entry( 
#    master=text_and_button,
    
    
#    )
#user_text = user_entry.get()
#user_entry.pack(side=tkinter.left, padx = (20,0))

input_text = tk.Text(
    master=text_and_button,
    height = 5,
    width = 40,
    font = ("Arial", 16 )
    )

input_text.pack(side=tk.LEFT, padx = (20,0))

encode_button = tk.Button(
    master = text_and_button,
    command = convert_click,
    text = "encode",
    width = 10,
    height = 2,
    bg = "black",
    fg = "white"
    )

encode_button.pack(side=tk.RIGHT, padx=(40,0))

morse_output_title = tk.Label(
    master = label_morse,
    text="Morse:",
    font = ("Arial", 16 )
    )
morse_output_title.pack(side=tk.LEFT, padx=(0,500))

output_text = tk.Text(
    master = output_frame,
    height = 5,
    width = 37,
    font = ("Arial", 18 )
    )
output_text.pack(side=tk.LEFT, padx = (0,100))


window.mainloop()
