def quickPower(a, n):
    if n == 0:
        return 1
    if n == 1:
        return a

    if n % 2 == 0:
        return quickPower(a, n / 2) * quickPower(a, n / 2)
    else:
        return quickPower(a, n - 1) * a
