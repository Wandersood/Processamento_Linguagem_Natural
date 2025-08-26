i = 0

while i<20:
	print(i)
	i +=1

	if i==10:
		i =11
		continue
	if i==18:
		break
else:
	print("Fim do laco while")

print("Executa essa linha")
print("fim do programa")

print("Inicio FOR")
for a in range(0,20,1):
	print(a)
print("fim do programa FOR")
