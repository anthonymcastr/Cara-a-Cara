import random
import time

# Dicionário com esportes e dicas
esportes = {
    "⚽": {"nome": "Futebol", "dicas": ["Uma partida tem 90 minutos.", "O Brasil tem 5 Copas do Mundo.", "Cada time joga com 11 jogadores.", "A bola é redonda.", "É o esporte mais popular do mundo.", "O objetivo é fazer gols.", "Tem impedimento.", "É jogado em campo de grama.", "Tem goleiro.", "Cristiano Ronaldo e Messi são estrelas desse esporte."]},
    "🏀": {"nome": "Basquete", "dicas": ["Cada cesta vale de 1 a 3 pontos.", "É jogado com as mãos.", "Michael Jordan é um ícone.", "Tem dribles e enterradas.", "A bola é laranja.", "A quadra é coberta.", "5 jogadores por time em quadra.", "A NBA é o principal campeonato.", "Tem tempo limitado por posse.", "Existe o arremesso de 3 pontos."]},
    "🎾": {"nome": "Tenis", "dicas": ["A bola deve quicar no campo adversário.", "É jogado com raquete.", "Pode ser individual ou em duplas.", "Tem game, set e match.", "Wimbledon é um torneio famoso.", "Roger Federer é um nome forte no esporte.", "O campo pode ser de saibro, grama ou duro.", "Tem vantagem e igualdade.", "É silencioso durante os pontos.", "A bola é pequena e amarela."]},
    "🏐": {"nome": "Volei", "dicas": ["Cada time tem 6 jogadores em quadra.", "É jogado com as mãos.", "Tem saque, bloqueio e cortada.", "A bola não pode tocar o chão.", "O Brasil é referência mundial.", "Existe o líbero, que usa uniforme diferente.", "É disputado em sets.", "Pode ser jogado na praia também.", "Tem rotação entre jogadores.", "A rede separa os dois lados."]},
    "🏈": {"nome": "Futebol Americano", "dicas": ["A bola tem formato oval.", "Cada jogada é tática.", "Tem touchdown e field goal.", "É muito popular nos EUA.", "Os jogadores usam capacetes.", "O Super Bowl é a final mais famosa.", "Tem posições como quarterback e linebacker.", "Avanço por jardas.", "É um esporte de contato.", "Tem 4 quartos no jogo."]},
    "⚾": {"nome": "Beisebol", "dicas": ["É muito popular no Japão e nos EUA.", "Tem bastão e luvas.", "O jogador corre por bases.", "Tem home run.", "O arremessador é o pitcher.", "O receptor é o catcher.", "Jogo com 9 entradas.", "A bola é branca com costura vermelha.", "Time que marca mais corridas vence.", "Tem rebatedores."]},
    "🥊": {"nome": "Boxe", "dicas": ["É um esporte de combate.", "Os atletas usam luvas.", "Tem categorias por peso.", "Muhammad Ali é uma lenda.", "Tem rounds e juízes.", "Não pode golpear abaixo da linha de cintura.", "É praticado no ringue.", "Objetivo é nocautear ou pontuar mais.", "Tem contagem de 10 no nocaute.", "Cada round dura 3 minutos."]},
    "🏓": {"nome": "Tenis de Mesa", "dicas": ["Também é chamado de ping pong.", "Jogado com raquetes pequenas.", "A mesa tem rede no meio.", "A bola é leve e pequena.", "Popular na China.", "Os pontos vão até 11.", "Pode ser jogado em duplas.", "É muito rápido.", "A bola deve quicar dos dois lados.", "A mesa é verde ou azul."]},
    "🏸": {"nome": "Badminton", "dicas": ["Usa peteca (volante).", "As raquetes são finas e leves.", "Pode ser individual ou em duplas.", "É jogado em quadra coberta.", "É o esporte de raquete mais rápido do mundo.", "Tem saque e rally.", "Popular na Ásia.", "O objetivo é cair no lado adversário.", "A pontuação vai até 21.", "A rede é mais baixa que a do vôlei."]},
    "⛳": {"nome": "Golfe", "dicas": ["O objetivo é colocar a bola no buraco.", "Usa tacos.", "É jogado em campo aberto.", "Tem 18 buracos por padrão.", "Tiger Woods é um ícone do esporte.", "É jogado com calma e precisão.", "Cada buraco tem par específico.", "A bola é pequena e branca.", "Pode demorar horas uma partida.", "O menor número de tacadas vence."]},
    "🤽": {"nome": "Polo Aquatico", "dicas": ["É jogado dentro da piscina.", "Cada time tem 7 jogadores.", "O objetivo é marcar gols.", "Exige muita resistência.", "A bola é arremessada com a mão.", "Tem goleiro.", "Não pode encostar no fundo da piscina.", "Tem exclusões temporárias.", "A bola é amarela.", "É um esporte olímpico."]},
    "🥋": {"nome": "Judo", "dicas": ["É um esporte de origem japonesa.", "Usa kimono.", "Tem faixas de graduação.", "Tem projeções e imobilizações.", "É disputado no tatame.", "O objetivo é derrubar ou imobilizar.", "Tem pontuação como ippon e waza-ari.", "Respeito é fundamental.", "É muito praticado no Brasil.", "Foi criado por Jigoro Kano."]}
}

def salvar_ranking(nome, pontos, duracao, resultado):
    with open("ranking.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome} - {pontos} eliminações - {duracao:.2f} segundos - {resultado}\n")

def criar_tabuleiro():
    emojis = list(esportes.keys())
    random.shuffle(emojis)
    return [emojis[i:i+4] for i in range(0, len(emojis), 4)]

def mostrar_tabuleiro(tabuleiro, revelados, oculto=False):
    print("    A    B    C    D")
    for i, linha in enumerate(tabuleiro):
        linha_str = f"{i+1} | " + " | ".join(
            ["❓" if oculto and revelados[i][j] else "❌" if not revelados[i][j] else emoji
             for j, emoji in enumerate(linha)]
        ) + " |"
        print(linha_str)

def coordenada_para_indices(coordenada):
    colunas = {"A": 0, "B": 1, "C": 2, "D": 3}
    if len(coordenada) != 2:
        return None, None
    coluna = colunas.get(coordenada[0].upper())
    linha = int(coordenada[1]) - 1 if coordenada[1].isdigit() else None
    return linha, coluna

nome_jogador = input("Digite seu nome para começar: ").strip()
tabuleiro_jogador = criar_tabuleiro()
tabuleiro_maquina = criar_tabuleiro()
revelados_jogador = [[True]*4 for _ in tabuleiro_jogador]
revelados_maquina = [[True]*4 for _ in tabuleiro_maquina]
emoji_secreto_maquina = random.choice([emoji for linha in tabuleiro_jogador for emoji in linha])
emoji_secreto_jogador = random.choice([emoji for linha in tabuleiro_maquina for emoji in linha])
pontos_jogador = 0
pontos_maquina = 0
inicio = time.time()

print("\n🎮 Bem-vindo ao Cara a Cara dos Esportes!")
print(f"Boa sorte, {nome_jogador}!")

while True:
    print("\n🔍 Seu Tabuleiro:")
    mostrar_tabuleiro(tabuleiro_jogador, revelados_jogador)
    print("\n🎯 Tabuleiro da Máquina:")
    mostrar_tabuleiro(tabuleiro_maquina, revelados_maquina, oculto=True)

    coord = input("\nDigite a coordenada para ELIMINAR um esporte do tabuleiro da máquina (ex: B2): ").upper()
    linha, coluna = coordenada_para_indices(coord)

    if linha is None or coluna is None or linha >= len(tabuleiro_maquina) or coluna >= 4:
        print("Coordenada inválida.")
        continue

    if not revelados_maquina[linha][coluna]:
        print("Essa posição já foi eliminada.")
        continue

    emoji = tabuleiro_maquina[linha][coluna]
    dicas = esportes[emoji]["dicas"][:]
    random.shuffle(dicas)
    print(f"\n📌 Dica: {dicas[0]}")
    resposta = input("Qual é o esporte? ").strip().upper()

    if resposta == esportes[emoji]["nome"].upper():
        revelados_maquina[linha][coluna] = False
        pontos_jogador += 1
        print(f"✅ Você eliminou {emoji}!")
    else:
        print("❌ Resposta incorreta.")

   
    print("\n🤖 Vez da máquina...")
    time.sleep(1)
    opcoes = [(i, j) for i in range(len(tabuleiro_jogador)) for j in range(4) if revelados_jogador[i][j]]
    if opcoes:
        i, j = random.choice(opcoes)
        acertou = random.random() < 0.3
        emoji = tabuleiro_jogador[i][j]
        if emoji == emoji_secreto_maquina and acertou:
            print("A máquina tentou adivinhar e acertou seu esporte secreto!")
            revelados_jogador[i][j] = False
            pontos_maquina += 1
        elif emoji != emoji_secreto_maquina:
            revelados_jogador[i][j] = False
            pontos_maquina += 1
            print(f"A máquina eliminou uma peça em {chr(j+65)}{i+1}")
        else:
            print("A máquina tentou e errou.")
    time.sleep(1)

    fim = time.time()
    restantes_jogador = sum(row.count(True) for row in revelados_jogador)
    restantes_maquina = sum(row.count(True) for row in revelados_maquina)

    if restantes_jogador == 1 or restantes_maquina == 1:
        print("\n🎮 Fim de jogo!")
        print(f"{nome_jogador}: {pontos_jogador} eliminações")
        print(f"Máquina: {pontos_maquina} eliminações")
        resultado = "Vitória" if pontos_jogador > pontos_maquina else "Derrota"
        print(f"\n🏁 Resultado: {resultado}!")
        salvar_ranking(nome_jogador, pontos_jogador, fim - inicio, resultado)
        break
