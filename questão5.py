listaNotas = []
notasAluno = []

for i in range(2):
 	media = 0
 	notasAluno = []
 	print ('Aluno: ' + str(i + 1))

 	for j in range(4):
 		notasAluno.append(float(input('Digite a nota: ' + '\n')))
 		media += notasAluno[j]
 		print (media)

 	media = media/4
 	listaNotas.append(media)

print (listaNotas)