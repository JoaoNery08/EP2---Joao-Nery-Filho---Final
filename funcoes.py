#Exercício 1
import random

def rolar_dados(quantidade):
 
    return [random.randint(1, 6) for _ in range(quantidade)]

#Exercício 2
def guardar_dado(dados_rolados, dados_no_estoque, indice):

    if 0 <= indice < len(dados_rolados):
        dado = dados_rolados[indice]
        nova_lista_rolados = dados_rolados[:indice] + dados_rolados[indice+1:]
        nova_lista_estoque = dados_no_estoque + [dado]
        return [nova_lista_rolados, nova_lista_estoque]
    
    else:
        return [dados_rolados, dados_no_estoque]



