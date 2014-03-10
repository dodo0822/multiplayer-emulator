import socket

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
    print line
