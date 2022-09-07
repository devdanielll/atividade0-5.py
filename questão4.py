vetor = []
par = []
impar = []

for numero in range(20):
    vetor.append(int(input("Digite um numero: ")))

for numero in range(0, 20):
    if vetor[numero] % 2 == 0:
        par.append(vetor[numero])
    else:
        impar.append(vetor[numero])

print("Vetor com 20 elementos: " + str(vetor))
print("Vetor com elementos pares: " + str(par))
print("Vetor com elementos impares: " + str(impar))