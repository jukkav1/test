#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint
from tarkistin import tarkistus

max_pisteet = {
    "pelaaja": "",
    "ykköset": 5,
    "kakkoset": 10,
    "kolmoset": 15,
    "neloset": 20,
    "vitoset": 25,
    "kutoset": 30,
    "summa": 105,
    "hyvitys": 50,
    "1 pari": 12,
    "2 paria": 22,
    "kolmiluku": 18,
    "neliluku": 24,
    "YATZY!": 50,
    "pieni suora": 15,
    "suuri suora": 20,
    "mökki": 28,
    "sattuma": 30,
    "yhteensä": 374,
}

poytakirja = {
    "pelaaja": "",
    "ykköset": -1,
    "kakkoset": -1,
    "kolmoset": -1,
    "neloset": -1,
    "vitoset": -1,
    "kutoset": -1,
    "summa": -1,
    "hyvitys": -1,
    "1 pari": -1,
    "2 paria": -1,
    "kolmiluku": -1,
    "neliluku": -1,
    "YATZY!": -1,
    "pieni suora": -1,
    "suuri suora": -1,
    "mökki": -1,
    "sattuma": -1,
    "yhteensä": -1,
}


def heitaValitut(nopat: list, valitut: list) -> list:
    """Arpoo uudestaan valitut nopat"""
    for noppa in valitut:
        nopat[int(noppa)] = randint(1, 6)
        print(f"{nopat[int(noppa)]}, ", end=" ")
    return nopat


def laskeTulos(nopat: list) -> int:
    """Laskee noppien summan"""
    tulos = 0
    for _ in nopat:
        tulos += nopat[int(_)]
    return tulos


def merkitseNopat(nopat: list, merkatut) -> list:
    """Merkitään 'merkatut' nopat tulostaulukkoon"""
    ### Tämä ei ole valmis ###
    print("Merkataan nopat", merkatut)
    print("Mihin merkitään?")
    tarkistus(nopat)
    return nopat


def main():
    """Pääohjelma"""
    nopat = [0, 0, 0, 0, 0]
    while 1:
        heittocounter = 1
        print("\033c")
        heitto = heitaValitut(nopat, [0, 1, 2, 3, 4])
        print(f"{heittocounter}. heittosi\t", (heitto))
        print("tulos:\t\t", tarkistus(heitto))

        while heittocounter < 3:
            valitut = list(input("\nValitse uudelleenheitettävät nopat: "))
            heittocounter += 1
            uusiheitto = heitaValitut(heitto, valitut)
            print(f"{heittocounter}. heittosi\t", (uusiheitto))
            print("Tulokset:\t", tarkistus(uusiheitto))

        valitut = list(input("\nValitse merkattavat nopat."))
        heitto = merkitseNopat(uusiheitto, valitut)

        jatka = input("\n\nJatketaanko vielä? Q: quit ")
        if (jatka != "") and (jatka[0] in ["q", "Q"]):
            break
        continue


if __name__ == "__main__":
    main()
