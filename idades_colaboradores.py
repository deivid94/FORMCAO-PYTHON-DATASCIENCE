idades_colaboradores = {

'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]

 }

total_idade = 0

for setor, idades in idades_colaboradores.items():
    media_de_idade = sum(idades) / len(idades)
print (f'O {setor} com a maior média é: {media_de_idade}')

total_idade += sum(idades)

media_total = total_idade / (len(idades) * len(idades_colaboradores))
print(f' a media total de idade é : {media_total}')