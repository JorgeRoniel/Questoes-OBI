F, R = [int(n) for n in input().split()] #pegamos o tamanho da fita e quantas partes estão coloridas
posicoes_gotas = [int(n) for n in input().split()] #pegamos as posições onde foi colocado as gotas

posicoes_coloridas = set(posicoes_gotas) #coloco as posições e coloco num conjunto
dias = 0 #uma  variavel para contar os dias

while len(posicoes_coloridas) < F: #Enquanto houver posições não coloridas...
    novas_pos_coloridas = set() #Outro conjunto para pegar as novas posições coloridas

    #para cada posiçao em posições coloridas, verificamos seus vizinhos, se não estiverem coloridos, adicionamos no conjunto nova_pos_coloridas
    for posicao in posicoes_coloridas:
        if posicao > 1:
            novas_pos_coloridas.add(posicao - 1)
        
        if posicao < F:
            novas_pos_coloridas.add(posicao + 1)
    
    posicoes_coloridas.update(novas_pos_coloridas) #atualizamos o primeiro conjunto
    dias += 1 #acrescentamos 1 ao dias

print(dias)