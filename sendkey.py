from subprocess import call
from subprocess import check_output
from time import sleep

def findwindow():
    wm_output = check_output(["wmctrl", "-lp"])
    
    n = ""
    
    for line in wm_output.split('\n'):
        if line != '':
            if "VBA-M" in line:
                print int(line.split(' ')[0][2:], 16)
                n = str(int(line.split(' ')[0][2:], 16))

    if n != "":
        print "VBA-M window ID# => " + n
    else:
        print "Cannot find VBA-M window!"

    return n

def sendkey(k, n):
    if k == "A" or k == "a":
        k = "z"

    if k == "B" or k == "b":
        k = "x"

    if k == "down":
        k = "Down"

    if k == "up":
        k = "Up"

    if k == "left":
        k = "Left"

    if k == "right":
        k = "Right"

    if k == "start":
        k = "Return"
    call(["xdotool", "windowactivate", n])
    sleep(0.1)
    call(["xdotool", "keydown", k])
    sleep(0.25)
    call(["xdotool", "keyup", k])

