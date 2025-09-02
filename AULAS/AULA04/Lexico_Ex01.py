import nltk
from nltk import tokenize
from typing import Dict

# --- INFORMAÇÕES IMPORTANTES ---
# A linha nltk.download() não é necessária no seu código final.
# Você só precisa executá-la UMA VEZ em um script separado para baixar os pacotes.
# Depois de baixados, os pacotes ficam salvos no seu computador.
# Exemplo de script de setup (executar só uma vez):
#
# import nltk
# nltk.download('punkt')
# ------------------------------------------------------------------------------------

# 1. CARREGAR O LÉXICO DE SENTIMENTOS
dicionario_lexico: Dict[str, int] = {}

# O uso do 'with' garante que o arquivo será fechado automaticamente no final.
with open("C:\\Users\\wrs_w\\OneDrive\\Desktop\\FATEC\\PROCESSAMENTO DE LINGUAGEM NATURAL - ISW_037\\AULAS\\AULA04\\lexico_v3.0.txt", "r", encoding="utf-8") as arquivo:
	#
	for linha in arquivo:
		campos = linha.strip().split(",")
		if len(campos) >= 3:
			chave = campos[0]
			try:
				valor = int(campos[2])
				dicionario_lexico[chave] = valor
			except ValueError:
				pass

# 2. PREPARAR O TEXTO PARA ANÁLISE
texto_escolhido = '''Não se esqueça da oração. Cada vez que você orar, se sua oração for sincera, haverá um novo sentimento e um novo significado nela, o que lhe dará nova coragem.'''

texto_CB = texto_escolhido.lower()
tokens = tokenize.word_tokenize(texto_CB, language='portuguese')

print("\nTexto a ser analisado:", texto_escolhido)
print("Tokens gerados:", tokens)

# 3. REALIZAR A ANÁLISE DE SENTIMENTO
pontuacao = 0
palavras_encontradas = []

for token in tokens:
	if token in dicionario_lexico:
		valor_sentimento = dicionario_lexico[token]
		palavras_encontradas.append(f"{token} ({valor_sentimento})")
		pontuacao += valor_sentimento

# 4. EXIBIR E GRAVAR O RESULTADO
print("\n--- Análise de Sentimento ---")
print("Palavras com sentimento encontradas no texto:", ", ".join(palavras_encontradas))
print(f"PONTUAÇÃO FINAL DO TEXTO: {pontuacao}")

with open("C:\\Users\\wrs_w\\OneDrive\\Desktop\\FATEC\\PROCESSAMENTO DE LINGUAGEM NATURAL - ISW_037\\AULAS\\AULA04\\ex01.txt", "w", encoding="utf-8") as gravacao:
	gravacao.write("--- Análise de Sentimento ---\n")
	gravacao.write(f"Texto Analisado: {texto_escolhido}\n")
	gravacao.write(f"Palavras com sentimento encontradas: {', '.join(palavras_encontradas)}\n")
	gravacao.write(f"Pontuação Final: {pontuacao}\n")

print("\nResultado da análise foi salvo no arquivo 'ex01.txt'.")

