x1 = int(input("Digite a coordenada x de Ted: "))
y1 = int(input("Digite a coordenada y de Ted: "))
x2 = int(input("Digite a coordena x do guarda-chuva: "))
y2 = int(input("Digite a coordenada y do guarda-chuva: "))

amigo = input("Digite o nome do amigo: ")

distancia_original = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5

if amigo == "Barney":
    distancia_final = distancia_original + 10
elif amigo == "Marshall":
    distancia_final = distancia_original - 5
elif amigo == "Lily":
    distancia_final = distancia_original - 10
elif amigo == "Robin":
    distancia_final = distancia_original + 5

print(f"Pelos meus cálculos a distância final encontrada foi {round(distancia_final)}!")

if distancia_final <= 50:
    if amigo == "Barney":
        print("Nossa, eu sou incrível! Vimos o guarda-chuva em 5 minutos. Tão lendário que eu poderia até ter pego ele pra mim! Desafio aceito!")
    elif amigo == "Marshall":
        print("Obrigado pela ajuda, Marsh! Tão bom saber que a gente pode contar com os amigos pra achar a nossa cara-metade. Encontramos o guarda-chuva!")
    elif amigo == "Lily":
        print("Ah! Não te falei? Peguei um atalho! Lilypad sabe das coisas. O guarda-chuva está aqui, e nem nos cansamos muito!")
    elif amigo == "Robin":
        print("Bem... acho que isso realmente aconteceu. Nem foi tão difícil assim. O guarda-chuva está bem aqui, Ted. Onde está o mistério?")
else:
    if amigo == "Barney":
        print("Esse não era o caminho para o guarda-chuva, mas com certeza é o caminho para uma noite lendária! Challenge accepted, vista seu terno!")
    elif amigo == "Marshall":
        print("Tudo bem, cara. O destino é paciente. O importante é que estamos juntos nessa. Vamos tentar de novo amanhã.")
    elif amigo == "Lily":
        print("Isso não faz sentido! Meu atalho deveria ter funcionado! Que saco! Fiquei com fome de tanta caminhada.")
    elif amigo == "Robin":
        print("Sério, Ted? Um guarda-chuva? O destino é um conceito abstrato.")