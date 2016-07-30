# -*- coding:utf-8 -*-

from tkinter import *
import tkinter.simpledialog as dl
import tkinter.messagebox as mb
import random


root = Tk()
w = Label(root, text = "Guess number!")
w.pack()

mb.showinfo('Hello!', '''The number is between 1~99.
You got only 5 times !
    Good luck!''')

number = random.randint(1,99)
times = 5

while times > 0:
    guess = dl.askinteger('Have a try!', 'Enter a number')
    if guess == number:
        output = "Bingo! You are such a genius!"
        mb.showinfo('Hint:', output)
        break
    elif guess < number:
        times = times-1
        output = '''Nope,it's lower than the number.Have another try.
        The times left:''' + str(times)
        mb.showinfo('Hint:', output)
        continue
    else:
        times = times-1
        output = '''Nope,it's higher than the number.Have another try.
        The times left:''' + str(times)
        mb.showinfo('Hint:', output)
        continue
while times == 0:
    output_last = "Oops,you have run out your times.The number is:" + str(number)
    mb.showinfo('Hint:', output_last)
    break

mb.showinfo('Hint:', '''Game over.
Thanks for playing!''')
    