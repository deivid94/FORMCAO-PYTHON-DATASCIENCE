dados_venda = {
    'Produto A': 300,
    'Produto B': 80,
    'Produto C': 60,
    'Produto D': 200,
    'Produto E': 250,
    'Produto F': 30,
}

total_vendas = 0
produto_mais_vendido = ''
unidades_produtos_mais_vendido = 0

for produtos in dados_venda:
    total_vendas += dados_venda[produtos]

if dados_venda[produtos] > unidades_produtos_mais_vendido:
    unidades_produtos_mais_vendido = dados_venda[produtos]
    produto_mais_vendido = produtos

print (f'Total de vendaas é {total_vendas}')
print (f'{produto_mais_vendido} é o mais vendido')    