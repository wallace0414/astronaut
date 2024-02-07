def beolvas():
    lista = []
    with open('astronauts.csv', 'r', encoding='utf-8') as forrasfajl:
        for sor in forrasfajl:
            adatok = sor.strip().split(',')
            szuletesnap = adatok[4]
            lista.append(szuletesnap)
    lista.pop(0)
    return lista


def felbont(lista):
    honapok_lista = []
    for elem in lista:
        felbontott = elem.split('/')
        honapok_lista.append(felbontott[0])
    return honapok_lista


def szamlal(honapok_lista):
    honapok_szama = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in honapok_lista:
        index = (int(i)) - 1
        honapok_szama[index] = int(honapok_szama[index]) + 1
    return honapok_szama

def elso_harom(honapok_szama, x):
    honapok = ['Január', 'Február', 'Március', 'Április', 'Május', 'Június', 'Július', 'Augusztus', 'Szeptember', 'Október', 'November', 'December']
    sorrend = sorted(zip(honapok_szama, honapok), reverse=True)
    print(f'1. {sorrend[0][1]}  {(sorrend[0][0] / x * 100):.1f}%')
    print(f'2. {sorrend[1][1]}  {(sorrend[1][0] / x * 100):.1f}%')
    print(f'3. {sorrend[2][1]}  {(sorrend[2][0] / x * 100):.1f}%')

def main():
    honapok_lista = felbont(beolvas())
    honapok_szama = szamlal(honapok_lista)
    elso_harom(honapok_szama, len(honapok_lista))

main()