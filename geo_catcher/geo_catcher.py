import folium
import geocoder
import random

name = input("現在地: ")

a = geocoder.osm(name)
location = a.latlng

m = folium.Map(location=location)
folium.CircleMarker(location = location, radius=200
                         , popup = "あなたの行動範囲", color="black", fill=True, fill_color="white").add_to(m)

while True:
    name = input("気になる場所: ")
    if name == "":
        break

    a = geocoder.osm(name)
    location = a.latlng

    folium.Marker(location = location, popup = name).add_to(m)

m.save("location.html")
print("出力しました")
