idade = int(input('digite a idade: '))

if idade>=18:
    print('maior de idade')
else:
    print('Menor de idade')

# uso do elif(else if)

nota1= int(input('digite a nota 1') )
nota2= int(input('digite a nota 2') )
nota3= int(input('digite a nota 3') )

media= (nota1+nota2+nota3)/3

print (media)


numero_escolhido=int(input('digite um numero'))
numero_sorteado=10

while numero_escolhido != numero_sorteado:
    print('você errou')
    
    numero_escolhido=int(input('digite um numero'))
print ('você acertou')
