# Remigiusz Wilk
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('input.html')

@app.route('/odczyt')
def odczyt_z_pliku():
    argumenty = request.args
    for klucz, wartosc in argumenty.items():
        print(f'{klucz}: {wartosc}')
    return f'argumenty: {argumenty}'


@app.route('/zapis')
def zapis_do_pliku():
    marka = request.args.get('Marka')
    model = request.args.get('Model')
    with open('baza.txt', mode='a') as plik:

        if marka and model:
            dane = model + marka
            print(f'{marka}: {model}')
            plik.write(dane)
            return f'Dane samochodu: {dane}'
        else:
            return f'Brak danych do zapisu!'



if __name__ == "__main__":
    app.run()
