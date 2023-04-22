import random 

lista_nome_codemons_agua= ['Python','JavaScript','Portugol']
lista_nome_codemon_fogo = ['Java','C++','PHP']
lista_nome_codemon_planta = ['Go','Ruby','C']

lista_ataque_normal = ['Debugar','VsCode','Curso-6meses']
lista_ataque_especial = ['LinuxBest','Alura','CódigoSujo']
lista_buff_status = ['Buff Vida','Buff Ataque','Buff Defesa']

lista_ataque_agua = ['Chuva de Dev','Código Limpo']
lista_ataque_fogo = ['Js=Java','Sublime']
lista_ataque_planta = ['Guanabara','Chuva de Gafanhotinhos']

lista_nomes_lider_ginasio = ['Brock','Misty','Surge','Erika','Koga','Sabrina','Blaine','Giovanni']

lista_itens = []

linha = '-' * 30

#Tuplas das listas de ataques
ataque_normal_um,ataque_normal_dois,ataque_normal_tres=lista_ataque_normal
ataque_especial_um,ataque_especial_dois,ataque_especial_tres = lista_ataque_especial
buff_um,buff_dois,buff_tres = lista_buff_status

ataque_elemental_um_agua,ataque_elemental_dois_agua = lista_ataque_agua
ataque_elemental_um_fogo,ataque_elemental_dois_fogo = lista_ataque_fogo
ataque_elemental_um_planta,ataque_elemental_dois_planta = lista_ataque_planta



while True:
    dinheiro_codemon=0
    partidas_vencidas =0
    print(linha)
    criar_codemon = input('Vamos a criação de Codemon!\nDeseja criar seus codemons de maneira [A]leatória ou [C]ustomizada?!: ').lower()
    print(linha)
    
    #Criação de Pokemon aleatória!
    if criar_codemon == 'a':

        while True:

            aleatorizar_nome=random.randint(0,2)

            if aleatorizar_nome==0:
                nome_codemon_protagonista=lista_nome_codemons_agua[random.randint(0,2)]
                elemento_codemon_protagonista = 'Água'
            if aleatorizar_nome==1:
                nome_codemon_protagonista=lista_nome_codemon_fogo[random.randint(0,2)]
                elemento_codemon_protagonista = 'Fogo'
            if aleatorizar_nome==2:
                nome_codemon_protagonista=lista_nome_codemon_planta[random.randint(0,2)]
                elemento_codemon_protagonista = 'Planta'

            vida_codemon_protagonista = random.randint(700,999)
            defesa_codemon_protagonista = random.randint(300,600)
            ataque_codemon_protagonista = random.randint(200,400)
            velocidade_codemon_protagonista = random.randint(100,200)

            
            print(f'O status do seu codemon ficaram:\n{linha}\n{nome_codemon_protagonista}\nElemento: {elemento_codemon_protagonista}\nVida: {vida_codemon_protagonista}\nDefesa: {defesa_codemon_protagonista}\nAtaque: {ataque_codemon_protagonista}\nVelocidade: {velocidade_codemon_protagonista}')            
            print(linha)
            tentar_capturar = input('Deseja tentar capturar esse codemon?[S] ou [N]: ').lower().startswith('s')
            print(linha)

            if tentar_capturar is True:

                for i in range(1,4,1):

                    capturar_chance = 30

                    print('Vamos tentar Capturar!')
                    print(f'Está é sua {i} tentativa! Vc ainda tem {3-i} chances!')

                    if random.randint(0,100)>capturar_chance:
                        print(linha)
                        input('Infelizmente não foi dessa vez :/\nAperte para continuar:')
                        print(linha)
                        continue

                    else:
                        print(linha)
                        print('Parabéns vc CONSEGUIU AWESOME!')
                        break

                else:
                    print('Infelizmente vc não conseguiu capturar dessa vez!\nTente Novamente Com outro codemon!!')
                    print(linha)
                    continue
            else:

                print('Que pena que os status não estavão bons :/\nTente achar um melhor!')
                input('Clique para continuar: ')
                continue

            print(linha)
            print(f'Agora vamos ver quais são os ataques do {nome_codemon_protagonista}!')
            break

    #Criação de Codemon Customizada!
    elif criar_codemon == 'c':


        while True:

            nome_codemon_protagonista = input('Digite aqui o nome do seu codemon: ')
            print(linha)

            if nome_codemon_protagonista not in lista_nome_codemon_fogo or nome_codemon_protagonista not in lista_nome_codemons_agua or nome_codemon_protagonista not in lista_nome_codemon_planta:

                while True:

                    print('Digite aqui o elemento do seu pokemon:')
                    print(linha)

                    elemento_codemon_protagonista = int(input('[1] - Água\n[2] - Fogo\n[3] - Planta\nDigite aqui: '))

                    if elemento_codemon_protagonista == 1:
                        lista_nome_codemons_agua.append(nome_codemon_protagonista)
                        elemento_codemon_protagonista='Água'
                    elif elemento_codemon_protagonista==2:
                        lista_nome_codemon_fogo.append(nome_codemon_protagonista)
                        elemento_codemon_protagonista='Fogo'
                    elif elemento_codemon_protagonista==3:
                        lista_nome_codemon_planta.append(nome_codemon_protagonista)
                        elemento_codemon_protagonista='Planta'
                    else:
                        print('Infelizmente digitou um valor errado tente novamente!')
                        continue
                    break

            elif nome_codemon_protagonista in lista_nome_codemons_agua:

                elemento_codemon_protagonista='Água'
            
            elif nome_codemon_protagonista in lista_nome_codemon_fogo:

                elemento_codemon_protagonista = 'Fogo'
            
            elif nome_codemon_protagonista in lista_nome_codemon_planta:

                elemento_codemon_protagonista = 'Planta'

            while True:
                try:
                    print(linha)
                    vida_codemon_protagonista = int(input('Digite aqui a vida do seu codemon!'))
                    defesa_codemon_protagonista = int(input('Digite aqui a defesa do seu codemon!'))
                    ataque_codemon_protagonista = int(input('Digite aqui o ataque do seu codemon!'))
                    velocidade_codemon_protagonista = int(input('Digite aqui a velocidade do seu codemon! '))
                except:
                    print(linha)
                    print('Infelizmente você digitou algum dos valores errado!\nTente novamente!')
                    continue
                break
            
            print(linha)
            
            print(f'O status do seu codemon ficaram:\n{linha}\n{nome_codemon_protagonista}\nElemento: {elemento_codemon_protagonista}\nVida: {vida_codemon_protagonista}\nDefesa: {defesa_codemon_protagonista}\nAtaque: {ataque_codemon_protagonista}\nVelocidade: {velocidade_codemon_protagonista}')            
            capturar_codemon_customizado = input(f'{linha}\nDeseja capturar este codemon? [S] ou [N]\nDigite aqui: ').lower().startswith('s')
            print(linha)

            if capturar_codemon_customizado is True:
                print(f'Vamos ver quais são os ataques do {nome_codemon_protagonista}!')
                break
            else:
                print('Espero que o próximo codemon seja melhor!')
                continue  
    else:
        print('Infelizmente vc digitou um valor errado!\nTente Novamente!')
        continue
    
    #Ataques Codemon
    while True:

        habilidade_um_protagonista = lista_ataque_normal[random.randint(0,2)]
        habilidade_dois_protagonista = lista_ataque_especial[random.randint(0,2)]
        habilidade_tres_protagonista = lista_buff_status[random.randint(0,2)]

        if elemento_codemon_protagonista=='Água':
            habilidade_quatro_protagonista = lista_ataque_agua[random.randint(0,1)]
        if elemento_codemon_protagonista=='Fogo':
            habilidade_quatro_protagonista = lista_ataque_fogo[random.randint(0,1)]
        if elemento_codemon_protagonista=='Planta':
            habilidade_quatro_protagonista = lista_ataque_planta[random.randint(0,1)]

        print(linha)
        input('Confirme para ver as habilidades do seu Codemon!')
        print(linha)
        
        print(f'{nome_codemon_protagonista}\n{linha}\n[1] - {habilidade_um_protagonista}\n[2] - {habilidade_dois_protagonista}\n[3] - {habilidade_tres_protagonista}\n[4] - {habilidade_quatro_protagonista}')
        print(linha)

        visualizar_descricao_habilidades = input('Deseja visualizar a lista de descrição das habilidades?[S] ou [N]\nDigite aqui: ').lower().startswith('s')

        if visualizar_descricao_habilidades is True:

            while True:

                print('Digite aqui a opção que deseja realizar: ')
                print(linha)
                print('[1] - Ataques Normais\n[2] - Ataques Especiais\n[3] - Buffs Status\n[4] - Ataques Elementais\n[5] - Sair')    
                print(linha)
                opcao_descricao=input('Digite aqui a opção que deseja: ')
                print(linha)

                if opcao_descricao=='1':
                    print(f'{ataque_normal_um} = | Poder: 80 Acuracy: 100 |')
                    print(f'{ataque_normal_dois} = | Poder: 90 Acuracy: 100 |')
                    print(f'{ataque_normal_tres} = | Poder:100 Acuracy: 100 |')
                
                if opcao_descricao=='2':
                    print(f'{ataque_especial_um} = | Poder: 130 Acuracy: 90 |')
                    print(f'{ataque_especial_dois} = | Poder: 140 Acuracy: 90 |')
                    print(f'{ataque_especial_tres} = | Poder: 150 Acuracy: 90 |')
                
                if opcao_descricao =='3':
                    print(f'{buff_um} = Restaura ou Aumenta 20% da vida!')
                    print(f'{buff_dois} = Aumenta 15% do poder de ataque!')
                    print(f'{buff_tres} = Aumenta 20% da defesa!')
                
                if opcao_descricao=='4':

                    if elemento_codemon_protagonista=='Água':
                        print(f'{ataque_elemental_um_agua} = | Poder 125 Acuracy: 90 |')
                        print(f'{ataque_elemental_dois_agua} = | Poder 140 Acuracy 80 |')

                    if elemento_codemon_protagonista=='Fogo':
                        print(f'{ataque_elemental_um_agua} = | Poder 125 Acuracy 90 |')
                        print(f'{ataque_elemental_dois_agua} = | Poder 140 Acuracy 80 |')

                    if elemento_codemon_protagonista=='Planta':
                        print(f'{ataque_elemental_um_agua} = | Poder: 125 Acuracy 90 |')
                        print(f'{ataque_elemental_dois_agua} = | Poder: 140 Acuracy 80 |')
                
                if opcao_descricao=='5':
                    print('Byebye')
                    print(linha)
                    break

                print(linha)
                input('Aperte para continuar! ')
                print(linha)
        break
    
    nome_lider_ginasio = lista_nomes_lider_ginasio[random.randint(0,7)]

    #Rinha Codemon
    for i in range(1,5,1):

        vida_codemon_protagonista_restante = vida_codemon_protagonista
        ataque_codemon_protagonista_batalha = ataque_codemon_protagonista
        defesa_codemon_protagonista_batalha = defesa_codemon_protagonista

        #Criação de Codemon Inimigo
        
        aleatorizar_nome_inimigo = random.randint(0,2)

        if aleatorizar_nome_inimigo == 0:
            nome_codemon_inimigo = lista_nome_codemons_agua[random.randint(0,2)]
        if aleatorizar_nome_inimigo == 1:
            nome_codemon_inimigo = lista_nome_codemon_fogo[random.randint(0,2)]
        if aleatorizar_nome_inimigo ==2:
            nome_codemon_inimigo = lista_nome_codemon_planta[random.randint(0,2)]

        vida_codemon_inimigo = random.randint(500,600) + (i*70)
        defesa_codemon_inimigo = random.randint(200,400) + (i*50)
        ataque_codemon_inimigo = random.randint(200,300) + (i*25)
        velocidade_codemon_inimigo = random.randint(100,200) 

        habilidade_um_inimigo = lista_ataque_normal[random.randint(0,2)]
        habilidade_dois_inimigo = lista_ataque_especial[random.randint(0,2)]
        habilidade_tres_inimigo = lista_buff_status[random.randint(0,2)]

        if nome_codemon_inimigo in lista_nome_codemons_agua:
            habilidade_quatro_inimigo = lista_ataque_agua[random.randint(0,1)]
            elemento_codemon_inimigo = 'Água'
        if nome_codemon_inimigo in lista_nome_codemon_fogo:
            habilidade_quatro_inimigo = lista_ataque_fogo[random.randint(0,1)]
            elemento_codemon_inimigo = 'Fogo'
        if nome_codemon_inimigo in lista_nome_codemon_planta:
            habilidade_quatro_inimigo = lista_ataque_planta[random.randint(0,1)]
            elemento_codemon_inimigo = 'Planta'

        vida_codemon_inimigo_batalha = vida_codemon_inimigo
        ataque_codemon_inimigo_batalha = ataque_codemon_inimigo
        defesa_codemon_inimigo_batalha = defesa_codemon_inimigo


        print(linha)

        if i==4:

            print(f"A batalha Final! Controla o lider de ginásio {nome_lider_ginasio}")

        else:

            print(f'Disputa número {i}/4')

        print(f'{nome_codemon_protagonista} X {nome_codemon_inimigo}')
        print(f'{elemento_codemon_protagonista} X {elemento_codemon_inimigo}')

        #Vantagem elemental

        if elemento_codemon_inimigo==elemento_codemon_protagonista:
            vantagem_elemental='Iguais'

        elif elemento_codemon_protagonista=='Água' and elemento_codemon_inimigo=='Fogo':
            vantagem_elemental='Protagonista'
            
        elif elemento_codemon_protagonista=='Água' and elemento_codemon_inimigo=='Planta':
            vantagem_elemental='Inimigo'

        elif elemento_codemon_protagonista=='Fogo' and elemento_codemon_inimigo=='Planta':
            vantagem_elemental='Protagonista'
        
        elif elemento_codemon_inimigo=='Água' and elemento_codemon_protagonista=='Fogo':
            vantagem_elemental='Inimigo'
        
        elif elemento_codemon_inimigo=='Água' and elemento_codemon_protagonista=='Planta':
            vantagem_elemental='Protagonista'
        
        elif elemento_codemon_inimigo=='Fogo' and elemento_codemon_protagonista=='Planta':
            vantagem_elemental='Inimigo'

        if vantagem_elemental=='Protagonista':

            vida_codemon_protagonista_restante+=(vida_codemon_protagonista*10/100)
            ataque_codemon_protagonista_batalha+=(ataque_codemon_protagonista*10/100)
            defesa_codemon_protagonista+=(defesa_codemon_protagonista*10/100)

        if vantagem_elemental=='Inimigo':

            vida_codemon_inimigo_batalha+=(vida_codemon_inimigo*10/100)
            ataque_codemon_inimigo_batalha+=(ataque_codemon_inimigo*10/100)
            defesa_codemon_inimigo_batalha+=(defesa_codemon_inimigo*10/100)

        if vantagem_elemental=='Iguais':

            print('Não tem vantagem elemental! Os dois são do mesmo elemento!')

        else:

            print(f'O codemon {vantagem_elemental} recebe 10% de status a mais pela vantagem elemental!')

        print(linha)    
        input('Aperte aqui para continuar: ')

        if velocidade_codemon_protagonista>=velocidade_codemon_inimigo:
            vez_de_jogar = 1
        else:
            vez_de_jogar = 2

        while True:
            
            print(linha)
            print(f'{nome_codemon_protagonista}') 
            
            parte_vida = 0
            barra_vida = ''

            while True:

                if parte_vida<vida_codemon_protagonista_restante:
                    
                    barra_vida+='|'
                    parte_vida+=(vida_codemon_protagonista*5/100)
                else:
                    break

            print(f'Vida: {barra_vida}\n{linha}')
            print(f'[1] - {habilidade_um_protagonista}\n[2] - {habilidade_dois_protagonista}\n[3] - {habilidade_tres_protagonista}\n[4] - {habilidade_quatro_protagonista}\n[5] - Ver bolsa de itens')  
            print(linha)
    
            print(f'{nome_codemon_inimigo}')

            parte_vida = 0
            barra_vida = ''

            while True:

                if parte_vida<vida_codemon_inimigo_batalha:
                    
                    barra_vida+='|'
                    
                    parte_vida+=(vida_codemon_inimigo*5/100)
                else:
                    break
            
            print(f'Vida: {barra_vida}')

            acao_protagonista_batalha = input(f'{linha}\nDigite aqui a ação que deseja realizar: ')   

            if acao_protagonista_batalha!='1' and acao_protagonista_batalha!='2' and acao_protagonista_batalha!='3' and acao_protagonista_batalha!='4' and acao_protagonista_batalha!='5':
                
                print('Por favor digite um valor válido!')
                continue
            
            if acao_protagonista_batalha=='5':
                
                print(linha)

                contador = 1

                if len(lista_itens)==0:

                    print('Infelizmente vc não tem itens na sua bag!')
                    input('Aperte aqui para continuar: ')
                    continue

                else:

                    for i in range(0,len(lista_itens),1):

                        print(f'[{contador}] - {lista_itens[i]}')
                        contador+=1
                        i+=1

                    else:

                        print('[3] - sair da mochila de itens!')

                print(lista_itens)
                usar_item = int(input('Digite aqui o item que deseja usar: '))

                if usar_item==3:

                    print('Vai sair sem usar nada? aff')
                    continue

                elif usar_item>len(lista_itens) or usar_item<len(lista_itens):

                    print('Infelizmente essa opção não temos')
                    continue

                elif usar_item==1:
                    item_usado = lista_itens[0]
                elif usar_item==2:
                    item_usado = lista_itens[1]

                if item_usado == 'Poção pequena':

                    vida_codemon_protagonista_restante+=300
                    print('A vida do codemon curou ou aumentou 300 HP!')
                    lista_itens.remove(item_usado)

                if item_usado == 'Poção grande':

                    vida_codemon_protagonista_restante+=600
                    print('A vida do codemon aumentou ou curou 600 HP!')
                    lista_itens.remove(item_usado)

                if item_usado  == 'Aumento Ataque':

                    ataque_codemon_protagonista_batalha+=150
                    print('O ataque do codemon aumentou 150 AP!')
                    lista_itens.remove(item_usado)
                    
            for i in range(0,2,1):

                numero_testar_chance_acerto = random.randint(0,100)

                if vez_de_jogar==1:
                    
                    if acao_protagonista_batalha=='5':
                        vez_de_jogar+=1
                        continue

                    if acao_protagonista_batalha=='1':
                        poder_ataque = 80+(lista_ataque_normal.index(habilidade_um_protagonista)*10)
                        chance_de_acerto = 100
                        habilidade_usada = habilidade_um_protagonista

                    if acao_protagonista_batalha=='2':
                        poder_ataque = 130 + (lista_ataque_especial.index(habilidade_dois_protagonista)*10)
                        chance_de_acerto=90
                        habilidade_usada = habilidade_dois_protagonista
                        
                    if acao_protagonista_batalha=='3':
                        habilidade_usada = habilidade_tres_protagonista
                        
                        if habilidade_tres_protagonista==buff_um:
                            vida_codemon_protagonista_restante+=(vida_codemon_protagonista*20/100)
                            frase_de_buff = f'A sua vida aumentou ou recuperou em {vida_codemon_protagonista*20/100}!'

                        if habilidade_tres_protagonista==buff_dois:
                            ataque_codemon_protagonista_batalha+=(ataque_codemon_protagonista*15/100)
                            frase_de_buff = f'O seu ataque aumentou em {ataque_codemon_protagonista*15/100}!'

                        if habilidade_tres_protagonista==buff_tres:
                            defesa_codemon_protagonista_batalha+=(defesa_codemon_protagonista*20/100)
                            frase_de_buff = f'A sua defesa aumentou em {defesa_codemon_protagonista}!'

                    if acao_protagonista_batalha=='4':

                        #Gambiarra pra facilitar trabalho

                        if habilidade_quatro_protagonista=='Chuva de Dev' or habilidade_quatro_protagonista=='Js=Java' or habilidade_quatro_protagonista=='Guanabara':
                            poder_ataque = 125
                            chance_de_acerto = 85

                        else:
                            poder_ataque=140
                            chance_de_acerto=90

                        habilidade_usada = habilidade_quatro_protagonista
                    
   

                        print(linha)
                    print(f'Você utilizou a habilidade {habilidade_usada}!!\n{linha}')

                    if acao_protagonista_batalha=='3':

                        print(frase_de_buff)
                    else:

                        if numero_testar_chance_acerto>chance_de_acerto:

                            print('Infelizmente você errou o ataque :/\nMais sorte na próxima!')
                        else:

                            dano_causado = (poder_ataque+(ataque_codemon_protagonista_batalha*10/100))+(defesa_codemon_inimigo_batalha*12/100)
                            print(f'O dano causado foi de {dano_causado:.0f}!')
                            vida_codemon_inimigo_batalha-=dano_causado

                            if vida_codemon_inimigo_batalha<=0:
                                break

                    input('Aperte para continuar!')
                    vez_de_jogar+=1
                    continue

                print(linha)

                if vez_de_jogar==2:

                    movimento_aleatorio_inimigo = random.randint(1,4)   
                    
                    if movimento_aleatorio_inimigo==1:
                        poder_ataque = 80+(lista_ataque_normal.index(habilidade_um_inimigo)*10)
                        chance_de_acerto = 100
                        habilidade_usada = habilidade_um_inimigo

                    if movimento_aleatorio_inimigo==2:
                        poder_ataque = 130 + (lista_ataque_especial.index(habilidade_dois_inimigo)*10)
                        chance_de_acerto=90
                        habilidade_usada = habilidade_dois_inimigo
                        
                    if movimento_aleatorio_inimigo==3:
                        habilidade_usada = habilidade_tres_inimigo
                        
                        if habilidade_tres_inimigo==buff_um:
                            vida_codemon_inimigo_batalha+=(vida_codemon_inimigo*20/100)
                            frase_de_buff = f'A vida do inimigo aumentou ou recuperou em {vida_codemon_inimigo*20/100}!'

                        if habilidade_tres_inimigo==buff_dois:
                            ataque_codemon_inimigo+=(ataque_codemon_inimigo*15/100)
                            frase_de_buff = f'O ataque do inimigo aumentou em {ataque_codemon_inimigo*15/100}!'

                        if habilidade_tres_inimigo==buff_tres:
                            defesa_codemon_inimigo_batalha+=(defesa_codemon_inimigo*20/100)
                            frase_de_buff = f'A defesa do inimigo aumentou em {defesa_codemon_inimigo*20/100}!'
                        
                    if movimento_aleatorio_inimigo==4:

                    #Gambiarra pra facilitar trabalho
                        if habilidade_quatro_inimigo=='Chuva de Dev' or habilidade_quatro_inimigo=='Js=Java' or habilidade_quatro_inimigo=='Guanabara':
                            poder_ataque = 125
                            chance_de_acerto = 85
                            habilidade_usada = habilidade_quatro_inimigo

                        else:
                            poder_ataque=140
                            chance_de_acerto=90
                            habilidade_usada = habilidade_quatro_inimigo
                    
                    print(f'O inimigo utilizou a habilidade {habilidade_usada}!!\n{linha}')
                        
                    if movimento_aleatorio_inimigo==3:
                        print(frase_de_buff)
                        
                    else:

                        if numero_testar_chance_acerto>chance_de_acerto:
                            print('Infelizmente o inimigo errou o ataque :/')

                        else:
                            dano_causado = (poder_ataque+(ataque_codemon_inimigo_batalha*10/100))+(defesa_codemon_protagonista_batalha*12/100)
                            print(f'O dano causado foi de {dano_causado:.0f}!')
                            vida_codemon_protagonista_restante-=dano_causado

                            if vida_codemon_protagonista_restante<=0:
                                break

                    input('Aperte para continuar!')
                    vez_de_jogar-=1
                    continue

            entrar_loja = False

            if vida_codemon_inimigo_batalha<=0:

                input(f'Parabéns! a vida do inimigo chegou a 0!\nVc conseguiu mais R$ 150.00.\n{linha}\n')

                dinheiro_codemon +=150
                partidas_vencidas +=1

                if partidas_vencidas!=4:

                    entrar_loja = input('Deseja entrar na loja para comprar itens?[S] ou [N]: ').lower().startswith('s')

                    if entrar_loja is True:

                        while True:
                            
                            print(f'Qual item deseja comprar?!\n{linha}\n[1] - Poção pequena (Cura 300 HP) - R$150\n[2] - Poção Grande (Cura 600 HP) - R$300\n[3] - Aumento Ataque (Aumenta 100 pontos de ataque) - R$150\n[4] - Sair da loja')
                            opcao_comprar_item = input(f'{linha}\nDinheiro codemon: R$ {dinheiro_codemon}\nDigite aqui o que deseja: ')
                            dinheiro_insuficiente = False

                            if opcao_comprar_item=='1' and dinheiro_codemon>=150:
                                lista_itens.append('Poção pequena')
                                item_comprado = 'Poção pequena'
                                dinheiro_codemon-=150

                            elif opcao_comprar_item=='2' and dinheiro_codemon>=300:
                                lista_itens.append('Poção grande')
                                item_comprado = 'Poção grande'
                                dinheiro_codemon-=300

                            elif opcao_comprar_item=='3' and dinheiro_codemon>=150:
                                lista_itens.append('Aumento Ataque')
                                item_comprado = 'Aumento Ataque'
                                dinheiro_codemon-=150

                            elif opcao_comprar_item=='4':
                                print('Obrigado pela preferência a minha loja :)')
                                break
                            else:
                                dinheiro_insuficiente = True

                            print(linha)

                            if dinheiro_insuficiente is True:
                                print('Infelizmente ou vc digitou a opção errada ou é pobre :/')
                            else:
                                print(f'O item comprado foi: {item_comprado}, dinheiro restante: {dinheiro_codemon}')

                            print(linha)

                vitoria_batalha=1
                break
            
            if vida_codemon_protagonista_restante<=0:
                input('Infelizmente vc perdeu!')
                vitoria_batalha=0
                break

            

        if partidas_vencidas==4 and vitoria_batalha==1:
            print(f'Parabéns vc derroutou {nome_lider_ginasio}\nTome sua Insígnia!\n{linha}')
            break

        elif vitoria_batalha==0:
            print('Infelizmente você não conseguiu desse vez :/')
            break

        else:

            print(f'{linha}\nSeu codemon subiu um level!\nEle está no level {i+1}')
            print(f'Os status do {nome_codemon_protagonista} aumentaram em 15%!')

            vida_codemon_protagonista+=(vida_codemon_protagonista*15/100)
            defesa_codemon_protagonista+=(defesa_codemon_protagonista*15/100)
    
            ataque_codemon_protagonista+=(ataque_codemon_protagonista*15/100)
            
    resetar_jogo = input('Deseja voltar a tela de criação de codemon? [S] ou [N]: ').lower().startswith('s')
        
    if resetar_jogo is True:   
        print('Desejo sucesso nas suas próximas disputas :)')
        continue
    else:
        print('Já ta parando? Nutela...')
        break

