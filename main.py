import discord
from random import randint as random


from zxc_pars import zxc_pars


from KEYS import ds_token,_list_calls,_list_hate_words,_list_for_hate


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {}!'.format(self.user))


    async def on_message(self, message):
        if message.content in _list_calls:
            _str = x.zxc().split('\n')
            print(_str)
            for item in _str:
                await message.channel.send(item)
        if random(0,100) <= 100:
            if message.author.id in _list_for_hate:
                await message.channel.send(_list_hate_words[random(0,len(_list_hate_words)-1)])

        print(message.author.id, message.content)


x = zxc_pars()


client = MyClient()
client.run(ds_token)
