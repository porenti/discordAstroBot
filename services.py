#я обязательно закончу этот файл
from random import randint as random


from googletrans import Translator
translator = Translator()

class funcionality():
    def engspeach(self,text):
        _new_text = ""
        _cache_text = text.split(' ')
        for item in _cache_text:
            if random(0,5) >= 3:
                _new_text += str(translator.translate(item).text)
            else:
                _new_text += str(item)
            _new_text += " "

        return  _new_text
