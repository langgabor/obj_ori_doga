from abc import ABC, abstractmethod

class Jarat(ABC):
    def __init__(self, jaratszam, celallomas, jegyar):
        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar

    @abstractmethod
    def jarat_info(self):
        pass

class BelfoldiJarat(Jarat):
    def __init__(self, jaratszam, celallomas, jegyar):
        super().__init__(jaratszam, celallomas, jegyar)

    def jarat_info(self):
        return f"Belföldi járat: {self.jaratszam}, célállomás: {self.celallomas}, jegyár: {self.jegyar}"

class NemzetkoziJarat(Jarat):
    def __init__(self, jaratszam, celallomas, jegyar):
        super().__init__(jaratszam, celallomas, jegyar)

    def jarat_info(self):
        return f"Nemzetközi járat: {self.jaratszam}, célállomás: {self.celallomas}, jegyár: {self.jegyar}"
