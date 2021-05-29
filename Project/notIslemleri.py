import sqlite3
import datetime
import locale

locale.setlocale(locale.LC_ALL, '')

def databaseOlustur():
    connection = sqlite3.connect("database.db")


def tabloOlustur():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    sql = "CREATE TABLE IF NOT EXISTS notlar (tarih DATETIME, baslik TEXT, icerik TEXT)"
    cursor.execute(sql)

    connection.commit()
    connection.close()

def notAl(baslik, icerik):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    trh = datetime.datetime.today()
    tarih = datetime.datetime.strftime(trh, "%d %B %Y")

    sql1 = f'SELECT baslik FROM notlar WHERE baslik = "{baslik}"'
    cursor.execute(sql1)
    veri = cursor.fetchall()
    

    if not veri:
        sql2 = f'INSERT INTO notlar VALUES("{tarih}", "{baslik}", "{icerik}")'
        cursor.execute(sql2)
    else:
        i = len(veri)
        baslik = f'{baslik} {i+1}'
        sql3 = f'INSERT INTO notlar VALUES("{tarih}", "{baslik}", "{icerik}")'
        cursor.execute(sql3)

    connection.commit()
    connection.close()
    return f'{baslik} başlıklı not başarı ile kaydedildi.'

def baslikIleNotSil(baslik):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    sql = f'DELETE FROM notlar WHERE baslik="{baslik}"'
    cursor.execute(sql)

    connection.commit()
    connection.close()

    return f'{baslik} başlıklı not başarı ile silindi.'

def tarihIleNotSil(tarih):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    sql = f'DELETE FROM notlar WHERE tarih="{tarih}"'
    cursor.execute(sql)

    connection.commit()
    connection.close()                                    

    return f'{tarih} tarihli bütün notlar başarı ile silindi.'

def butunNotlariSil():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    sql1 = "SELECT * FROM notlar"
    cursor.execute(sql1)
    veri = cursor.fetchall()

    if not veri:
        return "Silmek için bir not bulamadım."
    else:
        sql2 = f'DELETE FROM notlar'
        cursor.execute(sql2)

        connection.commit()
        connection.close()

        return "Bütün notların silindi."


def baslikIleNotGoster(baslik):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    sql = f'SELECT * FROM notlar WHERE baslik="{baslik}"'
    cursor.execute(sql)

    veri = cursor.fetchall()
    if not veri:
        return "Bu isimde bir not bulamadım."
    else:
        tVeri = ""
        for n in veri:
            for i in n:
                tVeri = tVeri + i + " - "
            tVeri = tVeri + "&"

        connection.commit()
        connection.close()

        return tVeri

def tarihIleNotGoster(tarih):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    sql = f'SELECT * FROM notlar WHERE tarih="{tarih}"'
    cursor.execute(sql)

    veri = cursor.fetchall()
    if not veri:
        return "Bu tarihte bir not bulamadım."
    else:
        tVeri = ""
        for n in veri:
            for i in n:
                tVeri = tVeri + i + " - "
            tVeri = tVeri + "&"

        connection.commit()
        connection.close()

        return tVeri

def butunNotlariGoster():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    sql = 'SELECT * FROM notlar'
    cursor.execute(sql)

    veri = cursor.fetchall()
    if not veri:
        return "Hiç notun yok"
    else:
        tVeri = ""
        for n in veri:
            for i in n:
                tVeri = tVeri + i + " - "
            tVeri = tVeri + "&"

        connection.commit()
        connection.close()

        return tVeri




















    
