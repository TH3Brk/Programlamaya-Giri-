#Üç sayıdan en büyüğünü/küçüğünü bulan kod
liste = []
while len(liste) < 3 :
    giriş = int(input("Lütfen {}.Sayıyı Giriniz : ".format(len(liste) + 1)))
    liste.append(giriş)
liste.sort()
print("En Büyük Sayı : {}\nEn Küçük Sayı : {}".format(liste[2],liste[0]))

#Klavyeden 3 sayı okuyarak bu sayılardan en büyüğünü veya en küçüğünü ekrana yazan kodu yazınız.