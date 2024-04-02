import tkinter as tk
import sqlite3
class User():
    def __init__(self) -> None:
        self.name = ""
        self.email = ""
        self.history = []
        self.future = []

class HomeView(tk.Frame):
    def __init__(self, master, user):
        super().__init__(master)
        self.master = master
        self.user = user
        self.pack()
    
    def draw_navbar(self):

        self.navbar = tk.Frame(self.master, bg = "black")
        self.navbar.pack(side = tk.LEFT, padx= 5, pady= 5, fill = tk.Y)

        self.navigation = tk.Frame(self.navbar, bg = "#202020")
        self.navigation.pack(side = tk.TOP, padx = 5, pady= 5)

        self.home_button = tk.Button(self.navigation, text = "Home", bg = "#202020", borderwidth=0, command = lambda: self.master.switch_page(HomeView))
        self.home_button.pack(side = tk.TOP, padx= 5, pady= 5)

        self.search_button = tk.Button(self.navigation, text = "Search" , bg = "#202020", borderwidth=0, command = lambda: self.master.switch_page(None))
        self.search_button.pack(side = tk.TOP, padx= 5, pady= 5)

        self.playlists_frame = tk.Frame(self.navbar, bg = "#202020")
        self.playlists_frame.pack(side = tk.TOP)

        self.title = tk.Label(self.playlists_frame, text = "Your Library", bg = "#202020")
        self.title.pack(side = tk.LEFT, padx = 5, pady = 5)

        self.add_playlist = tk.Button(self.playlists_frame, text = "+", command = None)
        self.add_playlist.pack(side = tk.LEFT, padx = 5, pady = 5)



    def draw_middle(self):
        self.middle = tk.Frame(self.master)
        self.middle.pack(side = tk.LEFT, ipadx = 5, ipady=5, fill = tk.BOTH)

        self.header = tk.Frame(self.middle)
        self.header.pack(side = tk.TOP)

        if not len(self.user.history):
            backfg = "grey"
        else:
            backfg = "white"

        if not len(self.user.future):
            fowardfg = "grey"
        else:
            fowardfg = "white"

        self.back_btn = tk.Button(self.header, text = "<", fg = backfg, command = lambda: self.master.switch_page(None))
        self.back_btn.pack(side = tk.LEFT)

        self.forward_btn = tk.Button(self.header, text = ">", fg = fowardfg, command = lambda: self.master.switch_page(None))
        self.forward_btn.pack(side = tk.LEFT)
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
    def __init__(self, user, cursor):
        self.user = user
        self.cursor = cursor

class View():
    def __init__(self, master, user):
        self.master = master
        self.current_page = None
        self.user = user

    def open(self, page_class):
        if self.current_page:
            self.current_page.destroy()
        # Create new page
        self.current_page = page_class(self.master, self.user)
        self.current_page.draw()

class Controller():
    def __init__(self):
        self.user = User()
        conn = sqlite3.connect("SpotifyClone.db")
        self.model = Model(self.user, conn.cursor())
        self.root = tk.Tk()
        self.view = View(self.root, self.user)
        self.run()
        
    def run(self):
        self.view.open(HomeView)
        self.root.mainloop()

controller = Controller()
controller.run()