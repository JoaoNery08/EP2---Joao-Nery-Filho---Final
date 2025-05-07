#Exercício 1
import random

def rolar_dados(quantidade):
 
    return [random.randint(1, 6) for _ in range(quantidade)]

#Exercício 2
def guardar_dado(dados_rolados, dados_no_estoque, indice):
    
    if 0 <= indice < len(dados_rolados):
        dado = dados_rolados.pop(indice)
        dados_no_estoque.append(dado)
    return [dados_rolados, dados_no_estoque]
