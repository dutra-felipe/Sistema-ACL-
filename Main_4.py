import os

class GrupoAcesso:
    def __init__(self, nome):
        self.nome = nome
        self.privilégios = []

    def adicionar_privilegio(self, privilegio):
        self.privilégios.append(privilegio)

    def remover_privilegio(self, privilegio):
        if privilegio in self.privilégios:
            self.privilégios.remove(privilegio)
        else:
            print("Privilégio não encontrado no grupo.")

    def listar_privilégios(self):
        print("Privilégios do grupo:", self.nome, '\n')
        for privilegio in self.privilégios:
            print(privilegio.nome)

class Privilegio:
    def __init__(self, nome):
        self.nome = nome

def salvar_grupos(grupos):
    with open('grupos.txt', 'w') as file:
        for grupo in grupos:
            file.write(grupo.nome + ':' + ','.join([p.nome for p in grupo.privilégios]) + '\n')

def carregar_grupos():
    grupos = []
    try:
        with open('grupos.txt', 'r') as file:
            for line in file:
                nome, privilégios = line.strip().split(':')
                grupo = GrupoAcesso(nome)
                for priv in privilégios.split(','):
                    grupo.adicionar_privilegio(Privilegio(priv))
                grupos.append(grupo)
    except FileNotFoundError:
        pass
    return grupos

def mostrar_grupos_arquivo():
    try:
        with open('grupos.txt', 'r') as file:
            print("\n=== Grupos de Acesso no Arquivo ===\n")
            print(file.read())
    except FileNotFoundError:
        print("Arquivo de grupos não encontrado.")

def main():
    # Limpa a tela do terminal
    os.system('clear' if os.name == 'posix' else 'cls')

    grupos = carregar_grupos()

    while True:
        print("\n=== Menu de Opções ===\n")
        print("1. Manutenção do Grupo de Acessos")
        print("2. Manutenção de Privilégios no Grupo de Acesso")
        print("3. Mostrar Grupos de Acesso no Arquivo")
        print("4. Sair do programa")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            # Manutenção do Grupo de Acessos
            os.system('clear' if os.name == 'posix' else 'cls')
            print("\n=== Manutenção do Grupo de Acessos ===\n")
            print("1. Criar novo grupo de acesso")
            print("2. Remover grupo de acesso")
            print("3. Voltar\n")
            sub_opcao = input("\n\nEscolha uma opção: ")

            if sub_opcao == '1':
                os.system('clear' if os.name == 'posix' else 'cls')
                mostrar_grupos_arquivo()
                nome_grupo = input("\nDigite o nome do novo grupo de acesso: ")
                novo_grupo = GrupoAcesso(nome_grupo)
                grupos.append(novo_grupo)
                print("\n\nNovo grupo de acesso criado com sucesso.")
                salvar_grupos(grupos)
            elif sub_opcao == '2':
                os.system('clear' if os.name == 'posix' else 'cls')
                mostrar_grupos_arquivo()
                nome_grupo = input("\nDigite o nome do grupo de acesso a ser removido: ")
                for grupo in grupos:
                    if grupo.nome == nome_grupo:
                        grupos.remove(grupo)
                        print("\nGrupo de acesso removido com sucesso.")
                        salvar_grupos(grupos)
                        break
                else:
                    print("\nGrupo de acesso não encontrado.")
            elif sub_opcao == '3':
                os.system('clear' if os.name == 'posix' else 'cls')
                continue  # Continue para voltar ao menu de opções
            else:
                print("\nOpção inválida.")
            continue

        elif opcao == '2':
            # Manutenção de Privilégios no Grupo de Acesso
            os.system('clear' if os.name == 'posix' else 'cls')
            print("\n=== Manutenção de Privilégios no Grupo de Acesso ===")
            mostrar_grupos_arquivo()
            nome_grupo = input("Digite o nome do grupo de acesso: ")
            for grupo in grupos:
                if grupo.nome == nome_grupo:
                    os.system('clear' if os.name == 'posix' else 'cls')
                    print("\n1. Incluir privilégio no grupo de acesso")
                    print("2. Remover privilégio do grupo de acesso")
                    print("3. Listar privilégios do grupo de acesso")
                    sub_opcao = input("\nEscolha uma opção: ")
                    if sub_opcao == '1':
                        os.system('clear' if os.name == 'posix' else 'cls')
                        nome_privilegio = input("Digite o nome do privilégio a ser incluído: ")
                        novo_privilegio = Privilegio(nome_privilegio)
                        grupo.adicionar_privilegio(novo_privilegio)
                        print("\n\nPrivilégio incluído no grupo de acesso.")
                        salvar_grupos(grupos)
                    elif sub_opcao == '2':
                        os.system('clear' if os.name == 'posix' else 'cls')
                        mostrar_grupos_arquivo()
                        nome_privilegio = input("\nDigite o nome do privilégio a ser removido: ")
                        for priv in grupo.privilégios:
                            if priv.nome == nome_privilegio:
                                grupo.remover_privilegio(priv)
                                os.system('clear' if os.name == 'posix' else 'cls')
                                print("Privilégio removido do grupo de acesso.")
                                salvar_grupos(grupos)
                                break
                        else:
                            os.system('clear' if os.name == 'posix' else 'cls')
                            print("Privilégio não encontrado no grupo de acesso.")
                    elif sub_opcao == '3':
                        os.system('clear' if os.name == 'posix' else 'cls')
                        grupo.listar_privilégios()
                    else:
                        os.system('clear' if os.name == 'posix' else 'cls')
                        print("Opção inválida.")
                    break
            else:
                print("Grupo de acesso não encontrado.")

        elif opcao == '3':
            # Opção para mostrar grupos de acesso no arquivo
            os.system('clear' if os.name == 'posix' else 'cls')
            mostrar_grupos_arquivo()
            
        elif opcao == '4':
            # Opção para sair do programa
            break

        else:
            print("\nOpção inválida, Tente novamente.")


if __name__ == "__main__":
    main()
