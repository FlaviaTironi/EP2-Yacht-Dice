import random

def rolar_dados(n):
    lista = []
    i = 0
    while i < n:
        numero = random.randint(1,6)
        lista.append(numero)
        i += 1
    return lista

def guardar_dado(dados_rolados,dados_no_estoque,dado_para_guardar):
    lista_final = []
    
    
    lista_final.append(dados_no_estoque)
    lista_final.append(dados_rolados)
    
    return lista_final