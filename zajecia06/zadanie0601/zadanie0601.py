from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['get', 'post'])
def wprowadz():
    return render_template('wprowadz.html')


@app.route('/wynik')
def wynik():
    try:
        l1 = int(request.args.get('liczba1'))
        l2 = int(request.args.get('liczba2'))
        wynik = l1 * l2

    except ValueError:
        return render_template('blad.html')
    return render_template('wynik.html', l1=l1, l2=l2, wynik=wynik)


if __name__ == '__main__':
    app.run(debug=True)
