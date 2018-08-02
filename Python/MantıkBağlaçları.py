#Mantık Bağlaçları
a = int(input("Lütfen 1.Sayıyı Sayı Giriniz : "))
b = int(input("Lütfen 2.Sayıyı Sayı Giriniz : "))
c = int(input("Lütfen 3.Sayıyı Sayı Giriniz : "))
print (a , b , c, sep = " , ") #sep parametresi aralara virgül koymayı sağlar veya istenen herhangi bir karakteri
if (a < b and a > c):
    print("1. Sayı, 2. ve 3. sayıların arasında bir değere sahiptir")
else :
    print("1. Sayı, 2. ve 3. sayıların arasında bir değere sahip değildir")
if (a == b and a < c ):
    print("1. Sayı 2. Sayıya Eşittir ve 3. Sayıdan Küçüktür")
else :
    print("1. Sayı 2. Sayıya Eşit Değildir veya 3. Sayıdan Büyüktür")
if (a > b or a > c):
    print("1. Sayı, 2. veya 3. Sayıdan Büyüktür")
else :
    print("1. Sayı, 2. veya 3. Sayıdan Büyük Değildir")
if (a == b and b == c):
    print("Bütün sayılar birbirine eşittir")
else:
    print("Bütün sayılar birbirine eşit değildir")
#Bütün durumlar elif ile bir arada değerlendirilebilir

#Klavyeden üç sayı alarak mantık bağlaçlarını kullanan örnek bir kod yazınız. Örneğin okunan sayılar a, b ve c olsun. Sırasıyla, a'nın b ve c arasında olup olmadığını, a'nın b'ye eşit ve aynı zamanda c'den küçük olup olmadığını a'nın b'den veya c'den büyük olup olmadığını üç sayının birbirine eşit olup olmadığını kontrol edip ekrana basan kodu yazınız.
