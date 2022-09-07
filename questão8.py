vetorA = []
soma = 0

for numero in range(10):
    vetorA.append(int(input("Digite um numero: ")))
    soma = soma + (vetorA[len(vetorA)-1]**2)

print("A soma dos quadrados dos elementos do vetor A " + str(soma))