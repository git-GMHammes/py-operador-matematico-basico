"""
Caululadora Python
isdigit - Informa se foi digitado um numero ou um caracter
"""
print(f'Operadores matematico Python')
print()
valor1 = input('Digite o primeiro número: ')
operador1 = input('Digite o operador: ')
valor2 = input('Digite o segundo número: ')
if valor1.isdigit() and valor2.isdigit():
    valor1 = float(valor1)
    valor2 = float(valor2)
    resultado1 = float(0.0)
    if operador1 == '+':
        resultado1 = valor1+valor2
    elif operador1 == "-":
        resultado1 = valor1-valor2
    elif operador1 == "/":
        resultado1 = valor1/valor2
    elif operador1 == "*":
        resultado1 = valor1*valor2
    print()
    print(f'Resultado: {resultado1}')
else:
    print(f'Valor digitado está incorreto!!')
print()
print(f'Calculadora Python apenas para soma')
print()
valor1 = input('Digite o primeiro número: ')
valor2 = input('Digite o segundo número: ')
try:
    valor1 = float(valor1)
    valor2 = float(valor2)
    print(f'Resultado é {valor1+valor2}')
except:
    print()
    print(f'Você não digitou números válidos!!!')
