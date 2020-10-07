primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
n = int(input("Digite o numero que voce deseja procurar: "))
min = 0
max = int(len(primes)) - 1 
while True:
    if min > max:
        print("O numero", n, "nao esta na lista.")
        break
    guess = int((min + max) / 2)
    if primes[guess] < n:
        min = guess + 1
    elif primes[guess] > n:
        max = guess - 1
    elif primes[guess] == n:
        print('O numero ', n, 'esta no indice',guess)
        break
