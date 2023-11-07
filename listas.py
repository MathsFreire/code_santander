# criando listas
lista = [1, 2, 3, 4] #lista criada já inserido os valores
lista = [] #lista vazia
lista = [ 2 , 'm', 3.1] # lista pode conter qualquer tipo de dado
lista_de_listas = [ 1 , 2 ,[1,2,4]] # listas podem ser criadas dentro de uma lista

# como indexar lista
lista = [ 10, 25 , 22]
print(lista[0]) # dentro do [] colocar a posição de dentro da lista, obs: começa sempre o 0
print(lista[-1]) # você pode acessar a lista de tras para frente usando o negativo

lista = [ 10, 25 , 22, 40, 50 , 70, 8]
print(lista[0:3]) # no caso está acessando a lista do 0 até o 2 obs: menor do que 3
print(lista[0:6:2]) # pulando de dois em dois com o ultimo :2


for elemento in lista:
    print(elemento)

print('comprimento da lista', len(lista)) # len() é utilizado para saber o comprimento da lista

for i in range(len(lista)): # usando o len() dentro do range para jogar como valor de range o tamanho total da lista
    print(lista[i]) #vai listar todos os valores da lista 

#append

lista.append(3) # inclui o valor do parametro no ultimo indice da lista

lista.insert(2, 5) # inclui no indice 2 o valor 5

lista2 = [1, 2 , 3]

lista.extend(lista2) # inclui uma lista dentro de outra lista ao final

lista.pop() # tira um elemento da lista, no caso em vazio o ultimoda lista

lista.pop(1) # tira valor do indice expecifico ao colocar dentro do parametro.

lista.remove(3) # remove elemento 3 dentro da lista(valor 3) vai sempre remover o primeiro se tiver mais de um na lista

lista.count(2)

print('indice do elemento', lista.index(5))

lista.sort() # ordena a lista de forma crescente

lista.sort(reverse=true) # ordena a lista de forma decrescente




print(len(lista)) # imprime o tamanho da lista

print(sum(lista)) # faz a soma dos elementos da lista

print(min(lista)) # mostra o menor valor dentre os elementos

print(max(lista)) # mostra o maior valor dentre os elementos

