arquivo = open ("C:\\Users\\wrs_w\\OneDrive\\Desktop\\FATEC\\PROCESSAMENTO DE LINGUAGEM NATURAL - ISW037\\AULAS\\AULA04\\arquivo.txt", "w", encoding="utf-8")

#for i in range(10):
	#letra = arquivo.read(1)
	#print (letra)
arquivo.write("Olá, tudo bem?\n")
arquivo.write("Estou escrevendo no arquivo.\n")
arquivo.write("Até mais!\n")
arquivo.close()

