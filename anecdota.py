import requests
from random import randint as random


from config import _rnm_a


class anec_pars():
    def anec(self):
        n = random(0,len(_rnm_a)-1)
        url = 'http://rzhunemogu.ru/RandJSON.aspx?CType={}'.format(_rnm_a[n])
        r = requests.get(url)
        html = r.text
        anek = html[12:(len(html)-2)] #🤡
        return anek

#a = anec_pars()
#print(a.anec())
