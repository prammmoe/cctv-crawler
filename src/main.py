# main.py

from locations.atcs_kota import ATCSKota
from locations.kominfo_sleman import KominfoSlemanCCTV
from locations.bantul import BantulCCTV

def main():
    print("Choose CCTV to run:")
    print("1. ATCS Kota")
    print("2. Kominfo Sleman CCTV")
    print("3. Bantul CCTV")
    choice = input("Enter choice: ")

    if choice == '1':
        cctv = ATCSKota()
    elif choice == '2':
        cctv = KominfoSlemanCCTV()
    elif choice == '3':
        cctv = BantulCCTV()
    else:
        print("Invalid choice!")
        return
    
    cctv.run()

if __name__ == "__main__":
    main()
