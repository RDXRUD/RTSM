from websocket import create_connection
import json
import pandas as pd


socket= "wss://prodata.tradingview.com/socket.io/websocket"

# ~m~55~m~{"m":"chart_create_session","p":["cs_ioPrMxKyQTRQ",""]}

ws=create_connection(socket)


def create_msg(ws,fun,arg):
   ms=json.dumps({"m":fun,"p":arg})
   msg="~m~"+str(len(ms))+"~m~"+ms
   print(msg)
   ws.send(msg)

create_msg(ws,"chart_create_session",["cs_ioPrMxKyQTRQ",""])
create_msg(ws,"resolve_symbol",["cs_ioPrMxKyQTRQ","sds_sym_1","={\"adjustment\":\"splits\",\"symbol\":\"NVDA\"}"])
create_msg(ws,"create_series",["cs_ioPrMxKyQTRQ","sds_1","s1","sds_sym_1","1D",300,""])
# # create_msg(ws,"create_series",["cs_ioPrMxKyQTRQ","sds_1","s1","sds_sym_1","1D",10,""])
create_msg(ws,"create_study",["cs_ioPrMxKyQTRQ","st12","st1","sds_1","BarSetContinuousRollDates@tv-corestudies-28",{"currenttime":"now"}])
# # ~m~3824~m~{"m":"create_study","p":["cs_ioPrMxKyQTRQ","st13","st1","sds_1","Script@tv-scripting-101!",{"text":"bmI9Ks46_pRO+m5YAQUmxRa07gLXBCw==_0cIHbbqYN6ICMwkyd9+Q0/lqSi6ymXHwK7oHb+YC0DCnCV9dvMPN7huDqi5ygluemrrIvGVGVq9J813g6YBXHwy/11gLnKwq8B7dqGNfkdvlEkl7eJiGZFkVRyU1ESUHe7upX6sV0CXdq4XkeSPfNFkMSEWNzYlTkQQRpwgNhB25FjVxQPh5ZzzggtviE4RfqYhdOZqCSyVidgNH+Fq4Fhl6OVKfbkjfAF6Q4mEwvs/A9Ymx0te1LalBIS1Ugq6DuYS9+uxMxPzGDkkma9ZgalfXafyR2TUmjOOXWDNmWYp2STcf5I0Djx7WLhS9y8sh5FqRoTHqj8ZSS+IrIyjGgKaQZLG4iwxYPVkvpjLaRJrbJsHtjF1LtikjDgzIyutpJVdY7DY1tZ/rXzexKRmgU92I/3PfJG6NVStMtxA3q3j58ZdCu066vc4qGOw44X9FnTuFaqX+WtdYv8LkH6F+J4G3ITssRWwGZi9E55B2pVLODgFyh4bX5AV++Nywkp82Ee4eom8Refaym3g0untyI0uddNnw5bpkW+YlPKIgPqdGBWUyxczUJVKphN/co55UjMcG4mNodaPjzmiG5CxdwquGLgQjX84GA3KbtOdtxNAZ6C3grnm1iP8PQEypiNhr2b4qsQz4TwzDbUrw3N6GkxLPgxdaevNETw6LBpGu2enomFpco2gkmmeZHb+EAuoEBL0wPdS4WiHYF+zvQIWTVol2ZzrcYvz9ykBQk3zxPDXjAZYcNWEuK1Hdh0+JPB+H5FazTEzEdCHyBYyJOi13dYFG3vHMrejrsVCWLJcMu4VuyFWn4qG3P03pHgRhKzX/1vNHW22JqXSvZyM07PpSB8wuSjR2U6EIaMqSFdOuGuOJVDVNjCk4koOeyPhTZKGJ175DfNLwaXTAR/wClhBBtnaDFQBlIv7QQS520y9VnI0+XcRqZk9c/7BIyzg1OUHkfbhDaDhs9ZX8rhY7w8E7G1NSsp8a5wnyW6/dNj2udCK+2UYOf42/CkJgkLYe7FZPSGFFEDrp5IJN4V/U7Wyhb67OoJDR/jUqvzeE93ekyzFKqJDYbcykzCdFxgrEheuBvFK85F0ebteqzntFaJCm8U9iIBRneLKN5ocgtEXNQeC4ac4UWq6XP0wG/t0rdudp7KbzUsqZ3GBoo1gM4oHgtAsOcUlNTLyhJ+mw3j5rha2wsx68ytrs/rx7QMvSGX+KrFrRahq5aYe6Yh3K9PrFzn0ssMayGfC8bgj6bQhFN9vTm/ANFQH7OnfSxSt9gwscy8/mzMALWOZspIhZZnSm8Sng4yRzchp93hNskVLOAo7k7uJMHUKvFg8/6C5d/vQYyAt4ZE/OqUNS309oKbVNx+kXXM4eCKnbxfaV6oKeAdP+z70rUjBHge+TX/dlaGzC2CN3eGpZDzxAgtXkhnJNkh6YVr5+0mujvMLPkHmqZJDtOO0WxbAACBDYpTRv5Xa4+BOP7/rLTSBc1p+4VZvmGXBDC+X0uFVY4JZn2SkjdbosCRXyZm+srqU221Ow9rIzzaRhSf3VCVdPV+G6WhkRRA5YHqehHTLgGZKPM8XTnYitQQG4UULykW3qjsvb9qJBqBwBK3KxpFBRmoxMp/WgJqChI9ltX+n/zgiP2p07ZZCy54y+BG4lX3e88BmwH+ymYaZy5cm0hjOIabxs0NN8jgQYOHxmF/1qDbCFbbu2TFdu8S4r1XhqhFycGc5X2NEFP4wzjevGI9RGYCxVuJbCjl9iV+ItWWoLf0+Lp6YAu3+uG08mS6XdA3xMZGTRVQQaiMAR9CkA3bNoRaVcKTNHe3XDWXcJgXX7f0LL2ObwCma4DqgrFvP+MUIT0OxPhkMCOAmJ7MEbR0bodl/azHIj0WIYe7grLAy6/T/SXwPvWuyN9+eAtQ2M9NiBb4aYSJ9QJx8hxRBJWYl4zqdhFCbTZvwY5QPF/ADvlkMlddgKvgTyZBzFmrV9kWCwW0dqVkHmcGzX1J+Wd/UWj82aCaZwuIeF23v9nG8F6X6WgIO98VYWu6J+YiIdSEqn4Sff+fdFI/XfcT9JGJ1r0jJVrjrXoPsYxLlmNh8o7YWMCX2nU7LpRIhmRvcb0dukvZMlvbqPB3uR5cVPny8J1VabJh+Bh1YLkCvOT5kb5uu8HHMEwTJQ2mF83vMT2fSQNw4ZGkotcsB426U6ZRKTpKDLPMpcEh1fOMS9RjcmsPZZQ6yoKtToveDFknv8N6jSW2f/NxqKzx+6cMGYa94DnM3mVRwD++kuDXV5c+0d1Yz2GYOG0cyFoDVP2gwU3/7V52bQgZepwSWmy6a5sxncOZqzfHPLWN59gDGn8WzQ/fiMV046JLZoLeBe23FZBgItvHqhBEtj24+Ij8tbOSKPdTVr9VEuaBXvDM+bp1irDuWwK7WsJt2OJouSD1FoIr0mCzt/U9/d6yZgNesWRdKib6r+oSuH3epmg/lW9hKmjD0YmqKe02yWCZUAElopCaBcQY4aPYe700gMG+6uwzm3/+/iHNZ8ahaKgAo/45RuDvPoi8e38THp5MS3LvTnTv213y7NwQDP5hdyrjgln+56LgEPXWbrdtyx37NJKxGGXkZc3F6KWjAlVPBXwfCf5IJbrbG7yQf47A+BKT7YQagqVZG/azhqY9EXMGpjZzSnAjv6iU/pACHX3ymqvQaHqUcbEVA9JaUxKqrLqeE2tOTVCzhKUINCBkU5IlBdg85YtoszfDCcPf2rvmWetr5eyboGGwYYfblWawoPFLxBWHFgja7M0BGzJgX47ps77LvB","pineId":"PUB;UvZfCLbA4lM9Bj4j6LdBDJrDeZSlr2jx","pineVersion":"8.0","pineFeatures":{"v":"{\"indicator\":1,\"plot\":1,\"str\":1,\"ta\":1,\"math\":1,\"alertcondition\":1,\"label\":1,\"request.security\":1}","f":true,"t":"text"},"in_0":{"v":"close","f":true,"t":"source"},"in_1":{"v":"NSE:NIFTY","f":true,"t":"symbol"},"in_2":{"v":55,"f":true,"t":"integer"},"in_3":{"v":true,"f":true,"t":"bool"},"in_4":{"v":true,"f":true,"t":"bool"},"in_5":{"v":true,"f":true,"t":"bool"},"in_6":{"v":false,"f":true,"t":"bool"},"in_7":{"v":5,"f":true,"t":"integer"},"in_8":{"v":false,"f":true,"t":"bool"},"in_9":{"v":50,"f":true,"t":"integer"},"in_10":{"v":true,"f":true,"t":"bool"},"in_11":{"v":true,"f":true,"t":"bool"},"in_12":{"v":50,"f":true,"t":"integer"},"in_13":{"v":"rgba(76,175,80,0.15)","f":true,"t":"color"},"in_14":{"v":"rgba(242,54,69,0.15)","f":true,"t":"color"},"__profile":{"v":false,"f":true,"t":"bool"}}]}

def format_data(data):
    start=data.find('"s":[')
    end=data.find(',"ns":')
    final_data=json.loads(data[start+4:end])
    
    fdata=[]
    for item in final_data:
        fdata.append(item["v"])
    
    print(pd.DataFrame(fdata))
    
    


while True:
    res=ws.recv()    
    print(res)
    print("/n")
    
    # if "series_completed"  in res:
    #     break
    # format_data(res)