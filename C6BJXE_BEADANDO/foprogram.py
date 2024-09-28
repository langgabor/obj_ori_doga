from legitarsasag import LegiTarsasag
from jarat import BelfoldiJarat, NemzetkoziJarat
from jegyfoglalas import JegyFoglalas

def alapadatok_betoltese():
    legi_tarsasag = LegiTarsasag("Példa Légi Társaság")
    legi_tarsasag.jarat_hozzaadasa(BelfoldiJarat("B001", "Budapest", 10000))
    legi_tarsasag.jarat_hozzaadasa(BelfoldiJarat("B002", "Debrecen", 8000))
    legi_tarsasag.jarat_hozzaadasa(NemzetkoziJarat("N001", "London", 50000))

    foglalasok = JegyFoglalas()
    foglalasok.foglalas(legi_tarsasag.jaratok[0])
    foglalasok.foglalas(legi_tarsasag.jaratok[0])
    foglalasok.foglalas(legi_tarsasag.jaratok[1])
    foglalasok.foglalas(legi_tarsasag.jaratok[1])
    foglalasok.foglalas(legi_tarsasag.jaratok[2])
    foglalasok.foglalas(legi_tarsasag.jaratok[2])

    return legi_tarsasag, foglalasok

def main():
    legi_tarsasag, foglalasok = alapadatok_betoltese()

    while True:
        print("\n1. Járatok listázása")
        print("2. Jegy foglalása")
        print("3. Foglalás lemondása")
        print("4. Foglalások listázása")
        print("5. Kilépés")

        valasztas = input("Válassz egy opciót: ")

        if valasztas == "1":
            legi_tarsasag.jaratok_listazasa()

        elif valasztas == "2":
            legi_tarsasag.jaratok_listazasa()
            jaratszam = input("Add meg a foglalni kívánt járat számát: ").strip().upper()
            for jarat in legi_tarsasag.jaratok:
                if jarat.jaratszam.upper() == jaratszam:
                    foglalasok.foglalas(jarat)
                    break
            else:
                print("Nincs ilyen járat.")

        elif valasztas == "3":
            foglalasi_szam = input("Add meg a lemondani kívánt foglalási számot: ").strip().upper()
            foglalasok.foglalas_lemondasa(foglalasi_szam)

        elif valasztas == "4":
            foglalasok.foglalasok_listazasa()

        elif valasztas == "5":
            print("Kilépés...")
            break

        else:
            print("Érvénytelen opció, próbáld újra.")

if __name__ == "__main__":
    main()
