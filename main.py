import requests

BASE_URI = "https://www.bitmex.com/api/v1"
QUOTE_URI = BASE_URI+"/quote/bucketed"

def getCloses(tf, csv, count):
    param = {
    "symbol": "XBTUSD",
    "binSize": tf,
    "count": count,
    "reverse": True
    }
    

    response = requests.get(QUOTE_URI, params=param)
    bitmex = [close for close in response.json()]
    bitmex.reverse()

    with open(csv, "a") as file:
        for close in bitmex:
            file.write(f"{close['timestamp'].split('T')[0]}, {close['timestamp'].split('T')[1].split('.')[0]} ,{round(close['bidPrice'])} \n")


getCloses("1h", "bitcoin-1h-closes.csv", 24)
getCloses("1d", "bitcoin-1d-closes.csv", 1)
getCloses("5m", "bitcoin-5m-closes.csv", 288)

