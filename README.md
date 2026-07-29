# Hyprsaver
A simple script that can be used with hypridle to play Windows screensavers via Wine on Hyprland idle.

## The Issue
Since Hyprland tiles windows automatically, loading a screensaver via Wine will open each screensaver (there will be multiple if you have multiple monitors) as individual windows and attempt to tile them on the current workspace, rather than attempt to put them in full screen. To my knowledge, there is no easy configuration option that can be added to ``hyprland.conf`` to solve this, as each screensaver will have a different name, and etcetera. Moreover, having hypridle point directly to the wine command to load the screensaver causes an infinite pause-resume cycle within hypridle as, for whatever reason, wine screensavers cause input to be detected by hypridle on load, thus causing a resume and an infinite reload.
## The Solution
I created a simple Python script that uses ``hyprctl --batch`` commands to

1. Check whether there is a screensaver already loaded, and if not
2. Detect all monitors plugged in to computer
3. Open the screensaver windows
4. Tile the screensaver windows to each monitor
5. Put each screensaver window in full screen

There is a tad more than that, but that is the basics of how it functions.
## Usage
Run ``python3 hyprsaver.py path_to_screensaver.scr``, replacing ``path_to_screensaver.scr`` with the full path to the downloaded Windows screensaver. I also provided the hypridle config I am using, but, basically if you want to use it with hypridle, just set the ``on-timeout`` to the script (i.e. the command noted above).
