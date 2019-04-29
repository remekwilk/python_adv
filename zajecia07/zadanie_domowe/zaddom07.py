# Remigiusz Wilk
from flask import Flask, render_template
import json

app = Flask(__name__)


def pobierz_dane():
    with open('ludzie.json') as f:
        return json.load(f)


@app.route('/')
def index():
    lista_osob = pobierz_dane()
    return render_template('lista.html', lista_osob=lista_osob)


@app.route('/osoba/<int:indeks>')
def osoba(indeks):
    lista_osob = pobierz_dane()
    # print(lista_osob)
    # print(lista_osob[0]['imie'])
    context = {}
    for osoba in lista_osob:
        if indeks == osoba['id']:
            print(osoba)
            context['osoba'] = osoba
            break

        if indeks != osoba['id']:
            context['error'] = f'Brak osob o id: {indeks}.'

    return render_template('osoba.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
