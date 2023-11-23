gabarito = ['D', 'A', 'C', 'B', 'A', 'D', 'C', 'C', 'A', 'B']
respotas = []
nota = 0

for index in range (0,10):
    respotas.append(input(f' Insira A respostas da questao {index + 1}: ').upper())

for index in range(0,10):
    if(respotas[index] == gabarito[index]):
        nota += 1
print(f'Nota final: {nota}')        