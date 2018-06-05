########################### START: libreria consola ###################################
from colorama import *
from time import sleep
import os

init(convert=True)

def clearScreen():
    os.system('cls')	

def cargarPrograma():    
    print(Style.RESET_ALL)
    clearScreen()
    print("Cargando programa... ")
    for arch in range(0,101,10):
        sleep(0.5)
        print(Cursor.UP(1)+Cursor.FORWARD(20)+Fore.YELLOW + str(arch)+'%' )
    sleep(1)   
    
