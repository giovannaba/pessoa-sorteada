import random

qtdPessoas = int(input('Quantas pessoas irá participar desse sorteio: '))
lista = []
for c in range (1, qtdPessoas+1):
    nomes = str(input('Informe o nome da pessoa para incluí-lá no sorteio: '))
    lista.append(nomes)
escolhido = random.choice(lista)
print('A pessoa escolhida foi: {}'.format(escolhido))