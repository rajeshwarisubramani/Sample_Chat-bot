# -*- coding: utf-8 -*-
import tkinter
from tkinter import *


def chatbot_response(msg):
    return 'static text'

def send():
    msg = TextEntryBox.get("1.0", 'end-1c').strip()
    TextEntryBox.delete('1.0', 'end')
    
    if msg != '':
        ChatHistory.config(state=NORMAL)
        ChatHistory.insert('end', "you: " +msg+ "\n\n")
        res = chatbot_response(msg)
        ChatHistory.insert('end', "Bot: " +res)
        ChatHistory.config(state=DISABLED)
        ChatHistory.yview('end')

base = tkinter.Tk()
base.title("New Chatbot")
base.geometry("400x500")
base.resizable(width=False, height=False)


#chat history
ChatHistory = Text(base, bd=0, bg='white', font='Arial')
ChatHistory.config(state=DISABLED)
SendButton = Button(base, font=('Arial', 12, 'bold'), text="Send", bg="#dfdfdf", command=send)
TextEntryBox = Text(base, bd=0, bg='white', font='Arial')
ChatHistory.place(x=6, y=6, height=386, width=386)
TextEntryBox.place(x=128, y=400, height=80, width=265)
SendButton.place(x=6, y=400, height=80, width=125)
 
base.mainloop()