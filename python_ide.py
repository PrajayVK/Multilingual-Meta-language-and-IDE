#Importing the necessary libraries 
from tkinter import *

#compiler is the main IDE
compiler = Tk()
compiler.title("DOSA - Multilingual IDE")

#Menu bar with fancy things
menu_bar = Menu(compiler)

#Run bar
run_bar = Menu(menu_bar)
run_bar.add_command(label='Run')

menu_bar.add_cascade(label='Run', menu=run_bar)
compiler.config(menu = menu_bar)


editor = Text()
editor.pack()

compiler.mainloop()

