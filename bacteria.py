"""
Para um estudo envolvendo o nível de multiplicação de bactérias em uma colônia,
foi coletado o número de bactérias multiplicadas por dia e pode ser observado
a seguir: [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9].
Tendo esses valores, faça um código que gere uma lista contendo o percentual de crescimento
de bactérias por dia, comparando o número de bactérias
em cada dia com o número de bactérias do dia anterior.
Dica: para calcular o percentual de crescimento usamos a
seguinte equação: 100 * (amostra_atual - amostra_passada) / (amostra_passada).
"""

bacterias = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]
percentual_de_crescimento = []
for i in range(len (bacterias)):
    resultado = 100 * (bacterias[i] - bacterias[i - 1])/ (bacterias[i - 1])
    percentual_de_crescimento.append(int(resultado))
print(percentual_de_crescimento)
