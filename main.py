from diaolog import Ui_Dialog
from giris import *
from kayit_ol import *
from kitap_kayit import *
from randevu import *
from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
randevu = QtWidgets.QWidget()
ui = Ui_randevu()
ui.setupUi(randevu)

app1 = QtWidgets.QApplication(sys.argv)
giris = QtWidgets.QWidget()
ui1 = Ui_giris()
ui1.setupUi(giris)

app2 = QtWidgets.QApplication(sys.argv)
kayit_ol = QtWidgets.QWidget()
ui2 = Ui_kayit_ol()
ui2.setupUi(kayit_ol)

app3 = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui3: Ui_Dialog = Ui_Dialog()
ui3.setupUi(Dialog)

app4 = QtWidgets.QApplication(sys.argv)
kitap_kayit = QtWidgets.QMainWindow()
ui4 = Ui_kitap_kayit()
ui4.setupUi(kitap_kayit)

import sqlite3

connect = sqlite3.connect("kutuphane.db")
cursor = connect.cursor()


def tablo_olustur():
    cursor.execute("Create Table if not exists kitaplık (kitap_no integer, kitap_adi text, yazar text, yayinevi text, teslim_tarihi text )")
    connect.commit()


def tablo2_olustur():
    cursor.execute("Create Table if not exists giris (kullanici_adi int,sifre int )")
    connect.commit()


def tablo3_olustur():
    cursor.execute("Create Table if not exists randevu(kat int, masa int, tarih text)")


tablo_olustur()
tablo2_olustur()
tablo3_olustur()


class Kitaplarin_bilgisi:
    def __int__(self):
        self.girisac()
        self.Dialogac()
        self.kayitolac()
        self.kitapkayitac()
        self.randevuac()

    def girisac():
        giris.show()
        sys.exit(app.exec_())
        Dialog.close()
        kayit_ol.close()
        randevu.close()
        kitap_kayit.close()

    def Dialogac():
        giris.close()
        Dialog.show()
        sys.exit(app.exec_())
        kayit_ol.close()
        randevu.close()
        kitap_kayit.close()

    def kayitolac():
        giris.close()
        Dialog.close()
        kayit_ol.show()
        randevu.close()
        kitap_kayit.close()
        sys.exit(app.exec_())

    def randevuac():
        giris.close()
        randevu.show()
        sys.exit(app.exec_())
        kayit_ol.close()
        Dialog.close()
        kitap_kayit.close()

    def kitapkayitac():
        giris.close()
        randevu.close()
        kayit_ol.close()
        Dialog.close()
        kitap_kayit.show()
        sys.exit(app.exec_())


class giris_kısmı():
    def __init__(self):
        super.__init__(self)
        self.Ui2=Ui_kayit_ol
        self.Ui2.setupUi(self)
        self.kayitol_buttonkısmı()
    def kayitol_buttonkısmı(self):
        pass





    def girisbuttonu():
        kullanici_adi = ui1.lineEdit.text()
        sifre = ui1.lineEdit_2.text()
        cursor.execute("SELECT * FROM ogrenci WHERE kullanici_adi='%s' and sifre='%s'" % (kullanici_adi, sifre))
        connect.commit()
        Kitaplarin_bilgisi.kitapkayitac()







class kitapkayit:
    def kayıtbutton():
        kitap_no = ui4.kitapnoLine.text()
        kitap_adi = ui4.kitapAdiLine.text()
        yazar = ui4.yazarLine.text()
        yayinevi = ui4.yayineciLine.text()
        teslim_tarihi = ui4.teslimTarihiLine.text()
        cursor.execute("Insert into kitaplık (kitap_no, kitap_adi, yazar , yayinevi, teslim_tarihi) VALUES(?,?,?,?,?)",(kitap_no, kitap_adi, yazar, yayinevi, teslim_tarihi))
        connect.commit()
    def silbutton():
        pass

Kitaplarin_bilgisi.girisac()


