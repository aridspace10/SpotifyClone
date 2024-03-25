import tkinter as tk
class HomeView(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()
        # Add widgets for the home page
class Model():
    def __init__(self):
        pass

class View():
    def __init__(self, master):
        self.master = master
        self.current_page = None

    def open(self, page_class):
        if self.current_page:
            self.current_page.destroy()
        # Create new page
        self.current_page = page_class(self.master)
        self.current_page.pack()

class Controller():
    def __init__(self):
        self.model = Model()
        self.root = tk.Tk()
        self.view = View(self.root)
        self.run()
        self.root.mainloop()
    
    def run(self):
        self.view.open(HomeView)

controller = Controller()
controller.run()