"""Lab 05: Leap Year."""


def is_leap_year(year: int) -> bool:
    if year < 0 or type(year) != int:
        raise ValueError("Bitte gültige Zahl eingeben")
    if year % 4 == 0 or year % 400 == 0:
        if year % 100 == 0:
            return False
        else:
            return True
    else:
        return False
    


if __name__ == "__main__":
    print("2000:", is_leap_year(2000))
    print("1900:", is_leap_year(1900))
    print("2024:", is_leap_year(2024))
