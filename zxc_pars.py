import requests
from bs4 import BeautifulSoup

#код уродливый, да

class zxc_pars():
    def zxc(self):
        _list = ['Овен','Телец','Рак','Рыбы','Водолей','Козерог','Дева','Близнецы','Лев','Весы','Скорпион','Стрелец']
        url = 'https://vk.com/wall-193489972?own=1'
        r = requests.get(url)
        html_doc = r.text
        soup = BeautifulSoup (html_doc, 'html.parser')
        z = soup.findAll("div", {"class": "pi_text"})[1].get_text()[1:]
        #я уверен что это можно оптимизировать, но я не знаю как
        z = z.replace(_list[0],'<:swastika:786866651148058635>' + _list[0]).replace(_list[1],'\n'+_list[1]).replace(_list[2],'\n<:kotikfeeee:830398580551712768>'+_list[2]).replace(_list[3],'\n<:GayPride:509424847026126854>'+_list[3]).replace(_list[4],'\n<:toxic:841049700546117663>'+_list[4]).replace(_list[5],'\n'+_list[5])
        z = z.replace(_list[6],'\n'+_list[6]).replace(_list[7],'\n<:TehePelo:509424973442711562>'+_list[7]).replace(_list[8],'\n'+_list[8]).replace(_list[9],'\n<:roflanEbalo:509400537133744149>'+_list[9]).replace(_list[10],'\n'+_list[10]).replace(_list[11],'\n<:stalin:786867127092117505>'+_list[11])
        #я придумал как это сделать, но сделаю потом (цикл и второй список)
        return z

#x = zxc_pars()
#print(x.zxc())
