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
    Developer1 = Developer("Ricsi", "SolArch", "Frontend")
    Developer2 = Developer("Angéla", "ZerTeng", "Tesztelő")
    Developer3 = Developer("Peti", "KefERP", "Backend")
    Developer4 = Developer("Éva", "KefERP", "Frontend")
    print()
    print(Developer4 == Developer2)
