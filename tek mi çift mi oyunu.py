import time 
print("yaş bulma oyunumuzu beğendiğinize göre yeni bir oyun daha oynayalım ")
print("tahmin etmen için bekliyorum")
tahmini= input("tahmini bekliyorum dostm: ")
oyun = "tek mi çift mi"
if tahmini == oyun:
    print("waaaoow bu zekanın bi kaynağı olmalı ")
else:
    print("yanlış bildin ne yazıkki")
time.sleep(3)
print("neyse boşver adamım")
time.sleep(3)
print("tek mi çift mi oynayalım o zaman")
sayi =  int(input("sayı : "))
if  sayi  % 2 == 0 :
    print("sayınız çift")
else:
    print("sayınız tek")
time.sleep(5)
print("biraz uzattım ama eğlenelim son bi soru daha ama bu en zoru")

print("dünyanın en yakışıklı ve karizmatik adamının adı nedir ?")
time.sleep(3)
sormakısmı = input("evet cevabını alayım:  ")
cevap = "Tayyar"
if sormakısmı == cevap :
    print("evet doğru bildin tebrikler")
else:
    print("bunu biliyosun bence")
time.sleep(2)


