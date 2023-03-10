#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint
import sys

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


def tarkistus(heitto):
    # Kehittyneempi tapa tarkistaa parit ja 3-luku
    # pistelista

    # lasketaan 1:t, 2:t, 3:t, 4:t, 5:t ja 6:t listaan.
    y = [
        heitto.count(1),
        heitto.count(2),
        heitto.count(3),
        heitto.count(4),
        heitto.count(5),
        heitto.count(6),
    ]
    score = []
    print("\n\t\t [1, 2, 3, 4, 5, 6]")
    print("numerot:\t", y)

    def t2(y):
        selite = []
        # z = y
        # z.sort()
        if y.count(2) > 0:
            selite.append("pari")
            if (y.count(2) == 2) or (y.count(3)):
                selite.append("kaksi paria")

        if y.count(3):
            selite.append("Kolmiluku")
            if y.count(2) == 1:
                selite.append("mökki")
        if y.count(4):
            selite.append("Neliluku!")
        if y.count(5):
            selite.append("Yatzy!")
        else:
            if sorted(y) == [1, 2, 3, 4, 5]:
                selite.append("Pieni suora")
            elif sorted(y) == [2, 3, 4, 5, 6]:
                selite.append("Suuri suora")

        return selite

    def pari(y):  # pari tai kaksi paria
        z = y.count(2)
        if z > 0:
            if z == 1:
                return 1
            elif z == 2:
                return 2
        else:
            return 0

    def kolmiluku(y):  # kolmiluku tai mökki
        if y.count(3):
            if y.count(2):
                return 5
            else:
                return 3
        else:
            return 0

    def suorat(y):  # pieni tai iso suora
        z = y
        z.sort()
        if z == [1, 2, 3, 4, 5]:
            return 1
        if z == [2, 3, 4, 5, 6]:
            return 2
        else:
            return 0

    def neliluku(y):  # neliluku
        if y.count(4):
            return 1
        else:
            return 0

    def yatzy(y):  # YATZY
        if y.count(5):
            return 5
        else:
            return 0

    score.insert(0, pari(y))
    score.insert(1, kolmiluku(y))
    score.insert(2, neliluku(y))
    score.insert(3, yatzy(y))
    score.insert(4, suorat(y))

    print(t2(y))

    return score


def uusiHeitto(nopat: list) -> list:
    for i in range(0, 5):
        nopat[i] = randint(1, 6)
    return nopat


def heitaValitut(nopat: list, valitut: list) -> list:
    """Arpoo uudestaan valitut -muuttujassa saadut nopat"""
    for noppa in valitut:
        print("Noppa", noppa, ".. ", end="")
        nopat[int(noppa)] = randint(1, 6)
        print(nopat[int(noppa)])
    return nopat


def laskeTulos(nopat: list) -> int:
	# laskee noppien summan
	t = 0
	for noppa in nopat:
		t += nopat[int(noppa)]
	return t


def merkitseNopat(nopat: list, merkatut) -> list:
	print("Merkataan nopat", merkatut)
	print("Mihin merkitään?")
	tarkistus(nopat)
	return nopat


def main():
	nopat = [0, 0, 0, 0, 0]
	while 1:
		h = 1
		print("\033c")
		heitto = uusiHeitto(nopat)
		print(f"{h}. heittosi\t", (heitto))
		sc = tarkistus(heitto)
		print("tulos:\t\t", (sc))

		while h < 3:
			valitut = list(input("\nValitse uudelleenheitettävät nopat: "))
			h += 1
			uusiheitto = heitaValitut(heitto, valitut)
			print(f"{h}. heittosi\t", (uusiheitto))
			sc = tarkistus(uusiheitto)
			print("Tulokset:\t", sc)

		valitut = list(input("\nValitse merkattavat nopat."))
		heitto = merkitseNopat(uusiheitto, valitut)

		jatka = input("\n\nJatketaanko vielä? Q: quit ")
		if jatka == "": continue
		if jatka[0] in ["q", "Q"]:
			print("Exit.")
			sys.exit()
		else:
			continue


if __name__ == "__main__":
    main()
