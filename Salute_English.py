
#başlıyorum ---- Penceremizi oluşturalım
import customtkinter as ctk

#jsonu çağıralım
import json as js
#pillow çağıralım
from PIL import Image

#bunlarda önemli
import os
import sys
def kaynak_yolu(goreli_yol):
    try:
        temel_yol = sys._MEIPASS
    except AttributeError:
        temel_yol = os.path.abspath(".")

    return os.path.join(temel_yol, goreli_yol)

#denemeeee
with open(
    kaynak_yolu("questions.json"),
    "r",
    encoding="utf-8"
) as dosya:
    sual = js.load(dosya)

#index
index=0

#ünite seçmek için fonksiyon
def unite_sec(unite_no):
    global aktif_unite, index

    aktif_unite = sual[f"unit{unite_no}"]
    index = 0
    soru_goster()
    soru_ekranı.tkraise()


def buton_boyutlandir(event):
    yukseklik = max(60, int(app.winfo_height() * 0.15))
    genislik = int(yukseklik * 2 / 3)

    for buton in unit_butonlari+şık_butonları:
        buton.configure(width=genislik, height=yukseklik)


#doğru mu yanllış mı?
def kontrol(secilen_cevap):
    dogru_cevap = aktif_unite[index]["dogru_cevap"]
    if secilen_cevap == dogru_cevap:
        bildirim_metni = "Evet, cevabınız doğru."
        renk = "#1c362d"   # açık yeşil
    else:
        bildirim_metni = f"Hayır, cevabınız yanlış. Doğru cevap: {dogru_cevap}"
        renk = "#8B0000"   # koyu kırmızı

    sonuc_bildirim = ctk.CTkToplevel(master=soru_ekranı)
    sonuc_bildirim.overrideredirect(True)
    sonuc_bildirim.attributes("-topmost", True)
    sonuc_bildirim.configure(fg_color="#f8f0e5")

    genislik, yukseklik = 300, 80
    x = app.winfo_screenwidth() - genislik - 20
    sonuc_bildirim.geometry(f"{genislik}x{yukseklik}+{x}+20")

    cerceve = ctk.CTkFrame(master=sonuc_bildirim, corner_radius=10)
    cerceve.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
    cerceve.configure(fg_color="#f8f0e5")

    etiket = ctk.CTkLabel(
        master=cerceve,
        text=bildirim_metni,
        text_color=renk,
        wraplength=250,
        anchor="w",
        font=( "Arial", 24 )
    )
    etiket.grid(row=0, column=0, sticky="nsew", padx=15, pady=12)

    cerceve.grid_columnconfigure(0, weight=1)
    sonuc_bildirim.after(3000, sonuc_bildirim.destroy)
   

#ölçekli ol please
def olcekli_resim_yukle(resim_yolu, genislik_orani=0.9, yukseklik_orani=0.5):

    pil_resim = Image.open(resim_yolu)

    app.update_idletasks()

    hedef_genislik = int(app.winfo_width() * genislik_orani)
    hedef_yukseklik = int(app.winfo_height() * yukseklik_orani)

    orijinal_genislik, orijinal_yukseklik = pil_resim.size

    oran = min(
        hedef_genislik / orijinal_genislik,
        hedef_yukseklik / orijinal_yukseklik
    )

    yeni_genislik = int(orijinal_genislik * oran)
    yeni_yukseklik = int(orijinal_yukseklik * oran)

    return ctk.CTkImage(
        light_image=pil_resim,
        dark_image=pil_resim,
        size=(yeni_genislik, yeni_yukseklik)
    )

#soru gösterme fonksiyonu
def soru_goster():

    gorsel_yolu= kaynak_yolu(
    aktif_unite[index]["soru"]
)

    ctk_resim = olcekli_resim_yukle(
        gorsel_yolu,
        0.9,
        0.5
    )

    soru_label.configure(image=ctk_resim)
    soru_label.image = ctk_resim

#ileri tuşu comandı
def ileri():
    global index
    son_indeks = min(39, len(aktif_unite) - 1)

    if index < son_indeks:
        index += 1
        soru_goster()
   


#geri tuşu commandı     
def geri():
    global index
    if index > 0:
        index -= 1
        soru_goster()


def yeniden_boyutlandir(event):
    yeni_boyut = max(16, min(32, int(app.winfo_width() * 0.03)))
    #info_font.configure(size=yeni_boyut)

print(kaynak_yolu("sorular/001.png"))
print(kaynak_yolu("questions.json"))


#BU KSIMDAN SONRASI GUI İLE İLGİLİDİR
#BU KSIMDAN SONRASI GUI İLE İLGİLİDİR
#BU KSIMDAN SONRASI GUI İLE İLGİLİDİR


#penceremiz 
app=ctk.CTk()
app.title("adını bilmediğim ama ilerde adı olacak olan proje")
app.attributes("-fullscreen", True)
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1),
app.configure(fg_color="#100B1D")

#frame sistemini oluşturacağım(umarım🤲)
ekran_1=ctk.CTkFrame(app)
ekran_1.configure(fg_color="#f8f0e5")
soru_ekranı=ctk.CTkFrame(app)
ekran_1.grid(row=0, column=0, sticky="nsew")
soru_ekranı.grid(row=0, column=0, sticky="nsew")
soru_ekranı.configure(fg_color="#f8f0e5")
info_ekranı=ctk.CTkFrame(app)
info_ekranı.grid(row=0, column=0, sticky="nsew")
info_ekranı.configure(fg_color="#f8f0e5")
ekran_1.tkraise()

def info_ac():
    info_ekranı.tkraise()

#framelerin grid sistemi
for i in range(4):
    ekran_1.grid_columnconfigure(i, weight=1)
for i in range(6):
    ekran_1.grid_rowconfigure(i, weight=1)

#framelerin grid sistemi
for i in range(4):
    soru_ekranı.grid_columnconfigure(i, weight=1)
for i in range(6):
    soru_ekranı.grid_rowconfigure(i, weight=1)

#çıkış tuşunu unutmuşum pardon 
cks=ctk.CTkButton(
    master=ekran_1,
    text="Çıkış",
    command=app.destroy,
    height=75,
    width=100
)
cks.configure(fg_color="#123327", hover_color="#3a745f", text_color="#ccb79b")
cks.grid(row=0, column=3, padx=20, pady=0, sticky="e")

#ünite tuşları
unit_butonlari = [] 
for i in range(1, 11):
    unit = ctk.CTkButton(
        master=ekran_1,
        text=f"Ünite {i}",
        command=lambda x=i: unite_sec(x), height=90, width=150
    )
    unit.configure(fg_color="#1c362d", hover_color="#26493D", text_color="#ccb79b")

    unit.grid(
        row=(i-1)//2 ,
        column=(i-1)%2,
        padx=10,
        pady=0,
        sticky="w"
    )
    unit_butonlari.append(unit)

#ana ekrana dön
ana_ekrana_dön=ctk.CTkButton(
    master=soru_ekranı,
    text="Ana Ekran'a Dön",
    command=ekran_1.tkraise
)
ana_ekrana_dön.configure(fg_color="#266851", hover_color="#3a745f", text_color="#f8f0e5")
ana_ekrana_dön.grid(row=0, column=0, padx=10, pady=10)

#şıklar çok şıklar HAHAHHAHAHA
şık_butonları=[]
şıklar=["A", "B", "C", "D"]
for i, şık in enumerate (şıklar):
    şık_tuşu=ctk.CTkButton(
        master=soru_ekranı,
        text=şık,
        command=lambda secilen=şık: kontrol(secilen),
        width=150,
        height=75
    )

    şık_tuşu.configure(fg_color="#0E3023", hover_color="#174d39", text_color="#ccb79b")
    şık_tuşu.grid(row=3, column=i, padx=10, pady=10)
    şık_butonları.append(şık_tuşu)

#soru göster
soru_label = ctk.CTkLabel(
    master=soru_ekranı,
    text=""
)

soru_label.grid(
    row=1,
    column=0,
    columnspan=4,
    sticky="nsew"
)

#ileri tuşu
ileri_tuşu=ctk.CTkButton(
    master=soru_ekranı, 
    text="İleri",
    command=ileri
)
ileri_tuşu.configure(fg_color="#4d6a4e", hover_color="#425d43", text_color="#f8f0e5")
ileri_tuşu.grid(row=0, column=2, padx=10, pady=10)

#geri tuşu
geri_tuşu=ctk.CTkButton(
    master=soru_ekranı,
    text="Geri",
    command=geri
)
geri_tuşu.configure(fg_color="#4d6a4e", hover_color="#425d43", text_color="#f8f0e5")
geri_tuşu.grid(row=0, column=1, padx=10, pady=10) 

#info_metni
info_font = ctk.CTkFont(size=20)
info=ctk.CTkLabel(
    master=ekran_1,
    text="Çözmek istediğiniz üniteyi seçip açabilirsiniz🎀",
    font= info_font,
    text_color="#0E3023")

app.bind("<Configure>", yeniden_boyutlandir)
info.grid(row=1, column=4, sticky="nsew")
info.configure(wraplength=app.winfo_width()*0.8)

info_butonu=ctk.CTkButton(
    master=ekran_1,
    text= "Hakkında", 
    fg_color="#0E3023", 
    hover_color="#174d39",
    command=info_ac
)

info_butonu.grid(row=4, column=6, padx=10, pady=10)
about_text = "Salute English v1.0\n\nUsed Technologies:\nPython\nCustomTkinter\n\nQuestion Content:\n\n\nDeveloper:\nCivan Nur"

about_label = ctk.CTkLabel(
    master=info_ekranı,
    text=about_text,
    justify="left",
    text_color="#0E3023",
    font=info_font
)
about_label.grid(row=5, column=4, )
about_label.configure(wraplength=app.winfo_width()*0.8)


kapat_btn = ctk.CTkButton(
    master=info_ekranı,
    text="← Ana Menü",
    width=150,
    command=ekran_1.tkraise,
    fg_color="#0E3023", 
    hover_color="#174d39"
)

kapat_btn.grid(column=0,row=0)

print(kaynak_yolu("sorular/001.png"))
print(kaynak_yolu("questions.json"))

#PENCEREYİ AÇIK TUTMAK İÇİN FONKSİYON

app.mainloop()
