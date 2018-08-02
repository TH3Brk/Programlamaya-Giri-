#Basit İşlemler
print("Sizden iki adet sayı alınacak lütfen ilkinin daha büyük olmasına özen gösterin")
giriş1 = int(input("Lütfen 1.Sayıyı Sayı Giriniz : "))
giriş2 = int(input("Lütfen 2.Sayıyı Sayı Giriniz : "))
print("Alınan 2 Sayının Toplama - Çıkarma - Çarpma - Bölme Sonuçları :")
print("Toplama : {}\nÇıkarma : {}\nÇarpma : {}\nBölme : {}".format(giriş1 + giriş2 , giriş1 - giriş2 , giriş1 * giriş2, (int)(giriş1 / giriş2)))
#Üssteki kod da \n => bir aşağı satıra geçmeyi sağlıyor, bölmede int ile cast edilmesinin sebebi normalde bölüm işlemi sonucu ondalıklı çıkar

#Ekrandan okunan iki tam sayı (int) için basit işlemler yaparak ekrana sonuçları basan kod yazınız. Bu işlemler toplama, çıkarma, çarpma, bölme işlemleridir