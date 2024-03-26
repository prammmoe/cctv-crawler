import cv2
import os
import time

cntr = 1
capturing = True
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
        print("opened")

         # Get current hour (in WIB)
        current_hour = int(time.strftime('%H'))

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
            while not ((time.time() - start) > 10):
                pass
            cntr = cntr + 1
            if cntr > count_pic:
                capturing = False
        vcap.release()

print(f"Finish, successfully collected {count_pic} images")
