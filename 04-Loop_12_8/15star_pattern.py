i = 1

while i <= 5:
    if i == 1 or i == 3:
        n = 1
    elif i == 2 or i == 4:
        n = 2
    else:
        n = 3

    j = 1
    while j <= n:
        print("*", end="")
        j = j + 1

    print()
    i = i + 1