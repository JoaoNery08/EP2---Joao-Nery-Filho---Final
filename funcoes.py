#Exercício 1
import random

def rolar_dados(quantidade):
 
    return [random.randint(1, 6) for _ in range(quantidade)]

#Exercício 2

def guardar_dado(dados_rolados, dados_no_estoque, indice):

    if 0 <= indice < len(dados_rolados):
        dado = dados_rolados.pop(indice) #para retornar ou remover um indice específico de uma lista, nesse caso o que se recebe da função
        dados_no_estoque.append(dado)
    return [dados_rolados, dados_no_estoque]

#Exercício 3

def remover_dado(dados_rolados, dados_no_estoque, indice):

    if 0 <= indice < len(dados_no_estoque):
        dado = dados_no_estoque.pop(indice)
        dados_rolados.append(dado)
    return [dados_rolados, dados_no_estoque]

#Exercício 4
def calcula_pontos_regra_simples(dados):
    pontos = {i: 0 for i in range(1, 7)}  # Inicia o dicionário com 0 para cada face

    for dado in dados:
        if 1 <= dado <= 6:
            pontos[dado] += dado

    return pontos

#Exercício 5 

def calcula_pontos_soma(dados):
    total = 0

    for dado in dados:
        total += dado
    return total

#Exercício 6 
def calcula_pontos_sequencia_baixa(dados):
    #Filtra os dados para garantir que temos apenas números de 1 a 6
    dados = [dado for dado in dados if 1 <= dado <= 6]

    #Verifica se tem pelo menos 4 elementos
    if len(dados) < 4:
        return 0

    #Verifica todas as combinações de 4 dados consecutivos
    for i in range(len(dados) - 3):

        #Ordena os dados
        sequencia = sorted(dados[i:i+4])

        #Verifica se a sequência de 4 dados é consecutiva
        if sequencia[0] + 1 == sequencia[1] and sequencia[1] + 1 == sequencia[2] and sequencia[2] + 1 == sequencia[3]:
            return 15

    return 0
