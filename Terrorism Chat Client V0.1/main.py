import json
import tkinter
import threading
import websocket
from tkinter import *
from tkinter import messagebox

#relx left to right
#rely top to bottom

class app(Frame):
    def __init__(self, master=None):
        self.ws = websocket.WebSocket()
        self.ws.connect('wss://Websocket.sachsthebased.repl.co')

        threading._start_new_thread(self.get_messages, (self, None))

        Frame.__init__(self, master)

        for guild in self.get_user()["Guilds"]:
            Button(root, text=guild["Name"], pady=7, command=None).place(relx=1, rely=0, anchor='ne')

        self.master = master
        self.pack(fill=BOTH, expand=1)
        self.configMenus()

        self.message_box = Entry(root, width=81)
        self.send_button = Button(root, text="Send", pady=7, command=self.send_message)

        self.message_box.place(relx=0.5, rely=0.63,anchor= CENTER)
        self.send_button.pack()

        self.messages = tkinter.Text(master, height=50, width=150)
        self.messages.place(relx=.5, rely=0.35,anchor= CENTER)

        root.bind('<Return>', self.send_message)

    def configMenus(self):
        menu = Menu(self.master)
        self.master.config(menu=menu)
        guilds = Menu(menu)
        menu.add_cascade(label="Rooms", menu=guilds)

        for guild in self.get_guilds()["Guilds"]:
            guilds.add_command(label=guild["Name"])

    def get_guilds(self):
        with open('user.json', 'r') as f:
            guilds = json.load(f)
        return guilds

    def send_message(self, placeholder=None):
        if len(str(self.message_box.get())) > 0:
            payload = {
                "Content": self.message_box.get(),
                "Token": "SachsIsBased",
                "Location": str(72)
            }
            self.message_box.delete(0, END)
            self.ws.send(json.dumps(payload))
            Format = f"\n{self.get_user()['Username']}: {payload['Content']}"
            self.messages.insert(tkinter.END, Format)
            self.messages.see("end")

    def get_messages(self, placeholder, placeholder2):
        Label(self.master, text="Messages\n").pack()
        while True:
            response = self.ws.recv()
            response = json.loads(response)
            Format = f"\n{response['Author']}: {response['Content']}"
            self.messages.insert(tkinter.END, Format)
            self.messages.see("end")

    def get_user(self):
        with open('user.json', 'r') as f:
            user = json.load(f)
        return user

root = Tk()
app = app(root)

root.wm_title("Terrorism Chat 1.0")
root.iconbitmap("terror.ico")
root.geometry("600x800")

root.mainloop()
