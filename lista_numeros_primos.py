numero = int( input("digite um numero"))
lista = []
for num in range (2, numero + 1 ):
    primo = True
    for i in range (2, int(num ** 0.5)+1):
        if(num % i == 0):
            primo = False
            break
    if primo:
        lista.append(num)
print(lista)        