from helpers.choose_location import choose_location
from helpers.capture_images import capture_images
from helpers.get_count_pic import get_count_pic

class BantulCCTV:
    def __init__(self):
        self.location = [
            "SimpangKorpriBarat",
            "TPRParangtritis",
            "PasarBantul",
            "MasjidMakamImogiri",
            "BendungNiten",
            "PerempatanPaseban",
            "SimpangKorpriUtara",
            "TerminalMakamImogiri",
            "BendungKlegen",
            "BunderanSrandakan",
        ]   

    def run(self):
        selected_location = choose_location(self.location)
        count_pic = get_count_pic()
        capture_images(self.location, selected_location, count_pic)