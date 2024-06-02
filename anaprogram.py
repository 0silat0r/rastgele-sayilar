# rastgele-sayilar Python Programi
# Kodlayan: 0silat0r

# Kütüphanelerin Eklenmesi
import os
import random
import datetime
import time

# Fonksiyonlarin Yazilmasi
def clear():
    os.system("clear")
def sayiUret():
    sayi = random.randint(1,1000)
    print(f"Uretilen rastgele bir sayi: {sayi}")
    time.sleep(0.5)

# Ana Programin Yazilmasi
sistem_zamani = datetime.datetime.now()
clear()
print("rastgele-sayilar V1")
print("Kodlayan: cpu-astatine")
print(f"Sistem Zamani: {sistem_zamani}")
while True:
    try:
        sayiUret()
    except KeyboardInterrupt:
        print("\nProgramdan cikis yaptiniz!")
        break
