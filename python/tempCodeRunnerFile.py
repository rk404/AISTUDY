def potega(x, n):
    if n == 0:
        return 1
    else:
        return x * potega(x, n - 1)
print(potega(4, 2))  # 8
