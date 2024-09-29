import cv2
import os
import time


class Bandung:
    def __init__(self):
        self.counter = 1
        self.capturing = True
        self.location = [
            "Cicendo",
            "DepanTop",
            "bragaaa",
            "AsiaAfrikaBRITowerdua",
            "tamblong",
            "balkott",
            "riausiter",
            "CICA",
            "CICA4",
            "Cicend4",
            "Cicen",
            "Cicend",
            "Ciktm",
            "CICAB",
            "Ciktmp",
            "Cipanyl",
            "CICAB6"
        ]
        self.count_pic = 0
        self.cctv_brand = [
            "DAHUA",
            "HIKSVISION",
            "HUAWEI"
        ]
        self.error_log = []

    def choose_location(self):
        for idx, loc in enumerate(self.location):
            print(f"{idx + 1}. {loc}")
        i = input("Pilih lokasi: ")
        self.selected_location = int(i) - 1

    def get_count_pic(self):
        self.count_pic = int(input("Jumlah gambar: "))

    def capture_images(self):
        print("Opening stream ...")
        for brand in self.cctv_brand:
            if not self.capturing:
                break

            stream_url = f"https://pelindung.bandung.go.id:3443/video/{brand}/{self.location[self.selected_location]}.m3u8"
            print(f"Trying stream URL: {stream_url}")
            vcap = cv2.VideoCapture(stream_url)

            if vcap.isOpened():
                print("Stream opened successfully.")
                # Create dirs
                directory = self.location[self.selected_location]
                complete_dir = os.path.join('images', directory)

                if not os.path.exists(complete_dir):
                    os.makedirs(complete_dir)

                while self.capturing and self.counter <= self.count_pic:
                    ret, frame = vcap.read()

                    if ret:
                        filename = os.path.join(complete_dir, f"{time.time()}.jpg")
                        cv2.imwrite(filename, frame)
                        print(f"Image: {filename}")

                        start = time.time()
                        while not ((time.time() - start) > 10):  # Capture delay min 10 seconds
                            pass

                        self.counter += 1

                    else:
                        print("Failed to capture image.")
                        self.capturing = False
                        break

                vcap.release()
            else:
                error_message = f"Failed to open stream for brand: {brand}"
                print(error_message)
                self.error_log.append(error_message)

        if self.capturing:
            print(f"Process ended prematurely. Collected {self.counter - 1} images")
            print("Error log:")
            for error in self.error_log:
                print(error)

    def run(self):
        self.choose_location()
        self.get_count_pic()
        self.capture_images()