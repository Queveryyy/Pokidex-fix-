from cProfile import label
from distutils.log import info
from operator import truediv
from re import L
from tkinter import *
from turtle import bgcolor
from webbrowser import get


from setuptools import Command

quev=Tk()

#def
def WIT():
    if True:
        print('ddd')

def SEARCH():
    text = searchbar.get()
    if text == 'pikachu':
        info = pikachu



#buttons

BG = PhotoImage(file='PokedexBG.png')
Label(quev,image=BG).pack()

pikachu = ('\nWhat is it?: Pikachu is a electric type pokemon.\n \nMoveset?: It has many moves ranging from Thunderbolts to iron tales! \n \nWhere can i find it?: Pikachu can be found near the mountains in the Kanto Region!')

Find = Button(quev,text= '\nExecute Command! \n ', bg='yellow', fg='green', command=SEARCH, width=16)
Find.place(x=91, y=449)


WhatIsIt = Label(quev, fg='black', bg='green', width='48', text=info)
WhatIsIt.place(x=428, y=155)


searchbar = Entry(quev, fg = 'black', bg='red', width=43)
searchbar.place(x=57, y=136)

dum = Label(quev, text='type here genius ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑', bg='yellow')
dum.place(x=57, y=155)

WIT = Checkbutton(quev, bg='#387cfc')
WIT.place(x=53, y=395)

MS = Checkbutton(quev, bg='lime')
MS.place(x=105, y=395)

WFT = Checkbutton(quev, bg='dark orange')
WFT.place(x=175, y=395)



#quevs!
quev.title('Pokidex by quev, BETA')
quev.configure(bg='black')
quev.minsize(width=350, height=600)
quev.config(bg='red')
quev.iconbitmap('pokemon-go.png')


quev.mainloop()