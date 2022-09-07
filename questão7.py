idades = []
alturas = []

for i in range(1,6):
    print('%dº Pessoa' %i)
    idade = int(input('Digite a idade: '))
    altura = float(input('Digite a altura: '))
    idades.append(idade)
    alturas.append(altura)

print('Ordem lida')

print('Alturas')
print(alturas)

print("\n")

print('Idades')
print(idades)

print('Ordem inversa')
print('Alturas')

alturas.reverse()
print(alturas)

print("\n")

print("Idades")

idades.reverse()
print(idades)

print("\n")