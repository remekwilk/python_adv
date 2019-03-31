# Remigiusz Wilk

def unikalne_adresy_ip():
    plik = open('apache_logs', mode='r')
    ip = [adres.split()[0] for adres in plik.readlines()]
    nowy_ip = list(set(ip))

    # ip = []
    # for adres in plik.readlines():
    #     adres = adres.split()
    #     adres = adres[0]
    #     ip.append(adres)
    # nowy_ip = list(set(ip))

    return nowy_ip


if __name__ == '__main__':
    print(unikalne_adresy_ip())
