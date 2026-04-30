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

def remover_dado(dados_rolados,dados_no_estoque,dado_para_remover):
    final = []
    dados_rolados.append(dados_no_estoque[dado_para_remover])
    del dados_no_estoque[dado_para_remover]

    final.append(dados_rolados)
    final.append(dados_no_estoque)
    return final

def calcula_pontos_regra_simples(lista):
    dic ={1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    for n in lista:
        dic[n] +=n
    return dic

def calcula_pontos_soma(lista):
    soma = 0
    for n in lista:
        soma += n
    return soma

def calcula_pontos_sequencia_baixa(lista):
    if (1 in lista and 2 in lista and 3 in lista and 4 in lista) or (2 in lista and 3 in lista and 4 in lista and 5 in lista) or (3 in lista and 4 in lista and 5 in lista and 6 in lista):
        valor = 15
    else:
        valor = 0
    return valor

def calcula_pontos_sequencia_alta(lista):
    if 1 in lista and 2 in lista and 3 in lista and 4 in lista and 5 in lista or 2 in lista and 3 in lista and 4 in lista and 5 in lista and 6 in lista:
        valor = 30
    else:
        valor = 0
    
    return valor

def calcula_pontos_full_house(dados):
    numeros = []
    primeiro = 0
    segundo = 0
    soma = 0 

    for d in dados:
        soma += d 

    for d in dados:
        if d not in numeros:
            numeros.append(d)
        
    for d in dados:
        if len(numeros) == 1:
            primeiro = 5
            segundo = 5
        else:
            if d == numeros[0]:
                primeiro += 1
            if d == numeros[1]:
                segundo += 1
        

    if (primeiro == 3 and segundo == 2) or (primeiro == 2 and segundo == 3):
        resultado = soma
    else:
        resultado = 0
    
    return resultado

def calcula_pontos_quadra(dados):
    repetições = {}
    soma = 0 

    for d in dados:
        soma += d 

    for d in dados:
        if d in repetições:
            repetições[d] += 1
        else:
            repetições[d] = 1

    quadra = False
    for valor in repetições.values():
        if valor >= 4:
            quadra = True
    
    if quadra: 
        resultado = soma
    else:
        resultado = 0
    
    return resultado 

def calcula_pontos_quina(dados):
    repetições = {}
    soma = 0

    for d in dados:
        if d in repetições:
            repetições[d] += 1
        else:
            repetições[d] = 1

    cinco = False
    for valor in repetições.values():
        if valor >= 5:
            cinco = True
    
    if cinco: 
        resultado = 50
    else:
        resultado = 0
    
    return resultado 

def calcula_pontos_regra_avancada(lista_5_num):
    dic = {'cinco_iguais': calcula_pontos_quina(lista_5_num),
    'full_house': calcula_pontos_full_house(lista_5_num),
    'quadra': calcula_pontos_quadra(lista_5_num),
    'sem_combinacao': calcula_pontos_soma(lista_5_num),
    'sequencia_alta': calcula_pontos_sequencia_alta(lista_5_num),
    'sequencia_baixa': calcula_pontos_sequencia_baixa(lista_5_num)}

    return dic

def faz_jogada(lista_dados, categoria, dic_cartela):
    regra_simples = [1, 2, 3, 4, 5, 6]

    if categoria in regra_simples or categoria in ['1','2','3','4','5','6']:
        cat_int = int(categoria)
        resultado = calcula_pontos_regra_simples(lista_dados)
        dic_cartela["regra_simples"][cat_int] = resultado[cat_int]
    else:
        resultado = calcula_pontos_regra_avancada(lista_dados)
        dic_cartela["regra_avancada"][categoria] = resultado[categoria]
    
    return dic_cartela


def imprime_cartela(cartela):
    print("Cartela de Pontos:")
    print("-"*25)    
    for i in range(1, 7):
        filler = " " * (15 - len(str(i)))
        if cartela['regra_simples'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_simples'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    for i in cartela['regra_avancada'].keys():
        filler = " " * (15 - len(str(i)))
        if cartela['regra_avancada'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_avancada'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    print("-"*25)

