from leapyear import is_leapyear

if __name__ == "__main__":
    year = int(input("Jahr: "))
    if not is_leapyear(year):
        addition = "k"
    else:
        addition = ""

    print(f"Das Jahr {year} war {addition}ein Schaltjahr")

