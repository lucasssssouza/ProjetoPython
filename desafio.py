import os
totalCompra = 0
prod = []
quantProd = []
precoUNI = []
def inicio():
    os.system('cls')
    global totalCompra
    global prod
    global quantProd
    global precoUNI
    totalCompra = 0
    prod.clear()
    quantProd.clear()
    precoUNI.clear()
    produtos()
    
def total(ti):
    global totalCompra
    global prod
    global quantProd
    global precoUNI
    totalCompra += ti
    escolha = input('[F] Para finalizar a venda [C] para continuar').upper()
    if escolha == 'C':
        os.system('cls')
        produtos()
    else:
        os.system('cls')
        for descricao,quantidade,precouni in zip(prod, quantProd,precoUNI):
            print(f'{descricao} --- QTD -> {quantidade:,.3f} -- PREÇO UNI {precouni:,.2f} -- TOTAL ITEM {quantidade*precouni:,.3f}')

        print(f'\nPreço Total da compra R${totalCompra:,.2f}')


        print(f'\n\nIMPOSTO NACIONAL R${totalCompra*0.05:,.2f}')
        print(f'IMPOSTO ESTADUAL R${totalCompra*0.08:,.2f}')
        print(f'IMPOSTO MUNICIPAL R${totalCompra*0.12:,.2f}')
        escolha = input('\n\nPARA INICIAR NOVA VENDA TECLE [S]').upper()
        if escolha == 'S':
            os.system('cls')
            inicio()
        else:
            os.system('cls')
            print('OBRIGADO. VOLTE SEMPRE')
            escolha = input('\n\n\n\n\nPARA INICIAR NOVA VENDA TECLE [S]').upper()
            if escolha == 'S':
                inicio()
            else:
                print('Programa finalizado')

#========================= INICIO CADASTRO DE PRODUTOS ======================================================================================
def cadastroProduto(codProduto):
    global prod
    global quantProd
    alfacecrespa = 3.99 # cod 1
    alfaceamericana = 7.95 # cod 2
    alfacelisa = 7.99 # cod 3
    bananananica = 4.99 # cod 4
    bananaprata = 7.99 # cod 5
    bananaterra = 7.49 # cod 6
    macaverde = 17.99 # cod 7
    macafuji = 15.90 # cod 8
    macagala = 7.90 # cod 9
    omo = 12.99 # cod 10
    brilhante = 10.99 # cod 11
    qboa = 8.99 # cod 12
    ype = 6.99 # cod 13
    veja = 6.99 # cod 14
    urca = 4.99 # cod 15
    arrozDallas = 29.99 # cod 16
    arrozTioLauterio = 31.99 # cod 17
    feijaoCarioca = 9.99 # cod 18
    feijaoPreto = 11.99 # cod 19
    macarraoDallas = 5.99 # cod 20
    macarraoRenata = 3.99 # cod 21
    paoFrances = 17.99 # cod 22

    if codProduto == 1: # cod 1
        quantidade= float(input('DIGITE A QUANTIDADE/PESO: '))
        totalItem = (quantidade * alfacecrespa)
        prod.append('Alface Crespa')
        quantProd.append(quantidade)
        precoUNI.append(alfacecrespa)
        return total(totalItem)
    elif codProduto == 2: # cod 2
        quantidade= float(input('DIGITE A QUANTIDADE/PESO: '))
        totalItem = (quantidade * alfaceamericana)
        prod.append('Alface Americana')
        precoUNI.append(alfaceamericana)
        quantProd.append(quantidade)
        return total(totalItem)
    elif codProduto == 3: # cod 3
        quantidade= float(input('DIGITE A QUANTIDADE/PESO: '))
        totalItem = (quantidade * alfacelisa)
        prod.append('Alface Lisa')
        precoUNI.append(alfacelisa)
        quantProd.append(quantidade)
        return total(totalItem)
    elif codProduto == 4: # cod 4
        quantidade= float(input('DIGITE A QUANTIDADE/PESO: '))
        totalItem = (quantidade * bananananica)
        prod.append('Banana Nanica')
        precoUNI.append(bananananica)
        quantProd.append(quantidade)
        return total(totalItem)
    elif codProduto == 5: # cod 5
        quantidade= float(input('DIGITE A QUANTIDADE/PESO: '))
        totalItem = (quantidade * bananaprata)
        prod.append('Banana Prata')
        precoUNI.append(bananaprata)
        quantProd.append(quantidade)
        return total(totalItem)
    elif codProduto == 6: # cod 6
        quantidade= float(input('DIGITE A QUANTIDADE/PESO: '))
        totalItem = (quantidade * bananaterra)
        prod.append('Banana da Terra')
        precoUNI.append(bananaterra)
        quantProd.append(quantidade)
        return total(totalItem)
    elif codProduto == 7: # cod 7
        quantidade= float(input('DIGITE A QUANTIDADE/PESO: '))
        totalItem = (quantidade * macaverde)
        prod.append('Maçã Verde')
        precoUNI.append(macaverde)
        quantProd.append(quantidade)
        return total(totalItem)
    elif codProduto == 8: # cod 8
        quantidade= float(input('DIGITE A QUANTIDADE/PESO: '))
        totalItem = (quantidade * macafuji)
        prod.append('Maçã Fuji')
        precoUNI.append(macafuji)
        quantProd.append(quantidade)
        return total(totalItem)
    elif codProduto == 9: # cod 9
        quantidade= float(input('DIGITE A QUANTIDADE/PESO: '))
        totalItem = (quantidade * macagala)
        prod.append('Maçã Gala')
        precoUNI.append(macagala)
        quantProd.append(quantidade)
        return total(totalItem)
    elif codProduto == 10: # cod 10
        quantidade= float(input('DIGITE A QUANTIDADE/PESO: '))
        totalItem = (quantidade * omo)
        prod.append('Sabão em pó OMO')
        precoUNI.append(omo)
        quantProd.append(quantidade)
        return total(totalItem)
    elif codProduto == 11: # cod 11
        quantidade= float(input('DIGITE A QUANTIDADE/PESO: '))
        totalItem = (quantidade * brilhante)
        prod.append('Sabão em pó BRILHANTE')
        precoUNI.append(brilhante)
        quantProd.append(quantidade)
        return total(totalItem)
    elif codProduto == 12: # cod 12
        quantidade= float(input('DIGITE A QUANTIDADE/PESO: '))
        totalItem = (quantidade * qboa)
        prod.append("AGUA SANITARIA Q'BOA")
        precoUNI.append(qboa)
        quantProd.append(quantidade)
        return total(totalItem)
    elif codProduto == 13: # cod 13
        quantidade= float(input('DIGITE A QUANTIDADE/PESO: '))
        totalItem = (quantidade * ype)
        prod.append("AGUA SANITARIA YPÊ")
        precoUNI.append(ype)
        quantProd.append(quantidade)
        return total(totalItem)
    elif codProduto == 14: # cod 14
        quantidade= float(input('DIGITE A QUANTIDADE/PESO: '))
        totalItem = (quantidade * veja)
        precoUNI.append(veja)
        prod.append("DESINFETANTE VEJA")
        quantProd.append(quantidade)
        return total(totalItem)
    elif codProduto == 15: # cod 15
        quantidade= float(input('DIGITE A QUANTIDADE/PESO: '))
        totalItem = (quantidade * urca)
        prod.append("DESINFETANTE URCA")
        precoUNI.append(urca)
        quantProd.append(quantidade)
        return total(totalItem)
    elif codProduto == 16: # cod 16
        quantidade= float(input('DIGITE A QUANTIDADE/PESO: '))
        totalItem = (quantidade * arrozDallas)
        prod.append("ARROZ DALLAS 5KG")
        precoUNI.append(arrozDallas)
        quantProd.append(quantidade)
        return total(totalItem)
    elif codProduto == 17: # cod 17
        quantidade= float(input('DIGITE A QUANTIDADE/PESO: '))
        totalItem = (quantidade * arrozTioLauterio)
        prod.append("ARROZ TIO LAUTERIO 5KG")
        precoUNI.append(arrozTioLauterio)
        quantProd.append(quantidade)
        return total(totalItem)
    elif codProduto == 18: # cod 18
        quantidade= float(input('DIGITE A QUANTIDADE/PESO: '))
        totalItem = (quantidade * feijaoCarioca)
        prod.append("FEIJÃO CARIOCA 1KG")
        precoUNI.append(feijaoCarioca)
        quantProd.append(quantidade)
        return total(totalItem)
    elif codProduto == 19: # cod 19
        quantidade= float(input('DIGITE A QUANTIDADE/PESO: '))
        totalItem = (quantidade * feijaoPreto)
        prod.append("FEIJÃO PRETO 1KG")
        precoUNI.append(feijaoPreto)
        quantProd.append(quantidade)
        return total(totalItem)
    elif codProduto == 20: # cod 20
        quantidade= float(input('DIGITE A QUANTIDADE/PESO: '))
        totalItem = (quantidade * macarraoDallas)
        prod.append("MACARRÃO DALLAS UN")
        precoUNI.append(macarraoDallas)
        quantProd.append(quantidade)
        return total(totalItem)
    elif codProduto == 21: # cod 21
        quantidade= float(input('DIGITE A QUANTIDADE/PESO: '))
        totalItem = (quantidade * macarraoRenata)
        prod.append("NACARRAÃO RENATA UN")
        precoUNI.append(macarraoRenata)
        quantProd.append(quantidade)
        return total(totalItem)
    elif codProduto == 22: # cod 22
        quantidade= float(input('DIGITE A QUANTIDADE/PESO: '))
        totalItem = (quantidade * paoFrances)
        prod.append("PÃO FRANCÊS KG")
        precoUNI.append(paoFrances)
        quantProd.append(quantidade)
        return total(totalItem)

#========================= FIM CADASTRO DE PRODUTOS ======================================================================================

#============================================================================== INICIO MENU INICIAL ======================================================================================
def produtos():
    print('[1] - FRUTAS E VERDURAS ')
    print('[2] - PRODUTOS DE LIMPEZA ')
    print('[3] - MERCEARIA')
    print('[4] - PADARIA ')
    secao = input('Digite o codigo da seção que deseja localizar o produto: ')
    if secao == '1':
        os.system('cls')
        frutasverduras()
    elif secao == '2':
        os.system('cls')
        prodLimpeza()
    elif secao == '3':
        os.system('cls')
        mercearia()
    elif secao == '4':
        os.system('cls')
        padaria()
    else:
        os.system('cls')
        print('Opção invalida')
        produtos()
#=============================================================================== FIM MENU INICIAL ======================================================================================

#========================= INICIO SEÇÃO ======================================================================================
def frutasverduras(): # OK
    os.system('cls')
    print('[1] - ALFACE ')
    print('[2] - BANANA ')
    print('[3] - MAÇÃS ')
    print('[0] - VOLTAR PARA LISTA DE SEÇÕES ')
    produto = int(input(('Digite o codigo do produto que deseja ver as variedades ')))
    if produto == 0: # Volta para lista de seções
        os.system('cls')
        produtos()
    elif produto == 1: # Avança para o grupo de alfaces
        os.system('cls')
        alface()
    elif produto == 2: # Avança para o grupo de bananas
        os.system('cls')
        banana()
    elif produto == 3: # Avança para o grupo de Maçãs
        os.system('cls')
        maca()
def prodLimpeza():
    os.system('cls')
    print('[1] - SABÃO EM PÓ ')
    print('[2] - AGUA SANITARIA ')
    print('[3] - DESINFETANTE ')
    print('[0] - VOLTAR PARA LISTA DE SEÇÕES ')
    produto = int(input(('Digite o codigo do produto que deseja ver as variedades ')))
    if produto == 0: # Volta para lista de seções
        os.system('cls')
        produtos()
    elif produto == 1: # Avança para o grupo de SABÃO EM PÓ
        os.system('cls')
        sabaoempo()
    elif produto == 2: # Avança para o grupo de AGUA SANITARIA
        os.system('cls')
        aguasanitaria()
    elif produto == 3: # Avança para o grupo de DESINFETANTE
        os.system('cls')
        desinfetante()
def mercearia():
    os.system('cls')
    print('[1] - ARROZ ')
    print('[2] - FEIJÃO ')
    print('[3] - MACARRÃO ')
    print('[0] - VOLTAR PARA LISTA DE SEÇÕES ')
    produto = int(input(('Digite o codigo do produto que deseja ver as variedades ')))
    if produto == 0: # Volta para lista de seções
        os.system('cls')
        produtos()
    elif produto == 1: # Avança para o grupo de ARROZ
        os.system('cls')
        arroz()
    elif produto == 2: # Avança para o grupo de FEIJÃO
        os.system('cls')
        feijao()
    elif produto == 3: # Avança para o grupo de MACARRÃO
        os.system('cls')
        macarrao()
def padaria():
    os.system('cls')
    print('[1] - PÃO FRANCÊS KG')
    print('[0] - VOLTAR PARA LISTA DE SEÇÕES ')
    produto = int(input(('Digite o codigo do produto que deseja ver as variedades ')))
    if produto == 0: # Volta para lista de seções
        os.system('cls')
        produtos()
    elif produto == 1: # Avança para o produto pao frances
        os.system('cls')
        paoFrances()
#========================= FIM SEÇÃO ======================================================================================

#============================================================================== INICIO GRUPOS ======================================================================================
def alface(): # Grupo Alface OK
    os.system('cls')
    print('[1] - ALFACE CRESPA ')
    print('[2] - ALFACE AMERICANA')
    print('[3] - ALFACE LISA \n')
    print('[9] - VOLTAR PARA LISTA DE PRODUTOS SEÇÃO FRUTAS E VERDURAS ')
    print('[0] - VOLTAR PARA LISTA DE SEÇÕES ')
    tipoproduto = int(input(('Digite o codigo do produto que deseja ver as variedades ')))
    if tipoproduto == 0:
        os.system('cls')
        produtos()
    elif tipoproduto ==9:
        os.system('cls')
        frutasverduras()
    elif tipoproduto == 1:
        os.system('cls')
        alfacecrespa()
    elif tipoproduto == 2:
        os.system('cls')
        alfaceAmericana()
    elif tipoproduto == 3:
        os.system('cls')
        alfaceLisa()
def banana(): # Grupo Bananas OK
    os.system('cls')
    print('[1] - BANANA NANICA ')
    print('[2] - BANANA DA TERRA')
    print('[3] - BANANA PRATA \n')
    print('[9] - VOLTAR PARA LISTA DE PRODUTOS SEÇÃO FRUTAS E VERDURAS ')
    print('[0] - VOLTAR PARA LISTA DE SEÇÕES ')
    tipoproduto = int(input(('Digite o codigo do produto que deseja ver as variedades ')))
    if tipoproduto == 0: # Volta para lista de Seções
        os.system('cls')
        produtos()
    elif tipoproduto ==9: # Volta para Seção de Frutas e Verduras
        os.system('cls')
        frutasverduras()
    elif tipoproduto == 1: #Banana Nanica
        os.system('cls')
        bananananica()
    elif tipoproduto == 2: #Banana da Terra
        os.system('cls')
        bananaterra()
    elif tipoproduto == 3: #Banana Prata
        os.system('cls')
        bananaprata()
def maca(): # Grupo Maçãs OK
    os.system('cls')
    print('[1] - MAÇÃ VERDE ')
    print('[2] - MAÇÃ FUJI')
    print('[3] - MAÇÃ GALA \n')
    print('[9] - VOLTAR PARA LISTA DE PRODUTOS SEÇÃO FRUTAS E VERDURAS ')
    print('[0] - VOLTAR PARA LISTA DE SEÇÕES ')
    tipoproduto = int(input(('Digite o codigo do produto que deseja ver as variedades ')))
    if tipoproduto == 0: # Volta para lista de Seções
        os.system('cls')
        produtos()
    elif tipoproduto ==9: # Volta para Seção de Frutas e Verduras
        os.system('cls')
        maca()
    elif tipoproduto == 1: #Maça verde
        os.system('cls')
        macaverde()
    elif tipoproduto == 2: #Maça Fuji
        os.system('cls')
        macafuji()
    elif tipoproduto == 3: #Maça Gala
        os.system('cls')
        macagala()
def sabaoempo(): # Grupo sabão em pó OK
    os.system('cls')
    print('[1] - SABÃO EM PÓ OMO')
    print('[2] - SABÃO EM PÓ BRILHANTE\n')
    print('[9] - VOLTAR PARA LISTA DE PRODUTOS DE LIMPEZA ')
    print('[0] - VOLTAR PARA LISTA DE SEÇÕES ')
    tipoproduto = int(input(('Digite o codigo do produto que deseja ver as variedades ')))

    if tipoproduto == 0: # Volta para lista de Seções
        os.system('cls')
        produtos()
    elif tipoproduto ==9: # Volta para a seção de produtos de limpeza
        os.system('cls')
        prodLimpeza()
    elif tipoproduto == 1: #SABÃO EM PÓ OMO
        os.system('cls')
        omo()
    elif tipoproduto == 2: #SABÃO EM PÓ BRILHANTE
        os.system('cls')
        brilhante()
def aguasanitaria(): # Grupo agua sanitaria OK
    os.system('cls')
    print("[1] - AGUA SANITARIA - Q'BOA ")
    print("[2] - AGUA SANITARIA - YPÊ ")
    print('[9] - VOLTAR PARA LISTA DE PRODUTOS SEÇÃO PRODUTOS DE LIMPEZA ')
    print('[0] - VOLTAR PARA LISTA DE SEÇÕES ')
    tipoproduto = int(input(('Digite o codigo do produto que deseja ver as variedades ')))

    if tipoproduto == 0: # Volta para lista de Seções
        os.system('cls')
        produtos()
    elif tipoproduto ==9: # Volta para a seção de produtos de limpeza
        os.system('cls')
        prodLimpeza()
    elif tipoproduto == 1: #AGUA SANITARIA Q'BOA
        os.system('cls')
        qboa()
    elif tipoproduto == 2: #AGUA SANITARIA YPÊ
        os.system('cls')
        ype()
def desinfetante(): # Grupo Desinfetante OK
    os.system('cls')
    print("[1] - DESINFETANTE VEJA ")
    print("[2] - DESINFETANTE URCA ")
    print('[9] - VOLTAR PARA LISTA DE PRODUTOS SEÇÃO PRODUTOS DE LIMPEZA ')
    print('[0] - VOLTAR PARA LISTA DE SEÇÕES ')
    tipoproduto = int(input(('Digite o codigo do produto que deseja ver as variedades ')))

    if tipoproduto == 0: # Volta para lista de Seções
        os.system('cls')
        produtos()
    elif tipoproduto ==9: # Volta para a seção de produtos de limpeza
        os.system('cls')
        prodLimpeza()
    elif tipoproduto == 1: #DESINFETANTE VEJA
        os.system('cls')
        veja()
    elif tipoproduto == 2: #DESINFETANTE URCA
        os.system('cls')
        urca()
def arroz():
    os.system('cls')
    print("[1] - ARROZ DALLAS 5KG ")
    print("[2] - ARROZ TIO LAUTERIO ")
    print('[9] - VOLTAR PARA LISTA DE PRODUTOS SEÇÃO MERCEARIA ')
    print('[0] - VOLTAR PARA LISTA DE SEÇÕES ')
    tipoproduto = int(input(('Digite o codigo do produto que deseja ver as variedades ')))

    if tipoproduto == 0: # Volta para lista de Seções
        os.system('cls')
        produtos()
    elif tipoproduto ==9: # Volta para a seção de mercearia
        os.system('cls')
        mercearia()
    elif tipoproduto == 1: #arroz dallas
        os.system('cls')
        arrozDallas()
    elif tipoproduto == 2: #arroz tio lauterio
        os.system('cls')
        arrozTioLauterio()
def feijao():
    os.system('cls')
    print("[1] - FEIJÃO CARIOCA 1KG ")
    print("[2] - FEIJÃO PRETO 1KG ")
    print('[9] - VOLTAR PARA LISTA DE PRODUTOS SEÇÃO MERCEARIA ')
    print('[0] - VOLTAR PARA LISTA DE SEÇÕES ')
    tipoproduto = int(input(('Digite o codigo do produto que deseja ver as variedades ')))

    if tipoproduto == 0: # Volta para lista de Seções
        os.system('cls')
        produtos()
    elif tipoproduto ==9: # Volta para a seção de mercearia
        os.system('cls')
        mercearia()
    elif tipoproduto == 1: #feijaoCarioca
        os.system('cls')
        feijaoCarioca()
    elif tipoproduto == 2: #feijaoPreto
        os.system('cls')
        feijaoPreto()
def macarrao():
    os.system('cls')
    print("[1] - MACARRÃO DALLAS UN ")
    print("[2] - MACARRÃO RENATA UN  ")
    print('[9] - VOLTAR PARA LISTA DE PRODUTOS SEÇÃO MERCEARIA ')
    print('[0] - VOLTAR PARA LISTA DE SEÇÕES ')
    tipoproduto = int(input(('Digite o codigo do produto que deseja ver as variedades ')))

    if tipoproduto == 0: # Volta para lista de Seções
        os.system('cls')
        produtos()
    elif tipoproduto ==9: # Volta para a seção de mercearia
        os.system('cls')
        mercearia()
    elif tipoproduto == 1: #MACARRÃO DALLAS
        os.system('cls')
        macarraoDallas()
    elif tipoproduto == 2: #MACARRÃO RENATA
        os.system('cls')
        macarraoRenata()
#=============================================================================== FIM GRUPOS ======================================================================================

#====================== INICIO PRODUTOS ======================================================================================
def alfacecrespa(): # Cod 1
    print(f'PREÇO DE VENDA ALFACE CRESPA R$3.99')
    print('[1] COMPRAR')
    print('[0] VOLTAR')
    comprar = int(input(('DIGITE [1] PARA COMPRAR|| [0] PARA VOLTAR... ')))
    if comprar == 0:
        os.system('cls')
        alface()
    elif comprar == 1:
        cadastroProduto(1)
def alfaceAmericana(): # Cod 2
    print(f'PREÇO DE VENDA ALFACE AMERICANA R$7.95')
    print('[1] COMPRAR')
    print('[0] VOLTAR')
    comprar = int(input(('DIGITE [1] PARA COMPRAR|| [0] PARA VOLTAR... ')))
    if comprar == 0:
        os.system('cls')
        alface()
    elif comprar == 1:
        cadastroProduto(2)
def alfaceLisa(): # Cod 3
    print(f'PREÇO DE VENDA ALFACE LISA R$7.99')
    print('[1] COMPRAR')
    print('[0] VOLTAR')
    comprar = int(input(('DIGITE [1] PARA COMPRAR|| [0] PARA VOLTAR... ')))
    if comprar == 0:
        os.system('cls')
        alface()
    elif comprar == 1:
        cadastroProduto(3)
def bananananica(): # Cod 4
    print(f'PREÇO DE VENDA BANANA NANICA R$4.99')
    print('[1] COMPRAR')
    print('[0] VOLTAR')
    comprar = int(input(('DIGITE [1] PARA COMPRAR|| [0] PARA VOLTAR... ')))
    if comprar == 0: # Volta para Lista de produtos
        os.system('cls')
        banana()
    elif comprar == 1:
        cadastroProduto(4)
def bananaprata(): # Cod 5
    print(f'PREÇO DE VENDA BANANA PRATA R$7.99')
    print('[1] COMPRAR')
    print('[0] VOLTAR')
    comprar = int(input(('DIGITE [1] PARA COMPRAR|| [0] PARA VOLTAR... ')))
    if comprar == 0: # Volta para Lista de produtos
        os.system('cls')
        banana()
    elif comprar == 1:
        cadastroProduto(5)
def bananaterra(): # Cod 6
    print(f'PREÇO DE VENDA BANANA DA TERRA R$7.49')
    print('[1] COMPRAR')
    print('[0] VOLTAR')
    comprar = int(input(('DIGITE [1] PARA COMPRAR|| [0] PARA VOLTAR... ')))
    if comprar == 0: # Volta para Lista de produtos
        os.system('cls')
        banana()
    elif comprar == 1:
        cadastroProduto(6)
def macaverde(): # Cod 7
    print(f'PREÇO DE VENDA MAÇÃ VERDE R$17.99 KG')
    print('[1] COMPRAR')
    print('[0] VOLTAR')
    comprar = int(input(('DIGITE [1] PARA COMPRAR|| [0] PARA VOLTAR... ')))
    if comprar == 0: # Volta para Lista de produtos
        os.system('cls')
        maca()
    elif comprar == 1:
        cadastroProduto(7)
def macafuji(): # Cod 8
    print(f'PREÇO DE VENDA MAÇÃ FUJI R$15.90 KG')
    print('[1] COMPRAR')
    print('[0] VOLTAR')
    comprar = int(input(('DIGITE [1] PARA COMPRAR|| [0] PARA VOLTAR... ')))
    if comprar == 0: # Volta para Lista de produtos
        os.system('cls')
        maca()
    elif comprar == 1:
        cadastroProduto(8)
def macagala(): # Cod 9
    print(f'PREÇO DE VENDA MAÇÃ GALA R$7.99 KG')
    print('[1] COMPRAR')
    print('[0] VOLTAR')
    comprar = int(input(('DIGITE [1] PARA COMPRAR|| [0] PARA VOLTAR... ')))
    if comprar == 0: # Volta para Lista de produtos
        os.system('cls')
        maca()
    elif comprar == 1:
        cadastroProduto(9)
def omo(): # Cod 10
    print(f'PREÇO DE VENDA SABÃO EM PÓ OMO R$12,99 UN')
    print('[1] COMPRAR')
    print('[0] VOLTAR')
    comprar = int(input(('DIGITE [1] PARA COMPRAR|| [0] PARA VOLTAR... ')))
    if comprar == 0: # Volta para Lista de produtos
        os.system('cls')
        sabaoempo()
    elif comprar == 1:
        cadastroProduto(10)
def brilhante(): # Cod 11
    print(f'PREÇO DE VENDA SABÃO EM PÓ BRILHANTE R$10,99 UN')
    print('[1] COMPRAR')
    print('[0] VOLTAR')
    comprar = int(input(('DIGITE [1] PARA COMPRAR|| [0] PARA VOLTAR... ')))
    if comprar == 0: # Volta para Lista de produtos
        os.system('cls')
        sabaoempo()
    elif comprar == 1:
        cadastroProduto(11)
def qboa(): # Cod 12
    print(f"PREÇO DE VENDA AGUA SANITARIA - Q'BOA R$8,99 UN")
    print("[1] COMPRAR")
    print('[0] VOLTAR')
    comprar = int(input(('DIGITE [1] PARA COMPRAR|| [0] PARA VOLTAR... ')))
    if comprar == 0: # Volta para Lista de produtos
        os.system('cls')
        aguasanitaria()
    elif comprar == 1:
        cadastroProduto(12)
def ype(): # Cod 13
    print(f"PREÇO DE VENDA AGUA SANITARIA - YPÊ R$6,99 UN")
    print("[1] COMPRAR")
    print('[0] VOLTAR')
    comprar = int(input(('DIGITE [1] PARA COMPRAR|| [0] PARA VOLTAR... ')))
    if comprar == 0: # Volta para Lista de produtos
        os.system('cls')
        aguasanitaria()
    elif comprar == 1:
        cadastroProduto(13)
def veja(): # Cod 14
    print(f"PREÇO DE VENDA DESINFETANTE VEJA - YPÊ R$6,99 UN")
    print("[1] COMPRAR")
    print('[0] VOLTAR')
    comprar = int(input(('DIGITE [1] PARA COMPRAR|| [0] PARA VOLTAR... ')))
    if comprar == 0: # Volta para Lista de produtos
        os.system('cls')
        desinfetante()
    elif comprar == 1:
        cadastroProduto(14)
def urca(): # Cod 15
    print(f"PREÇO DE VENDA DESINFETANTE URCA - YPÊ R$4,99 UN")
    print("[1] COMPRAR")
    print('[0] VOLTAR')
    comprar = int(input(('DIGITE [1] PARA COMPRAR|| [0] PARA VOLTAR... ')))
    if comprar == 0: # Volta para Lista de produtos
        os.system('cls')
        desinfetante()
    elif comprar == 1:
        cadastroProduto(15)
def arrozDallas(): # Cod 16
    print(f"PREÇO DE VENDA ARROZ DALLAS 5KG R$29,99 UN")
    print("[1] COMPRAR")
    print('[0] VOLTAR')
    comprar = int(input(('DIGITE [1] PARA COMPRAR|| [0] PARA VOLTAR... ')))
    if comprar == 0: # Volta para Lista de produtos
        os.system('cls')
        arroz()
    elif comprar == 1:
        cadastroProduto(16)
def arrozTioLauterio(): # Cod 17
    print(f"PREÇO DE VENDA ARROZ TIO LAUTERIO 5KG R$31,99 UN")
    print("[1] COMPRAR")
    print('[0] VOLTAR')
    comprar = int(input(('DIGITE [1] PARA COMPRAR|| [0] PARA VOLTAR... ')))
    if comprar == 0: # Volta para Lista de produtos
        os.system('cls')
        arroz()
    elif comprar == 1:
        cadastroProduto(17)
def feijaoCarioca(): # Cod 18
    print(f"PREÇO DE VENDA FEIJÃO CARIOCA 1KG R$9,99 UN")
    print("[1] COMPRAR")
    print('[0] VOLTAR')
    comprar = int(input(('DIGITE [1] PARA COMPRAR|| [0] PARA VOLTAR... ')))
    if comprar == 0: # Volta para Lista de produtos
        os.system('cls')
        feijao()
    elif comprar == 1:
        cadastroProduto(18)
def feijaoPreto (): # Cod 19
    print(f"PREÇO DE VENDA FEIJÃO PRETO 1KG R$9,99 UN")
    print("[1] COMPRAR")
    print('[0] VOLTAR')
    comprar = int(input(('DIGITE [1] PARA COMPRAR|| [0] PARA VOLTAR... ')))
    if comprar == 0: # Volta para Lista de produtos
        os.system('cls')
        feijao()
    elif comprar == 1:
        cadastroProduto(19)
def macarraoDallas (): # Cod 20
    print(f"PREÇO DE VENDA MACARRÃO DALLAS R$5,99 UN")
    print("[1] COMPRAR")
    print('[0] VOLTAR')
    comprar = int(input(('DIGITE [1] PARA COMPRAR|| [0] PARA VOLTAR... ')))
    if comprar == 0: # Volta para Lista de produtos
        os.system('cls')
        macarrao()
    elif comprar == 1:
        cadastroProduto(20)
def macarraoRenata(): # Cod 21
    print(f"PREÇO DE VENDA MACARRÃO RENATA R$3,99 UN")
    print("[1] COMPRAR")
    print('[0] VOLTAR')
    comprar = int(input(('DIGITE [1] PARA COMPRAR|| [0] PARA VOLTAR... ')))
    if comprar == 0: # Volta para Lista de produtos
        os.system('cls')
        macarrao()
    elif comprar == 1:
        cadastroProduto(21)
def paoFrances(): # Cod 22
    print(f"PREÇO DE VENDA PÃO FRANCÊS R$17,99 KG")
    print("[1] COMPRAR")
    print('[0] VOLTAR')
    comprar = int(input(('DIGITE [1] PARA COMPRAR|| [0] PARA VOLTAR... ')))
    if comprar == 0: # Volta para Lista de produtos
        os.system('cls')
        padaria()
    elif comprar == 1:
        cadastroProduto(22)
#==================== FIM PRODUTOS ======================================================================================
inicio()
