# toggle-vpn-launch-apps


### Configuration:

1. Open config.py and add your Cisco Any Connect password (String) for 'password' variable.
2. Add alias for your shell profile to path of vpnToggle.py script. 
   For example, if you use ZSH, add this to your .zshrc file in ~ directory.
   
    alias boot="python ~/wakeup/vpnToggle.py"

Options:

-off    Toggle VPN off (shut down Any Connect program)
-vpn    Toggle VPN on without laumnching additional programs
    
