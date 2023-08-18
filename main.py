import tkinter as tk
from PIL import Image, ImageTk
from functools import reduce
import re
import shuffle

root = tk.Tk()
root.title("Shuffle Simulater")
root.geometry("720x480")

Canvas = tk.Canvas(root,bg="white", height=180, width=715)
Canvas.place(x=0, y=0)

def show_deck(deck):
    image_pathes = [ 
            "cards/" + card.replace("♠️","spade/").replace("♥️","heart/").replace("♦️","diamond/").replace("♣️","club/") + ".png" 
            for card in deck
        ]
    Images = [ Image.open(path).resize((90,120)) for path in image_pathes]
    TkImages = [ ImageTk.PhotoImage(img) for img in Images]
    global Canvas
    
    # x = 0
    # for img in TkImages:
    #     Canvas.create_image(10 + x, 30, image=img, anchor=tk.NW)
    #     x += 12
    Pitch = 12 
    reduce(lambda _,img: Canvas.create_image(10 + Pitch*TkImages.index(img), 30, image=img, anchor=tk.NW) ,TkImages)
    
    root.mainloop()

cards = [ [suit + str(num)  for num in range(1,13 + 1)] for suit in ["♠️", "♥️", "♦️", "♣️"]]
deck = reduce(lambda sum,current:sum + current ,cards)

match_shuffle = lambda name: re.compile(r'.*_shuffle').fullmatch(name)
shuffle_names = list(filter(match_shuffle ,dir(shuffle)))

def shuffle_clicked(event):
    name = event.widget["text"]
    shuffle_func = getattr(shuffle,name)
    global deck
    deck = shuffle_func(deck)
    show_deck(deck)

Shuffle_buttons = tk.Frame(root,width=620,height=480,bg="skyblue")
Shuffle_buttons.place(x=10,y =240)

Buttons = [ tk.Button(Shuffle_buttons,text=func_name) for func_name in shuffle_names ]

reduce(lambda _,button: button.bind("<ButtonPress>",shuffle_clicked) ,Buttons)
reduce(lambda _,button: button.pack(fill ="x", padx=20, side ="left") ,Buttons)

show_deck(deck)
root.mainloop()