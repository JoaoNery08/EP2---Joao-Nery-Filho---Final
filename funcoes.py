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

    #Se a lista de dados não tiver pelo menos 4 elementos, retorna 0
    if len(dados) < 4:
        return 0

    #Verifica todas as combinações possíveis de 4 dados consecutivos
    for i in range(len(dados)):
        for j in range(i + 1, len(dados)):
            for k in range(j + 1, len(dados)):
                for l in range(k + 1, len(dados)):
                    sequencia = [dados[i], dados[j], dados[k], dados[l]]
                    sequencia.sort()  # Ordena para garantir que a sequência seja crescente
                    if sequencia[0] + 1 == sequencia[1] and sequencia[1] + 1 == sequencia[2] and sequencia[2] + 1 == sequencia[3]:
                        return 15

    return 0

#Exercício 7 
def calcula_pontos_sequencia_alta(dados):

    #Conta quantas vezes aparece cada número de 1 a 6
    tem_1 = 0
    tem_2 = 0
    tem_3 = 0
    tem_4 = 0
    tem_5 = 0
    tem_6 = 0

    for dado in dados:
        if dado == 1:
            tem_1 = 1
        elif dado == 2:
            tem_2 = 1
        elif dado == 3:
            tem_3 = 1
        elif dado == 4:
            tem_4 = 1
        elif dado == 5:
            tem_5 = 1
        elif dado == 6:
            tem_6 = 1

    # Verifica se temos 1-2-3-4-5 ou 2-3-4-5-6
    if tem_1 and tem_2 and tem_3 and tem_4 and tem_5:
        return 30
    elif tem_2 and tem_3 and tem_4 and tem_5 and tem_6:
        return 30
    else:
        return 0
    
#Exercício 8 
def calcula_pontos_full_house(dados):

    cont_1 = 0
    cont_2 = 0
    cont_3 = 0
    cont_4 = 0
    cont_5 = 0
    cont_6 = 0

    for valor in dados:
        if valor == 1:
            cont_1 += 1
        elif valor == 2:
            cont_2 += 1
        elif valor == 3:
            cont_3 += 1
        elif valor == 4:
            cont_4 += 1
        elif valor == 5:
            cont_5 += 1
        elif valor == 6:
            cont_6 += 1

    #Verifica se tem um trio (3 iguais) e um par (2 iguais)
    encontrou_trio = False
    encontrou_par = False

    #Verifica todas as contagens
    contadores = [cont_1, cont_2, cont_3, cont_4, cont_5, cont_6]

    for cont in contadores:
        if cont == 3:
            encontrou_trio = True
        elif cont == 2:
            encontrou_par = True

    if encontrou_trio and encontrou_par:
        soma = 0
        for valor in dados:
            soma += valor
        return soma
    else:
        return 0
    
#Exercício 9
def calcula_pontos_quadra(dados):

    cont_1 = 0
    cont_2 = 0
    cont_3 = 0
    cont_4 = 0
    cont_5 = 0
    cont_6 = 0

    for valor in dados:
        if valor == 1:
            cont_1 += 1
        elif valor == 2:
            cont_2 += 1
        elif valor == 3:
            cont_3 += 1
        elif valor == 4:
            cont_4 += 1
        elif valor == 5:
            cont_5 += 1
        elif valor == 6:
            cont_6 += 1

    #Verifica se algum número apareceu 4 ou mais vezes
    if (cont_1 >= 4 or cont_2 >= 4 or cont_3 >= 4 or
        cont_4 >= 4 or cont_5 >= 4 or cont_6 >= 4):
        
        soma = 0
        for valor in dados:
            soma += valor
        return soma
    else:
        return 0
    
#Exercício 10
def calcula_pontos_quina(dados):
    
    cont_1 = 0
    cont_2 = 0
    cont_3 = 0
    cont_4 = 0
    cont_5 = 0
    cont_6 = 0

    for valor in dados:
        if valor == 1:
            cont_1 += 1
        elif valor == 2:
            cont_2 += 1
        elif valor == 3:
            cont_3 += 1
        elif valor == 4:
            cont_4 += 1
        elif valor == 5:
            cont_5 += 1
        elif valor == 6:
            cont_6 += 1

    if (cont_1 >= 5 or cont_2 >= 5 or cont_3 >= 5 or
        cont_4 >= 5 or cont_5 >= 5 or cont_6 >= 5):
        return 50
    else:
        return 0