"""def saudacao(nome):
    print(f'Bom dia {nome}')
    print('tudo bem?')

saudacao('matheus')

def saudacao(nome, curso='Python'):
    print(f'Bom dia {nome}, tudo bem?')
    print(f'Como vai seu curso de {curso}')

saudacao('Matheus')

def soma(numero1, numero2):
    return numero1+numero2

resultado=soma(5 , 6)
print(resultado)"""

def calculadora(num1, operacao, num2):
    if operacao == '*':
        return num1 * num2
    elif operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '/':
        return num1 / num2
    elif operacao == '**':
        return num1 ** num2
    elif operacao == '1/2':
        return num1 **(1/2)
    
termina=False
while termina != True:
    resultado = calculadora(int(input('numero 1: ')), input('operacao: '), int(input('numero 2: ')))
    print(resultado)
    consulta= input('Deseja deseja calcular novamente?(S/N)')
    if consulta == 'N':
        termina=True
    else:
        termina=False

print(resultado)
    