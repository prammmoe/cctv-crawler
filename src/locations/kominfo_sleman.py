from helpers.choose_location import choose_location
from helpers.capture_images import capture_images
from helpers.get_count_pic import get_count_pic

class KominfoSlemanCCTV:
    def __init__(self):
        self.location = [
            "FlyOver_JomborTimur",
            "Perempatan_DemakIjo1",
            "Sidomoyo_Utara",
            "Munggur1",
            "Patran_Godean",
            "Tirtoadi_Selatan",
            "Banyurejo_Utara",
            "Terminal_Condongcatur1",
            "Tirtoadi_Utara",
            "Banyurejo_Selatan",
            "Munggur2",
            "Selomartani_Selatan",
            "Maguwoharjo2",
            "Bundaran_UGM1",
            "Perempatan_Godean",
            "Pertigaan_PasarGamping",
            "Maguwoharjo6",
            "Terminal_Condongcatur2",
            "Sidomoyo_Selatan",
            "PosPolisi_Jombor",
            "Perempatan_UPN1",
            "Pertigaan_Maguwo2",
            "Proliman_1",
            "Maguwoharjo4",
            "Maguwoharjo3",
            "Selomartani_Utara",
            "Maguwoharjo5",
            "Margokaton_Utara",
            "Babarsari2",
            "Margokaton_Selatan",
            "Perempatan_PasarStan",
            "Pertigaan_PasarPrambanan",
            "Babarsari1",
            "Bantulan_Timur"
        ]

    def run(self):
        selected_location = choose_location(self.location)
        count_pic = get_count_pic()
        capture_images(self.location, selected_location, count_pic)
