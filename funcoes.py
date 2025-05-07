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


