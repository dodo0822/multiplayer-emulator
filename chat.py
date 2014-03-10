import socket
import sendkey
import infowindow
from threading import Thread

class BgProcess(Thread):
    def __init__(self, app):
        Thread.__init__(self)
        self.app = app
        self._stop = False

    def stop(self):
        self._stop = True
        
    
    def run(self):
        window_id = sendkey.findwindow()
        
        nick = "dodo0822"
        channel = "#dodo0822"

        password = raw_input("Enter PW: ")

        server = "irc.twitch.tv"

        irc = socket.socket()
        irc.connect((server, 6667))

        irc.send("PASS " + password + "\n")
        irc.send("NICK " + nick + "\n")
        irc.send("JOIN " + channel + "\n")


        while not self._stop:
            line = irc.recv(1024)
            tokens = line.split(':')
            if len(tokens) > 2:
                if tokens[2] != "":
                    c = tokens[2].split('\n')[0]
                    print "Send to " + window_id + ": " + c
                    status = sendkey.sendkey(c, window_id)
                    if status:
                        user = tokens[1].split('!')[1].split('@')[0]
                        app.updateText(user + " : " + c[0:len(c)-1])

app = infowindow.runwindow()
thread = BgProcess(app)
thread.start()
app.mainloop()
