import os
import random
import requests
from colorama import init, Fore

os.system("cls || clear") 
init()
banner = Fore.RED + f"""
                 _          _   _ _ _             
     /\         (_)        | \ | (_) |            
    /  \   _ __  _ ______ _|  \| |_| |_ _ __ ___  
   / /\ \ | '_ \| |_  / _` | . ` | | __| '__/ _ \ 
  / ____ \| | | | |/ / (_| | |\  | | |_| | | (_) |
 /_/    \_\_| |_|_/___\__,_|_| \_|_|\__|_|  \___/ 
                                                                                              
            By : @Unknown-user-dev 
        https://github.com/Unknown-user-dev
"""

print(banner)

def menu():
    print(Fore.GREEN + """
    [1] Generate and Check Nitro
    [2] Credits
    [3] Exit
    """)
    choice = input(Fore.BLUE + "Your choice : " + Fore.WHITE)
    if choice not in ["1", "2", "3"]:
        os.system("cls || clear")
        print(banner)
        print(Fore.RED + "Please enter a valid choice" + Fore.WHITE)
        menu()

    if choice == "2":
        os.system("cls || clear")
        print(banner)
        print(Fore.GREEN + "By : @Unknown-user-dev | github.com/Unknown-user-dev | >_Unknown User#8624 | Student of Lycée Robespierre 2TNE" + Fore.WHITE)
        menu()
    elif choice == "3":
        print(Fore.RED + "Bye !" + Fore.WHITE)
        exit()
    if choice == "1":
        os.system("cls || clear")
        print(banner)
        print(Fore.GREEN + "Generating and checking nitro codes..." + Fore.WHITE)
        while True:
            code = "".join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=16))
            r = requests.get(f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true")
            if r.status_code == 200:
                print(Fore.GREEN + f"Valid code found : {code}" + Fore.WHITE)
                with open("nitro.txt", "a") as f:
                    f.write(f"{code} | https://discord.gift/{code} | Valid code found")
                    print(Fore.GREEN + f"Code saved in nitro.txt" + Fore.WHITE)
                    break
            else:
                print(Fore.RED + f"Invalid code : {code}" + Fore.WHITE)
                
if __name__ == "__main__": menu()
