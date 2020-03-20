import requests
from bs4 import BeautifulSoup, ResultSet
import pandas as pd
from requests import Response


def futbolcu_kisisel_bilgileri(futbolcu_URL):
    URL = futbolcu_URL
    page: Response = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    dogum_yeris = soup.find('span', {'id':'ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuDisplay1_oyuncuBilgileri_Label7'})
    dogum_yeric = soup.find('span', {'id':'ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuDisplay1_oyuncuBilgileri_Label1'})
    print(dogum_yeris.string,":", dogum_yeric.string)
    dogum_tarihis = soup.find('span', {'id':'ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuDisplay1_oyuncuBilgileri_Label10'})
    dogum_tarihic = soup.find('span', {'id':'ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuDisplay1_oyuncuBilgileri_Label2'})
    print(dogum_tarihis.string,":", dogum_tarihic.string)

futbolcu_kisisel_bilgileri('https://www.tff.org/Default.aspx?pageId=30&kisiId=1055923')
