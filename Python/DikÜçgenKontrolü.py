#Dik Üçgen Kontrolü 
import math

sayı1 = int(input("Lütfen 1. Kenarı Giriniz : "))
sayı2 = int(input("Lütfen 2. Kenarı Giriniz : "))
sayı3 = int(input("Lütfen 3. Kenarı Giriniz : "))
if sayı3 == math.sqrt((sayı1 ** 2 ) + (sayı2 ** 2)):
    print("Bu bir dik üçgen")
else : 
    print("Bu bir dik üçgen değil!!")

#Kullanıcıdan üç adet sayı alarak bu sayıların bir dik üçgenin kenar uzunlukları olup olmadığını hesaplatan bir kod yazınız(Yardım: Bir üçgenin dik olduğunu anlamak için a2+b2=c2 pisagor bağlantısından yararlanabilirsiniz)