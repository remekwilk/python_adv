from flask import Flask, request

app = Flask(__name__)


@app.route('/odczyt')
def odczyt_z_pliku():
    try:
        with open('baza.txt', mode='r') as plik:
            d = plik.read()
        return f'Dane w bazie to: \n{d}'
    except FileNotFoundError:
        return f'Najpierw zapisz coś do bazy!'


@app.route('/zapis')
def zapis_do_pliku():
    dane = request.args.get('dane')
    with open('baza.txt', mode='a') as plik:

        if dane:
            plik.write(dane + '\n')
            return f'Zapisano do bazy dane: \n{dane}'
        else:
            return f'Brak danych do zapisu!'


if __name__ == "__main__":
    app.run()
