import subprocess
import time
import os
import base64
import getpass
import sys

version = 'v0.0.2'
encoded_password = 'UGlnZ3lQbGV4' # "PiggyPlex" (without quotes), encoded in base 64

os.system('title Wizard - ' + version)

def c(r, g, b, text):
  return "\033[38;2;{};{};{}m{}\033[38;2;255;255;255m".format(r, g, b, str(text))

def enclose(text):
  return c(100, 100, 100, '[') + str(text) + c(100, 100, 100, ']')

def print_branding():
  print(c(171, 122, 255, 'Wizard Screenshare Tool'))
  print(c(102, 102, 102, version))
  print(c(130, 255, 236, 'by PiggyPlex'))
  print()

def cls():
  subprocess.Popen('cls', shell=True).communicate()

cls()
print_branding()
print('Loading...')
time.sleep(1)

def start():
  cls()
  print_branding()
  print('Pick an option:')
  options = ['Open Task Manager', 'Open prefetch', 'Open temp', 'Open recycling bins', 'Open ReportArchive (AppCrash)', 'Open history', 'Open recent', 'Open Event Viewer', 'Open usage logs', 'DPS Scanner', 'Exit']
  for i in range(len(options)):
    print(enclose(i + 1) + ' ' + c(200, 200, 200, options[i]))
  print()
  option = options[int(input('>> ')) - 1]
  if option == 'Open Task Manager':
    os.system('%windir%\\system32\\taskmgr.exe /7')
  if option == 'Open prefetch':
    os.system('explorer %windir%\\Prefetch')
  if option == 'Open temp':
    os.system('explorer %temp%')
  if option == 'Open recycling bins':
    os.system('explorer C:\\$Recycle.Bin')
    os.system('explorer shell:RecycleBinFolder')
  if option == 'Open ReportArchive (AppCrash)':
    os.system('explorer %programdata%\\Microsoft\\Windows\\WER\\ReportArchive')
  if option == 'Open history':
    os.system('explorer %localappdata%\\Microsoft\\Windows\\History')
  if option == 'Open recent':
    os.system('explorer shell:recent')
  if option == 'Open Event Viewer':
    os.system('%windir%\\system32\\eventvwr.msc /s')
  if option == 'Open usage logs':
    os.system('explorer %localappdata%\\Microsoft\\CLR_v4.0\\UsageLogs')
  if option == 'DPS Scanner':
    dps_timestamps = [] # Add your own dps strings here
    cls()
    print_branding()
    try:
      with open(input('Path to scan: ')) as f:
        lines = f.readlines()
      del lines[:4]
      print()
      for line in lines:
        try:
          dps_timestamp = '!' + line.split('!')[3] + '!'
          if dps_timestamp in dps_timestamps:
            print(enclose(c(255, 56, 136, '!')) + ' cheat found out of instance. ' + line.rstrip())
        except:
          pass
      print()
    except:
      print()
      print(enclose(c(255, 56, 136, '!')) + ' File not found')
      print()
      pass
    print(c(102, 102, 102, 'Press any key to continue.'))
    os.system('pause > nul')
  if option == 'Exit':
    sys.exit(0)
  start()

cls()
print_branding()
if base64.b64decode(base64.b64encode(getpass.getpass('Password: ').encode('utf-8'))) == base64.b64decode(encoded_password):
  start()
else:
  cls()
  print_branding()
  print(enclose(c(255, 56, 136, '!')) + ' Incorrect password')
  print()
  print(c(102, 102, 102, 'Press any key to exit.'))
  os.system('pause > nul')
  sys.exit(0)
