import requests
from bs4 import BeautifulSoup
from config import zz,zz_n


class zxc_pars():
    def zxc(self):
        url = 'https://vk.com/wall-193489972?own=1'
        r = requests.get(url)
        html_doc = r.text
        soup = BeautifulSoup (html_doc, 'html.parser')
        z = soup.findAll("div", {"class": "pi_text"})[1].get_text()[1:]
        for i in range(len(zz)):
            z = z.replace(zz[i],zz_n[i])
        z = z.replace('Показать полностью...','')
        return z

#x = zxc_pars()
#print(x.zxc())
