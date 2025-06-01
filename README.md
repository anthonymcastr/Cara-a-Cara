# 🎮 Cara a Cara dos Esportes

Um jogo interativo de adivinhação no terminal, inspirado no clássico "Cara a Cara", onde o jogador deve adivinhar esportes com base em dicas e eliminar opções em um tabuleiro. A partida é contra uma inteligência artificial simples que também tenta eliminar suas opções até restar apenas uma!

## 🧠 Como Funciona

- Um tabuleiro com emojis de esportes é gerado aleatoriamente para o jogador e para a máquina.
- Cada rodada, o jogador escolhe uma coordenada (ex: B2) para tentar eliminar um esporte do tabuleiro da máquina.
- O programa fornece uma dica e o jogador tenta adivinhar o nome do esporte.
- A máquina também tenta eliminar esportes do tabuleiro do jogador aleatoriamente.
- O jogo termina quando restar apenas uma opção visível em um dos tabuleiros.

## 🛠️ Tecnologias Utilizadas

- Python 3
- `random` para sorteios e embaralhamento de emojis
- `time` para medir a duração da partida
- Manipulação de arquivos (`ranking.txt`) para salvar resultados

## 📁 Estrutura do Projeto

- `main.py`: Código principal do jogo.
- `ranking.txt`: Arquivo de texto onde os resultados das partidas são salvos (criado automaticamente).

## 🚀 Como Executar

1. Certifique-se de ter o Python 3 instalado.
2. Clone o repositório:

```bash
git clone https://github.com/seuusuario/cara-a-cara-esportes.git
cd cara-a-cara-esportes
