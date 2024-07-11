import pyfiglet
from random import randint
import time
import platform
import sys

#Defines Variables
banner = pyfiglet.figlet_format("Pingu Un-Fryer 3000")
bannerwelcome = pyfiglet.figlet_format("Welcome Space")
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
def StevenProgramKill():
    print("noooo steven badbadbadbad")
    time.sleep(3)
    exit()


def ProgramKill():
    print("No Access...")
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
    print("DONE! UNFRYING PINGU ENDED WITH SUCCESS!!! (Code: 0x0)")
    time.sleep(3)
    exit()
          
def Continue():
    print("Logging in... Please wait.")
    time.sleep(2)
    print(50*"#")
    print(bannerwelcome)
    print(50*"#")
    PinguYN = input("Welcome. Pingu was last fried today at #General. Do you wish to unfry him? (Y/N)")
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
    StevenProgramKill()
else:
    ProgramKill()




