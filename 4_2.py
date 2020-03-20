import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys


def futbolcu_kisisel_bilgileri(futbolcu_URL):
    URL = futbolcu_URL
    # URL = 'https://www.tff.org/Default.aspx?pageId=30&kisiId=1055923'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup.prettify())

    # isim = gelen_soup.find("span", id="ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuDisplay1_oyuncuBilgileri_lblAdi")
    # isim_text = list(isim)[0]
    # print(isim_text)
    # sys.exit()
    # my_tablex = gelen_soup.find_all(id_="ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuDisplay1_oyuncuBilgileri")
    # my_table = soup.find_all(id="ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuDisplay1_oyuncuBilgileri")
    my_table = soup.find("table", {"width": "100%", "border": "0", "cellspacing": "0", "cellpadding": "3"})
    print(len(my_table))
    print(my_table)
    sys.exit()
    rows_output = my_table.find_all('td')

    for i in rows_output:
        print(len(i))
        print(i)
        kisisel_bilgiler_baslik = i[0]
        dogum_yeri = i[1]
        dogum_tarihi = i[2]
        uyruk = i[3]
        # futbolcu_menajeri= i[4]

    print(kisisel_bilgiler_baslik, dogum_yeri, dogum_tarihi, uyruk)

    #
    # sys.exit()
    # rows_output = my_table.find_all(class_='GriBorder OyuncuKartAltBG')

    # print(type(rows_output))
    # print(rows_output)
    # sys.exit()

    """futbolcu_isim_resim = rows_output

    kisisel_bilgiler_baslik
    dogum_yeri
    dogum_tarihi
    uyruk
    #futbolcu_menajeri

    lisans_bilgileri_baslik
    lisans_no
    kulup
    sozlesme_baslangic_tarihi
    sozlesme_bitis_tarihi
    yurt_disina_cikis_tarihi"""


def futbolcu_hareket_bilgileri(futbolcu_URL):
    URL = futbolcu_URL
    # URL = 'https://www.tff.org/Default.aspx?pageId=30&kisiId=1055923'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup.prettify())

    isim = soup.find("span", id="ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuDisplay1_oyuncuBilgileri_lblAdi")
    isim_text = list(isim)[0]
    # sys.exit()
    my_table = soup.find('table', {'class': 'MasterTable_TFF_Contents'})
    # print(my_table)
    # sys.exit()
    # table = soup.find('table', border=1)
    rows_output = my_table.find_all('tr')
    print(type(rows_output))
    # print(type(rows))
    # print(rows)
    oynadigi_takim = []
    sozlesme_baslangic_tarihi = []
    sozlesme_bitis_tarihi = []
    lisans_turu = []
    lisans_verilis_tarihi = []
    yurtdisina_cikis_tarihi = []
    for row in rows_output:
        data = row.find_all("td")
        if len(data) > 0:
            # print(data[1].get_text().strip())
            oynadigi_takim.append(data[0].get_text().strip())
            sozlesme_baslangic_tarihi.append(data[1].get_text().strip())
            sozlesme_bitis_tarihi.append(data[2].get_text().strip())
            lisans_turu.append(data[3].get_text().strip())
            lisans_verilis_tarihi.append(data[4].get_text().strip())
            yurtdisina_cikis_tarihi.append(data[5].get_text().strip())

            # print(str(rn).strip() + "\t" + sr + "\t" + d + "\t" + n)
            # print(rn_list)

    oyuncu_hareketleri = pd.DataFrame({
        "OYNADIĞI TAKIM": oynadigi_takim,
        "SÖZLEŞME BAŞLANGIÇ TARİHİ": sozlesme_baslangic_tarihi,
        "SÖZLEŞME BİTİŞ TARİHİ": sozlesme_bitis_tarihi,
        "LİSANS TÜRÜ": lisans_turu,
        "LİSANS VERİLİŞ TARİHİ": lisans_verilis_tarihi,
        "YURTDIŞINA ÇIKIŞ TARİHİ": yurtdisina_cikis_tarihi
    })

    print(isim_text, "\n", oyuncu_hareketleri)

    # oyuncu_hareketleri.to_csv("futbolcu_bilgileri.csv", mode="a")


"""for i in range(105933, 105944):
    futbolcu_hareket_bilgileri('https://www.tff.org/Default.aspx?pageId=30&kisiId='+str(i)+'')"""

futbolcu_kisisel_bilgileri('https://www.tff.org/Default.aspx?pageId=30&kisiId=1055923')
futbolcu_hareket_bilgileri('https://www.tff.org/Default.aspx?pageId=30&kisiId=1055923')
