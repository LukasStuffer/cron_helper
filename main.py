#!/usr/bin/env python3

# Lukas Stuffer
# IG: _lukasstuffer_

# include this script in the server's cron job


import subprocess
from datetime import datetime
from colorama import Fore, Style

if __name__ == "__main__":
    
    print ("\n2023-2024 (c) Lukas Stuffer")
    print ("IG: _lukasstuffer_")
    
    
    # name/description : command
    work = [
        ['DB-Maintenance'   , 'python3 /var/python/maintenance/main.py'],
        ['Virustotal-Check' , 'python3 /var/python/virustotal/main.py']
    ]
    
    
    # start work
    for i in range(len(work)):
    
        # start script
        print (f"\n> {Fore.GREEN}{Style.BRIGHT}START{Style.RESET_ALL} {work[i][0]}")
        cmd = str(work[i][1])
    
        try:
    
            result = subprocess.run(cmd, shell=True, check=True, text=True)
    
        except Exception as e:
            print(f"> {Fore.RED}{Style.BRIGHT}ERROR{Style.RESET_ALL} {e}")
        
    
    # debug/heartbeat
    try:
        time_now = str(datetime.now()).split('.')[0]
    
        file_path = './last_call.txt'
        with open(file_path, 'w') as output:
            output.write(time_now)
    
    except Exception as e:
        print (f"\n> {Fore.RED}{Style.BRIGHT}ERROR{Style.RESET_ALL} {e}")
    
    
    print(f"\n> END")
