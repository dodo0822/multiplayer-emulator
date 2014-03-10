import socket
import sendkey

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


while True:
    line = irc.recv(1024)
    tokens = line.split(':')
    if len(tokens) > 2:
        if tokens[2] != "":
            c = tokens[2].split('\n')[0]
            print "Send to " + window_id + ": " + c
            sendkey.sendkey(c, window_id)
