import cv2
import os
import time


class CCTVJogjaKota:
    def __init__(self):
        self.counter = 1
        self.capturing = True
        self.location = [
            "ATCS_jogokaryan",
            "ATCS_Simpang_Patangpuluhan",
            "ATCS_mirota",
            "ATCS_gramedia"
        ]
        self.count_pic = 0 

    def choose_location(self):
        for idx, loc in enumerate(self.location):
            print(f"{idx + 1}. {loc}")
        i = input("Pilih lokasi: ")
        self.selected_location = int(i) - 1

    def get_count_pic(self):
        self.count_pic = int(input("Jumlah gambar: "))
    
    def capture_images(self):
        print("Opening stream ...")
        while self.capturing:
            vcap = cv2.VideoCapture(f"https://cctvjss.jogjakota.go.id/atcs/{self.location[self.selected_location]}.stream/playlist.m3u8")

            if vcap.isOpened():
                print("Collected")

                # Create dirs
                directory = 'images/' + self.location[self.selected_location]
                complete_dir = os.path.join('datasets', directory)
                
                if not os.path.exists(complete_dir):
                    os.makedirs(complete_dir)

                ret, frame = vcap.read()

                if ret:
                    filename = os.path.join(complete_dir, f"{time.time()}.jpg")
                    cv2.imwrite(filename, frame)
                    print(f"Image: {filename}")

                    start = time.time()
                    while not ((time.time() - start) > 10): # Capture delay min 10 seconds to avoid duplicate images and to increase datasets variance
                        pass

                    self.counter += 1
                    if self.counter > self.count_pic:
                        self.capturing = False

                vcap.release()
        
        print(f"Finish, successfully collected {self.count_pic} images")

    def run(self):
        self.choose_location()
        self.get_count_pic()
        self.capture_images()