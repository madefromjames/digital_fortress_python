from tkinter import *

window = Tk()
window.minsize(width=500, height=500)
button = Button(text="Click")
window.title("Python app")
greet = Label(text='Hello')
word = Label(text='Enter your username')
greet.pack()
word.pack()
input = Entry()
input.pack()
button.pack()
window.mainloop()