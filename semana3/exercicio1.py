'''
Exercício 1 - Semana 3
Crie um programa que imprime todos 
os números pares no intervalo de 
0 a 20.
'''
for numero in range(0,21):
    resto = numero%2
    if resto == 0:
        print(numero)


