from src.locations.yogyakarta import atcs, atcs_kota, atcs_kp, kominfo_sleman, malioboro, bantul, cctv_jogjakota, malioboro_mam
from src.locations.bandung import bandung
from src.locations import malioboro_mam
from src.locations.semarang import semarang
from src.locations.surakarta import surakarta

def main():
    print("Choose CCTV to run:")
    print("1. ATCS Kota")
    print("2. Kominfo Sleman CCTV")
    print("3. Bantul CCTV")
    print("4. ATCS")
    print("5. ATCS Kulon Progo")
    print("6. ATCS Malioboro")
    print("7. Semarang")
    print("8. Bandung")
    print("9. ATCS Jogja Kota")
    print("10. ATCS Surakarta")
    print("11. Malioboro Only")
    choice = input("Enter choice: ")

    if choice == '1':
        cctv = atcs_kota.ATCSKota()
    elif choice == '2':
        cctv = kominfo_sleman.KominfoSlemanCCTV()
    elif choice == '3':
        cctv = bantul.BantulCCTV()
    elif choice == '4':
        cctv = atcs.ATCS()
    elif choice == '5':
        cctv = atcs_kp.ATCSKulonProgo()
    elif choice == '6':
        cctv = malioboro.MaliboroCCTV()
    elif choice == '7':
        cctv = semarang.Semarang()
    elif choice == '8':
        cctv = bandung.Bandung()
    elif choice == '9':
        cctv = cctv_jogjakota.CCTVJogjaKota()
    elif choice == '10':
        cctv = surakarta.Surakarta()
    elif choice == '11':
        cctv = malioboro_mam.Malioboro()
    else:
        print("Invalid choice!")
        return
    
    cctv.run()

if __name__ == "__main__":
    main()
