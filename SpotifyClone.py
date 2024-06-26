import tkinter as tk
import sqlite3
import datetime
class User():
    def __init__(self) -> None:
        self.id = 1
        self.name = ""
        self.email = ""
        self.history = []
        self.future = []

class Model():
    def __init__(self, user, cursor):
        self.user = user
        self.cursor = cursor

    def get_playlists(self, id: int) -> list:
        self.cursor.execute("SELECT * FROM playlist WHERE userid = ?", (id,))
        return self.cursor.fetchall()

    def get_songs_in_playlist(self, id: int) -> list:
        self.cursor.execute("SELECT * FROM songs_playlist WHERE playlistid = ?", (id,))
        return self.cursor.fetchall()
    
    def get_artist(self, id: int) -> list:
        self.cursor.execute("SELECT * FROM artist WHERE id = ?", (id,))
        return self.cursor.fetchall()[0]
    
    def get_song(self, id: int) -> list:
        self.cursor.execute("SELECT * FROM songs where id = ?", (id,))
        return self.cursor.fetchall()[0]
    
    def get_album(self, id: int) -> list:
        self.cursor.execute("SELECT * FROM album WHERE id = ?", (id,))
        return self.cursor.fetchall()[0]
    
    def convert_str_datetime(self, date: str) -> datetime.datetime:
        return datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    
    def time_difference(self, date: datetime.datetime) -> str:
        diff = datetime.datetime.now() - date
        if (diff.days):
            # Added less then 7 days
            if (diff.days < 7):
                if (diff.days == 1):
                    return str(diff.days) + " day ago"
                else:
                    return str(diff.days) + " days ago"
            else:
                if (diff.days < 28):
                    weeks = int(diff.days / 4)
                    if (weeks == 1):
                        return str(weeks) + " week ago"
                    return str(weeks) + " weeks ago"
                else:
                    return date.strftime("%b %d, %Y")
        else:
            # Added less then 60 seconds ago
            if (diff.total_seconds() < 60):
                return str(int(diff.total_seconds())) + " seconds ago"
            else:
                # Added less then 60 minutes ago
                if (diff.total_seconds() / 60 < 60):
                    return str(int(diff.total_seconds() / 60)) + " minute ago"
                else:
                    hours = int(diff.total_seconds() / 3600)
                    if (hours == 1):
                        return str(hours) + " hour ago"
                    return str(hours) + " hours ago"

class HomeView(tk.Frame):
    def __init__(self, master, user, model):
        super().__init__(master)
        self.master = master
        self.user = user
        self.model = model
        self.cur_playlist = 1
        self.middle_sec = "P"
        self.pack()
    
    def draw_navbar(self):
        self.navbar = tk.Frame(self.master, bg = "black")
        self.navbar.pack(side = tk.LEFT, padx= 5, pady= 5, fill = tk.Y)

        self.navigation = tk.Frame(self.navbar, bg = "#202020")
        self.navigation.pack(side = tk.TOP, padx = 5, pady= 5)

        self.home_button = tk.Button(self.navigation, text = "Home", bg = "#202020", borderwidth=0, command = lambda: self.change_middle('H'))
        self.home_button.pack(side = tk.TOP, padx= 5, pady= 5)

        self.search_button = tk.Button(self.navigation, text = "Search" , bg = "#202020", borderwidth=0, command = lambda: self.master.switch_page(None))
        self.search_button.pack(side = tk.TOP, padx= 5, pady= 5)

        self.home_button.bind("<Button-1>", lambda event, s = "Home": self.change_middle(s))
        self.search_button.bind("<Button-1>", lambda event, s = "Search": self.change_middle(s))

        self.playlists_frame = tk.Frame(self.navbar, bg = "#202020")
        self.playlists_frame.pack(side = tk.TOP)

        self.title = tk.Label(self.playlists_frame, text = "Your Library", bg = "#202020")
        self.title.pack(side = tk.TOP, padx = 5, pady = 5)

        self.add_playlist = tk.Button(self.playlists_frame, text = "+", command = None)
        self.add_playlist.pack(side = tk.TOP, padx = 5, pady = 5)

        playlists = self.model.get_playlists(self.user.id)
        for playlist in playlists:
            frame = tk.Frame(self.playlists_frame, bg = "#202020")
            frame.pack(side = tk.TOP)

            title = tk.Label(frame, text = str(playlist[1]), fg = "white", bg = "#202020")
            title.pack(side = tk.TOP, padx = 5, pady = 5)

            frame.bind("<Enter>", lambda event, f=frame: self.hover_on(f))
            frame.bind("<Leave>", lambda event, f=frame: self.hover_off(f))

            frame.bind("<Button-1>", lambda event, p=playlist[0]: self.change_middle(p))
            title.bind("<Button-1>", lambda event, p=playlist[0]: self.change_middle(p))

    def change_middle(self, section) -> None:
        if (type(section) == int):
            self.middle_sec = "P"
            self.cur_playlist = section
        else:
            self.middle_sec = section
        self.middle.destroy()
        self.draw_middle()

    def draw_playlist(self):
        self.songs_frame = tk.Frame(self.middle, bg = "#202020")
        self.songs_frame.pack(side = tk.TOP)

        songs = self.model.get_songs_in_playlist(self.cur_playlist)
        for song in enumerate(songs):
            frame = tk.Frame(self.songs_frame, bg = "#202020")
            frame.pack(side = tk.TOP, fill= tk.X, expand = tk.TRUE)
            
            tk.Label(frame, text = str(song[0] + 1), bg = "#202020").pack(side = tk.LEFT)
            names = tk.Frame(frame, bg = "#202020")
            names.pack(side = tk.LEFT)

            song_data = self.model.get_song(song[1][1])
            tk.Label(names, fg = "white", text = song_data[1], bg = "#202020").pack(anchor = tk.NW)
            tk.Label(names, fg = "gray", text = self.model.get_artist(song_data[6])[1], bg = "#202020", font=("Helvetica", 8)).pack(anchor = tk.NW)

            tk.Label(frame, text = self.model.get_album(song_data[2])[1], bg = "#202020", fg = "gray").pack(side = tk.LEFT, ipadx= 5, ipady = 5)

            tk.Label(frame, text = self.model.time_difference(self.model.convert_str_datetime(song[1][2])), bg = "#202020", fg = "gray").pack(side = tk.LEFT, ipadx= 5, ipady = 5)

            tk.Label(frame, text = song_data[5], bg = "#202020", fg = "gray").pack(side = tk.LEFT, ipadx= 5, ipady = 5)
            frame.bind("<Enter>", lambda event, f=frame: self.hover_on(f))
            frame.bind("<Leave>", lambda event, f=frame: self.hover_off(f))

    def draw_home(self) -> None:
        self.type_frame = tk.Frame(self.middle)
        self.type_frame.pack(side = tk.TOP)

        tk.Button(self.type_frame, text = "All", command = None).pack(side = tk.LEFT)
        tk.Button(self.type_frame, text = "Music", command = None).pack(side = tk.LEFT)
        tk.Button(self.type_frame, text = "Podcasts", command = None).pack(side = tk.LEFT)
        tk.Button(self.type_frame, text = "Audiobooks", command = None).pack(side = tk.LEFT)
        
    def draw_middle(self):
        self.middle = tk.Frame(self.master, bg = "#202020")
        self.middle.pack(side = tk.LEFT, ipadx = 5, ipady=5, fill = tk.BOTH, expand = tk.TRUE)

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

        if self.middle_sec == "P":
            self.draw_playlist()
        elif self.middle_sec == "H":
            self.draw_home()
        
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
    
    def hover_on(self, widget: tk.Widget) -> None:
        widget.config(bg = "lightgray")
        if type(widget) == tk.Frame:
            widgets = widget.winfo_children()
            for widget in widgets:
                self.hover_on(widget)

    def hover_off(self, widget: tk.Widget) -> None:
        widget.config(bg = "#202020")
        if type(widget) == tk.Frame:
            widgets = widget.winfo_children()
            for widget in widgets:
                self.hover_off(widget)

class View():
    def __init__(self, master, user, model):
        self.master = master
        self.current_page = None
        self.user = user
        self.model = model

    def open(self, page_class):
        if self.current_page:
            self.current_page.destroy()
        # Create new page
        self.current_page = page_class(self.master, self.user, self.model)
        self.current_page.draw()

class Controller():
    def __init__(self):
        self.user = User()
        conn = sqlite3.connect("SpotifyClone.db")
        self.model = Model(self.user, conn.cursor())
        self.root = tk.Tk()
        self.view = View(self.root, self.user, self.model)
        self.run()
        
    def run(self):
        self.view.open(HomeView)
        self.root.mainloop()

controller = Controller()
controller.run()