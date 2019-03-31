# Remigiusz Wilk
from flask import Flask, request, render_template
import json

app = Flask(__name__)


@app.route('/', methods=['get', 'post'])
def welcome():
    return render_template('welcome.html')


@app.route('/wprowadz')
def wprowadz():
    return render_template('wprowadz.html')


@app.route('/odczyt', methods=['get', 'post'])
def odczyt_z_pliku():
    try:
        with open('auta.json', mode='r') as plik:
            dane = json.load(plik)
            print(dane)
            return render_template('zapis.html', dane=dane)
    except FileNotFoundError:
        return render_template('blad.html' , error='Plik nie istnieje')

@app.route('/zapis', methods=['get', 'post'])
def zapis_do_pliku():

    marka = request.args.get('Marka')
    model = request.args.get('Model')
    if marka and model:
        lista_aut = []
        wpis = {'Marka': marka, 'Model': model}
        lista_aut.append(wpis)

        with open('auta.json', mode='a') as plik:
            json.dump(lista_aut, plik)
            return render_template('zapis.html', **wpis)
    else:
        return render_template('blad.html', error='Nie wprowadzono auta')


if __name__ == "__main__":
    app.run()
