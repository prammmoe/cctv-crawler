# Main Class

from locations import atcs, atcs_kota, atcs_kp, kominfo_sleman, malioboro, bantul, semarang, bandung

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
    else:
        print("Invalid choice!")
        return
    
    cctv.run()

if __name__ == "__main__":
    main()
