votos_marca_design_infantil = {

'Design 1' :1334,
'Design 2': 982,
'Design 3': 1751, 
'Design 4': 210, 
'Design 5': 1811,
'Design 6': 2000  
}
voto_de_referencia = votos_marca_design_infantil.get("Design 1")

design_mais_votado = 0

for voto in votos_marca_design_infantil:
    
    if votos_marca_design_infantil[voto] > voto_de_referencia:
        design_mais_votado = votos_marca_design_infantil[voto]
print (f'O Design mais votado foi:  {design_mais_votado}')        