from typing import Text
import pikepdf
from colorama import Fore, Back, Style
from tqdm import tqdm
print (Fore.YELLOW+Style.BRIGHT+"""  _____  _____  ______      _____ _____            _____ _  ________ _____  
 |  __ \|  __ \|  ____|    / ____|  __ \     /\   / ____| |/ /  ____|  __ \ 
 | |__) | |  | | |__      | |    | |__) |   /  \ | |    | ' /| |__  | |__) |
 |  ___/| |  | |  __|     | |    |  _  /   / /\ \| |    |  < |  __| |  _  / 
 | |    | |__| | |        | |____| | \ \  / ____ \ |____| . \| |____| | \ \ 
 |_|    |_____/|_|         \_____|_|  \_\/_/    \_\_____|_|\_\______|_|  \_\
                                                                            
                                                                            """)
print(Fore.RED+"")
#Import Passlist Like This [example.txt]
wordlist1=str(input("Enter Password List Name: "))
passwords = [line.strip() for line in open(wordlist1)]
#Input File Name Like This [example.pdf]
fille=str(input("Enter File Name: "))
for password in tqdm(passwords, "Try To Crack Pdf"):
    try:
        #Import Pdf To Crack
        with pikepdf.open(fille, password=password) as pdf:           
            #The Correct Password
            print(Back.GREEN+Style.BRIGHT+Fore.WHITE+"\n\n[+]Correct Password Is:","»",password,"«",Style.RESET_ALL+"\n" )
            print(Style.RESET_ALL)
            break
    except pikepdf._qpdf.PasswordError as e:
        continue
print("File Name :",fille," »»» ","Correct Password :",password,file=open("correct pass.txt","a"))    
