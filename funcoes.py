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

def remover_dado(lista_rolados,lista_guardados,n):
    final = []
    estoque_final = []
    rolados_final =[]

    i =0
    for y in lista_guardados:
        rolados_final.append(y)
        
    for x in lista_guardados:
        if i == n:
            rolados_final.append(x)
        else:
            estoque_final.append(x)
    
    final.append(rolados_final)
    final.append(estoque_final)
    return final