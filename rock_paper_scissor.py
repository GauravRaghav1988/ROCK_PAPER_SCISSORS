from tkinter import *
import random


root = Tk()                                    #use to initialized Tkinter to create window
root.geometry('800x500')                       #sets the window width and height
root.resizable(0,0)                            #fix the size of the window
root.title('DataFlair-Rock,Paper,Scissors')    #setting the title of the window
root.config(bg='white')                        #sets color of the background

#label is widget used when we want to display text that users can’t modify
#root is the name of our window
#text which displays on the label as the title of that label
#font in which form the text is written
#pack used to the organized widget in form of block
Label(root, text = 'WELCOME TO ROCK, PAPER ,SCISSORS GAME' , font='arial 20 bold', bg = 'seashell2').pack()

#user_take is a string type variable that stores the choice that the user enters.
#Entry() widget used when we want to create an input text field.

user_take = StringVar()
Label(root, text = 'CHOOSE BETWEEN: ROCK, PAPER ,SCISSORS' , font='arial 15 bold', bg = 'seashell2').place(x =150,y=70)
Entry(root, font = 'CommentsStyle 25', textvariable = user_take , bg = 'antiquewhite2').place(x=200 , y = 130)


comp_pick = random.randint(1,3)
if comp_pick == 1:
    comp_pick = 'ROCK'
elif comp_pick == 2:
    comp_pick = 'PAPER'
else:
    comp_pick = 'SCISSORS'
    Result = StringVar()


    def play():
        user_pick = user_take.get()
        if user_pick == comp_pick:
            Result.set('ITS A TIE ,YOU BOTH CHOOSE SAME')
        elif user_pick == 'ROCK' and comp_pick == 'PAPER':
            Result.set('YOU LOOSE SORRY,COMPUTER SELECTED: PAPER')
        elif user_pick == 'ROCK' and comp_pick == 'SCISSORS':
            Result.set('YOU WON ..YUPPIEEE..!,COMPUTER SELECTED: SCISSORS')
        elif user_pick == 'PAPER' and comp_pick == 'SCISSORS':
            Result.set('YOU LOOSE SORRY,COMPUTER SELECTED: SCISSORS')
        elif user_pick == 'PAPER' and comp_pick == 'ROCK':
            Result.set('YOU WON ..YUPPIEEE..!,COMPUTER SELECTED: ROCK')
        elif user_pick == 'SCISSORS' and comp_pick == 'ROCK':
            Result.set('YOU LOOSE SORRY,COMPUTER SELECTED: ROCK')
        elif user_pick == 'SCISSORS' and comp_pick == 'PAPER':
            Result.set('YOU WON ..YUPPIEEE..!,COMPUTER SELECTED: PAPER')
        else:
            Result.set('invalid: choose any one -- ROCK, PAPER, SCISSORS')

#This function set all variables to an empty string.
    def Reset():
        Result.set("")
        user_take.set("")

    def Exit():
        root.destroy()    #root.destroy() will quit the rock paper scissors program by stopping the mainloop().



#Button() widget used when we want to display a button.
#command called the specific function when the button will be clicked.
#root.mainloop() method executes when we run our program.
    Entry(root, font='arial 10 bold', textvariable=Result, bg='WHITE', width=100, ).place(x=25, y=400)

    Button(root, font='arial 13 bold', text='PLAY', padx=5, bg='seashell4', command=play).place(x=350, y=190)

    Button(root, font='arial 13 bold', text='RESET', padx=5, bg='seashell4', command=Reset).place(x=70, y=310)

    Button(root, font='arial 13 bold', text='EXIT', padx=5, bg='seashell4', command=Exit).place(x=630, y=310)

    root.mainloop()