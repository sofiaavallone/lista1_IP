# Recebendo as informações
casos = int(input())
dias = int(input())
assistencia_casos = int(input())
operacao_campo = int(input())
operacao_especial = input().lower()
if operacao_especial == "sim":
    tipo_especial = input()
localizacao = input().capitalize()

media = casos / dias
desclassificacao = True

# Primeiro requisito
if localizacao != "Manhattan" and localizacao != "Brooklyn":
    print("Os casos não são nas áreas designadas por Holt. Peralta está desclassificado!")
else:
    print("Pelo menos nos bairros corretos Jake está!")
    # Segundo requisito
    if casos < 20:
        print("Vishh, Jake já foi eliminado por não ter o mínimo de casos necessários.")
    else:
        print("Detetive Peralta bateu o mínimo de casos, ele ainda está dentro da competição.")
        # Terceiro requisito
        if media < 0.5:
            print("A média diária de casos tá muito baixa, Peralta foi desclassificado.")
        else:
            print("Parece que Jake é bem consistente na sua média diária de casos.")
            # Quarto requisito
            if assistencia_casos < 5:
                print("Desclassificado! Jake precisa ajudar mais os companheiros.")
            else:
                print("Peralta ajudou bastante outros detetives, ele ainda está na competição!")
                # Quinto requisito
                if operacao_campo < 20:
                    print("Peralta precisa sair mais da delegacia, está faltando ação em campo!")
                else: 
                    print("Jake ainda sobrevive por sua participação em campo, será que ele vai levar pra casa o prêmio?")
                    desclassificacao = False
                    if operacao_especial == "sim":
                        print("Minha nossa! Jake Peralta é realmente um detetive diferenciado.")
                    else:
                        print("Para que operação especial quando se tem números, não é?")

#  Cálculo da pontuação
pontuacao = casos * 2 + assistencia_casos * 1.5 + operacao_campo * 0.5
if operacao_especial == "sim":
    if tipo_especial == "Infiltração":
        pontuacao = pontuacao + 0.5 * pontuacao
    elif tipo_especial == "Escuta":
        pontuacao = pontuacao + 0.3 * pontuacao
    elif tipo_especial == "Invasão":
        pontuacao = pontuacao + 0.2 * pontuacao
    else:
        pontuacao = pontuacao + 0.1 * pontuacao

if desclassificacao == False:
    if pontuacao >= 70:
        print("Jake é candidato forte ao prêmio. Será que Holt vai premiá-lo?")
    elif pontuacao >= 40 and pontuacao <= 69:
        print("Muito bem! Mas ainda é incerto se vai ser suficiente para ganhar o prêmio.")
    else:
        print("Muito difícil de Jake ganhar o prêmio.")              