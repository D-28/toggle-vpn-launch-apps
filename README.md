# toggle-vpn-launch-apps

For MacOS Only

This vpnToggle.py script reads variables from config.py to automate VPN and launch everyday programs.



### Configuration:

1. Open config.py and add your Cisco Any Connect password (String) for 'password' variable.
2. Add alias for your shell profile to path of vpnToggle.py script. 
   For example, if you use ZSH, add this to your .zshrc file in ~ directory:
   
    alias boot="python ~/wakeup/vpnToggle.py"

Options:

"boot -off"   :     Toggle VPN off (shut down Any Connect program)

"boot -vpn"   :     Toggle VPN on without launching additional programs
    

NOTE:

1. Launch different programs by changing the path for sys.run() command in vpnToggle.py
2. pyautogui.position() is used to get X,Y Coordinates of mouse position at runtime. 
3. VIP Access / Cisco Any Connect always launch to same relative window position. 
4. The coordinates for clicking the aforementioned program buttons are found in config.py.
5. Modify these coordinates if necessary. 
