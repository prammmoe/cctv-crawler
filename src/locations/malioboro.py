from helpers.choose_location import choose_location
from helpers.capture_images import capture_images
from helpers.get_count_pic import get_count_pic

class MaliboroCCTV:
    def __init__(self):
        self.location = [
            "UPTMalio5_Perwakilan",
            "UPTMalio4_DepanDPRD",
            "UPTMalio11_TerangBulan",
            "UPTMalio3_DepanDispar",
            "UPTMalio10_Kepatihan",
            "UPTMalio24_SimpangReksobayan",
            "UPTMalio21_UtaraInnaGaruda",
            "UPTMalio9_MutiaraBaru",
            "UPTMalio13_GunungMas",
            "UPTMalio12_Ramayana",
            "UPTMalio1_SelatanTeteg",
            "UPTMalio_NolKmUtara",
            "UPTMalio22_SimpangPajeksan",
            "UPTMalio_NolKmGedungAgung",
            "UPTMalio25_UtaraMall",
            "UPTMalio6_MallUtara"
        ]   

    def run(self):
        selected_location = choose_location(self.location)
        count_pic = get_count_pic()
        capture_images(self.location, selected_location, count_pic)
