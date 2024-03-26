# CCTV Crawler 

Simple CCTV Crawler for Jogja ATCS CCTV

## Installation

To install this crawler, follow the required steps below:
1. Clone the repository:
```
git clone https://github.com/prammmoe/cctv-crawler.git
```

2. Install cv2

```
pip install opencv-python
```

3. Run the script using (run from src) 

```
python main.py
```

or

```
python src/main.py
```
When running from parent directory

## Documentations

### Location 

For the location code below:

```
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
```

You can add more specific location by adding it into the list. Some locations are disabled for crawling, but you can try your luck.

### Pathing

Image directory will automatically made when the code finish running and collecting image. The directory saving the file is in images folder and the location will be the subfolder.

Complete structure:

    .
    ├── images
    │   ├──
    │   {location} 
    │   └──
    │   {image files}
    ├── src                     # Source files 
    │   └──
    │   main.py                 # main script 
    ├── .gitignore
    └── README.md


### Endpoint

1. MAM Jogjaprov Endpoint 
```
https://mam.jogjaprov.go.id:1937/{cctv-category}
```
For the CCTV Category, you can change based what shown on the website https://mam.jogjaprov.go.id/cctvs

Prefer using just two endpoint: /atcs/ and /atcs-kota/

2. CCTV Jogjakota Endpoint
```
https://cctvjss.jogjakota.go.id/atcs/
```
For the CCTV endpoint, we only used /atcs/ as referred from https://cctv.jogjakota.go.id/