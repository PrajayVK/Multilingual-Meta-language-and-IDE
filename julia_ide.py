from tkinter import *
from tkinter.ttk import Style

def toggle_dark_mode():
    # Get the current theme
    current_theme = theme_choice.get()

    if current_theme == "clam":
        # Switch to the dark theme
        style.theme_use('alt')
        theme_choice.set('alt')
    else:
        # Switch back to the light theme
        style.theme_use('clam')
        theme_choice.set('clam')

compiler = Tk()
compiler.title('DOSA - Multilingual IDE')

# Set the style to 'clam' for the light theme
style = Style(compiler)
style.theme_use('clam')

# Add a menu option to toggle dark mode
theme_choice = StringVar()
theme_choice.set('clam')
dark_mode_menu = Menu(compiler, tearoff=0)
dark_mode_menu.add_radiobutton(label='Light Mode', variable=theme_choice, value='clam', command=toggle_dark_mode)
dark_mode_menu.add_radiobutton(label='Dark Mode', variable=theme_choice, value='alt', command=toggle_dark_mode)
menu_bar = Menu(compiler)
menu_bar.add_cascade(label='View', menu=dark_mode_menu)
compiler.config(menu=menu_bar)

editor = Text()
editor.pack()

code_output = Text(height=10)
code_output.pack()

compiler.mainloop()



