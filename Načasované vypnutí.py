from datetime import datetime
from datetime import timedelta
import time
import os
import platform as ptfm


def win_vypnout():
    return os.system("shutdown /s /t 1")
def linux_vypnout():
    return os.system("poweroff")
sys = ptfm.system()
print("Pro správné fungování aplikace nezavírejte tohle okno až do vypnutí počítače")
print("Za kolik hodin se mám vypnout")
cas_ted = datetime.now()
cas = cas_ted.strftime("%H:%M:%S")
print("Aktuální čas: ", cas)
hodiny = int(input("Zadejte hodniny: "))
minuty = int(input("Zadejte minuty: "))
sekundy = int(input("Zadejte sekundy: "))
hodiny = hodiny * (60*60)
minuty = minuty * 60
vysledek = int(hodiny + minuty + sekundy)
vyp_cas = cas_ted + timedelta(seconds=vysledek)
print("Počítač bude vypnut v", vyp_cas)
print("Nezavírejte prosím tohle okno!!!!")
time.sleep(vysledek)
if sys =="Windows":
    win_vypnout()    
if sys =="Linux":
    linux_vypnout()