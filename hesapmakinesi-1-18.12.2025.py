while True:
    islem=input("""Yapmak istediğiniz işlemi girin (toplama, çıkarma, çarpma, bölme)
Çıkmak için 'q' ya basın: """)
    if islem=="q":
        break
    elif islem!="toplama" and islem!="çıkarma" and islem!="çarpma" and islem!="bölme":
        print("""Belitilen işlemlerden birini giriniz
            (toplama, çıkarma, çarpma, bölme)""")
        continue
    else:
        sayı1=int(input("Bir sayı girin: "))
        sayı2=int(input("Bir sayı daha girin: "))
        if islem=="toplama":
            toplama=sayı1+sayı2
            print("Toplam: ", toplama)
        elif islem=="çıkarma":
            cıkarma=sayı1-sayı2
            print("Fark:", cıkarma)
        elif islem=="çarpma":
            carpma=sayı1*sayı2
            print("Çarpım:", carpma)
        elif islem=="bölme":
            if sayı2==0:
                print("Bir sayı sıfıra bölünemez.")
                break
            else:
                bolme=sayı1/sayı2
                print("Bölüm:", bolme)
22.12
23.12