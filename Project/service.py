from flask import Flask
from respOfModel import *
import datetime
from filmOnerisi.movieReccom import oneriYap
from yemekOnerisi import yemekOneriApp
from apiler.nobetciEczaneApi import eczaneBul
from apiler.havaDurumuApi import havaDurumu
from notIslemleri import *
import webbrowser


app = Flask(__name__)

@app.route("/getResp/<string:text>")
def getResp(text):
    resp = getResponse(text)
    return resp

@app.route("/saat")
def saatiSoyle():
    saat = datetime.datetime.now().strftime("%H:%M:%S")
    return saat

@app.route("/arama/<string:text>")
def webdeAra(text):
    url = "https://google.com/search?q="+text
    webbrowser.get().open(url)
    return f"{text} ile ilgili bulduklarım bunlar."

@app.route("/filmOnerisi/<string:text>")
def filmOner(text):
    resp = oneriYap(text)
    mov = random.choice(resp)
    return f'O zaman {mov} filmini de sevebilirsin.'

@app.route("/yemekOnerisi/<string:inp>")
def yemekOner(inp):
    resp = yemekOneriApp.oneriYap(inp)
    return resp

@app.route("/nobetciEczane/<string:il>,<string:xloc>,<string:yloc>")
def nobetciEczane(il,xloc,yloc):
    resp = eczaneBul(il,xloc,yloc)
    return resp

@app.route("/notAl/<string:baslik>,<string:icerik>")
def notAlma(baslik,icerik):
    resp = notAl(baslik,icerik)
    return resp

@app.route("/baslikIleNotSil/<string:baslik>")
def notSil1(baslik):
    resp = baslikIleNotSil(baslik)
    return resp

@app.route("/tarihIleNotSil/<string:tarih>")
def notSil2(tarih):
    resp = tarihIleNotSil(tarih)
    return resp

@app.route("/butunNotlariSil")
def notSil3():
    resp = butunNotlariSil()
    return resp

@app.route("/baslikIleNotGoster/<string:baslik>")
def notBul1(baslik):
    resp = baslikIleNotGoster(baslik)
    return resp

@app.route("/tarihIleNotGoster/<string:tarih>")
def notBul2(tarih):
    resp = tarihIleNotGoster(tarih)
    return resp

@app.route("/butunNotlariGoster")
def notBul3():
    resp = butunNotlariGoster()
    return resp

@app.route("/havaDurumu/<string:city>")
def hava(city):
    resp = havaDurumu(city)
    return resp



    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)























