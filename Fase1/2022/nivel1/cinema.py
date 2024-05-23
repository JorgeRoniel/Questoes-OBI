def tabela_idades(idade):
    valor = 0.0
    if idade <= 17:
        valor = 15
    elif idade >= 18 and idade < 60:
        valor = 30
    elif idade >= 60:
        valor = 20
    
    return valor

idade1 = int(input())
idade2 = int(input())

v1 = tabela_idades(idade1)
v2 = tabela_idades(idade2)

print(v1 + v2)