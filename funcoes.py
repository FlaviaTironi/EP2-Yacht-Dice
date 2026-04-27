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
    estoque = []
    rolados = []
    
    for x in dados_no_estoque:
        estoque.append(x)

    i = 0 
    for y in dados_rolados:
        if i == dado_para_guardar:
            estoque.append(y)
        else:
            rolados.append(y)
        i += 1
    
    lista_final.append(rolados)
    lista_final.append(estoque)
    
    return lista_final