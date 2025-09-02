import nltk
from nltk import tokenize
from nltk.corpus import stopwords # Importa o módulo de stopwords
from typing import Dict, List
import os

# --- INICIALIZAÇÃO DO NLTK ---
# Este bloco diz ao NLTK para procurar os dados na pasta local 'dados_nltk'.
# Garante que o script funcione corretamente após executar 'download_dados.py'.
PASTA_DADOS_NLTK = 'dados_nltk'
if os.path.exists(PASTA_DADOS_NLTK):
	nltk.data.path.append(PASTA_DADOS_NLTK)
else:
	print(f"Aviso: A pasta de dados '{PASTA_DADOS_NLTK}' não foi encontrada.")
	print("Execute o script 'download_dados.py' primeiro.")
	exit()
# ------------------------------------------------------------------------------------

# 1. CARREGAR O LÉXICO DE SENTIMENTOS
dicionario_lexico: Dict[str, int] = {}
caminho_lexico = "C:\\Users\\wrs_w\\OneDrive\\Desktop\\FATEC\\PROCESSAMENTO DE LINGUAGEM NATURAL - ISW037\\AULAS\\AULA04\\lexico_v3.0.txt"

with open(caminho_lexico, "r", encoding="utf-8") as arquivo:
	for linha in arquivo:
		campos = linha.strip().split(",")
		if len(campos) >= 3:
			chave = campos[0]
			try:
				valor = int(campos[2])
				dicionario_lexico[chave] = valor
			except ValueError:
				pass

# 2. PREPARAR O TEXTO E CALCULAR MÉTRICAS
texto_escolhido = '''Não se esqueça da oração. Cada vez que você orar, se sua oração for sincera, haverá um novo sentimento e um novo significado nela, o que lhe dará nova coragem.'''

texto_CB = texto_escolhido.lower()
tokens = tokenize.word_tokenize(texto_CB, language='portuguese')

print("\nTexto a ser analisado:", texto_escolhido)
print("Tokens gerados:", tokens)

# Métricas de Riqueza Lexical
tamanho_texto = len(tokens)
vocabulario_geral = set(tokens) # Usar 'set' é mais eficiente para obter itens únicos
tamanho_vocabulario = len(vocabulario_geral)
if tamanho_texto > 0:
	riqueza = tamanho_vocabulario / tamanho_texto
	print(f"Riqueza do vocabulário: {riqueza:.2f} ({tamanho_vocabulario} palavras únicas em {tamanho_texto} tokens totais)")

# 3. REMOVER STOPWORDS
# Carrega a lista de stopwords padrão do NLTK para o português
lista_stopwords_nltk = stopwords.words('portuguese')

# Adiciona pontuações à lista de stopwords para uma limpeza mais completa
pontuacoes = ['.', ',', '!', '?', ';', ':']
stopwords_completas = set(lista_stopwords_nltk + pontuacoes)

# Remove a palavra 'não' da lista para não inverter o sentimento
stopwords_completas.remove('não')

# Cria a lista de tokens limpos (sem stopwords)
tokens_limpos: List[str] = []
for token in tokens:
	# A lógica correta: checa se o token atual não está na lista de stopwords
	if token not in stopwords_completas:
		tokens_limpos.append(token) # Adiciona o token correto

print(f"\nVocabulário sem stopwords: {tokens_limpos}")

# 4. REALIZAR A ANÁLISE DE SENTIMENTO
pontuacao = 0
palavras_encontradas = []

# Agora o loop percorre a lista de tokens limpos
for token in tokens_limpos:
	if token in dicionario_lexico:
		valor_sentimento = dicionario_lexico[token]
		palavras_encontradas.append(f"{token} ({valor_sentimento})")
		pontuacao += valor_sentimento

# 5. EXIBIR E GRAVAR O RESULTADO
print("\n--- Análise de Sentimento ---")
print("Palavras com sentimento encontradas no texto:", ", ".join(palavras_encontradas))
print(f"PONTUAÇÃO FINAL DO TEXTO: {pontuacao}")

caminho_saida = "C:\\Users\\wrs_w\\OneDrive\\Desktop\\FATEC\\PROCESSAMENTO DE LINGUAGEM NATURAL - ISW037\\AULAS\\AULA04\\ex01.txt"
with open(caminho_saida, "w", encoding="utf-8") as gravacao:
	gravacao.write("--- Análise de Sentimento ---\n")
	gravacao.write(f"Texto Analisado: {texto_escolhido}\n")
	gravacao.write(f"Tokens Limpos: {', '.join(tokens_limpos)}\n")
	gravacao.write(f"Palavras com sentimento encontradas: {', '.join(palavras_encontradas)}\n")
	gravacao.write(f"Pontuação Final: {pontuacao}\n")

print(f"\nResultado da análise foi salvo no arquivo '{caminho_saida}'.")
