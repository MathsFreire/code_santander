#Listas 
Notas = [7.9, 9.7, 8.2]

# Criando Listas
Lista = []
Lista = list()
Lista = [26, 'Olly', 3.14159, False]
Listas_de_Listas = [10, [1,2,3]]

#Indexação e Slices (Fatiamento)

lista = [10, 'Olly',3.1415, True]

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
# print (lista[4])

#Slices

lista = [10,50,30,40,25,5]

print(lista[0:3])
print(lista[3:6])

#> Interações com FOR

# 1. Utilizando os próprios elementos da lista

for elemento in lista:
    print (elemento)

# 2. Utilizando os indices 

print('comprimento da lista:', len(lista))

for i in range (len(lista)):
    print(lista [i])

# > Métodos de listas

lista = [1, 3, 12, 8, 2]

# append

print('Antes do apprend:', lista)

lista.append (3)

print('Depois do append',lista)

# Insert

lista.insert(2, 10)
print ('depois do insert:', lista )

# Extend

Lista2 = [1, 2, 3]
lista.extend(Lista2)
print('Depois do extend:', lista)

# Pop

lista.pop(0)
print('lista após o pop:', lista)

# Remove

lista.remove(3)

print('Depois do remove', lista)

# Count 

print ('Quantidade de 2 na lista:', lista.count(2))

#Index 

print ('Indice do elemento 12:', lista.index(12))

#Sort

lista.sort() #Ordena a lista de forma crescente
lista.sort(reverse=True) #Ordena de forma decrescente

#Funções para listas

# Len
print (len(lista))
# Sum
print(sum(lista))
# Max
print('Maior elemento da lista', max(lista))
#Min
print ('Menor elemento da lista', min(lista))
