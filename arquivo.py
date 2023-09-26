#vamos ler nome e telefone
#salvar em um arquivo
#salvar nome e telefone na mesma linha do arquivo
#criar uma lista de contato


# escrita de dois dados na mesma linha

#exercicio-contatos

contatos=open("AULA9-arquivo\\contatos.txt","a")
while True:
    nome=input("Digite o nome: ")
    if nome=="":
        break
    telefone=input("Digite o telefone: ")
    contatos.write("%s,%s\n" %(nome,telefone))
    
contatos.close()

#exercicio-ler contatos

arquivo = open("AULA9-arquivo\\contatos.txt","r")

for x in arquivo.readlines():
    lista=x.split(",")
    print(lista[0])
arquivo.close()

# readlines() retorna uma lista em que cada uma das linhas ocupa uma posicao/indice

#ex:

contato = open("AULA9-arquivo\\contatos.txt","r")
conteudo_arquivo = contato.readlines()
print(conteudo_arquivo) 

#exercicio multiplos de 4

arquivop = open("AULA9-arquivo\\pares.txt", "r")
multiplo = open("AULA9-arquivo\\multiplos4.txt", "w")

for x in arquivop.readlines():
    if int(x) % 4 == 0:
        multiplo.write("%s\n" % x)  # %s (s=string)

arquivop.close()
multiplo.close()

#exercicio- inverter ordem das linhas

par = open("AULA9-arquivo\\pares.txt", "r")
invertido = open("AULA9-arquivo\\invertido.txt", "w")
lista = par.readlines()
ultimo = len(lista) - 1

while ultimo >= 0:
    invertido.write("%s" % lista[ultimo])
    ultimo = ultimo - 1

invertido.close()
par.close()

#exercicio-somar

def somaArquivo():
    arquivo = open("AULA9-arquivo\\numeros2.txt", "r")
    lista = arquivo.readlines()
    numeros = lista[0].split(" ")  # " " é o caracter que vai separar os elementos da lista

    soma = 0
    for x in numeros:
        if x != "":
            soma = soma + int(x)
    return soma

print(somaArquivo())

#exercicio- ler,receber e retornar

def fazlista():
    arquivo = open("AULA9-arquivo\\numeros3.txt", "r")
    lista = []
    for x in arquivo.readlines():
        lista.append(x)
    return lista


def unicos(numeros):
    lista_unicos = []
    for x in numeros:
        if x not in lista_unicos:
            lista_unicos.append(x)
    return lista_unicos

numeros = fazlista()
print(unicos(numeros))

#exercicio par e impar

#gera ate 999 mas salva no txt dependendo se é par ou impar
par=open("AULA9-arquivo\\pares.txt","w")
impar=open("AULA9-arquivo\\impares","w")

for x in range(1000):
    if x%2 ==0:
        par.write("%s\n" %x) #salva no arquivo par se pertencer a condicao if
    else:
        impar.write("%s\n" %x)
par.close()
impar.close()

