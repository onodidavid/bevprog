class Developer:
    def __init__(self, név, projekt, szerepkör):
        self._név = név
        self._projekt = projekt
        self._szerepkör = szerepkör
        print("-- Developer létrehozva. --")
        print(f"{self._név} a {self._projekt}-en dolgozik {self._szerepkör} szerepkörben")

        def __eq__(self, másik):
            if self._projekt == másik._projekt:
                print(f"{self._név} és {másik._név} dolgoznak egy projekten")

if __name__ == "__main__":
    elso = Developer("Ricsi", "SolArch", "Frontend")
    masodik = Developer("Angéla", "ZerTeng", "Tesztelő")
    harmadik = Developer("Peti", "KefERP", "Backend")
    negyedik = Developer("Éva", "KefERP", "Frontend")
    print()
    print(masodik == negyedik)
