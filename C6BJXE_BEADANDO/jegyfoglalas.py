class JegyFoglalas:
    def __init__(self):
        self.foglalasok = []
        self.foglalasi_szam_counter = 1

    def foglalas(self, jarat):
        foglalasi_szam = f"F{self.foglalasi_szam_counter:03}"
        self.foglalasi_szam_counter += 1
        self.foglalasok.append((foglalasi_szam, jarat))
        print(f"Foglalás sikeres! Foglalási szám: {foglalasi_szam}, járat: {jarat.jarat_info()}")

    def foglalas_lemondasa(self, foglalasi_szam):
        for foglalas in self.foglalasok:
            if foglalas[0] == foglalasi_szam:
                self.foglalasok.remove(foglalas)
                print(f"Foglalás lemondva: {foglalasi_szam}")
                return
        print(f"Nincs ilyen foglalás: {foglalasi_szam}")

    def foglalasok_listazasa(self):
        if not self.foglalasok:
            print("Nincs egyetlen foglalás sem.")
        for foglalas in self.foglalasok:
            print(f"Foglalási szám: {foglalas[0]}, {foglalas[1].jarat_info()}")
