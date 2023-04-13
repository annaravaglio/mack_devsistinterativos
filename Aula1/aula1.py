from tkinter import *
from tkinter import ttk
from math import *

# print("Hello world")

# x = 2

# print("x: ", x)

# x = input("Digite um numero: ")

# print("x: ", x)

# x = input("Digite um numero: ")
# y = input("Digite um numero: ")

# print("x: ", x)
# print("y: ", y)
# print("x+y=", x+y)

# x = int(input("Digite um numero: "))
# y = int(input("Digite um numero: "))

# print("x: ", x)
# print("y: ", y)
# print("x+y=", x+y)

# x = float(input("Digite um numero: "))
# y = float(input("Digite um numero: "))

# print("x: ", x)
# print("y: ", y)
# print("x+y=", x+y)

# artilheiro = input("Digite o artilheiro: ")
# gol = int(input("Digite a qtd de gols: "))

# print("No ultimo campeonato o artilheiro " + artilheiro + "marcou", gol, "gols.")
# print("No ultimo campeonato o artilheiro " + artilheiro + " marcou " + str(gol) + " gols.")
# print(f'No ultimo campeonato o artilheiro {artilheiro} marcou {gol} gols.')

# n1 = float(input("Digite a N1: "))
# n2 = float(input("Digite a N2: "))

# print(f'A média aritmética de {n1} e {n2} é {(n1+n2)/2}')

# raio = float(input("Digite o raio: "))
# area = 3.14 * (raio**2)

# print(f'A área de uma circunferência de raio {raio} é {area}')

# fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
# celsius = 5*((fahrenheit-32)/9)

# print(f'A temperatura em fahrenheit {fahrenheit} em celsius é {celsius:.2f}')

# o produto do dobro do primeiro com a metade do segundo
# a soma do triplo do primeiro com o terceiro
# o terceiro elevado ao cubo

# x1 = int(input("Entre com x1 int: "))
# x2 = int(input("Entre com x2 int: "))
# x3 = float(input("Entre com x3 float: "))

# print(f'O produto do dobro do primeiro com a metade do segundo é {(2*x1)*(x2/2)}')
# print(f'A soma do triplo do primeiro com o terceiro é {((3*x1)+x3):.2f}')
# print(f'A terceiro elevado ao cubo é {(x3**3):.2f}')

#  1. Um determinado prêmio de loteria saiu para um bolão de três amigos. 
# Uma lei garante que todo prêmio de loteria deva pagar um imposto de 7% para os cofres estaduais. 
# Do total descontado o imposto, os amigos irão dividir o prêmio da seguinte maneira:
# O primeiro ganhador recebera 46%;
# O segundo recebera 32%;
# O terceiro recebera o restante; 
# Faça um programa que leia o valor total do prêmio, calcule o desconto, o valor que cada um tem direito e imprima o total do prêmio, 
# o premio descontado o imposto e a quantia recebida por cada um dos ganhadores.

# premio_bruto = float(input("Entre com valor do premio: "))

# premio_liquido = premio_bruto * 0,93

# premio_1 = premio_liquido * 0.46
# premio_2 = premio_liquido * 0.32
# premio_3 = premio_liquido - premio_1 - premio_2

# print(f'O valor bruto do premio é {premio_bruto:.2f}')
# print(f'O valor liquido do premio é {premio_liquido:.2f}')
# print(f'O valor do premio do primeiro ganhador é {premio_1:.2f}')
# print(f'O valor do premio do segundo ganhador é {premio_2:.2f}')
# print(f'O valor do premio do terceiro ganhador é {premio_3:.2f}')

# 2. Faça um programa para calcular a quantidade de latas de tintas necessárias para pintar uma parede. 
# O programa deverá solicitar ao usuário, a altura (float) e o comprimento(float) da parede. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 3,6 litros, que custam R$ 107,00. 
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

# altura = float(input("Entre com a altura da parede: "))
# comprimento = float(input("Entre com o comprimento da parede: "))

# area = (altura*comprimento)

# calc_vol_tinta_litro = area/3

# vol_lata = 3.6
# custo_lata = 107.0

# # arredonda para cima para pegar somente latas inteiras
# qtd_latas = ceil(calc_vol_tinta_litro/vol_lata)

# custo_total = qtd_latas * custo_lata

# print(f'A área da parede é {area:.2f}')
# print(f'A quantidade de litros para pintá-la é {calc_vol_tinta_litro:.2f}')
# print(f'A quantidade de latas necessárias para pintar a parede é de {qtd_latas:.2f}')
# print(f'O valor total de gasto é de {custo_total:.2f}')

# 3. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

# n1 = float(input("Digite a N1: "))
# n2 = float(input("Digite a N2: "))
# media = (n1+n2)/2

# print(f'A média aritmética de {n1:.2f} e {n2:.2f} é {media:.2f}')

# if media >= 7 and media < 10:
#     print("Aprovado")
# elif media >= 10:
#     print("Aprovado com distinção")
# else:
#     print("Reprovado")

#Um mercado está vendendo frutas com a seguinte tabela de preços:
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. 
# Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

# kg_maca = float(input("Digite quantos kg de maçã: "))
# kg_morango = float(input("Digite quantos kg de morango: "))

# print(f'Kg Maça = {kg_maca:.2f}')
# print(f'Kg Morango = {kg_morango:.2f}')
# total_kg = kg_maca + kg_morango

# if kg_maca >= 5:
#     valor_maca = 1.5
#     valor_total_maca = kg_maca * valor_maca
# else:
#     valor_maca = 1.8
#     valor_total_maca = kg_maca * valor_maca

# if kg_morango >= 5:
#     valor_morango = 2.2
#     valor_total_morango = kg_maca * valor_morango
# else:
#     valor_morango = 2.5
#     valor_total_morango = kg_maca * valor_morango

# total_bruto = valor_total_maca + valor_total_morango

# print(f'Valor Maça = {valor_maca:.2f}')
# print(f'Valor Morango = {valor_morango:.2f}')
# print(f'Valor Total Maça = {valor_total_maca:.2f}')
# print(f'Valor total Morango = {valor_total_morango:.2f}')

# if total_kg >= 8 or total_bruto >= 25:
#     total_liquido = total_bruto * 0.9
#     print(f'Valor total = {total_bruto:.2f}')
#     print(f'Desconto de 10% = {total_liquido:.2f}')
# else:
#     print(f'Valor total = {total_bruto:.2f}')

# 5. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda (que depende do salário bruto conforme tabela abaixo) e 3% para o Sindicato. O FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês. 
# Descontos do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% 

# valor_hora = float(input("Digite o valor da hora trabalhada: "))
# qtd_hora = float(input("Digite a qtd de horas trabalhadas: "))

# salario_bruto = valor_hora * qtd_hora
# inss = salario_bruto * 0.10
# fgts = salario_bruto * 0.11
# sindicato = salario_bruto * 0.03

# print(f'Salário bruto: {valor_hora} * {qtd_hora}: R$ {salario_bruto}')

# if salario_bruto <= 900:
#     ir = 0
#     print(f'(-) IR (ISENTO): R${ir:.2f}')
# elif salario_bruto > 900 and salario_bruto <= 1500:
#     ir = salario_bruto * 0.05
#     print(f'(-) IR (5%): R${ir:.2f}')
# elif salario_bruto > 1500 and salario_bruto <= 2500:
#     ir = salario_bruto * 0.10
#     print(f'(-) IR (10%): R${ir:.2f}')
# else:
#     ir = salario_bruto * 0.20
#     print(f'(-) IR (20%): R${ir:.2f}')

# total_descontos = ir + inss + sindicato
# salario_liquido = salario_bruto - total_descontos

# print(f'(-) INSS (10%): R${inss:.2f}')
# print(f'(-) Sindicato (3%): R${sindicato:.2f}')
# print(f'FGTS (11%): R${fgts:.2f}')
# print(f'Total de Descontos (IR+INSS+Sindicato): R${total_descontos:.2f}')
# print(f'Salário Líquido: R${salario_liquido:.2f}')

# 7. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

# num = int(input(f'Insira um número inteiro: '))

# fat_1 = 1
# fat_2 = 1
# cont = 1

# while cont <= num:

# for cont in range(num,num+1):

# print(f'fatoral no while é {fat_1}')
# print(f'fatoral no while é {fat_2}')

# 8. Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato

# import random

# n = int(input("Quantidade de candidatos: "))

# cont = 0
# candidato1 = 0
# candidato2 = 0
# candidato3 = 0

# while cont < n:
#     voto = random.randint(1,4)

#     if voto == 1:
#         candidato1+=1
#     elif voto == 2:
#         candidato2+=1
#     elif voto == 3:
#         candidato3+=1
#     else:
#         print("Opção Inválida")
#         cont-=1
#     cont+=1
#     print("Voto: ", voto)

# print(f'Quantidade de votos do candidato 1: {candidato1}')
# print(f'Quantidade de votos do candidato 2: {candidato2}')
# print(f'Quantidade de votos do candidato 3: {candidato3}')

# 9. Desenvolva um programa que faça a tabuada de um número inteiro que será digitado pelo usuário, 
# mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem 
# ser informados também pelo usuário, conforme exemplo abaixo:

# num = int(input("Insira o número da tabuada: "))
# minimo = int(input("Insira o minimo da tabuada: "))
# maximo = int(input("Insira o maximo da tabuada: "))

# for i in range(minimo,maximo+1):
#     print(f'{num} * {i} = {(num*i)}')

# A) Escreva uma função em Python que recebe como parâmetro o raio de um círculo, calcule e retorna sua área. Teste a sua função.
# 	A = π r²

# B) Escreva uma função em Python que recebe como parâmetro a temperatura em graus Fahrenheit, transforme e retorna a temperatura em graus Celsius. Teste a sua função.
# C = 5 * ((F-32) / 9).

# C) Escreva um programa em Python que peça dois números inteiros e um número real. Na sequência deve criar três funções:
# Função “Produto” que recebe dois números inteiros como parâmetros e retorna o produto dos números.
# Função “Soma”  que recebe um número inteiro e um número decimal como parâmetros e retorna a soma dos dois números.
# Função “Potencia” que recebe um número decimal como parâmetro e retorna o decimal elevado ao cubo.

def area_circulo(raio):
    return 3.14 * (raio**2)

def fah_para_cel(fahenheit):
        celsius = 5*((fahrenheit-32)/9)

def positivo_negativo(num):
      if num > 0:
           return "P"
      else:
           return "N"

def media_nota(n1,n2):
    media = (n1+n2)/2
    return media

def media_com_aprov(media):
    if media >= 7 and media < 10:
        return "Aprovado"
    elif media >= 10:
        return "Aprovado com distinção"
    else:
        return "Reprovado"

def main():
    # raio = float(input("Questão A: Insira o raio: "))
    # print(f'Resposta A: A área do círculo é: ', area_circulo(raio))

    # fahrenheit = float(input("QB: Digite a temperatura em Fahrenheit: "))
    # print(f'RQB: A temperatura em fahrenheit {fahrenheit} em celsius é {fah_para_cel(fahrenheit):.2f}')
    
    # num = float(input("Insira um número: "))
    # print(f'O número é: {positivo_negativo(num)}')

    n1 = float(input("Digite a N1: "))
    n2 = float(input("Digite a N2: "))
    
    print(f'A média aritmética de {n1:.2f} e {n2:.2f} é {media_nota(n1,n2):.2f}')
   
    media = media_nota(n1,n2)

    print(media_com_aprov(media))

main()