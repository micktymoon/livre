#/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import render_template
from run import app
from models import db, Livre, init_db

@app.route('/')
def racine():
    return render_template('accueil.html', title='Accueil')
db.create_all()
init_db()
db.create_all()
@app.route('/livre')
def livre():
    livres = Livre.query.order_by(Livre.date)
    return render_template('index.html', title='Livres', livres=livres)

if __name__ == '__main__':
    app.run()