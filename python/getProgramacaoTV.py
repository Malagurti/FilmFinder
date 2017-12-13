import urllib


f = urllib.urlopen("https://meuguia.tv/programacao/categoria/Filmes")
conteudo = f.read()

count = 0
indiceProcura = 0

while True:
	count = count + 1
	
	idx = conteudo.find("<a title=", indiceProcura)
	
	idx2 = conteudo.find("href=", idx)
	
	
	print conteudo[idx+10:idx2-2]
	
	idx3 = conteudo.find(">", idx2)
	print conteudo[idx2+6:idx3-1]
	
	
	indiceProcura = idx3
	
	if count == 5:
		break

