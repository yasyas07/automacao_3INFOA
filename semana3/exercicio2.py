'''
Exercício 2 - Semana 3
Crie um programa que imprime usando
for a figura abaixo:
*
**
***
****
*****
******
termina com 10 * na última linha
'''


num_asteri = 1
linha = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
for _ in linha:
    if num_asteri <= 10:
        print('*' * num_asteri)
    else:
        print('*' * 10)
   
