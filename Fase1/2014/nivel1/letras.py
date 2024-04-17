#pegamos a letra a ser contada e um texto
letra = input("digite a letra desejada: ")
texto = input("Digite o texto: ")

txt2 = texto.replace(letra, "1") #substituo a letra desejada por um caractere qualquer, por exemplo, usei o '1'
l = txt2.split() #separo cada palavra do texto e gurado em uma lista
ocorrencia = 0 # inicio uma variavel para contar as vezes que meu caractere especial aparecer

#percorro a lista, caso meu caractere especial esteja na palavra, eu adiciono 1 em ocorrencia
for i in l:
    if "1" in l:
        ocorrencia += 1

p = (ocorrencia * 100) / len(l) #calculo a porcentagem das ocorrencias
porcentagem = round(p, 1) # limito o numero a ter uma casa decimal
print(porcentagem) #mostro a porcentagem