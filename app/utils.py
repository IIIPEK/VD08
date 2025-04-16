from flask import request
import requests
from config import url
from translate import Translator

def get_message():
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        quote = data[0]['q']
        author = data[0]['a']
        translator = Translator(from_lang='en', to_lang='ru')
        try:
            quote_ru = translator.translate(quote)
            author_ru = translator.translate(author)
            print(quote_ru, author_ru)
        except:
            quote_ru, author_ru = None, None
        return quote, author, quote_ru, author_ru
    elif response.status_code == 429:
        return "Пожалуйста, подождите немного", 'Слишком частые запросы цитат'
    else:

        return "При запросе произошла ошибка",f'Error: {response.status_code}'
