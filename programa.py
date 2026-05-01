from funcoes import *

cartela = {'regra_simples': {1:-1,2:-1,3:-1,4:-1,5:-1,6:-1},'regra_avancada': {'sem_combinacao':-1,'quadra':-1,'full_house':-1, 'sequencia_baixa':-1, 'sequencia_alta':-1,'cinco_iguais':-1 }}

imprime_cartela(cartela)

rodada = 0
combs = ['1','2','3','4','5','6','cinco_iguais','full_house','quadra','sem_combinacao','sequencia_alta','sequencia_baixa']

while rodada < 12:
    rolados = rolar_dados(5)
    guardados = []
    rerrolagens = 0
    jogada = False

    print("Dados rolados:", rolados)
    print("Dados guardados:", guardados)
    print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

    while not jogada:
        acao = input()

        if acao == "1":
            print("Digite o índice do dado a ser guardado (0 a 4):")
            i = int(input())
            guardar = guardar_dado(rolados, guardados, i)
            rolados = guardar[0]
            guardados = guardar[1]

            print(f"Dados rolados: {rolados}")
            print(f"Dados guardados: {guardados}")
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

        elif acao == "2":
            print("Digite o índice do dado a ser removido (0 a 4):")
            indice = int(input())
            remover = remover_dado(rolados, guardados, indice)
            rolados = remover[0]
            guardados = remover[1]

            print(f"Dados rolados: {rolados}")
            print(f"Dados guardados: {guardados}")
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

        elif acao == "3":
            if rerrolagens < 2:
                rolados = rolar_dados(len(rolados))
                rerrolagens += 1

            elif rerrolagens>=2:
                print("Você já usou todas as rerrolagens.")
            
            print(f"Dados rolados: {rolados}")
            print(f"Dados guardados: {guardados}")
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

        elif acao == "4":
            imprime_cartela(cartela)

            print(f"Dados rolados: {rolados}")
            print(f"Dados guardados: {guardados}")
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

        elif acao == "0":
            print("Digite a combinação desejada:")
            comb = False

            while not comb:
                categoria = input()
                               
                if categoria in combs:
                    if categoria in cartela["regra_avancada"]:
                        utilizada = cartela["regra_avancada"][categoria] !=-1

                    else:
                        utilizada = cartela["regra_simples"][int(categoria)] != -1

                    if utilizada:
                        print("Essa combinação já foi utilizada.")

                    else:
                        faz_jogada(rolados + guardados, categoria, cartela)
                        jogada = True
                        comb = True
                
                else:
                    print("Combinação inválida. Tente novamente.")
            
            
        else:
            print("Opção inválida. Tente novamente.")
            
    rodada += 1

soma = 0
soma_simples = 0

for pontos in cartela['regra_simples'].values():
    if pontos >= 0:
        soma_simples += pontos
        soma += pontos

for pontos in cartela['regra_avancada'].values():
    if pontos >= 0:
        soma += pontos

if soma_simples >= 63:
    soma += 35

imprime_cartela(cartela)
print(f"Pontuação total: {soma}")                              