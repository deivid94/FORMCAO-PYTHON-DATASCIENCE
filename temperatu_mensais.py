temperatura_mensais = []
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

for index in range(0,13):
    temperatura_mensais.append(float(input(f'Digite a média de temperatura do mes {meses[index]}: ')))
print(temperatura_mensais)    



media_anual = sum(temperatura_mensais) / len(temperatura_mensais)

for index in range (0,12):
    if temperatura_mensais[index] > media_anual:
        print(meses[index])