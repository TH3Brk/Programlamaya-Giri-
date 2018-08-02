#Harf Notu Hesaplama
puan = int(input("Lütfen Notunuz Giriniz : "))
if (puan < 70):
    print("F aldınız")
elif (puan >= 70 and puan < 80):
    print("C aldınız")
elif (puan >= 80 and puan < 90):
    print("B aldınız")
else :
    print("A aldınız")

#Klavyeden 0 ile 100 arasında bir sayı okuyarak harf karşılığını bulunuz (A: 90 - 100, B: 80 -90, C:70-80 arası ve F: 70'in altı olarak kabul edebilirsiniz).