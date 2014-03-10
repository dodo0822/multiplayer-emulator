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

def isnumber(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def sendkey(key, n):
    k = ""

    tokens = key.lower().strip().split('*')
    times = 1
    key = tokens[0]

    if len(tokens) > 1:
        if isnumber(tokens[1]):
            times = int(tokens[1])
            if times > 10 or times < 1:
                times = 1
    
    if key == "a":
        k = "z"
    elif key == "b":
        k = "x"
    elif key == "down":
        k = "Down"
    elif key == "up":
        k = "Up"
    elif key == "left":
        k = "Left"
    elif key == "right":
        k = "Right"
    elif key == "start":
        k = "Return"
    else:
        print "Unknown key"
        return False

    print "Press " + k + " for " + str(times) + " time(s)"
    
    for i in range(0, times):
        call(["xdotool", "windowactivate", n])
        sleep(0.1)
        call(["xdotool", "keydown", k])
        sleep(0.25)
        call(["xdotool", "keyup", k])
        if times > 1:
            sleep(0.1)

    return True
