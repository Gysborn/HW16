from flask import Flask
from create_db import db  # Вся магия происходит тут
from flask import current_app as app, request, jsonify, redirect
from model import User, Order, Offer

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

app.app_context().push()

db.create_all()

@app.route('/')
def index():
    return 'Hello world'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
