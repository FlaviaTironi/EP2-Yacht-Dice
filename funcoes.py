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
    
    rolados = []
    for x in dados_rolados:
        if x in dados_no_estoque:
            rolados.append(x)

    dados_no_estoque.append(dados_rolados[dado_para_guardar])
    
    lista_final.append(rolados)
    lista_final.append(dados_no_estoque)
    
    return lista_final