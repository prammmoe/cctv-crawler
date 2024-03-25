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
i = input("pilih lokasi : ")
count_pic = int(input("jumlah gambar : "))

print("opening stream....")
while capturing:  # Take pictures forever
    vcap = cv2.VideoCapture(
        "https://mam.jogjaprov.go.id:1937/atcs-kota/"
        + location[int(i) - 1]
        + ".stream/playlist.m3u8"
    )
    if vcap.isOpened():
        print("opened")
        # Create directory for night images based on location
        directory = location[int(i) - 1]
        if not os.path.exists(directory):
            os.makedirs(directory)  # Create directory if it doesn't exist

        ret, frame = vcap.read()
        if ret:
            filename = os.path.join(directory, str(time.time()) + ".jpg")  # Use os.path.join for cleaner path construction
            # filename = location[int(i) - 1] + "/" + str(time.time()) + ".jpg"
            cv2.imwrite(filename, frame)  # Take picture
            print("collected dataset : " + filename)
            start = time.time()
            while not ((time.time() - start) > 10):
                pass
            cntr = cntr + 1
            if cntr > count_pic:
                capturing = False
        vcap.release()

print("Finish Crawl Data")
