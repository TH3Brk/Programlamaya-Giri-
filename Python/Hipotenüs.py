#Hipotenüsü Hesaplayan Kod
#İpucu math dosyasını import ederek sqrt fonksiyonunu kullanabilir siniz
import math 
kenar1 = int(input("1. Kenarı Giriniz : "))
kenar2 = int(input("2. Kenarı Giriniz : "))
hipotenüs = math.sqrt(kenar1**2 + kenar2**2)
print("Sonuç : ",int(hipotenüs))

#Bir dik üçgenin iki dik kenarını alarak hipotenüsünü hesaplayan kod yazınız. (Yardım: karekök almak için, C ve C++ dillerinde math.h dosyasını include ederek (#include <math.h>) sqrt() fonksiyonunu kullanabilirsiniz. Basitçe int x = sqrt(16); satırı sonrasında x değeri 4 olur) JAVA dilinde ise Math.sqrt() fonksiyonu kullanılabilir. Basitçe int x= Math.sqrt(16); satırından sonra x değeri 4 olur)