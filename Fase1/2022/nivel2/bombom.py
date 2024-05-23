ini = input()
dominante = ini[1]

Luana = 0
for i in range(3):
    carta = input()
    if carta[0] == 'A':
        Luana += 10
    elif carta[0] == 'J':
        Luana += 11
    elif carta[0] == 'Q':
        Luana += 12
    elif carta[0] == 'K':
        Luana += 13

    if carta[1] == dominante:
        Luana += 4

Edu = 0
for i in range(3):
    carta = input()
    if carta[0] == 'A':
        Edu += 10
    elif carta[0] == 'J':
        Edu += 11
    elif carta[0] == 'Q':
        Edu += 12
    elif carta[0] == 'K':
        Edu += 13

    if carta[1] == dominante:
        Edu += 4

if Luana > Edu:
    print("Luana")
elif Edu > Luana:
    print("Edu")
else:
    print("empate")
