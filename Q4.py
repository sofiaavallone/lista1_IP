# Entrada dos valores
artigos_s = int(input("Digite o número de artigos lidos por Sheldon: "))
artigos_l = int(input("Digite o número de artigos lidos por Leonard: "))
artigos_r = int(input("Digite o número de artigos lidos por Raj: "))
artigos_h = int(input("Digite o número de artigos lidos por Howard: "))
experimentos_s = int(input("Digite o número de experimentos realizados por Sheldon: "))
experimentos_l = int(input("Digite o número de experimentos realizados por Leonard: "))
experimentos_r = int(input("Digite o número de experimentos realizados por Raj: "))
experimentos_h = int(input("Digite o número de experimentos realizados por Howard: "))

# Cálculo das pontuações
pontuacao_s = artigos_s * 2 + experimentos_s * 2
pontuacao_l = artigos_l * 2 + experimentos_l * 2
pontuacao_r = artigos_r * 2 + experimentos_r * 2
pontuacao_h = artigos_h * 2 + experimentos_h * 2

# Saída das pontuações de cada um
print(f"Pontuação final: \nSheldon: {pontuacao_s}\nLeonard: {pontuacao_l}\nRaj: {pontuacao_r}\nHoward: {pontuacao_h}")

# Descobrir o vencedor
if pontuacao_s > pontuacao_r:
    vencedor = pontuacao_s
else:
    vencedor = pontuacao_r
if pontuacao_l > vencedor:
    vencedor = pontuacao_l
if pontuacao_h > vencedor:
    vencedor = pontuacao_h
