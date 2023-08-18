import tkinter as tk
from functools import reduce
import re
import shuffle

root = tk.Tk()
root.title("Shuffle Simulater")
root.geometry("640x480")

cards = [ [suit + str(num)  for num in range(1,13 + 1)] for suit in ["♠️", "♥️", "♦️", "♣️"]]
deck = reduce(lambda sum,current:sum + current ,cards)

match_shuffle = lambda name: re.compile(r'.*_shuffle').fullmatch(name)
shuffle_names = list(filter(match_shuffle ,dir(shuffle)))

def shuffle_clicked(event):
    name = event.widget["text"]
    shuffle_func = getattr(shuffle,name)
    global deck
    deck = shuffle_func(deck)
    print(deck)

    
Buttons = [ tk.Button(root,text=func_name) for func_name in shuffle_names ]

reduce(lambda _,button: button.bind("<ButtonPress>",shuffle_clicked) ,Buttons)
reduce(lambda _,button: button.grid() ,Buttons)


root.mainloop()