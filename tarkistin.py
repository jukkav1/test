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

    def lisaaSelite(y: list) -> list:
        """ottaa numeroita ja palauttaa listan mitä sarjoja numeroista saa"""
        selite = []

        if y.count(2) > 0:
            selite.append("pari")
            if (y.count(2) == 2) or (y.count(3)):
                selite.append("kaksi paria")

        # jos kolmiluku..
        if y.count(3):
            selite.append("kolmiluku")
            # jos lisäksi tasan yksi pari:
            if y.count(2) == 1:
                selite.append("mökki")

        if y.count(4):
            selite.append("neliluku")

        if y.count(5):
            selite.append("YATZY")

        else:  # pieni ja iso suora
            if y == [1, 1, 1, 1, 1, 0]:
                selite.append("pieni suora")
            elif y == [0, 1, 1, 1, 1, 1]:
                selite.append("suuri suora")
        return selite  # palauttaa selkeäkielisen selitteen

    def pari(y) -> int:
        """pari tai kaksi paria"""
        z = y.count(2)
        if z > 0:
            if z in [1, 2]:
                return z
        return 0

    def kolmiluku(y) -> int:
        """kolmiluku tai mökki"""
        if y.count(3):  # simple kolmiluku
            if y.count(2):  # 3-luku + pari = mökki
                return 5
            return 3
        return 0

    def suorat(y) -> int:
        """pieni tai iso suora"""
        if y == [1, 1, 1, 1, 1, 0]:
            # print("pieni suora")
            return 1
        if y == [0, 1, 1, 1, 1, 1]:
            # print("iso suora")
            return 2
        return 0

    def neliluku(y) -> int:
        """neliluku"""
        if y.count(4):
            return 1
        return 0

    def yatzy(y) -> int:
        """YATZY"""
        if y.count(5):
            return 5
        return 0

    score.insert(0, pari(y))
    score.insert(1, kolmiluku(y))
    score.insert(2, neliluku(y))
    score.insert(3, yatzy(y))
    score.insert(4, suorat(y))

    print(lisaaSelite(y))

    return score
