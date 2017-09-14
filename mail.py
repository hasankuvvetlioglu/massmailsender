import smtplib as sm 

from tkinter import *

class MailSender():
    def __init__(self):
        self.pencere = Tk()
        self.giris_pencere_olustur()
        
    def giris_pencere_olustur(self):
        try:
            self.uyari_penceresi_yok_et()
        except:
            pass
        self.pencere.title("Giriş")
        self.pencere.geometry("420x130")

        self.metin1 = Label(text="Öncelikle GMAIL hesabınıza giriş yapmalısınız!",font=20)
        self.metin1.grid(row=0,column=0,columnspan=5,padx=6,pady=4)

        self.metin2 = Label(text="Mail adresinizi giriniz:", font=15)
        self.metin2.grid(row=1,column=0,columnspan=3,padx=6,pady=2)

        self.mail_adresi = Entry()
        self.mail_adresi.grid(row=1,column=3,columnspan=2,padx=6,pady=2)

        self.metin3 = Label(text="Şifrenizi giriniz: ", font=15)
        self.metin3.grid(row=2,column=0,columnspan=3,padx=6,pady=2)

        self.mail_sifresi = Entry(show="*")
        self.mail_sifresi.grid(row=2,column=3,columnspan=2,padx=6,pady=2)

        self.buton_giris = Button(text="Giriş", command=self.giris_yap)
        self.buton_giris.grid(row=3,column=0,columnspan=5,padx=6,pady=2)

    def giris_pencere_yok_et(self):
        self.metin1.grid_forget()
        self.metin2.grid_forget()
        self.mail_adresi.grid_forget()
        self.metin3.grid_forget()
        self.mail_sifresi.grid_forget()
        self.buton_giris.grid_forget()

    def uyari_penceresi(self):
        self.giris_pencere_yok_et()

        self.pencere.title("Uyarı!")
        self.pencere.geometry("410x80")
        self.metin_uyari = Label(fg="red",font=30)
        self.metin_uyari.grid(row=0,column=0,columnspan=5,padx=6,pady=2)
        
        self.buton_tamam = Button(text="Tamam", comman=self.giris_pencere_olustur)
        self.buton_tamam.grid(row=1,column=0,columnspan=5,padx=6,pady=2)

    def uyari_penceresi_yok_et(self):
        self.metin_uyari.grid_forget()
        self.buton_tamam.grid_forget()

    def mail_kontrol(self):
        self.gmail_adresi = "@gmail.com"
        self.girilen_mail_adresi = self.mail_adresi.get()
        
        try:
            if self.girilen_mail_adresi[-10:] != self.gmail_adresi:
                self.uyari_penceresi()
                self.metin_uyari['text'] = "Lütfen geçerli bir mail adresi giriniz!"
            else: self.sifre_kontrol()

        except NameError:
            self.uyari_penceresi()
            self.metin_uyari['text'] = "Lütfen bir mail adresi giriniz!"

    def sifre_kontrol(self):
        self.kullanici_sifresi = self.mail_sifresi.get()

        if not len(self.kullanici_sifresi)>0:
            self.uyari_penceresi()
            self.metin_uyari['text'] = "Şifre alanı boş bırakılmamalı!"

        else: self.mail_hesabina_giris()
            

    def giris_yap(self):
        self.mail_kontrol()

    def mail_hesabina_giris(self):
        self.hazir()
        try:
            self.mail.login(self.girilen_mail_adresi,self.kullanici_sifresi)
        except:
            self.uyari_penceresi()
            self.pencere.geometry("410x100")
            self.metin_uyari['text'] = "Giriş GMAIL tarafından kabul edilmedi!\nLütfen bilgilerinizi kontrol ediniz ve \n düşük güvenlikli uygulamalar için izin veriniz."
        else: self.main_ekran_olustur()
    def hazir(self):
        self.mail = sm.SMTP("smtp.gmail.com", 587)
        self.mail.ehlo()
        self.mail.starttls()
    def main_ekran_olustur(self):
        
        self.giris_pencere_yok_et()
        self.pencere.title("Toplu Mail Gönder")
        self.pencere.geometry("260x190")

        self.metin4 = Label(text="Alıcıları virgül ile ayırınız.", font=20)
        self.metin4.grid(row=0,column=0,columnspan=3,padx=6,pady=2)

        self.alicilar = Entry()
        self.alicilar.grid(row=1,column=0,columnspan=3,padx=6,pady=2)

        self.metin5 = Label(text="Göndereceğiniz metni yazınız: ",font=20)
        self.metin5.grid(row=2,column=0,columnspan=3,padx=6,pady=2)
        
        self.gonderilecek_metin = Entry()
        self.gonderilecek_metin.grid(row=3,column=0,columnspan=3,padx=6,pady=2)

        self.gonder_butonu = Button(text="Gönder!", comman = self.maili_gonder)
        self.gonder_butonu.grid(row=4,column=0,columnspan=3,padx=6,pady=2)

        self.metin8 = Label(text="Türkçe karakterler kullanmamaya\nözen gösteriniz.")
        self.metin8.grid(row=5,column=0,columnspan=3,padx=6,pady=2)
    
    def main_ekran_yok_et(self):
        self.metin4.grid_forget()
        self.alicilar.grid_forget()
        self.metin5.grid_forget()
        self.gonderilecek_metin.grid_forget()
        self.gonder_butonu.grid_forget()
        self.metin8.grid_forget()

    def maili_gonder(self):
        self.alici = self.alicilar.get()
        self.alici_listesi = self.alici.split(",")

        self.gonderilecek_yazi = self.gonderilecek_metin.get()
        self.turkce_harfler = {"ı":"i", "ğ":"g", "Ğ":"G", "ş":"s", "Ş":"S", "İ":"I", "ö":"o", "Ö":"O", "ü":"u", "Ü":"u" , "ç":"c", "Ç":"C"}
        self.yeni_metin = ""
        for self.harf in self.gonderilecek_yazi:
            if self.harf in self.turkce_harfler:
                self.harf2 = self.turkce_harfler[self.harf]
                self.yeni_metin += self.harf2
            else: self.yeni_metin += self.harf
        try:
            for self.kisi in self.alici_listesi:
                if len(self.kisi) > 0:
                    self.mail.sendmail(self.girilen_mail_adresi,self.kisi,self.yeni_metin)
                else: pass
        except:
            self.uyari2_penceresi_olustur()
        else:
            if len(self.alici) > 0:
                self.main_ekran_yok_et()
                self.basari_ekrani_olustur()
            else:
                self.uyari2_penceresi_olustur()

    def basari_ekrani_olustur(self):
        self.main_ekran_yok_et()

        self.pencere.title("Başarılı!")
        self.pencere.geometry("250x85")
        self.metin6 = Label(text="Mail başarıyla gönderildi!", fg="green", font=20)
        self.metin6.grid(row=0,column=0,columnspan=3,padx=6,pady=2)
        self.buton_tamam1 = Button(text="Tamamdır!", command=self.basari_ekrani_yok_et)
        self.buton_tamam1.grid(row=1,column=0,columnspan=3,padx=6,pady=2)
        

    def basari_ekrani_yok_et(self):
        self.metin6.grid_forget()
        self.buton_tamam1.grid_forget()
        self.main_ekran_olustur()

    def uyari2_penceresi_olustur(self):
        self.main_ekran_yok_et()
        self.pencere.title("Hatalı giriş!")
        self.pencere.geometry("500x150")
        self.metin7 = Label(text="Hatalı bir giriş yaptınız!\nLütfen bilgileri kontrol ediniz.\nGöderilen mailleri GMAIL hesabınızdan kontrol ediniz!",font=20,fg="red")
        self.metin7.grid(row=0,column=0,columnspan=3,padx=6,pady=2)
        self.buton_tamam2 = Button(text="Tamam", command=self.uyari2_penceresi_yok_et)
        self.buton_tamam2.grid(row=1,column=0,columnspan=3,padx=6,pady=2)

    def uyari2_penceresi_yok_et(self):
        self.metin7.grid_forget()
        self.buton_tamam2.grid_forget()
        self.main_ekran_olustur()

uyg = MailSender()
mainloop()