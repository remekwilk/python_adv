from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('__main__', '.'))
template = env.get_template('zadanie0701_template_moje.html')

produkty = [
    {'nazwa': 'Karkówka bez kości', 'cena': 8.99, 'jednostka': 'kg', 'promocja': True},
    {'nazwa': 'Twaróg sernikowy 1kg', 'cena': 5.99, 'jednostka': 'op', 'promocja': True},
    {'nazwa': 'Mleko Świeże 2%', 'cena': 1.99, 'jednostka': 'op', 'promocja': True},
    {'nazwa': 'Herbata torebki 200g', 'cena': 9.99, 'jednostka': 'op', 'promocja': False},
    {'nazwa': 'Czekolada', 'cena': 2.49, 'jednostka': 'op', 'promocja': True},
    {'nazwa': 'Gruszki', 'cena': 2.99, 'jednostka': 'kg', 'promocja': True},
    {'nazwa': 'Cytryny', 'cena': 7.99, 'jednostka': 'kg', 'promocja': False},
]
context = {'abc': produkty}
wyrenderowany_html = template.render(context)  # tutaj wyrenderuj html'a

with open('zadanie0701.html', mode='w', encoding='windows-1250') as f:
    f.write(wyrenderowany_html)
