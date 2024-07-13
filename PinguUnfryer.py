import pyfiglet
from random import randint
import time
import platform
import sys

#Defines Variables
banner = pyfiglet.figlet_format("Pingu Un-Fryer 3000")
bannerwelcome = pyfiglet.figlet_format("Welcome Space")
bannersteven = pyfiglet.figlet_format("Welcome Steven")
bannerpingu = pyfiglet.figlet_format("Welcome Pingu")
hour = randint(0,24)
minute = randint(0,59)
system = platform.system()
release = platform.release()
version = platform.version()
arch = platform.architecture()
machine = platform.machine()

#Shows Banner and system information
print(50*"#")
print(banner)
print(50*"#")
print("Checking OS information, please wait...")
time.sleep(2)
print(system, release, version)
print(arch)
print(machine)
print(50*"#")

#Defines all functions
def Pingu():
    print("Logging in... Please wait.")
    time.sleep(2)
    print(50*"#")
    print(bannerpingu)
    print(50*"#")
    PinguQ = input("Welcome Pingu. You are being fried in #general. Do you wish to stop the frying process? (Y/N):")
    if PinguQ == "Y":
        StopFry()
    elif PinguQ == "N":
        ProgramKill2()
    else:
        ProgramKill3()

def StopFry():
    print("Stopping the frying process. Please wait...")
    time.sleep(1)
    for i in range(5):
        print("Working, Please Wait...")
        time.sleep(3)
    print("Process Stopped Successfully. (Code: 0x0)")
    time.sleep(3)
    exit()

def Steven():
    print("Logging in... Please wait.")
    time.sleep(2)
    print(50*"#")
    print(bannersteven)
    print(50*"#")
    StevenYN = input("Welcome Steven. Do you wish to unfry Pingu (U) or Re-Fry him? (R):" )
    if StevenYN == "U":
        UnfryQ()
    elif StevenYN == "R":
        Refry()
    else:
        ProgramKill3()
        
def Refry():
    RefryQ = input("Do you really want to deep re-fry Pingu? (Y/N)? ")
    if RefryQ == "Y":
        print("Refrying Pingu, please wait...")
        time.sleep(2)
        print("Wait...")
        time.sleep(2)
        print("Why would you fry Pingu? Why are you so mean...?")
        time.sleep(3)
        print("You made me angwy. I will remove system32 from your pc.")
        time.sleep(1)
        print("Enjoy some music in those last moments with your PC.")
        print("Music will be added in next version so stay tuned - dawu")
        time.sleep(2)
        print("Oh, sorry nevermind. I will just kill the program instead.")
        time.sleep(2)
        exit()
    elif RefryQ == "N":
        ProgramKill2()
    else:
        ProgramKill3()
        
def ProgramKill3():
    print("Thats not an option. Killing program...")
    exit()

def ProgramKill():
    print("No. You don't have access.")
    time.sleep(3)
    exit()
    
def ProgramKill2():
    print("So why are you even logging in?")
    time.sleep(3)
    exit()

def PinguUnfry():
    print("Unfrying Pingu, please wait...")
    time.sleep(1)
    for i in range(5):
        print("Working, Please Wait...")
        time.sleep(3)
    print("DONE! UNFRYING PINGU ENDED SUCCESSFULLY!!! (Code: 0x0)")
    time.sleep(3)
    exit()
          
def Continue():
    print("Logging in... Please wait.")
    time.sleep(2)
    print(50*"#")
    print(bannerwelcome)
    print(50*"#")
    UnfryQ()

def UnfryQ():
    PinguYN = input("Pingu was last fried today at #General. Do you wish to unfry him? (Y/N)")
    if PinguYN == "Y":
        PinguUnfry()
    else:
        ProgramKill2()

#Password = SgDepIsBest
username = input("Enter Roblox Username: ")
if username == "SpaceIDragon":
    password = input("Enter Password: ")
    if password == "SgDepIsBest":
        Continue()
    else:
        print("thats not you space!!!!")
        time.sleep(3)
        exit()
elif username == "RealStevenHaha":
    password = input("Enter Password: ")
    if password == "DontFryThePenguin":
        Steven()
    else:
        ProgramKill()

elif username == "PeppyThePingu":
    password = input("Enter Password: ")
    if password == "ShrimpyThePingu":
        Pingu()
    else:
        ProgramKill()

else:
    print("Wrong Username!")
    time.sleep(2)
    exit()



