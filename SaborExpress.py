import os

restaurantes = [{'nome': 'Praça', 'categoria': 'Japonesa','ativo': True}, 
                {'nome': 'Pizzaria Suprema', 'categoria': 'Pizzaria','ativo': True},
                {'nome': 'Cantina', 'categoria': 'Italiana','ativo': False},]

def exibir_nome_do_programa():
    '''
    Exibe o nome do programa, versão e desenvolvedor
    '''
    print('Sabor Express')
    print('Versão 1.0')
    print('Desenvolvido por: Herbeson Shelton')
    print('------------------------------------')
    print("""
    Ｓａｂｏｒ Ｅｘｐｒｅｓｓ
        """)

def exibir_menu():
    '''
    Exibe o menu principal do programa
    '''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_programa():
    '''
    Finaliza o programa
    '''
    os.system('cls')
    print('Programa Finalizado com Sucesso!...\n')

def voltar_menu_principal():
    '''
    Retorna ao menu principal do programa
    '''
    input('Pressione Enter para voltar ao menu principal...')
    main()

def exibir_subtitulo(texto):
    '''
    Exibe um subtitulo com o texto passado como argumento
    '''
    os.system('cls')
    linha = '-' * len(texto)
    print(linha)
    print(texto)
    print(linha + '\n')

def opcao_invalida():
    '''
    Exibe uma mensagem de opção inválida e retorna ao menu principal
    '''
    print('Opção Inválida! Tente Novamente...\n')
    exibir_menu()
    escolher_opcao()

def cadastrar_novo_restaurante():
    '''
    Função para cadastrar um novo restaurante
    
    Input:
    nome_do_restaurante: str
    categoria_do_restaurante: str

    Output:
    Adiciona um novo restaurante na lista de restaurantes

    '''
    exibir_subtitulo('Cadastrar Novo Restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante: ')
    categoria_do_restaurante = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria_do_restaurante, 'ativo': False}
    restaurantes.append(dados_restaurante)
    print(f'Restaurante {nome_do_restaurante} cadastrado com sucesso!\n')
    voltar_menu_principal()

def listar_restaurantes():
    '''
    Lista os restaurantes cadastrados e seus status
    '''
    os.system('cls')
    exibir_subtitulo('Listar Restaurantes')

    print(f'{"Nome do Restaurante".ljust(24)} | {"Categoria".ljust(20)} | Status\n')
    if len(restaurantes) > 0:
        for restaurante in restaurantes:
            nome_restaurante = restaurante['nome']
            categoria_restaurante = restaurante['categoria']
            status_restaurante = 'Ativado' if restaurante['ativo'] else 'Desativado'
            print(f'--- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {status_restaurante}\n')
    else:
        print('Nenhum restaurante cadastrado!\n')
        main()
    voltar_menu_principal()

def alternar_status_restaurante():
    '''
    Altera o status de um restaurante de ativo para inativo e vice-versa
    '''
    exibir_subtitulo('Alterando Status Restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o status: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            status = 'ativado' if restaurante['ativo'] else 'desativado'
            print(f'O restaurante {nome_restaurante} foi {status} com sucesso!\n')
            break
        else:
            print(f'Restaurante {nome_restaurante} não encontrado!\n')
            break
    voltar_menu_principal()

def escolher_opcao():
    '''
    Menu de escolha de opções
    '''
    try:
        opcao_escolhida = int(input('Escolha uma Opção: '))
        print(f'Você escolheu a opção - {opcao_escolhida} -')

        if opcao_escolhida == 1:
            print('Cadastrar restaurantes')
            cadastrar_novo_restaurante()

        elif opcao_escolhida == 2:
            print('Listar restaurantes')
            listar_restaurantes()

        elif opcao_escolhida == 3:
            print('Ativar restaurante')
            alternar_status_restaurante()
        elif opcao_escolhida == 4:
            finalizar_programa()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''
    Main function
    '''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_menu()
    escolher_opcao()

if __name__ == '__main__':
    main()