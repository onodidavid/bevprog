def division():
    a = int(input("Enter 'a' value: "))
    b = int(input("Enter 'b' value: "))
    c = 0
    try:
        c = a/b
        print(c)
    except ZeroDivisionError:
        print("Division by zero not allowed")
    finally:
        print("Out of try except block")
def main():
    while True:
        division()
if __name__ == "__main__":
    main()