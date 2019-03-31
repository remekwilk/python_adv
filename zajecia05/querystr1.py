from flask import Flask, request

app = Flask(__name__)

lista = ['Ambroży', 'Barnaba', 'Celina', 'Danuta', 'Eligiusz', 'Felicja']


@app.route('/osoby')
def odczyt_z_listy():
    # spróbuj http://127.0.0.1:5000/osoby?id=2

    indeks = request.args.get('id')
    if indeks:
        try:
            osoba = lista[int(indeks)]
            return f'Osoba pod indeksem {indeks} to {osoba}'
        except IndexError:
            return f'Nie ma indeksu {indeks} w liście'
        except ValueError:
            return f'{indeks} nie jest poprawnym indeksem'
    return f'Osoby na liście: {lista}'


if __name__ == "__main__":
    app.run()
