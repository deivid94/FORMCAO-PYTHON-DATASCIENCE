

dia = int(input('digite o dia: '))
mes = int(input('digite o mes: '))
ano = int(input('digite o ano: '))

meses_31_dias = [1,3,5,7,8,10,12]
meses_30_dias = [4,6,9,11]
bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

data_valida = True

if mes < 1 or mes > 12:
    data_valida = False
elif mes in meses_31_dias and (dia < 1 or dia >31):
    data_valida = False    
elif mes in  meses_30_dias and (dia < 1 or dia > 31):
    data_valida = False
elif (mes == 2):
    if bissexto and (dia <1 or dia > 31):
        data_valida = False
    elif not bissexto and (dia < 1 or dia > 28):
        data_valida = False
if (data_valida):
    print ('Data Valida')
else:
    print('Data Invalida')