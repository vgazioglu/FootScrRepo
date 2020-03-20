import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys


def futbolcu_kisisel_bilgileri(futbolcu_URL):
    URL = futbolcu_URL
    # URL = 'https://www.tff.org/Default.aspx?pageId=30&kisiId=1055923'
    page = requests.get(URL)
    # print(page)
    soup = BeautifulSoup(page.content, "html.parser")
    # print(soup.prettify())

    # isim = gelen_soup.find("span", id="ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuDisplay1_oyuncuBilgileri_lblAdi")
    # isim_text = list(isim)[0]
    # print(isim_text)
    # sys.exit()

    my_table = soup.find("table", {"border": "0", "cellpadding": "3", "cellspacing": "0", "width": "100%"})
    # my_table = soup.find("table", id="ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuDisplay1_oyuncuBilgileri")
    board_members = []

    for row in my_table.find_all_next('tr'):
        print(type(row), "\n")
        print(len(row), "\n")
        print("|----->", row.text, "<-----|", "\n")
        for cols in row.find_all('td'):
            print("|*****>", cols.text, "<*****|", "\n")




            """board_members.append(
                (b, cols[0].text.strip(), cols[1].text.strip(), cols[2].text.strip(), cols[3].text.strip()))

    rows_output = my_table.find_all('td')

    for i in rows_output:
        print(len(i))
        print(i)
        kisisel_bilgiler_baslik = i[0]
        dogum_yeri = i[1]
        dogum_tarihi = i[2]
        uyruk = i[3]
        futbolcu_menajeri = i[4]

    # print(kisisel_bilgiler_baslik, dogum_yeri, dogum_tarihi, uyruk, futbolcu_menajeri)"""


futbolcu_kisisel_bilgileri('https://www.tff.org/Default.aspx?pageId=30&kisiId=1055923')
