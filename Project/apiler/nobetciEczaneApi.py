import numpy as np

def isimKontrol(isim):
    Tr2Eng = str.maketrans("çğıöşü", "cgiosu")
    isim = isim.translate(Tr2Eng)
    if " " in isim:
        isim = isim.replace(" ","")
    return isim

def haversine_distance(lat1, lon1, lat2, lon2):
   r = 6371
   phi1 = np.radians(lat1)
   phi2 = np.radians(lat2)
   delta_phi = np.radians(lat2 - lat1)
   delta_lambda = np.radians(lon2 - lon1)
   a = np.sin(delta_phi / 2)**2 + np.cos(phi1) * np.cos(phi2) *   np.sin(delta_lambda / 2)**2
   res = r * (2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a)))
   return np.round(res, 2)
                       
def eczaneBul(il, xloc, yloc):
    import http.client
    import json
    
    il = isimKontrol(il.lower())
    
    xloc = float(xloc)
    yloc = float(yloc)
    
    conn = http.client.HTTPSConnection("www.nosyapi.com")
    boundary = ''
    payload = ''
    headers = {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer jcvw5t7UyqijTWYqR8nGEKaLFNjMlpr37HqSIFKKEcQHh20DWYoBo35xATy0',
      'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
    }
    conn.request("GET", f"/apiv2/pharmacy?city={il}", payload, headers)
    res = conn.getresponse()
    data = res.read()
    data = data.decode("utf-8")
    data = json.loads(data)

    minName = ""
    minDist = 9999
    
    for line in data["data"]:
        x = line["latitude"]
        y = line["longitude"]
        dist = haversine_distance(xloc,yloc,x,y)
        if dist < minDist:
            minDist = dist
            minName = line["EczaneAdi"]

    return minName
