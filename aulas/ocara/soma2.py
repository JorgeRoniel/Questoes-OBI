## Temos essa forma que da certo com complexidade O(n)
qtd_quadrados, soma = map(int, input().split())
valores = list(map(int, input().split()))

result = {0: 1}  # Inicializa com a soma 0 tendo frequência 1
soma_atual = 0
qtd_retangulos = 0

for valor in valores:
    soma_atual += valor
    
    # Verifica se a soma_atual - soma já foi encontrada antes
    if soma_atual - soma in result:
        qtd_retangulos += result[soma_atual - soma]

    # Atualiza a frequência da soma_atual no dicionário
    result[soma_atual] = result.get(soma_atual, 0) + 1

print(qtd_retangulos)  # Imprime a quantidade de retângulos com a soma desejada
