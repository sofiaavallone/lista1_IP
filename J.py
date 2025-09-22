print("Ted se iludiu de novo. Esse é o momento que ele mais precisa dos amigos dele…")
print("Quantos dos amigos dele conseguirão ajudar dessa vez?")

barney = False
robin = False
marshall = False
lily = False

# Entradas
quantidade_pessoas = int(input())
print("Hora da lista dos amigos da vez!")
# 0 pessoas
if quantidade_pessoas == 0:
    lugar = "MacLaren’s Pub"

# 1 pessoa
elif quantidade_pessoas == 1:
    
    nome1 = input()
    if nome1 == "Barney":
        barney = True
        print("Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
    elif nome1 == "Robin":
        robin = True
        print("Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
    elif nome1 == "Marshall":
        marshall = True
        print("O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
    elif nome1 == "Lily":
        lily = True
        print("Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
    else:
        print(f"{nome1} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")
    
    #  Outputs relacionados com combinações de nomes
    if marshall == True and lily == True:
        print("Nada melhor que um casal para dar conselhos de relacionamento.")
    if barney == True and marshall == True and lily == False and robin == False:
        print("Sem dúvida os melhores amigos de Ted. Mas tomara que Barney não queira implicar com Marshall sobre quem realmente é o melhor amigo dele.")
    if barney == True and robin == True and marshall == True and lily == True:
        print("O quinteto estará reunido nessa jornada! É o momento perfeito pra brincar de “Você conhece o Ted?”.")

    lugar = input()

# 2 pessoas
elif quantidade_pessoas == 2:

    nome1 = input()
    if nome1 == "Barney":
        barney = True
        print("Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
    elif nome1 == "Robin":
        robin = True
        print("Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
    elif nome1 == "Marshall":
        marshall = True
        print("O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
    elif nome1 == "Lily":
        lily = True
        print("Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
    else:
        print(f"{nome1} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")
    
    nome2 = input()
    if nome2 == "Barney":
        barney = True
        print("Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
    elif nome2 == "Robin":
        robin = True
        print("Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
    elif nome2 == "Marshall":
        marshall = True
        print("O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
    elif nome2 == "Lily":
        lily = True
        print("Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
    else:
        print(f"{nome2} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")
    
    #  Outputs relacionados com combinações de nomes
    if marshall == True and lily == True:
        print("Nada melhor que um casal para dar conselhos de relacionamento.")
    if barney == True and marshall == True and lily == False and robin == False:
        print("Sem dúvida os melhores amigos de Ted. Mas tomara que Barney não queira implicar com Marshall sobre quem realmente é o melhor amigo dele.")
    if barney == True and robin == True and marshall == True and lily == True:
        print("O quinteto estará reunido nessa jornada! É o momento perfeito pra brincar de “Você conhece o Ted?”.")

    lugar = input()

# 3 pessoas
elif quantidade_pessoas == 3:

    nome1 = input()
    if nome1 == "Barney":
        barney = True
        print("Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
    elif nome1 == "Robin":
        robin = True
        print("Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
    elif nome1 == "Marshall":
        marshall = True
        print("O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
    elif nome1 == "Lily":
        lily = True
        print("Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
    else:
        print(f"{nome1} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")
    
    nome2 = input()
    if nome2 == "Barney":
        barney = True
        print("Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
    elif nome2 == "Robin":
        robin = True
        print("Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
    elif nome2 == "Marshall":
        marshall = True
        print("O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
    elif nome2 == "Lily":
        lily = True
        print("Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
    else:
        print(f"{nome2} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")
    
    nome3 = input()
    if nome3 == "Barney":
        barney = True
        print("Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
    elif nome3 == "Robin":
        robin = True
        print("Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
    elif nome3 == "Marshall":
        marshall = True
        print("O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
    elif nome3 == "Lily":
        lily = True
        print("Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
    else:
        print(f"{nome3} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")
    
    #  Outputs relacionados com combinações de nomes
    if marshall == True and lily == True:
        print("Nada melhor que um casal para dar conselhos de relacionamento.")
    if barney == True and marshall == True and lily == False and robin == False:
        print("Sem dúvida os melhores amigos de Ted. Mas tomara que Barney não queira implicar com Marshall sobre quem realmente é o melhor amigo dele.")
    if barney == True and robin == True and marshall == True and lily == True:
        print("O quinteto estará reunido nessa jornada! É o momento perfeito pra brincar de “Você conhece o Ted?”.")

    lugar = input()

# 4 pessoas
else:

    nome1 = input()
    if nome1 == "Barney":
        barney = True
        print("Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
    elif nome1 == "Robin":
        robin = True
        print("Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
    elif nome1 == "Marshall":
        marshall = True
        print("O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
    elif nome1 == "Lily":
        lily = True
        print("Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
    else:
        print(f"{nome1} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")
    
    nome2 = input()
    if nome2 == "Barney":
        barney = True
        print("Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
    elif nome2 == "Robin":
        robin = True
        print("Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
    elif nome2 == "Marshall":
        marshall = True
        print("O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
    elif nome2 == "Lily":
        lily = True
        print("Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
    else:
        print(f"{nome2} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")
    
    nome3 = input()
    if nome3 == "Barney":
        barney = True
        print("Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
    elif nome3 == "Robin":
        robin = True
        print("Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
    elif nome3 == "Marshall":
        marshall = True
        print("O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
    elif nome3 == "Lily":
        lily = True
        print("Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
    else:
        print(f"{nome3} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")
    
    nome4 = input()
    if nome4 == "Barney":
        barney = True
        print("Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.")
    elif nome4 == "Robin":
        robin = True
        print("Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.")
    elif nome4 == "Marshall":
        marshall = True
        print("O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.")
    elif nome4 == "Lily":
        lily = True
        print("Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.")
    else:
        print(f"{nome4} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.")
    
#  Outputs relacionados com combinações de nomes
    if marshall == True and lily == True and quantidade_pessoas == 2:
        print("Nada melhor que um casal para dar conselhos de relacionamento.")
    if barney == True and marshall == True and quantidade_pessoas == 2:
        print("Sem dúvida os melhores amigos de Ted. Mas tomara que Barney não queira implicar com Marshall sobre quem realmente é o melhor amigo dele.")
    if barney == True and robin == True and marshall == True and lily == True:
        print("O quinteto estará reunido nessa jornada! É o momento perfeito pra brincar de “Você conhece o Ted?”.")

    lugar = input()


if lugar == "MacLaren’s Pub":
    quant_media_cervejas = int(input("Quantidade média de cervejas:"))

# Outputs relacionando nomes e lugares
if barney == True and lugar == "Arena de Laser Tag":
    print("Com certeza a Arena de Laser Tag foi escolhida por influência de Barney. Se arrume Ted, é hora de botar um terno, tomar um whisky e partir pra diversão.")
if robin == True  and lugar == "Carmichael’s" and quantidade_pessoas == 1:
    print("Acho que Ted e Robin vão sair em um date… Tomara que Ted não roube aquela trompa azul da parede de novo.")
if (barney == True or robin == True or marshall == True or lily == True) and lugar == "MacLaren’s Pub":
    print("Não tem erro, né? Estar no MacLaren’s é como estar em casa.")
if (barney == False or robin == False or marshall == False or lily == False) and lugar == "MacLaren’s Pub":
    print("Um lugar habitual, mas com uma galera diferente. Será estranho, mas Ted vai.")

# Relatório final
print()
if quantidade_pessoas == 0:
    print(f"Relatório da situação de Ted:")
    print(f"Ted foi para o MacLaren’s... Olhe em volta, Ted, você está sozinho.")
    print(f"- Quantidade de cervejas bebidas por Ted: {quant_media_cervejas * (quantidade_pessoas + 1)}")
elif quantidade_pessoas == 1:
    print(f"Relatório da situação de Ted:")
    print(f"- Ted foi consolado por: {nome1}.")
    print(f"- O local de afogar as mágoas foi: {lugar}.")
    print(f"- Saideira de um pra um. Nada melhor do que uma pessoa pra ouvir seus problemas.")
    if lugar == "MacLaren’s Pub":
        print(f"- Quantidade de cervejas bebidas pelo grupo: {quant_media_cervejas * (quantidade_pessoas + 1)} cervejas.")
elif quantidade_pessoas == 2:
    print(f"Relatório da situação de Ted:")
    print(f"- Ted foi consolado por: {nome1} e {nome2}.")
    print(f"- O local de afogar as mágoas foi: {lugar}.")
    print(f"- Duas pessoas se compadeceram com a situação do pobre Ted.")
    if lugar == "MacLaren’s Pub":
        print(f"- Quantidade de cervejas bebidas pelo grupo: {quant_media_cervejas * (quantidade_pessoas + 1)} cervejas.")
elif quantidade_pessoas == 3:
    print(f"Relatório da situação de Ted:")
    print(f"- Ted foi consolado por: {nome1}, {nome2} e {nome3}.")
    print(f"- O local de afogar as mágoas foi: {lugar}.")
    print(f"- Três pessoas! Ted conseguiu se divertir bastante.")
    if lugar == "MacLaren’s Pub":
        print(f"- Quantidade de cervejas bebidas pelo grupo: {quant_media_cervejas * (quantidade_pessoas + 1)} cervejas.")
else:
    print(f"Relatório da situação de Ted:")
    print(f"- Ted foi consolado por: {nome1}, {nome2}, {nome3} e {nome4}.")
    print(f"- O local de afogar as mágoas foi: {lugar}.")
    if barney == True and robin == True and marshall == True and lily == True:
        print("- O quinteto junto consegue resolver qualquer problema!")
    else:
        print("- Saiu um quinteto um pouco diferente do que a gente tá acostumado, mas no fim conseguiram deixar Ted alegre.")
    
    if lugar == "MacLaren’s Pub":
        print(f"- Quantidade de cervejas bebidas pelo grupo: {quant_media_cervejas * (quantidade_pessoas + 1)} cervejas.")
print("Pelo visto todo mundo já sabe como funciona a cabeça dele, né? Depois do rolê Ted conseguiu esfriar a cabeça e já tá pronto pra quebrar mais a cara. Quem será que serão os próximos a consolar o querido Ted Mosby?")
