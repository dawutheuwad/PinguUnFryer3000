import pyfiglet # type: ignore
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

def MisteryKill():
    print("JAJAJAJA YOU DUMB IDIOT YOU DONT KNOW THE MYSTERY MAN CODE HEHEHEHEHEHAHAHEHAHAEH GO EAT A HEDGEHOG!+!+!+!343")
    time.sleep(4)
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

def vigenere_decode(encoded_text_bytes, dfsfghjdkfsagghadfg342ö):
    # Convert hex to byte string
    encoded_text = encoded_text_bytes.decode('latin1');
    
    # Obfuscate the key usage
    a123431423421432joik3425h342ji5h342i6346 = [
        dfsfghjdkfsagghadfg342ö[:8],
        dfsfghjdkfsagghadfg342ö[8:16][::-1],
        dfsfghjdkfsagghadfg342ö[16:24],
        dfsfghjdkfsagghadfg342ö[24:32][::-1],
        dfsfghjdkfsagghadfg342ö[32:40],
        dfsfghjdkfsagghadfg342ö[40:48][::-1],
        dfsfghjdkfsagghadfg342ö[48:56],
        dfsfghjdkfsagghadfg342ö[56:64][::-1],
        dfsfghjdkfsagghadfg342ö[64:]
    ]
    
    # Reconstruct the key
    reconstructed_key = ''.join([
        a123431423421432joik3425h342ji5h342i6346[0],
        a123431423421432joik3425h342ji5h342i6346[1][::-1],
        a123431423421432joik3425h342ji5h342i6346[2],
        a123431423421432joik3425h342ji5h342i6346[3][::-1],
        a123431423421432joik3425h342ji5h342i6346[4],
        a123431423421432joik3425h342ji5h342i6346[5][::-1],
        a123431423421432joik3425h342ji5h342i6346[6],
        a123431423421432joik3425h342ji5h342i6346[7][::-1],
        a123431423421432joik3425h342ji5h342i6346[8]
    ])

    key_length = len(reconstructed_key)
    decoded_chars = []

    for i, char in enumerate(encoded_text):
        key_char = reconstructed_key[i % key_length]
        decoded_char = chr((ord(char) - ord(key_char)) % 256)
        decoded_chars.append(decoded_char)

    return ''.join(decoded_chars)
        
def qjat_zhe_gfjgucj():
    print(pyfiglet.figlet_format("logging in as big big man?"))
    time.sleep(2)
    print("getting super secre t pig big man stuff...")
    
    for i in range(0, 10):
        print(f"progress: {i * 10}%")
        time.sleep(randint(10, 40) / 10)

    if input("almost logged in as the big pig bistery man. but something is wrong, so tell me something epic. \n") == "beans":
        print("good job big misterios not actually men. what would you like to do? ")
        match str(input("type the code of what you'd like to do: ")):
            case "0b12389ö556854":
                print(pyfiglet.figlet_format("CODE RED PROTOCOL INITIATED."))
                time.sleep(1)
                print("PREPARING.....")

                for i in range(0, 10):
                    print(f"progress: {i * 10}%")
                    time.sleep(randint(10, 40) / 10)

                input("are you sure you want to do this?")
                print("i dont actually care what you want im too deep into this now heheheeh.")

                time.sleep(3)

                print(pyfiglet.figlet_format("launcched protocol step 1."))

                print("launching step 2....")
                time.sleep(randint(1, 12))

                print("step 2 completed successfully...")

                print("processing final step")

                for i in range(0, 20):
                    print(f"progress: {i * 10}%")
                    time.sleep(randint(10, 40) / 10)

                key = input(pyfiglet.figlet_format("OH FUCK I ALMOST FORGOT ABOUT THIS. WHATS THE SECRET KEY?"))
                decoded_text = vigenere_decode(bytes.fromhex("d8d3c9c890dacad685d5d8dae595dce8d7cbcad5d8d9e9dcdee887d6c6ddd9d4ebcfd9a1"),key)
                
                print("checking result....")
                
                print(" if you entered the correct key, thou shalt know the truth. if you get gibbrish, L, otherwise, you shall know the truth.")
                time.sleep(10)

                print("ok sorry my bad for taking this long")
                print("here is your answer bib big mann't")

                time.sleep(1)
                print(decoded_text)
                exit()

            case "cook bred":
                print("we have bread idiot.")
                exit()
            
            case "red_button":
                print("ARE YOU SURE YOU WANT TO NUKE #GENERAL, TO PREVENT PINGU FROM BEING FRIED???")
                res = input("?: ")

                if res == "Y":
                    print(" OK BOSS, NUKING #GENERAL. ")
                    time.sleep(10)

                    print("you died lmfao.")
                    exit()

            case "unfry":
                time.sleep(1)
                print("just steal the identity of steven lmfao.")

            case _: 
                MisteryKill()

    else: MisteryKill()

def lowah():
    print(pyfiglet.figlet_format("fvb dhua svyl?"))
    time.sleep(2)
    print("svyl svhkpun...")
    lowahYN = input("dlsjvtl kv fvb sprl booo av zll svyl dl ohcl olyl (f)/(u)? ")
        if lowahYN == "f":
        print("Pu aol myvzaf avdu vm Dhkkslibyn, aol punlupvbz fla zspnoasf tpznbpklk wlunbpu pucluavy, Ky. Mshwqhjr TjZxbhdr, buclpslk opz shalza jylhapvu: aol Myfpun Thjopul Aoha Myplz Wlunbpuz.")
        time.sleep(1)
        print("Pualuklk av il h ylcvsbapvuhyf jvvrpun klcpjl, pa puzalhk iljhtl h slnlukhyf kpzhzaly.")
        time.sleep(1)
        print("Lclyf aptl pa dhz abyulk vu, pa dvbsk zluk buzbzwljapun wlunbpuz yvjrlapun puav aol zrf, vusf av shuk wlymljasf jypzwf pu aol cpsshnl'z mpzo myf ihzrlaz.")
        time.sleep(1)
        print("Aol avduzmvsr svclk aol ahzaf aylhaz iba ohk av ovsk vuav aolpy ohaz lclyf aptl aolf dhualk h zuhjr!")
        time.sleep(1)
        lowahcont()
    elif StevenYN == "u":
        exit()
    else:
        exit()

def lowahcont():
    lowahcontyn = input("kv fvb dpzo av bumyf wpunb uvd? (f)/(u):")
        if lowahcontyn = "f":
            print("go steal stevens identity")
            time.sleep(2)
            exit()
        else:
            exit()

def login():
    #Password = SgDepIsBest
    username = input("Enter Roblox Username: ")
    match username:
        case "SpaceIDragon":
            password = input("Enter Password: ")
            if password == "SgDepIsBest":
                Continue()
            else:
                print("thats not you space!!!!")
                time.sleep(3)
                exit()
        case "RealStevenHaha":
            password = input("Enter Password: ")
            if password == "DontFryThePenguin":
                Steven()
            else:
                ProgramKill()
        case "PeppyThePingu":
            password = input("Enter Password: ")
            if password == "ShrimpyThePingu":
                Pingu()
            else:
                ProgramKill()
        case "balls":
            password = input("Enter Password: ")
            if password == "megaballz?":
                qjat_zhe_gfjgucj()
            else:
                ProgramKill()
        case "h5iBNDZlAGUAFhq":
            password = input("Enter Password: ")
            if password == "Whispersofthetwilightbreezecarrysecretsofthestars":
                lowah()
            else:
                ProgramKill()
        case _:
            print("Wrong Username!")
            time.sleep(2)
            exit() 

login()
