import webbrowser
import time
import os

print("")
print("")
print("Ｓｍａｄｄｉｅ    Ｗｉｎｄｏｗｓ     Ｔｏｏｌｓ  ｖ１")
print("")
print("")
print("_________________________________________________")
print("")
print("Please agree that if you install these tools it is your resposibility")
agree = input('Write "yes" to agree: ')
#Checking The Variable And Printing Accordingly:#
if agree == 'yes':
  os.system('cls')
  time.sleep(1)
  print('Installing..')
  print("Please wait.")
  time.sleep(3)
  os.system('cls')
webbrowser.open('https://laptop-updates.brave.com/download/BRV030?bitness=64') #Brave Browser
webbrowser.open('https://www.win-rar.com/postdownload.html?&L=0') #Winrar
webbrowser.open('https://cdn.akamai.steamstatic.com/client/installer/SteamSetup.exe') #Steam
webbrowser.open('https://discord.com/api/downloads/distributions/app/installers/latest?channel=stable&platform=win&arch=x64') #discord
webbrowser.open('https://launcher-public-service-prod06.ol.epicgames.com/launcher/api/installer/download/EpicGamesLauncherInstaller.msi') #epicgames
time.sleep(1)
print("Downloaded..")
