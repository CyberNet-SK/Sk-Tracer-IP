import time
import sys
import os
import requests
import json
from colorama import Fore, Style, init

# 
init(autoreset=True)

# 
B = Fore.BLUE + Style.BRIGHT
W = Fore.WHITE + Style.BRIGHT
R = Fore.RED + Style.BRIGHT
G = Fore.GREEN + Style.BRIGHT
Y = Fore.YELLOW + Style.BRIGHT
C = Fore.CYAN + Style.BRIGHT

def clear_screen():
    os.system('clear')

def banner():
    print(f"""
    {B}
     ██████╗██╗  ██╗    ███████╗██████╗ ██╗   ██╗
    ██╔════╝██║ ██╔╝    ██╔════╝██╔══██╗╚██╗ ██╔╝
    ██║      █████╔╝     ███████╗██████╔╝ ╚████╔╝ 
    ██║      ██╔═██╗     ╚════██║██╔═══╝   ╚██╔╝  
    ╚██████╗██║  ██╗    ███████║██║        ██║   
     ╚═════╝╚═╝  ╚═╝    ╚══════╝╚═╝        ╚═╝   
    {Y}--------------------------------------------------
    {G}>> Developer : SHEIKH SABBIR
    {G}>> Tool Name  : SK-TRACER-IP (Advanced Edition)
    {C}>> Status     : Authorized Personnel Only
    {Y}--------------------------------------------------
    """)

def ip_tracer():
    print(f"\n{C}[*] {W}Enter IP Address to Track (Leave blank for yours)")
    ip = input(f"{B}SK-TRACER > {W}").strip() # .strip() 
    
    print(f"\n{Y}[+] {G}Fetching Advanced Data... Please Wait...\n")
    time.sleep(1.5)
    
    # 
    api_url = f"http://ip-api.com/json/{ip}?fields=status,message,country,countryCode,regionName,city,district,zip,lat,lon,timezone,isp,org,as,query"
    
    try:
        response = requests.get(api_url)
        data = response.json()
        
        if data['status'] == 'success':
            print(f"{B}="*45)
            print(f"{B} IP ADDRESS    : {W}{data.get('query')}")
            print(f"{B} COUNTRY       : {W}{data.get('country')} ({data.get('countryCode')})")
            print(f"{B} DIVISION      : {W}{data.get('regionName')}")
            print(f"{B} SUB-DIVISION  : {W}{data.get('district') if data.get('district') else 'Not Found'}")
            print(f"{B} CITY/VILLAGE  : {W}{data.get('city')}")
            print(f"{B} POSTAL CODE   : {W}{data.get('zip')}")
            print(f"{B} ISP           : {W}{data.get('isp')}")
            print(f"{B} ORGANIZATION  : {W}{data.get('org')}")
            print(f"{B} TIMEZONE      : {W}{data.get('timezone')}")
            print(f"{B} LATITUDE      : {W}{data.get('lat')}")
            print(f"{B} LONGITUDE     : {W}{data.get('lon')}")
            print(f"{B} GOOGLE MAPS   : {G}https://www.google.com/maps?q={data.get('lat')},{data.get('lon')}")
            print(f"{B}="*45)
            print(f"\n{G}[!] Tracking Completed Successfully!")
        else:
            print(f"{R}[!] Error: {data.get('message')}")
            
    except Exception as e:
        print(f"{R}[!] Connection Error! Ensure internet is active.")
    
    input(f"\n{Y}Press Enter to return to Menu...")

def main_menu():
    while True:
        clear_screen()
        banner()
        print(f"{W}[ 1 ] IP Tracer (Track Any IP)")
        print(f"{W}[ 0 ] Exit Tool")
        print(f"{Y}--------------------------------------------------")
        
        choice = input(f"{C}SK-TRACER > {W}").strip()
        
        if choice == "1":
            ip_tracer()
        elif choice == "0":
            print(f"\n{G}Thanks for using Sk-Tracer-IP! Goodbye.")
            sys.exit()
        elif choice == "": # 
            continue
        else:
            print(f"{R}[!] Invalid Choice!")
            time.sleep(1)

if __name__ == "__main__":
    main_menu()
