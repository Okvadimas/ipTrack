def ipTrack():
    import os
    import requests
    import json
    import socket
    p = requests.get("http://api.ipify.org")
    b = requests.get("http://ip-api.com/json/").text

    c = json.loads(b)

    print("-" * 13, f"PUBLIC {p}", "-" * 14)
    print("   Hostname :", socket.gethostname())
    print("   IP address :", socket.gethostbyname(socket.gethostname()))
    print("   Country :", c["country"])
    print("   City :", c["city"])
    print("   Region :", c["regionName"])
    print("   Provider :", c["isp"])
    print("   Latittude :", c["lat"])
    print("   Longitude :", c["lon"])
    print("   Public Address:", c["query"])


ipTrack()
