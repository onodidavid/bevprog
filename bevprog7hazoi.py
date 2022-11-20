import string
mgh = "a", "á", "e", "é", "i", "í", "o", "ó", "ö", "ő", "u", "ú", "ü", "ű", "A", "Á", "E", "É", "I", "Í", "O","Ó", "Ö", "Ő","U",
"Ú", "Ü", "Ű" "\n"

with open("hazi.txt", "r", encoding='UTF-8') as f:
    with open("kimenet.txt", "w", encoding='UTF-8') as file:
        sor = f.readline()
        n = 1
        sor = sor.translate(str.maketrans('', '', string.punctuation))

        for i in sor:
            if i in mgh:
                sor = sor.replace(i, "")


        while sor:
            sor = f.readline()
            if sor.isspace():
                continue
            n += 1
            sor = sor.translate(str.maketrans('', '', string.punctuation))
            for i in sor:
                if i in mgh:
                    sor = sor.replace(i, "")
            if n % 3 == 0:
                file.write(sor + "\n")