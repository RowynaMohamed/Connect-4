from tkinter import *

from connect4 import play

diff=0
choice=0

window =Tk()
window.title("CONNECT-4-GAME")
window.geometry('500x500')

label1 = Label(window,text='choose between minimax algorithm and alphabeta',fg='green',font=('Arial',20))

label1.grid(row=0,column=0,padx=5,pady=10)

def choose(c):
    choice=c

def choose2(c):
    diff=c

button1 = Button(window,command=choose(1),text='MINMAX',fg='red',font=('Arial',20))

button1.grid(row=1,column=0,sticky=W)

button1 = Button(window,command=choose(2),text='ALPHA_BETA',fg='red',font=('Arial',20))

button1.grid(row=1,column=1,sticky=W)


label1 = Label(window,text='choose the difficulty of the game :',fg='green',font=('Arial',20))

label1.grid(row=2,column=0,padx=5,pady=10)

button1 = Button(window,command=choose2(1),text='EASY',fg='blue',font=('Arial',20))

button1.grid(row=3,column=0,sticky=W)
button1 = Button(window,command=choose2(2),text='MEDIUM',fg='blue',font=('Arial',20))

button1.grid(row=4,column=0,sticky=W)
button1 = Button(window,command=choose2(3),text='HARD',fg='blue',font=('Arial',20))

button1.grid(row=5,column=0,sticky=W)

def playy2():
    play(diff,choice)

button1 = Button(window,command=playy2,text='PLAY',fg='grey',font=('Arial',30))

button1.grid(row=7,column=1,sticky=W)






window.mainloop()