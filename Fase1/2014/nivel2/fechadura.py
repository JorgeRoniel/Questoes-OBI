#Como é falado na questão, pegamos do usuario o numero de pinos e  pegamos a altura que é necessaria para desbloquear a porta
N, M = [int(n) for n in input().split()]


alturas = [int(num) for num in input().split()] #lista definida para pegar a altura de cada pino

#aqui, pegamos a altura de cada pino, de acordo com o numero de pinos, e guardamos na lista "alturas"

    
contador = 0 #definimos um contador

for i in range(N-1): 
    dif = M - alturas[i] #pegamos a diferença entre a altura de desbloqueio e a altura atual
    alturas[i] += dif #somamos a diferença com o numero atual na lista
    alturas[i + 1] += dif #somamos tambem o proximo elemento com a diferença
    contador += abs(dif) #o contador recebe a diferença
    
print(contador) #o contador representa os movimentos necessarios para que o valor da altura de desbloqueio seja atingido por cada pino
