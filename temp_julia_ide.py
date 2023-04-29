import tkinter as tk
from tkinter.ttk import Style

class JuliaIDE:
    def __init__(self, master):
        self.master = master
        self.master.title('Julia IDE')
        self.current_theme = tk.StringVar()
        self.current_theme.set('clam')
        self.style = Style(self.master)
        self.style.theme_use('clam')
        self.menu_bar = tk.Menu(self.master)
        self.dark_mode_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.dark_mode_menu.add_radiobutton(label='Light Mode', variable=self.current_theme, value='clam', command=self.toggle_theme)
        self.dark_mode_menu.add_radiobutton(label='Dark Mode', variable=self.current_theme, value='alt', command=self.toggle_theme)
        self.menu_bar.add_cascade(label='View', menu=self.dark_mode_menu)
        self.master.config(menu=self.menu_bar)
        self.editor_frame = tk.Frame(self.master)
        self.editor_frame.pack(fill='both', expand=True)
        self.editor = tk.Text(self.editor_frame)
        self.editor.pack(side='left', fill='both', expand=True)
        self.editor_scrollbar = tk.Scrollbar(self.editor_frame, command=self.editor.yview)
        self.editor_scrollbar.pack(side='right', fill='y')
        self.editor.config(yscrollcommand=self.editor_scrollbar.set)
        self.output_frame = tk.Frame(self.master)
        self.output_frame.pack(fill='both', expand=True)
        self.code_output = tk.Text(self.output_frame, height=10)
        self.code_output.pack(side='left', fill='both', expand=True)
        self.code_output_scrollbar = tk.Scrollbar(self.output_frame, command=self.code_output.yview)
        self.code_output_scrollbar.pack(side='right', fill='y')
        self.code_output.config(yscrollcommand=self.code_output_scrollbar.set)

    def toggle_theme(self):
        current_theme = self.current_theme.get()

        if current_theme == 'clam':
            self.style.theme_use('alt')
            self.current_theme.set('alt')
        else:
            self.style.theme_use('clam')
            self.current_theme.set('clam')

root = tk.Tk()
ide = JuliaIDE(root)
root.mainloop()
