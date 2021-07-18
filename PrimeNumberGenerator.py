"""Prime Number Generator"""

PrimeNumbers = [2]
Number = 2
Count = 1

print(f'{Count}: {Number}')

while True:
    is_primeNumber = True
    for primeNumber in PrimeNumbers:
        if Number % primeNumber == 0:
            is_primeNumber = False
            break
    if is_primeNumber:
        PrimeNumbers.append(Number)
        Count += 1
        print(f'{Count}: {Number}')
    Number += 1
