import discord
from random import randint as random


from zxc_pars import zxc_pars
from anecdota import anec_pars


from KEYS import ds_token,_hate_list_a
from config import _night_list,_night_list_a,_hate_list,_list_calls,_rnm,_rnm_a


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {}!'.format(self.user))


    async def on_message(self, message):
        if message.content.title() in _list_calls:
            _str = x.zxc().split('(x)')
            print(_str)
            for item in _str:
                await message.channel.send(item)
        elif message.content.title() in _night_list:
            await message.channel.send(_night_list_a[random(0,len(_night_list_a)-1)])
        elif message.content.title() in _rnm:
            await message.channel.send(y.anec())
        #Ниже ошибка которая возникает при отправке пустого сообщения
        elif message.content.title()[0] == 'R':   #я понимаю что тут не надо создавать методы, но это временное решение, до переноса все в 1 класс
            try:
                _randomQst = message.content.title().split(' ')
                _randomFst = int(_randomQst[1])
                _randomScd = int(_randomQst[2]) #сделать 3й необязательный элемент который делает несколько итераций
                _randomAns = random(_randomFst,_randomScd)
            except:
                _randomAns = 'Пример запроса "r 0 100"'
            await message.channel.send(_randomAns)
        elif message.content.title()[0:4] == 'Flip': #это тоже перенести надо
            _Flip = random(0,1)
            if _Flip == 0:
                _FlipAnswer = 'ОРЁЛ'
            else:
                _FlipAnswer = 'РЕШКА'
            await message.channel.send(_FlipAnswer)
        elif message.content.title() == "End":
            await client.logout()


        if random(0,100) <= 50 or message.author.id == 211550782468784128:         #То что человек выполняет функцию не означает, что его не надо обозвать
            if message.author.id in _hate_list:
                await message.channel.send(_hate_list_a[random(0,len(_hate_list_a)-1)])
        print(message.author.id, message.content)


x = zxc_pars()
y = anec_pars()

client = MyClient()
client.run(ds_token)
