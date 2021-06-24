import discord
from random import randint as random


from zxc_pars import zxc_pars


from KEYS import ds_token,_list_calls,_list_hate_words,_list_for_hate,_night_list,_night_list_a


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {}!'.format(self.user))


    async def on_message(self, message):
        if message.content.title() in _list_calls:
            _str = x.zxc().split('\n')
            print(_str)
            for item in _str:
                await message.channel.send(item)
        elif message.content.title() in _night_list:
            await message.channel.send(_night_list_a[random(0,len(_night_list_a))])
        if random(0,100) <= 30:         #То что человек выполняет функцию не означает, что его не надо обозвать
            if message.author.id in _list_for_hate:
                await message.channel.send(_list_hate_words[random(0,len(_list_hate_words)-1)])
        print(message.author.id, message.content)


x = zxc_pars()


client = MyClient()
client.run(ds_token)
