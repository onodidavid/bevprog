def cm_to_inch_converter(float, unit):
    if unit == "cm":
        print(f"{float}cm = {float / 2.54}inch")
    elif unit == "inch":
        print(f"{float}inch = {float * 2.54}cm")
    else:
        print("Not Correct Unit!")


if __name__ == '__main__':
    number = float(input("Adjon meg egy számot: \n"))
    units = (input("Adjon meg egy mértékegységet (cm/inch): \n"))
    cm_to_inch_converter(number,units)