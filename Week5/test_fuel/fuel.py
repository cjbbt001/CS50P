def main():
    while True:
        try:
            print(gauge(convert(input("Fraction: "))))
            break
        except (ValueError, ZeroDivisionError):
            continue


def convert(fraction):
    x, y = map(int, fraction.split("/"))
    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError
    return round(x / y * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
