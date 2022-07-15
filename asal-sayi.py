min_sayi=int(input("Minimum sayıyı giriniz: "))
max_sayi=int(input("Maksimum sayıyı giriniz: "))
sayac=0
sayilar=[]
for i in range(min_sayi,max_sayi+1):
    for j in range(1,i+1):
        if(i%j==0):
            sayac+=1
    if(sayac==2):
        sayilar.append(i)
        sayac=0
    else:
        sayac=0
print(f"\n{min_sayi} ve {max_sayi} arasında {len(sayilar)} tane asal sayı var.\n{sayilar}\n")