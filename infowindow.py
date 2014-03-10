from Tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.parent = master
        self.hide = False
        self.initUI()

    def togglehide(self, event):
        self.parent.overrideredirect(not self.hide)
        self.hide = not self.hide
        self.parent.withdraw()
        self.parent.deiconify()

    def updateText(self, text):
        self.outputBox.insert(END, text + "\n")

    def initUI(self):
        self.outputBox = Text(self.parent, bg='black', height=20, fg='white', relief='flat', highlightthickness=0, yscrollcommand='TRUE')
        self.outputBox.pack(fill='both', expand=True)
        self.outputBox.insert(END, "hello\n")
        self.outputBox.bind("<Button-1>", self.togglehide)

def runwindow():
    root = Tk()
    # Code to add widgets will go here...
    app = Application(root)
    #app.parent.overrideredirect(True)
    app.parent.configure(background = 'black')
    app.parent.geometry('300x528+716+57')
    return app
