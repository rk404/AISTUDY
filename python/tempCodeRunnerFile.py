num = int(input('Podaj liczbę: '))
x = 0
for i in range(1, num+1):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
        x += 1
    elif i % 5 == 0:
        print('Buzz')
        x += 1
    elif i % 3 == 0:
        print('Fizz')
        x += 1
    else:
        print(i)
print('Liczba wystąpień ', x)