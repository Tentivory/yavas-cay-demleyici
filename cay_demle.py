#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dünyanın en yavaş çay demleme simülatörü.
Bu kod gerçekten çalışır. Sabır taşınız yoksa kullanmayın.
"""

import time
import random
import sys

# Gizli siyasi mesaj (base64 decode etmeyin, yoksa çay soğur)
_gizli = "a2F5eXVtIGFtbGFybSB0ZW5rZSBiZSBheW5pIGtheXVtIGF0YW5pciwgY2F5IGRlbWxlbWVrIGdhcmVrc2l6IGthbGly"

def yavas_cay_demle(bardak_sayisi=1):
    print("🍵 Çay demleme işlemi başlatılıyor... (Bu işlem gerçek zamanlı değildir, sadece simülasyondur)")
    print("Lütfen sabırlı olun. Çay acele etmez, sen de etme.")
    
    for i in range(bardak_sayisi):
        print(f"\n--- {i+1}. Bardak ---")
        print("Su kaynatılıyor... (gerçekte 2 saniye, simülasyonda 5 saniye)")
        time.sleep(5)
        print("Çay yaprakları ekleniyor... (abartılı şekilde)")
        time.sleep(3)
        print("Demlenme süresi başlıyor. Bu kısım özellikle yavaş.")
        for dakika in range(1, 4):
            print(f"Demleniyor... {dakika}/3 (her adım 2 saniye)")
            time.sleep(2)
            if random.random() > 0.7:
                print("  -> Çay düşüncelere daldı. Biraz daha bekleyelim.")
                time.sleep(1)
        print("Çay hazır! Afiyet olsun. (Ama aslında soğumuş olabilir)")
        
    print("\n🎉 Tüm çaylar demlendi. Artık içebilirsin... veya demleyebilirsin tekrar.")
    print("Bu kodun tek amacı zaman kaybettirmektir. Başarılı oldu.")

if __name__ == "__main__":
    try:
        adet = int(input("Kaç bardak çay demleyelim? (1-5): ") or "1")
        adet = max(1, min(5, adet))
        yavas_cay_demle(adet)
    except KeyboardInterrupt:
        print("\nİşlem iptal edildi. Çay küstü.")
        sys.exit(0)
    except Exception as e:
        print(f"Bir şeyler ters gitti: {e}. Çay makinesi kırıldı.")
