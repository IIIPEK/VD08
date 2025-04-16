from flask import Flask

from app.utils import get_message

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

from app import routes