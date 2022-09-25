def text(input):
    letters = {}
    for i in input:
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1

    print("Betűk gyakorisága: ", {str(letters)})

    reverse_text = input [::-1]
    print("Fordítva: ", {reverse_text})

    word_split = input.split(' ')
    print("Listába rendezve szavanként: ", word_split)

if __name__ == '__main__':
        user = input("Adjon meg egy mondatot: \n")
        text(user)


