def main(a, b, c):
    if a + b >= c and b + c >= a and a + c >= b:
        print(f"A {a}, {b}, {c} háromszög szerkeszthető")
    else:
        print(f"The {a}, {b}, {c}, oldalú háromszög NEM szerkeszthető ")

if __name__ == "__main__":
    print("Adja meg a háromszög oldalát cm-ben: ")
    A = float(input("a oldal (cm): "))
    B = float(input("b oldal (cm): "))
    C = float(input("a oldal (cm): "))
    main(A ,B, C)
