N,M = [int(n) for n in input().split()] #pegamos o numero total de palitos e o maximo que cada amigo pode pegar

maneiras = (N-1) * (N-2)/2 #Aqui, calculamos o total de maneiras de dividir os palitos, sem restrição

#Aqui, verificamos se pelo menos um dos 3 amigos pegou mais que m palitos, caso verdadeiro, subtraimos as combinações
if N - 1 - M >= 2:
    maneiras -= 3*(N - 1 - M)*(N - 2 - M)/2

#Verificamos quando dois amigos recebem mais do que m palitos, então somamos as combinações
if N - 1 - 2*M >= 2:
    maneiras += 3*(N - 1 - 2*M)*(N - 2 - 2*M)/2

#Aqui, verificamos se os tres amigos receberam mais do que m palitos, caso verdadeiro, subtraimos as combinações
if N - 1 - 3*M >= 2:
    maneiras -= (N - 1 - 3*M)*(N - 2 - 3*M)/2

print(maneiras)