# > FUNÇÕES

# 1. O que são funções e porque utilizá-las? 

# Funções que já utilizamos anteriormente... 
'''
print() # - Imprimi uma mensagem (int, float, str) no console (terminal,cmd)
input() # - Retorna um dado informado pelo usuário (entrada padrão) e pode receber uma string
len () # - Recebe uma lista e reforma o tamanho dessa lista
max () # - Retorna o maior valor de uma lista
'''
# 2. Crianção de funções

# Função inicial

def saudação():
    print('Seja bem-vindo(a)')
    print('Olá é um prazer você fazendo parte desse curso!')

saudação()

# Função com parâmetros

def saudação(nome, curso):
    print(f'Seja bem vindo(a), {nome}!')
    print (f'Olá, é um prazer ter você fazendo parte de{curso}!')


saudação('Gabriel', 'JAVASCRIPT')   

#Função com parâmetros Default


def saudação(nome, curso='Python'):
    print(f'Seja bem vindo(a), {nome}!')
    print (f'Olá, é um prazer ter você fazendo parte de {curso}!')


saudação('Gabriel',)   


#Função de retorno

def soma(num1, num2):
    return num1 + num2
resultado = soma (5, 8)
print('O resultado da soma é', resultado)

def calculadora (num1, num2, operacao='+'):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        return num1 / num2

resultado=calculadora(10,20,'-')
print (resultado)






