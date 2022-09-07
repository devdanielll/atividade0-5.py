vetor = []
soma=0

for i in range(5):
    vetor.append(int(input("Digite um número: ")))


soma = sum(vetor)
mult = (vetor[0]*vetor[1]*vetor[2]*vetor[3]*vetor[4])

print(vetor)
print(f'A soma dos valores é: {soma}')
print(f'A multiplicação dos vetores é: {mult}')
