#le o gabarito
arquivo_gabarito = open("respostas.txt", "r")
linha_gabarito = arquivo_gabarito.readline().strip()
arquivo_gabarito.close()

gabarito = linha_gabarito.split(",")

#le os candidatos
arquivo_candidatos = open("candidatos.txt", "r")
linhas_candidatos = arquivo_candidatos.readlines()
arquivo_candidatos.close()

ids = []
nomes = []
respostas_todos = []

#separa as informacoes dos candidatos nas listas
for linha in linhas_candidatos:
    linha = linha.strip()
    partes = linha.split(",")
    ids.append(partes[0])
    nomes.append(partes[1])
    respostas = partes[2:]       
    respostas_todos.append(respostas)


notas = []

#analisa as respostas e acertos
for i in range(len(nomes)):
    acertos = 0
    respostas = respostas_todos[i]


    for j in range(len(gabarito)):
        if j < len(respostas):
            if respostas[j] == gabarito[j]:
                acertos = acertos + 1

    notas.append(acertos)


#faz o arquivo com a classificacao 
arquivo_saida = open("classificacao.txt", "w")

for i in range(len(nomes)):
    linha = ids[i] + "," + nomes[i] + "," + str(notas[i]) + "\n"
    arquivo_saida.write(linha)

arquivo_saida.close()

print("Arquivo classificacao.txt gerado com sucesso!")