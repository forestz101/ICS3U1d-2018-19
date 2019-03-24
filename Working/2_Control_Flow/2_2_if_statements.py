def date(you, date):
    if you >= 8 or date > 8:
        return 2
    elif you <=2 or date <= 2:
        return 0
    else:
        return 1


date = date(2, 5)

if date == 2:
    print("Yes")
elif date == 1:
    print("Maybe")
else:
    print("No")
