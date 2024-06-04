# Crawler for CCTV
# MAM JogjaProv ATCS-Kota endpoint is: "https://mam.jogjaprov.go.id:1937/atcs-kota/"
# CCTV ATCS Jogja endpoint is: "https://cctvjss.jogjakota.go.id/atcs/" and it uses ".stream/chunklist_w128673376.m3u8" instead of ".stream/playlist.m3u8"
# When capturing from another endpoint category, you can change the path behind https://mam.jogjaprov.go.id:1937. Example https://mam.jogjaprov.go.id:1937/{another endpoint}

import cv2
import os
import time

cntr = 1
capturing = True
# You can add more location in here
location = [
    "Gondomanan",
    "Wirobrajan",
    "Gramedia",
    "Jetis",
    "SimpangTerbanUtara",
    "Serangan",
    "SimpangDemanganUtara",
    "UKDW",
    "APMD",
    "SimpangTerbanTimur",
    "SimpangDemanganSelatan",
    "SimpangTerbanBarat",
    "SimpangBalaikotaTimur",
    "Warungboto1",
    "Simpang_KolSugiono2",
    "SimpangPasarTeloUtara",
    "KMNol",
    "BPK",
    "ViewSimpangTugu",
    "ViewBukitKlangon",
    "ViewAlunAlunKidul",
    "ViewBaronTimur",
    "ViewSambisari",
    "Juadi",
    "SimpangAtmosukarto",
    "SimpangDeBritto",
    "Sajiono",
    "SimpangMandalakrida",
    "SimpangBasen",
    "Warungboto2",
    "Simpang_MenteriSupeno2",
    "MargoUtomo_SelatanOlive",
    "MargoUtomo_GowonganLor",
    "MargoUtomo_WismaRatih",
    "SimpangGambiranBarat",
    "SimpangRejowinangunTimur",
    "Simpang_SugengJeroni2",
    "MargoUtomo_TokoCatWahyu",
    "SimpangBalaikota",
    "AhmadJazuli",
    "FMNoto",
    "SimpangAmongrogoTimur",
    "ParkiranNgabean",
    "SimpangGambiranTimur",
    "Jlagran",
    "SimpangPatangpuluhan",
    "SimpangBorobudurPlaza",
    "SimpangMelia",
    "Simpang_MenteriSupeno1",
    "Simpang_SugengJeroni1",
    "YosSudarso",
    "Terban",
    "SimpangBausasran",
    "Pingit",
    "MargoUtomo_WijayaBaruTravel",
    "Simpang_PasarGading2",
    "SimpangJatikencana",
    "KyaiMojo1",
    "SimpangGaleriaTImurSelatan"
]
for idx, a in enumerate(location):
    print(str(idx + 1) + ". " + a)
i = input("Pilih lokasi: ")
count_pic = int(input("Jumlah gambar: "))

print("Opening stream....")
while capturing: 
    vcap = cv2.VideoCapture(
        "https://mam.jogjaprov.go.id:1937/atcs-kota/"
        + location[int(i) - 1]
        + ".stream/playlist.m3u8"
    )
    if vcap.isOpened():
        print("Collected")

        # Create directory based on location
        directory = location[int(i) - 1]
        complete_dir = 'images/' + directory
        if not os.path.exists(complete_dir):
            os.makedirs(complete_dir)

        ret, frame = vcap.read()
        if ret:
            filename = os.path.join(complete_dir, str(time.time()) + ".jpg")  # Path and image construction
            cv2.imwrite(filename, frame)  # Take picture
            print("Image: " + filename)
            start = time.time()
            while not ((time.time() - start) > 10): # Capture delay min 10 seconds to avoid duplicate images and to increase datasets variance
                pass
            cntr = cntr + 1
            if cntr > count_pic:
                capturing = False
        vcap.release()

print(f"Finish, successfully collected {count_pic} images")
