gabarito_aluno = [input("Digite a  letra das suas respostas")]
gabarito_prova =  []
repostas_validas = ['A','B','C','D']
i = 1
while i < 10:
    i+=1
    gabarito_aluno = [input("Digite a  letra das suas respostas: ")]
    if gabarito_aluno != repostas_validas:
        print("O cartao respostas é até a letra D")
    else:
         