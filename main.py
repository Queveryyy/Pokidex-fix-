from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
from traceback import print_tb

root = Tk()
root.title('Quevs Pokedex')
root.geometry('300x300')


#Labels

l = Label(root, text="Choose a Pokemon!")
l.pack()

#Functions

def p1():
    print("What is it?:Pikachu is a electric type pokemon. \nMoveset?: It has many moves ranging from Thunderbolts to Wil Charge \nWhere can i find it?: Pikachu can be found near the mountains in the Kanto Region!")


#Var

bgc = '006400' #dark green


root.configure(background='bgc')

#buttons and their style!

btn_style = ttk.Style()
btn_style.configure('Tbutton', background='3B3B3B')
btn_style.map('Tbutton', background=[('active','3B3B3B')])

pokemon1 = ttk.Button(root, text='Pikachu!', command=p1)
pokemon1.grid(row=0, column=1)

pokemon2 = ttk.Button(root, text='Charmander!')
pokemon2.grid(row=0, column=2)

pokemon3 = ttk.Button(root, text='Squirtle!')
pokemon3.grid(row=0, column=3)

pokemon4 = ttk.Button(root, text='bulbasaur!')
pokemon4.grid(row=0, column=4)


root.mainloop()

