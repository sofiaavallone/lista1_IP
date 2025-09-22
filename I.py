# Recebendo as informações
print("Bem-vindos ao Jimmy Jab!")
participante1 = input()
participante2 = input()
participante3 = input()
participante4 = input()

# Conferindo de Terry ou Holt estão competindo
if participante1 == "Terry" or participante1 == "Holt" or participante2 == "Terry" or participante2 == "Holt" or participante3 == "Terry" or participante3 == "Holt" or participante4 == "Terry" or participante4 == "Holt":
    print("Jimmy Jab CANCELADO!")
else:
    # Início da Bocatona
    print("Nosso primeiro evento é...\nA Bocatona!")
    # Opção se Scully está na competição
    if participante1 == "Scully" or participante2 == "Scully" or participante3 == "Scully" or participante4 == "Scully":
        print("Scully leva a melhor, não tem como competir com ele.")
        perderdor_bocatona = input()
        print(f"{perderdor_bocatona} não avançou para a próxima fase!")
    # Opção se Scully não está na competição
    else:
        vencedor_bocatona = input()
        perderdor_bocatona = input()
        print(f"{vencedor_bocatona} levou a melhor na Bocatona!")
        print(f"{perderdor_bocatona} não avançou para a próxima fase!")

    # Eliminando o perderdor
    if participante1 == perderdor_bocatona:
        participante1 = participante2
        participante2 = participante3
        participante3 = participante4
        participante4 = None
    elif participante2 == perderdor_bocatona:
        participante2 = participante3
        participante3 = participante4
        participante4 = None
    elif participante3 == perderdor_bocatona:
        participante3 = participante4
        participante4 = None
    else:
        participante4 = None

    print("O segundo evento é A corrida volumosa!")

    # Entrada dos tempos dos participantes restantes
    tempo_participante1 = int(input())
    tempo_participante2 = int(input())
    tempo_participante3 = int(input())

    # Descobrindo o maior e menor tempo e os finalistas
    if tempo_participante1 > tempo_participante2 and tempo_participante2 > tempo_participante3:
        print(f"{participante3} levou a melhor na Corrida Volumosa!")
        print(f"{participante1} não avançou para a próxima fase!")
        participante1 = participante2
        participante2 = participante3
        participante3 = None
    elif tempo_participante1 > tempo_participante3 and tempo_participante3 > tempo_participante2:
        print(f"{participante2} levou a melhor na Corrida Volumosa!")
        print(f"{participante1} não avançou para a próxima fase!")
        participante1 = participante2
        participante2 = participante3
        participante3 = None
    elif tempo_participante2 > tempo_participante1 and tempo_participante1 > tempo_participante3:
        print(f"{participante3} levou a melhor na Corrida Volumosa!")
        print(f"{participante2} não avançou para a próxima fase!")
        participante2 = participante3
        participante3 = None
    elif tempo_participante2 > tempo_participante3 and tempo_participante3 > tempo_participante1:
        print(f"{participante1} levou a melhor na Corrida Volumosa!")
        print(f"{participante2} não avançou para a próxima fase!")
        participante2 = participante3
        participante3 = None
    elif tempo_participante3 > tempo_participante2 and tempo_participante2 > tempo_participante1:
        print(f"{participante1} levou a melhor na Corrida Volumosa!")
        print(f"{participante3} não avançou para a próxima fase!")
        participante3 = None
    elif tempo_participante3 > tempo_participante1 and tempo_participante1 > tempo_participante2:
        print(f"{participante2} levou a melhor na Corrida Volumosa!")
        print(f"{participante3} não avançou para a próxima fase!")
        participante3 = None
        
    # Encontrando o vencedor
    if (participante1 == "Amy" and participante2 == "Jake") or (participante1 == "Jake" and participante2 == "Amy"):
        print("Jake ficou com o 2º lugar!")
        print("Amy VENCEU O JIMMY JABS!")
    else:
        vencedor = input()
        if vencedor == participante1:
            print(f"{participante2} ficou com o 2º lugar!")
            print(f"{vencedor} VENCEU O JIMMY JABS!")
        else:
            print(f"{participante1} ficou com o 2º lugar!")
            print(f"{vencedor} VENCEU O JIMMY JABS!")
