from streetview import search_panoramas, get_streetview
import re

charlie_api_key = "AIzaSyDEfSRd6SvLjAeM6t1OGEAvDN_i6OjDIi0"
    #plz dont share

def get_id_from_pano(pano): #weirdly can't subscript the Panorama object to get pano_id so use regex on string representation of obj
    pattern = r"pano_id='([^']+)'"
    match = re.search(pattern, str(pano))
    if match:
        return match.group(1)
    return None


london = [51.509865, -0.118092] #lat, long. found this online

for lat_add in range(-5, 6): #-5 km to 5 km
    for long_add in range(-5, 6):
        lat = london[0] + 0.01 * lat_add #0.01 latitude/longitude is about 1 km
        lon = london[1] + 0.01 * long_add

        panos = search_panoramas(lat=lat, lon=lon)
        if len(panos) > 0:
            closest = panos[0]
            id = get_id_from_pano(closest)

            image = get_streetview(
                pano_id="_R1mwpMkiqa2p0zp48EBJg",
                api_key=charlie_api_key
            )

            image.save(f"London/{id}.jpg", "jpeg")

            print(f"Lat: {lat}, long:{lon}, id:{id}")
