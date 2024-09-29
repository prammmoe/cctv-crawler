import cv2
import os
import time

def capture_images(location, selected_location, count_pic):
    counter = 1
    capturing = True
    
    print("Opening stream ...")
    while capturing:
        vcap = cv2.VideoCapture(f"https://mam.jogjaprov.go.id:1937/cctv-kominfosleman/{location[selected_location]}.stream/playlist.m3u8")

        if vcap.isOpened():
            print("Collected")

            # Create dirs
            directory = 'images/' + location[selected_location]
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

                counter += 1
                if counter > count_pic:
                    capturing = False

            vcap.release()
    
    print(f"Finish, successfully collected {count_pic} images")
