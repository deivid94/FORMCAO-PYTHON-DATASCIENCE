
## Com os mesmo dados da questao anterior defina quantas compras forem realizada
##acima de 3000

lista = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]

acima_de_tres_mil = []
for items in lista:
    if (items > 3000):
        acima_de_tres_mil = items


quantidade = len(repr(acima_de_tres_mil))
print (quantidade)

