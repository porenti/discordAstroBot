import requests
from bs4 import BeautifulSoup

#код уродливый, да

class zxc_pars():
    def zxc(self):
        _list = ['Овен','Телец','Рак','Рыбы','Водолей','Козерог','Дева','Близнецы','Лев',
                'Весы','Скорпион','Стрелец']
        url = 'https://vk.com/wall-193489972?own=1'
        r = requests.get(url)
        html_doc = r.text
        soup = BeautifulSoup (html_doc, 'html.parser')
        z = soup.findAll("div", {"class": "pi_text"})[1].get_text()[1:]
        #я уверен что это можно оптимизировать, но я не знаю как
        z = z.replace(_list[0],_list[0]).replace(_list[1],'\n'+_list[1]).replace(_list[2],'\n'+_list[2]).replace(_list[3],'\n'+_list[3]).replace(_list[4],'\n'+_list[4]).replace(_list[5],'\n'+_list[5])
        z = z.replace(_list[6],'\n'+_list[6]).replace(_list[7],'\n'+_list[7]).replace(_list[8],'\n'+_list[8]).replace(_list[9],'\n'+_list[9]).replace(_list[10],'\n'+_list[10]).replace(_list[11],'\n'+_list[11])
        return z

#x = zxc_pars()
#print(x.zxc())