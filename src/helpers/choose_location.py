def choose_location(location):
    for idx, loc in enumerate(location):
        print(f"{idx + 1}. {loc}")
    i = input("Pilih lokasi: ")
    return int(i) - 1