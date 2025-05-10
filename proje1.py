
print("\033[1;32;40m")# Renkli yazmak için
print("╔══════════════════════╗")
print("║     Proje Listesi    ║")
print("║  1.Hesap Makinesi    ║")
print("║  2.Tahmin Oyunu      ║")
print("║  3.Vki Hesaplama     ║")
print("║  4.Kur Dönüstürücü   ║")
print("║  5.Puan Hesaplama    ║")
print("║  6.Ruh Halini Söyle  ║")
print("║  7.                  ║")
print("║                      ║")
print("║ Seciminiz nedir?     ║")
print("╚══════════════════════╝")


secim = input("Seçiminizi girin (1-7): ")

if secim == "1":
    import hesapmakinesi
    hesapmakinesi()
elif secim == "2":
    import tahminoyunu
    tahminoyunu.tahmin_et()
elif secim == "3":
    import vki_hesaplama
    vki_hesaplama()
elif secim =="4":
    import kurdönüstürücü
    kurdönüstürücü()  
elif secim =="5" :
    import puanhesaplama
    puanhesaplama
elif secim =="6" :
    import ruhhalinisoyle
    ruhhalinisoyle.ruh_hali_oyunu()

