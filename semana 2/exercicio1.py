'''
Exercício 1:
 Crie um programa que lê dois número
 inteiros do teclado e após imprime 
 o maior números dentre eles.
'''



num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

if num1 > num2:
    print("O maior número é:", num1)
else:
    print("O maior número é:", num2)
