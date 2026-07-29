import time
import subprocess
import json
import sys
displays = []
windowsOne = []
windowsTwo = []
screensaverWins = []
screensaverFile = ""
for arg in sys.argv[1:]:
    screensaverFile += arg
    
print(screensaverFile)

def moveScreensavers():
    for i, screensaver in enumerate(screensaverWins):
        subprocess.Popen(['hyprctl', '--batch', 
            f'dispatch focuswindow address:{screensaver} ; dispatch fullscreen 0 ; dispatch movewindow mon:{displays[i]}'])
        print("moved", screensaver)
        time.sleep(1)
def getScreensaverWins():
    if len(windowsTwo) > len(windowsOne):
        while len(windowsTwo) > len(windowsOne):
            windowsOne.append(0)
        
        for i, window in enumerate(windowsTwo):
            if window != windowsOne[i]:
                screensaverWins.append(window)
                print("got screensaver", window)
    else:
        screensaverWins.append("none")
                        
def getMonitors():
    monitorDataRaw = (subprocess.run(['hyprctl', 'monitors', 'all', '-j'], stdout=subprocess.PIPE)).stdout
    monitorDataJson = json.loads(monitorDataRaw.decode('utf-8'))\
    
    for i, monitor in enumerate(monitorDataJson):
        displays.append(monitorDataJson[i]["name"])
        print("got monitor", monitor)
        
def getWindows(windows):
    windowDataRaw = (subprocess.run(['hyprctl', 'clients', '-j'], stdout=subprocess.PIPE)).stdout
    windowDataJson = json.loads(windowDataRaw.decode('utf-8'))\
    
    for i, window in enumerate(windowDataJson):
        windows.append(windowDataJson[i]["address"])

def moveCursor():
    subprocess.Popen(["hyprctl", "dispatch", "movecursor", "-1000", "0"], stdout=subprocess.DEVNULL)

isOpen = ((subprocess.run(["pgrep", r"\.scr$"], stdout=subprocess.PIPE)).stdout).decode('utf-8')
if isOpen == "":
    print("no saver open :)")
    moveCursor()
    getMonitors()
    getWindows(windowsOne)
    subprocess.Popen(["wine", screensaverFile, "/s"], stdout=subprocess.DEVNULL)
    time.sleep(1)
    getWindows(windowsTwo)
    getScreensaverWins()
    moveScreensavers()
else:
    print("saver already open :(")
