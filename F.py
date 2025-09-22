# Recebendo as informações
nome_item = input().lower()
valor_item = float(input())
responsavel = input().capitalize()
tipo_evento = input().lower()

# Regras de Ouro da Angela
if valor_item > 100.00 and responsavel != "Angela":
    print("Compra Reprovada!")
    print("Gasto excessivo e irresponsável! Onde está a disciplina fiscal?!")
elif valor_item > 100.00 and responsavel == "Angela":
    print("Compra Aprovada!")
    print("Apenas eu tenho discernimento para gastos desta magnitude.")
elif responsavel == "Angela":
    print("Compra Aprovada!")
    print("Compra feita por mim, obviamente dentro dos padrões de excelência.")
else:

    # Regras para Michael Scott
    if responsavel == "Michael":
        if nome_item == "mágica" or nome_item == "fantasia":
            print("Compra Reprovada!")
            print("O Comitê não financia frivolidades e palhaçadas, Michael.")
        elif valor_item > 60.00:
            print("Compra Aprovada com ressalvas!")
            if tipo_evento == "natal":
                print("O espírito natalino de Michael é... excessivo. A nota será conferida.")
            elif tipo_evento == "aniversário":
                print("Michael nunca gasta tanto nos aniversários dos funcionários, deve ser o dele!")
        elif valor_item <= 60.00:
            print("Compra Aprovada!")
            print("Uma compra surpreendentemente sensata vinda do Michael. Suspeito.")
    else:

        # Regras Halloween
        if tipo_evento == "halloween":
            if nome_item == "abóbora" and valor_item <= 30.00:
                print("Compra Aprovada!")
                print("Uma abóbora de tamanho e custo razoáveis. Eficiente.")
            elif nome_item == "abóbora" and valor_item > 30.00:
                print("Compra Aprovada com ressalvas!")
                print("Por que uma abóbora precisa ser tão cara? Extravagância.")
            else:
                if valor_item < 100 or responsavel != "Angela":
                    print("Compra Aprovada com ressalvas!")
                    print("Decoração de Halloween... Tenho certeza que Phyllis exagerou de novo.")
        else:

            # Regras Aniversário
            if tipo_evento == "aniversário":
                if nome_item == "bolo" and valor_item <= 40.00:
                    print("Compra Aprovada!")
                    print("Um bolo modesto para celebrar mais um ano de produtividade, parabéns!")
                elif nome_item == "sorvete de menta com chocolate":
                    print("Compra Reprovada!")
                    print("Este sabor de sorvete é uma abominação e não entrará em meu evento.")
                else:
                    print("Compra Aprovada!")
                    print("Itens de aniversário devem ser práticos, não uma distração do trabalho.")
            else:
                # Regras gerais
                if valor_item > 50.00:
                    print("Compra Aprovada com ressalvas!")
                    print("Está dentro do orçamento, mas não quer dizer que não vou verificar!")
                else:
                    print("Compra Aprovada!")
                    print("Esta compra não viola nenhum regulamento... por enquanto.")
