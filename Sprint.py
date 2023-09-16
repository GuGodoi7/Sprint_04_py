from datetime import date

# Menu para escolha de Pessoa fisica ou Juridica
def menu_pessoa():
    while True:
            print ('''
=======INFORME COMO DESEJA LOGAR NO SITE=======
(1) Pessoa física 
(2) Pessoa Jurídica
(3) Sair
==============================================''')
            escolha_pessoa = int(input("Escolha: "))
            list_escolha = (1, 2, 3)

            if escolha_pessoa in list_escolha:
                return escolha_pessoa
            else:
                print("Escolha inválida. Tente novamente.")

# Função para autenticar o usuário
def Cadastro(escolha):
        dados_cadastro = {}
        match escolha:
            case 1:
                nome = input("Nome: ")
                while True:
                    cpf = input("CPF: ")
                    # Valida cpf
                    cpf_digitos = [int(c) for c in cpf if c.isdigit()] # cria uma lista chamada cpf_digitos que contém apenas os dígitos numéricos do CPF
                    if Verifica_cpf(cpf_digitos):
                            break
                    else:
                        print("CPF inválido! Digite Novamente")
                endereco = input("Endereço: ")
                telefone = int(input("Telefone: "))
                email = input("E-mail: ")
                while True:
                    dia_nasc = int(input("Insira o dia de nascimento: "))
                    mes_nasc = int(input("Insira o mês de nascimento: "))
                    ano_nasc = int(input("Insira o ano de nascimento: "))
                    data_nasc = date(ano_nasc, mes_nasc, dia_nasc)
                    # Valda idade
                    if verificarIdade(data_nasc):
                        dados_cadastro = {"Nome": nome, "Cpf": cpf, "Endereço": endereco, "Telefone": telefone, "E-mail": email,
                                        "Data de Nascimento": data_nasc}
                        break
                    else:
                        print("Você deve ter pelo menos 18 anos para se cadastrar.")
                        exit()
            case 2:
                nome = input("Nome: ")
                while True:
                    # Valida CNPJ
                    cnpj = input("CNPJ: ")
                    if verifica_cnpj(cnpj):
                        break
                    else:
                        print("CNPJ inválido. Digite Novamente")
                endereco = input("Endereço: ")
                telefone = input("Telefone: ")
                email = input("e-mail: ")
                data_fundacao = input("Digite o ano de fundação: ")
                dados_cadastro = {"Nome" : nome , "Cnpj" : cnpj , "Endereço" : endereco, "Telefone" : telefone, "E-mail" : email, "Data de Fundação" : data_fundacao}
            case _:
                exit(print("Programa Finalizado. Volte sempre!"))
        return dados_cadastro

# Verificar se o cpf é valido
def Verifica_cpf(num):

    # Verifica se o dados possui 14 digitos
    if len(num) != 11:
        return False

    soma = 0
    j = 10
    # Percorre os 9 digitos
    for i in range(9):
        soma += num[i] * j
        j -= 1
    resto = soma % 11
    if resto < 2:
        dv1 = 0
    else:
        dv1 = 11 - resto
    # Dígito verificador #2
    soma = 0
    j = 11
    for i in range(10):
        soma += num[i] * j
        # Toda vez que passa aqui subtrai 1
        j -= 1
    resto = soma % 11
    if resto < 2:
        dv2 = 0
    else:
        dv2 = 11 - resto
    if num[9] == dv1 and num[10] == dv2:
        return True
    else:
        return False

#Verifica cnpj
def verifica_cnpj(cnpj):
    # Verifica se o dados possui 14 digitos
    if len(cnpj) != 14:
        return False
    
    # Calcula o primeiro dígito verificador
    soma = 0
    j = 5
    # Pecorre os 12 primeiros digitos 
    for i in range(12):
        soma += int(cnpj[i]) * j
        # Toda vez que passa aqui subtrai 1
        j -= 1
        # Quando chega no 1 ele volta para o 9
        if j == 1:
            j = 9
        # Calcula o resto da divisão da soma por 11,
    resto = soma % 11
    # Caso o resto da divisão seja menor que 2 o primeiro digito vai ser 0
    if resto < 2:
        digito_verificador_1 = 0
    # Caso seja maior que dois fazer resto - 11
    else:
        digito_verificador_1 = 11 - resto
    
    # Calcula o segundo dígito verificador
    soma = 0
    j = 6
    for i in range(13):
        soma += int(cnpj[i]) * j
        j -= 1
        if j == 1:
            j = 9
    resto = soma % 11
    if resto < 2:
        digito_verificador_2 = 0
    else:
        digito_verificador_2 = 11 - resto
    
    # Verifica se os dígitos verificadores calculados coincidem com os dígitos originais
    if int(cnpj[12]) == digito_verificador_1 and int(cnpj[13]) == digito_verificador_2:
        return True
    else:
        return False

# Verifica se usuario é maior de idade
def verificarIdade(data_nascimento):
    # Calcula a data atual
    data_atual = date.today()

    # Calcula a data há 18 anos atrás
    data_limite = data_atual.replace(year=data_atual.year - 18)

    # Compara a data de nascimento com a data limite
    return data_nascimento <= data_limite

# Coletar dados da bike 
def coleta_dados_bike():
    dados = []
    qtd_bike = int(input("Informe quantas bicicletas deseja cadastrar: "))

    for i in range(qtd_bike):
        list_cor = []
        bike = {}
        print(f"Bicicleta {i + 1}:")
        Marca = input("Digite a Marca da bike: ")
        bike["Marca"] = Marca
        Numeracao = input("Digite a numeração da bike: ")
        bike["Numeracao"] = Numeracao
        cor = input("Digite a cor da bike (Ex: Amarela, Preta): ")
        cores = cor.split(",")
        list_cor.append(cores)
        bike["Cores"] = list_cor
        while True:
            # valida data
            ano_bike = int(input("Digite o ano de fabricação da bike: "))
            if  ano_bike < date.today().year:
                bike["Ano"] = ano_bike
                break
            else:
                print("Data invalida. Tente Novamente")
        while True:
            # validavalor
            valor_mercado = float(input("Digite o valor de mercado da bike: "))
            if valor_mercado >= 2000:
                bike["Valor de Mercado"] = valor_mercado
                break
            else:
                print("Valor deve ser maior que 2000. Digite Novamente")
        funcao = input("Digite a função da bike (ex: Trabalho, lazer, competição): ")
        bike["Função"] = funcao
        modelo = input("Informe o modelo da sua bike (Ex: Bmx, Dobrável, Elétrica, Elétrica e Dobrável, Downhill, etc): ")
        bike["Modelo"] = modelo
        dados.append(bike)
    return dados

# Menu para escolher se a bike possui acessórios
def menu_acessorio():
    while True:
        print('''
================== Acessório ==================
(1) Caso sua bike tenha acessórios
(2) Caso não tenha acessórios
===============================================''')
        escolha_acessorio = int(input("Escolha: "))
        list_escolha_acessorio = (1,2)

        if escolha_acessorio in list_escolha_acessorio:
            return escolha_acessorio
        else:
            print("Escolha inválida. Tente novamente.")

# Coletar informações sobre acessórios
def acessorios(escolha_acessorio):
    acessorio = None  # Inicialize a variável acessorio aqui
    match escolha_acessorio:
        case 1: 
            acessorios = input("Informe as Modificações feitas: ")
            lista_acessorio = acessorios.split(", ")
            acessorio = {"Acessórios" : lista_acessorio}
        case 2:
            acessorio = {"Acessórios": ["Nenhum acessório"]}
    return acessorio

# Exibir os dados da bike e acessórios
def exibir_dados(dados, dados_cadastro):
    print("=============== CONFIRMAÇÃO DE DADOS ================")
    print("Dados do Cadastro:")
    for key, value in dados_cadastro.items():
        print(f"{key}: {value}")

    for i, bike in enumerate(dados):
        print(f"\nCadastro da Bicicleta {i + 1}:")
        for key, value in bike.items():
            if key == "Acessórios":
                print(f"{key}:")
                for acessorio_item in value:
                    print(f"{acessorio_item}")
            else:
                print(f"{key}: {value}")

# Função principal
def principal():
    while True:
        # Chama a função para escolher o tipo de pessoa
        escolha = menu_pessoa()
        # Faz o login de acordo com a escolha
        tipo_pessoa = Cadastro(escolha)

        print(f"\nSeja Bem-vindo {tipo_pessoa['nome']}")

        # Coleta dados sobre bicicletas
        dados = coleta_dados_bike()
        # Loop para cada bicicleta
        for i in range(len(dados)):
            # Exibe o número da bicicleta
            print(f"\nCadastro da Bicicleta {i + 1}")
            # Permite ao usuário escolher se a bicicleta possui acessórios
            escolha_acessorio = menu_acessorio()
            # Coleta informações sobre os acessórios
            acessorio = acessorios(escolha_acessorio)
            if acessorio:
                # Adiciona os acessórios aos dados da bicicleta
                dados[i]["Acessórios"] = acessorio.get("Acessórios", []) 
        # Exibe todos os dados coletados
        exibir_dados(dados, tipo_pessoa)
        confirma = input("\n(sim) se os dados estão corretos. (não) caso não estejam corretos: ")
        if confirma.lower() == 'sim' or confirma.lower() == 's':
            print("Etapa Concluída.")
            break

#PRICIPAL
principal()