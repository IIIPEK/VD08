from flask import render_template, redirect, url_for, request, flash
from app import app, get_message

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        quote, author, quote_ru, author_ru = get_message()
        return render_template('index.html', quote=quote, author=author, quote_ru=quote_ru, author_ru=author_ru)
    quote, author = get_message()
    return render_template('index.html', quote=quote, author=author)