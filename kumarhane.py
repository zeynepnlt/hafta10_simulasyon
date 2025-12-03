import random
def kumarhane_simulasyonu(senaryo_turu, simu_sayisi=10000):
    toplam_kasa_kazanci = 0

    if senaryo_turu == 1:
        # Pro vs Junior (Junior: %20, Pro: %70, Beraberlik: %10)
        p1_win_limit = 0.20
        p2_win_limit = 0.90  # 0.20 + 0.70
    else:
        # Eşitler (Oyuncu1: %40, Oyuncu2: %40, Beraberlik: %20)
        p1_win_limit = 0.40
        p2_win_limit = 0.80  # 0.40 + 0.40

    bahis = 10   # Her el ortaya konan miktar

    for _ in range(simu_sayisi):
        # Her oyun için paraları sıfırla
        p1_para = 100
        p2_para = 100
        oyun_kasa_kazanci = 0

        # Oyun döngüsü: Herhangi biri 3 TL ve altına düşene kadar
        while p1_para > 3 and p2_para > 3:
            zar = random.random()

            # Ortadaki toplam para (Pot)
            pot = bahis * 2

            # SENARYO
            if zar < p1_win_limit:
                # P1 Kazanır
                kasa_payi = pot * 0.10
                kazanan_payi = pot * 0.90

                p1_para += (kazanan_payi - bahis)  # Kendi bahsi çıktıktan sonraki net kar
                p2_para -= bahis
                oyun_kasa_kazanci += kasa_payi

            elif zar < p2_win_limit:
                # P2 Kazanır (Mantık aynı)
                kasa_payi = pot * 0.10
                kazanan_payi = pot * 0.90

                p2_para += (kazanan_payi - bahis)
                p1_para -= bahis
                oyun_kasa_kazanci += kasa_payi

            else:
                # Beraberlik (Para alınmıyor, oyun devam)
                pass

        # Oyun bitti, bu oyundaki kasa kazancını toplama ekle
        toplam_kasa_kazanci += oyun_kasa_kazanci

    # Ortalama kazancı döndür
    return toplam_kasa_kazanci / simu_sayisi


print("Simülasyon Başlatılıyor...")
durum1_kazanc = kumarhane_simulasyonu(1)
durum2_kazanc = kumarhane_simulasyonu(2)

print(f"1. Durum (Pro vs Junior) Kasa Ort. Kazancı: {durum1_kazanc:.2f} TL")
print(f"2. Durum (Eşit Seviye) Kasa Ort. Kazancı:   {durum2_kazanc:.2f} TL")

if durum2_kazanc > durum1_kazanc:
    print("\nSONUÇ: Eşit seviyedeki oyuncular oynadığında (2. Durum) kasa daha çok kazanır.")
else:
    print("\nSONUÇ: Farklı seviyedeki oyuncular oynadığında (1. Durum) kasa daha çok kazanır.")
