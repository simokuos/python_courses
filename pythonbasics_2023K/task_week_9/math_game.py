import tkinter as tk
from tkinter import ttk
from random import randint

class GLOBAL:
    first_number = 0
    second_number = 0
    sum = 0

class AppEvents:
    @staticmethod
    def setSum():
        number_1 = randint(1, 20)
        number_2 = randint(1, 20)
        GLOBAL.first_number = number_1
        GLOBAL.second_number = number_2
        GLOBAL.sum = number_1 + number_2
    @staticmethod
    def giveReward(self):
       
        newWindow = tk.Toplevel()

        newWindow.title("Reward")
        newWindow.geometry("200x300")

        img = tk.PhotoImage(file ='happycat.png')
        label = tk.Label(newWindow, image=img)
        label.image = img
        label.pack()



class GameFrame(ttk.Frame):
    def __init__(self,container):
        super().__init__(container)

        # grid layout manager
        self.columnconfigure(0,weight = 1)
        self.columnconfigure(1,weight = 1)
        self.columnconfigure(2,weight = 1)
        self.columnconfigure(3, weight = 1)
        self.__create_widgets()

    def __create_widgets(self):
        # Question generations
        
        AppEvents.setSum()
        question_label_text = str(GLOBAL.first_number) + " + " + str(GLOBAL.second_number)
        
        self.question_label = ttk.Label(self, text = question_label_text).grid(column=1, row=0, sticky=tk.W)
        self.number = tk.StringVar()
        ttk.Label(self, text='Sum:').grid(column = 0, row = 1, sticky=tk.W)
        user_input = ttk.Entry(self,textvariable = self.number, width=15)
        user_input.focus()
        user_input.grid(column=1, row=1, sticky=tk.W)

        self.summit = ttk.Button(self, text='Check Answer')
        self.summit['command'] = self.check_answer
        self.summit.grid(column=2, row=1, sticky=tk.W)

        self.label_text = 'Rigth Answer:'
        self.answer_label = ttk.Label(self, text=self.label_text, font =("Arial", 8 ))
        self.answer_label.grid(column = 1, row = 2, sticky=tk.W)
        self.youranswer_label = ttk.Label(self, text='Your Answer:', font =("Arial", 8 ) )
        self.youranswer_label.grid(column = 2, row = 2, sticky=tk.W)

    def check_answer(self):
        temp_answer = self.number.get()
        temp_sum = GLOBAL.sum
       
        self.answer_label['text'] = 'Rigth Answer:' + str(temp_sum)
        self.youranswer_label['text'] = 'Your Answer:' + str(temp_answer)
        if(temp_sum == int(temp_answer)):
           AppEvents.giveReward(self)
        AppEvents.setSum()

    
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # root window config
        self.title('Math game')
        self.geometry('400x200')

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        self.__create_widgets()

    def __create_widgets(self):

        game_frame = GameFrame(self)
        game_frame.grid(column = 0, row = 0)
        

if __name__ == "__main__":
    app = App()
    app.mainloop()