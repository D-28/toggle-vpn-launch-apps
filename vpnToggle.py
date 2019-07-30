from config import *
import pyautogui
import subprocess
import time
import sys
import webbrowser

def toggleVPNoff():
  subprocess.run(
      ["open", "/Applications/Cisco/Cisco AnyConnect Secure Mobility Client.app"])
  time.sleep(1)
  pyautogui.click(x=acX, y=acY)
  time.sleep(1)
  pyautogui.hotkey('command', 'q')

def toggleVPNon():
  subprocess.run(["open", "/Applications/VIP Access.app"])
  time.sleep(0.5)
  pyautogui.click(x=vpnX, y=vpnY)
  subprocess.run(
      ["open", "/Applications/Cisco/Cisco AnyConnect Secure Mobility Client.app"])
  time.sleep(1)
  pyautogui.moveTo(acX, acY, duration=0.10)
  pyautogui.click(x=acX, y=acY)
  time.sleep(0.5)
  pyautogui.typewrite(password)
  pyautogui.hotkey('command', 'v')
  pyautogui.hotkey('enter')
  time.sleep(1)
  pyautogui.hotkey('enter')
  pyautogui.hotkey('enter')
  pyautogui.hotkey('enter')
  time.sleep(3)
  pyautogui.hotkey('command', 'q')

def launchApps():
  subprocess.run(["open", "/Applications/Microsoft Outlook.app"])
  subprocess.run(["open", "/Applications/Slack.app"])
  # subprocess.run(["open", "/Applications/Telegram.app"])
  # subprocess.run(["open", "/Applications/Messages.app"])

  webbrowser.open('https://mail.google.com/mail/u/1/')
  webbrowser.open('https://mail.google.com/mail/u/0/')

if __name__ == '__main__':
  if (len(sys.argv) > 1 and sys.argv[1] == "-off"):
    toggleVPNoff()
  elif (len(sys.argv) > 1 and sys.argv[1] == "-vpn"):
      toggleVPNon()
  else:
    toggleVPNon()
    launchApps()
