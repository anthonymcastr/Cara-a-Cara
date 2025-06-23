import random
import time
import tkinter as tk
from tkinter import messagebox, simpledialog

## todas opções de esportes 
esportes = {
    "⚽": {"nome": "Futebol", "dicas": ["Uma partida tem 90 minutos.", "O Brasil tem 5 Copas do Mundo.", "Cada time joga com 11 jogadores.",
                                        "A bola é redonda.", "É o esporte mais popular do mundo.", "O objetivo é fazer gols.",
                                        "Tem impedimento.", "É jogado em campo de grama.", "Tem goleiro.",
                                        "Cristiano Ronaldo e Messi são estrelas desse esporte."]},
    "🏀": {"nome": "Basquete", "dicas": ["Cada cesta vale de 1 a 3 pontos.", "É jogado com as mãos.", "Michael Jordan é um ícone.",
                                         "Tem dribles e enterradas.", "A bola é laranja.", "A quadra é coberta.",
                                         "5 jogadores por time em quadra.", "A NBA é o principal campeonato.",
                                         "Tem tempo limitado por posse.", "Existe o arremesso de 3 pontos."]},
    "🎾": {"nome": "Tenis", "dicas": ["A bola deve quicar no campo adversário.", "É jogado com raquete.", "Pode ser individual ou em duplas.",
                                      "Tem game, set e match.", "Wimbledon é um torneio famoso.", "Roger Federer é um nome forte no esporte.",
                                      "O campo pode ser de saibro, grama ou duro.", "Tem vantagem e igualdade.",
                                      "É silencioso durante os pontos.", "A bola é pequena e amarela."]},
    "🏐": {"nome": "Volei", "dicas": ["Cada time tem 6 jogadores em quadra.", "É jogado com as mãos.", "Tem saque, bloqueio e cortada.",
                                      "A bola não pode tocar o chão.", "O Brasil é referência mundial.",
                                      "Existe o líbero, que usa uniforme diferente.", "É disputado em sets.",
                                      "Pode ser jogado na praia também.", "Tem rotação entre jogadores.",
                                      "A rede separa os dois lados."]},
    "🏈": {"nome": "Futebol Americano", "dicas": ["A bola tem formato oval.", "Cada jogada é tática.", "Tem touchdown e field goal.",
                                                 "É muito popular nos EUA.", "Os jogadores usam capacetes.",
                                                 "O Super Bowl é a final mais famosa.", "Tem posições como quarterback e linebacker.",
                                                 "Avanço por jardas.", "É um esporte de contato.", "Tem 4 quartos no jogo."]},
    "⚾": {"nome": "Beisebol", "dicas": ["É muito popular no Japão e nos EUA.", "Tem bastão e luvas.", "O jogador corre por bases.",
                                         "Tem home run.", "O arremessador é o pitcher.", "O receptor é o catcher.",
                                         "Jogo com 9 entradas.", "A bola é branca com costura vermelha.",
                                         "Time que marca mais corridas vence.", "Tem rebatedores."]},
    "🥊": {"nome": "Boxe", "dicas": ["É um esporte de combate.", "Os atletas usam luvas.", "Tem categorias por peso.",
                                     "Muhammad Ali é uma lenda.", "Tem rounds e juízes.",
                                     "Não pode golpear abaixo da linha de cintura.", "É praticado no ringue.",
                                     "Objetivo é nocautear ou pontuar mais.", "Tem contagem de 10 no nocaute.",
                                     "Cada round dura 3 minutos."]},
    "🏓": {"nome": "Tenis de Mesa", "dicas": ["Também é chamado de ping pong.", "Jogado com raquetes pequenas.",
                                             "A mesa tem rede no meio.", "A bola é leve e pequena.", "Popular na China.",
                                             "Os pontos vão até 11.", "Pode ser jogado em duplas.", "É muito rápido.",
                                             "A bola deve quicar dos dois lados.", "A mesa é verde ou azul."]},
    "🏸": {"nome": "Badminton", "dicas": ["Usa peteca (volante).", "As raquetes são finas e leves.",
                                         "Pode ser individual ou em duplas.", "É jogado em quadra coberta.",
                                         "É o esporte de raquete mais rápido do mundo.", "Tem saque e rally.",
                                         "Popular na Ásia.", "O objetivo é cair no lado adversário.",
                                         "A pontuação vai até 21.", "A rede é mais baixa que a do vôlei."]},
    "⛳": {"nome": "Golfe", "dicas": ["O objetivo é colocar a bola no buraco.", "Usa tacos.", "É jogado em campo aberto.",
                                     "Tem 18 buracos por padrão.", "Tiger Woods é um ícone do esporte.",
                                     "É jogado com calma e precisão.", "Cada buraco tem par específico.",
                                     "A bola é pequena e branca.", "Pode demorar horas uma partida.",
                                     "O menor número de tacadas vence."]},
    "🤽": {"nome": "Polo Aquatico", "dicas": ["É jogado dentro da piscina.", "Cada time tem 7 jogadores.",
                                             "O objetivo é marcar gols.", "Exige muita resistência.",
                                             "A bola é arremessada com a mão.", "Tem goleiro.",
                                             "Não pode encostar no fundo da piscina.", "Tem exclusões temporárias.",
                                             "A bola é amarela.", "É um esporte olímpico."]},
    "🥋": {"nome": "Judo", "dicas": ["É um esporte de origem japonesa.", "Usa kimono.", "Tem faixas de graduação.",
                                     "Tem projeções e imobilizações.", "É disputado no tatame.",
                                     "O objetivo é derrubar ou imobilizar.", "Tem pontuação como ippon e waza-ari.",
                                     "Respeito é fundamental.", "É muito praticado no Brasil.",
                                     "Foi criado por Jigoro Kano."]}
}
## cria um tabuleiro, torna os emojis uma lista c/ os esportes da sessão acima 
def criar_tabuleiro():
    emojis = list(esportes.keys())
    random.shuffle(emojis)
    return [emojis[i:i + 4] for i in range(0, len(emojis), 4)]
## funcao pra salvar o raking sempre que o jogo for finalizado, abrindo o arquivo ranking.txt
def salvar_ranking(nome, pontos, duracao, resultado):
    with open("ranking.txt", "a", encoding="utf-8") as arq:
        arq.write(f"{nome} - {pontos} eliminações - {duracao:.2f} segundos - {resultado}\n")

def mostrar_top10():
    try:
        with open("ranking.txt", "r", encoding="utf-8") as arq:
            linhas = arq.readlines() # le todas as linhas do arquivo

        dados = [] # lista pra guardar os dados do ranking
        for linha in linhas: #  percorre por cada linha do arquivo
            partes = linha.strip().split(" - ") # separa a linha em partes, usando o " - " como delimitador
            if len(partes) >= 4: #  verifica se a linha tem pelo menos 4 partes
                try:
                    pontos = int(partes[1].split()[0])
                    tempo = float(partes[2].split()[0])
                    dados.append((pontos, tempo, linha.strip()))
                except ValueError:
                    continue

        # ordenamos por pontuação (decrescente) e tempo (crescente)
        dados.sort(key=lambda x: (-x[0], x[1]))

        # selecionamos apenas os 10 primeiros
        top10 = dados[:10]
        if top10:
            texto = "\n".join([f"{i+1}. {item[2]}" for i, item in enumerate(top10)])
        else:
            texto = "Ainda não há registros no ranking."

    except FileNotFoundError:
        texto = "Ainda não há ranking registrado."

    messagebox.showinfo("🏆 Top 10 Ranking", texto)

# vamos usar o self para guardar as informacoes, cada atributo da classe vai ser um atributo do objeto, e vamos usar o self pra acessar
class JogoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Cara a Cara dos esportes - Elimine 11 e vença! 🏆")
        
        mostrar_top10()
        # perguntamos o nome
        # simple dialog vai pedir informacoes pro usuario, com uma caixa de dialogo q tem campo de texto
        self.nome = simpledialog.askstring("Nome", "Digite seu nome:", parent=self.root)
        if not self.nome:
            self.root.destroy();  return

        # estados iniciais do jogo
        self.tab_jog = criar_tabuleiro()
        self.tab_mac = criar_tabuleiro()
        self.revel_jog = [[True]*4 for _ in self.tab_jog]
        self.revel_mac = [[True]*4 for _ in self.tab_mac]
        self.emoji_secreto_mac = random.choice([e for linha in self.tab_jog for e in linha])
        self.emoji_secreto_jog = random.choice([e for linha in self.tab_mac for e in linha])
        self.pontos_jog = 0
        self.pontos_mac = 0
        self.inicio = time.time()

        # interface 
        self._construir_layout()
        self._atualizar_painel_pontos()

    # layout 
    def _construir_layout(self):
        topo = tk.Frame(self.root); topo.pack(pady=8)

        self.lbl_pontos = tk.Label(topo, font=("Helvetica", 12, "bold"))
        self.lbl_pontos.pack()

        quadros = tk.Frame(self.root); quadros.pack()

        self.frm_jogador = tk.LabelFrame(quadros, text=f"Seu Tabuleiro ({self.nome})")
        self.frm_maquina = tk.LabelFrame(quadros, text="Tabuleiro da Máquina")
        self.frm_jogador.grid(row=0, column=0, padx=10, pady=10)
        self.frm_maquina.grid(row=0, column=1, padx=10, pady=10)

        self.btns_jog = []   # botões do jogador (apenas exibição)
        self.btns_mac = []   # botões que o jogador pode clicar
        for i, linha in enumerate(self.tab_jog):
            fila_btns_jog, fila_btns_mac = [], []
            for j, emoji in enumerate(linha):
                # aqui pro jogador
                b = tk.Button(self.frm_jogador, text=emoji, width=4, height=2, # define o tamanho do botão (não do emoji em si), basicamente a área clicável
                              font=("Segoe UI Emoji", 20), state="disabled") # esse sim define o tamanho do emoji, a font 
                b.grid(row=i, column=j, padx=2, pady=2)
                fila_btns_jog.append(b)
                # aqui pra maquina
                b2 = tk.Button(self.frm_maquina, text="❓", width=4, height=2,
                               font=("Segoe UI Emoji", 20),
                               command=lambda r=i, c=j: self._click_maquina(r, c))
                b2.grid(row=i, column=j, padx=2, pady=2)
                fila_btns_mac.append(b2)
            self.btns_jog.append(fila_btns_jog)
            self.btns_mac.append(fila_btns_mac)

    # geral, movimentos do jogador e da máquina
    def _click_maquina(self, r, c):
        if not self.revel_mac[r][c]:    # caso já eliminado
            return

        emoji = self.tab_mac[r][c]
        dica = random.choice(esportes[emoji]["dicas"]) # puxo uma dica aleatoria do emoji clicado, com random, buscando no dicionario pela chave emoji
        resposta = simpledialog.askstring("Dica", f"{dica}\n\nQual é o esporte?") # questiono qual o esporte (utilizando o simpledialog)

        if resposta and resposta.strip().upper() == esportes[emoji]["nome"].upper(): ## igualamos a resposta do usuario com o nome do emoji, ignorando maiusculas e minusculas e também os espaços com strip
            self.revel_mac[r][c] = False
            self.btns_mac[r][c]["text"] = "❌" ## mudamos o texto do botão pra ❌
            self.btns_mac[r][c]["state"] = "disabled" ## desabilitamos o botão pós clique
            self.pontos_jog += 1 ## jogador ganha um ponto
            messagebox.showinfo("Correto", f"Você eliminou {emoji}!") ## mostramos uma janela c mensagem de sucesso e o emoji eliminado
        else:
            messagebox.showwarning("Errado", "Resposta incorreta.")

        self._maquina_joga()
        self._atualizar_painel_pontos()
        self._verificar_fim()

    def _maquina_joga(self):
     messagebox.showinfo("Vez da Máquina", "Agora a máquina vai jogar, clique em OK para continuar…")

     CHANCE_DE_ACERTO = 0.3 # defini 30% de chance da maquina acertar apenas

    # opções disponíveis (peças ainda não eliminadas)
     opcoes = [(i, j) for i in range(len(self.tab_jog))
              for j in range(4) if self.revel_jog[i][j]]
     if not opcoes:
        return

     i, j = random.choice(opcoes)
     emoji = self.tab_jog[i][j]
     acertou = random.random() < CHANCE_DE_ACERTO

     if acertou:
        self.revel_jog[i][j] = False
        self.btns_jog[i][j]["text"] = "❌"
        self.pontos_mac += 1

        if emoji == self.emoji_secreto_mac:
            msg = "A máquina tentou adivinhar e acertou seu esporte secreto!"
        else:
            msg = f"A máquina acertou e eliminou a peça em {chr(j+65)}{i+1}."
     else:
        if emoji == self.emoji_secreto_mac:
            msg = "A máquina tentou adivinhar seu esporte secreto, mas errou."
        else:
            msg = f"A máquina tentou eliminar a peça em {chr(j+65)}{i+1}, mas errou o palpite."

     messagebox.showinfo("Máquina", msg)

    # painel dos pontos e verificação de fim de jogo 
    def _atualizar_painel_pontos(self):
        self.lbl_pontos.config(
            text=f"{self.nome}: {self.pontos_jog} eliminações   |   Máquina: {self.pontos_mac} eliminações"
        )

    def _verificar_fim(self):
        rest_jog = sum(row.count(True) for row in self.revel_jog)
        rest_mac = sum(row.count(True) for row in self.revel_mac)
        if rest_jog == 1 or rest_mac == 1:
            fim = time.time()
            resultado = "Vitória" if self.pontos_jog > self.pontos_mac else "Derrota"
            salvar_ranking(self.nome, self.pontos_jog, fim - self.inicio, resultado)
            messagebox.showinfo("Fim de Jogo",
                                f"Resultado: {resultado}\n\n{self.nome}: {self.pontos_jog} eliminações\n"
                                f"Máquina: {self.pontos_mac} eliminações")
            self.root.destroy()

# executa o jogo
if __name__ == "__main__":
    tk.Tk().report_callback_exception = lambda *args: print("Erro:", args)  
    root = tk.Tk()
    game = JogoGUI(root)
    root.mainloop()
