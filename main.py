from pickletools import int4
import random
import time

print("""**************************************************

Sayı Tahmin Oyunu

1 ile 40 arasında sayıyı tahmin ediniz.

**************************************************""")

rastgele_sayı = random.randint(1,40)
tahin_hakkı = 7
while True:

    tahmin = int(input("Tahmininiz: "))

    if (tahmin < rastgele_sayı):
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)
        print("Daha yüksek bir sayı söyleyiniz.")
        tahin_hakkı -= 1

    elif (tahmin > rastgele_sayı):
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)
        print("Daha düşük bir sayı söyleyiniz.")
        tahin_hakkı -= 1
    else:
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)
        print("Tebrikler! sayımız: ",rastgele_sayı)
        break
    if (tahin_hakkı == 0 ):
        print("Tahmin hakkınız bitti...")
        print("Sayımız: ",rastgele_sayı)
        break