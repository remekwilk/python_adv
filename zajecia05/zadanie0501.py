from flask import Flask

app = Flask(__name__)


@app.route('/odczyt')
def odczyt_z_pliku():
    try:
        with open('baza.txt', mode='r') as plik:
            d = plik.read()
        return f'Dane w bazie to: {d}'
    except FileNotFoundError:
        return f'Najpierw zapisz coś do bazy!'


@app.route('/zapis/<dane>')
def zapis_do_pliku(dane):
    with open('baza.txt', mode='a') as plik:
        plik.write(dane + 'n')

    return f'Zapisano do bazy dane: {dane}'


if __name__ == "__main__":
    app.run()
