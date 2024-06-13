from helpers.choose_location import choose_location
from helpers.capture_images import capture_images
from helpers.get_count_pic import get_count_pic

class ATCSKota:
    def __init__(self):
        self.location = [
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
    
    def run(self):
        selected_location = choose_location(self.location)
        count_pic = get_count_pic()
        capture_images(self.location, selected_location, count_pic)
