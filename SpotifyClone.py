import tkinter as tk
class HomeView(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()
    
    def draw_navbar(self):
        self.navbar = tk.Frame(self.master)
        self.navbar.pack(side = tk.LEFT)

        self.navigation = tk.Frame(self.navbar)
        self.navigation.pack(side = tk.TOP)

        self.home_button = tk.Button(self.navigation, text = "Home", command = lambda: self.master.switch_page(HomeView))
        self.home_button.pack(side = tk.TOP)

        self.search_button = tk.Button(self.navigation, text = "Search", command = lambda: self.master.switch_page(None))
        self.search_button.pack(side = tk.TOP)

        self.playlists_frame = tk.Frame(self.navbar)
        self.playlists_frame.pack(side = tk.TOP)

    def draw_middle(self):
        self.middle = tk.Frame(self.master)
        self.middle.pack(side = tk.LEFT)

    def draw_right(self):
        self.right = tk.Frame(self.master)
        self.right.pack(side = tk.LEFT)
    
    def draw_bottom(self):
        self.bottom = tk.Frame(self.master)
        self.bottom.pack(side = tk.BOTTOM)

    def draw(self):
        self.draw_navbar()
        self.draw_middle()
        self.draw_right()
        self.draw_bottom()
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
        self.current_page.draw()

class Controller():
    def __init__(self):
        self.model = Model()
        self.root = tk.Tk()
        self.view = View(self.root)
        self.run()
        
    def run(self):
        self.view.open(HomeView)
        self.root.mainloop()

controller = Controller()
controller.run()