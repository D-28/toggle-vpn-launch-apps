from config import *
import pyautogui
import subprocess
import time
import sys
import os
import webbrowser

def toggleVPNoff():
  os.system("open /Applications/Cisco/Cisco AnyConnect Secure Mobility Client.app")
  time.sleep(1)
  pyautogui.click(x=acX, y=acY)
  time.sleep(1)
  pyautogui.hotkey('command', 'q')

def toggleVPNon():
  os.system("open \"/Applications/VIP Access.app\"")
  time.sleep(1)
  pyautogui.click(x=vpnX, y=vpnY)
  os.system("open \"/Applications/Cisco/Cisco AnyConnect Secure Mobility Client.app\"")
  time.sleep(2)
  pyautogui.click(x=acX, y=acY)
  time.sleep(1)
  pyautogui.typewrite(password)
  pyautogui.hotkey('command', 'v')
  pyautogui.hotkey('enter')
  time.sleep(1)
  pyautogui.hotkey('enter')
  time.sleep(1)
  pyautogui.hotkey('enter')
  time.sleep(1)
  pyautogui.hotkey('enter')

def launchApps():
  subprocess.run(["open", "/Applications/Slack.app"])
  webbrowser.open('https://mail.google.com/mail/u/0/')

if __name__ == '__main__':
  if (len(sys.argv) > 1 and sys.argv[1] == "-off"):
    toggleVPNoff()
  elif (len(sys.argv) > 1 and sys.argv[1] == "-vpn"):
      toggleVPNon()
  else:
    toggleVPNon()
    launchApps()
