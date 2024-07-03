#Exercícios propostos pelo curso Fundamentos de Linguagem Python Para Análise de Dados e Data Science pela Data Science Academy
#Exercícios Cap04

# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.
lista_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista_1)

# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela
lista_2 = ['martelo', 'ventilador', 'garrafa', 'computador', 'tesoura']
print(lista_2)

# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string
texto_1 = "A resposta para a vida, o universo e tudo o mais"
texto_2 = " é 42!"
texto_3 = texto_1 + texto_2
print(texto_3)

# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do 
# objeto tupla para verificar quantas vezes o número 4 aparece na tupla
lista_4 = (1, 2, 2, 3, 4, 4, 4, 5)
type(lista_4) #Usei a função para ter a certeza que tinha criado uma tupla
lista_4.count(4)

# Exercício 5 - Crie um dicionário vazio e imprima na tela
dicionario_vazio = {}
type(dicionario_vazio) #De novo usei a função type só para ter certeza
print(dicionario_vazio)


# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela
dicionario_1 = {"Lucas": 27, "Mario": 30, "Mariazinha": 55}
print(dicionario_1)

# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela

dicionario_1["Cleber"] = 54
print(dicionario_1)

# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. 
# Um dos valores deve ser uma lista de 2 elementos numéricos. 
# Imprima o dicionário na tela.

dicionario_2 = {"Parafuso": "0014", "Chave de fenda": "0011", "Martelo": ["1142", "8457"]}
print(dicionario_2)

# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, 
# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e 
# o quarto elemento um valor do tipo float.
# Imprima a lista.

elementos = ["Carro", ("rodas", 4), {"X-tudo": 15, "Hotdog": 10}, 12.5]
print(elementos)

# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
frase = 'Cientista de Dados é o profissional mais sexy do século XXI'

frase_cortada = frase[0:18]
print(frase_cortada)
