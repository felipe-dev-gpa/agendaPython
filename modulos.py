# ARQUIVO ONDE ESTARÃO TODOS OS MÉTODOS
class BD:
    def criaBD(self):
        with open("bancoDados.txt", "w") as arquivo:
            pass  # Cria/limpa o arquivo


def cadastraContato():
    nome = input("Entre com seu nome: ").title()
    telefone = input("Entre agora com o telefone: ")

    try:
        with open("bancoDados.txt", "r") as arquivo:
            contatos_existentes = arquivo.readlines()
    except FileNotFoundError:
        contatos_existentes = []

    # Verifica duplicatas
    for linha in contatos_existentes:
        contato_nome, contato_telefone = linha.strip().split(",")
        if nome == contato_nome and telefone == contato_telefone:
            print("Este contato já está cadastrado.\n")
            return

    with open("bancoDados.txt", "a") as arquivo:
        arquivo.write(f"{nome},{telefone}\n")

    print("Contato cadastrado com sucesso!\n")


def consultaContato():
    try:
        decisao = int(input("Que tipo de listagem deseja mostrar?\n1) Completa (Nome e Telefone)\n2) Apenas Nomes\n> "))
        
        with open("bancoDados.txt", "r") as arquivo:
            linhas = arquivo.readlines()
        
        if not linhas:
            print("Nenhum contato cadastrado ainda.")
            return

        print("\nLista de Contatos:")
        for linha in linhas:
            linha = linha.strip()
            if "," in linha:
                nome, telefone = linha.split(",")
                if decisao == 1:
                    print(f"Nome: {nome} | Telefone: {telefone}")
                elif decisao == 2:
                    print(f"Nome: {nome}")
                else:
                    print("Opção inválida.")
                    break
            else:
                print("Linha mal formatada no arquivo.")

    except FileNotFoundError:
        print("Nenhum contato encontrado. O arquivo ainda não foi criado.")
    except ValueError:
        print("Entrada inválida. Digite um número válido.")


def menuPrincipal():
    print("Seja bem-vindo à Agenda Cadastro!")

    while True:
        print("\nSelecione o serviço:")
        print("1) Cadastrar Contato")
        print("2) Consultar Contato")
        print("3) Sair")
        try:
            op = int(input("> "))
            if op == 1:
                cadastraContato()
            elif op == 2:
                consultaContato()
            elif op == 3:
                sair = int(input("Deseja sair da Agenda Cadastro?\n1) Sim\n2) Não\n> "))
                if sair == 1:
                    print("Obrigado por utilizar a Agenda Cadastro!")
                    break
                elif sair == 2:
                    continue
                else:
                    print("Opção inválida.")
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")


# Cria o arquivo antes de começar
banco = BD()
banco.criaBD()

# Chama o menu principal
menuPrincipal()
