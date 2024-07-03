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
