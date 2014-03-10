from subprocess import call
from time import sleep
n = raw_input("Process id: ")

while True:
    k = raw_input("Key: ")
    call(["xdotool", "windowactivate", n])
    sleep(0.1)
    call(["xdotool", "keydown", k])
    sleep(0.25)
    call(["xdotool", "keyup", k])

