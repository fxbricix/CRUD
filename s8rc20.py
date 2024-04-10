import json
# Author: Fabricio Moreira Pedroso
# Analysis and Systems Development. ( First Semester of College ).
# This code use Brazilian Portuguese.

# Funções do Código


def menu_principal():  # Função do Menu Principal
    print('----  MENU PRINCIPAL  ----\n[1] - Gerenciar Estudantes.\n[2] - Gerenciar Professores.\n[3] - Gerenciar Disciplinas.\n[4] - Gerenciar Turmas.\n[5] - Gerenciar Matrículas\n[0] - Sair\n--------------------------\n')
    return int(input('\nDigite o MENU que desejá acessar: '))


def menu_operacoes():  # Função do Menu de Operações
    print('[ ----  MENU  ---- ]\n[1] - Incluir\n[2] - Listar\n[3] - Editar\n[4] - Excluir\n[9] - Voltar\n')
    return int(input('Digite a OPERAÇÃO que desejá realizar: '))


def menu_op_matricula():
    print('[ ----  MENU  ---- ]\n[1] - Incluir\n[2] - Listar\n[3] - Excluir\n[9] - Voltar\n')
    return int(input('Digite a OPERAÇÃO que desejá realizar: '))


# Menu de operações feito em formato de função.
def proc_menu_op(opcao_operacoes, arquivo):
    match opcao_operacoes:
        case 1:
            incluir(arquivo)
        case 2:
            listar(arquivo)
        case 3:
            codigo = int(input('Digite o código a ser EDITADO: '))
            editar(codigo, arquivo)
        case 4:
            codigo = int(input('Digite o código a ser EXCLUIDO: '))
            excluir(codigo, arquivo)
        case 9:
            print('\nVoltando ao menu principal!\n')
            return False
        case _:
            print('Opção Inválida, Tente Novamente.')

    return True


def proc_menu_disciplinas(opcao_operacoes, arquivo):
    match opcao_operacoes:
        case 1:
            incluir_disciplina(arquivo)
        case 2:  # Listar
            listar_disciplina(arquivo)
        case 3:  # Editar
            codigo = int(input('Digite o código a ser EDITADO: '))
            editar_disciplina(codigo, arquivo)
        case 4:  # Excluir
            codigo = int(input('Digite o código a ser EXCLUIDO: '))
            excluir_disciplina(codigo, arquivo)
        case 9:  # Voltar
            print('\nVoltando ao menu principal!\n')
            return False
        case _:
            print('Opção Inválida, Tente Novamente.')

    return True


# Menu de operações feito em formato de função.
def proc_menu_turmas(opcao_operacoes, arquivo):
    match opcao_operacoes:
        case 1:
            incluir_turma(arquivo)
        case 2:  # Listar
            listar_turma(arquivo)
        case 3:  # Editar
            codigo = int(input('Digite o código a ser EDITADO: '))
            editar_turma(codigo, arquivo)
        case 4:  # Excluir
            codigo = int(input('Digite o código a ser EXCLUIDO: '))
            excluir_turma(codigo, arquivo)
        case 9:  # Voltar
            print('\nVoltando ao menu principal!\n')
            return False
        case _:
            print('Opção Inválida, Tente Novamente.')

    return True


# Menu de operações feito em formato de função.
def proc_menu_mat(opcao_operacoes, arquivo):
    match opcao_operacoes:
        case 1:  # Incluir
            incluir_matricula(arquivo)
        case 2:  # Listar
            listar_matricula(arquivo)
        case 3:  # Excluir
            codigo = int(input('Digite a matricula a ser EXCLUIDA: '))
            excluir_matricula(codigo, arquivo)
        case 9:  # Voltar
            print('\nVoltando ao menu principal!\n')
            return False
        case _:
            print('Opção Inválida, Tente Novamente.')

    return True


def incluir(arquivo):  # Inclusão
    codigo = int(input('Digite o código a ser incluido: '))
    nome = input('Digite o nome a ser incluido: ')
    cpf = input('Digite o CPF a ser inserido: ')
    dc = {  # Definição do dicionário com os dados.
        'Codigo': codigo,
        'Nome': nome,
        'CPF': cpf
    }

    lista = ler(arquivo)
    lista.append(dc)
    salvar(lista, arquivo)


def listar(arquivo):  # Listagem
    lista = ler(arquivo)
    if len(lista) == 0:
        print('Não há ninguém cadastrado.')
    else:
        for i in range(len(lista)):
            print(f'{lista[i]}')

    input('\nPressione ENTER para continuar!')


def editar(codigo, arquivo):  # Edição
    lista = ler(arquivo)
    for item in lista:
        if item['Codigo'] == codigo:
            item['Nome'] = input('Digite o novo nome: ')
            item['CPF'] = input('Digite o novo CPF: ')
            salvar(lista, arquivo)
            return
    print('Código não encontrado!')

    input('\nPressione ENTER para continuar')


def excluir(codigo, arquivo):  # Exclusão
    lista = ler(arquivo)
    remover = None
    for item in lista:
        if item['Codigo'] == codigo:
            remover = item
            break
    if remover is not None:
        lista.remove(remover)
        salvar(lista, arquivo)
    else:
        print('Código não encontrado. ')

    input('\nPressione ENTER para continuar')


def incluir_disciplina(arquivo):
    codigo_disciplina = int(input('Digite o código da disciplina: '))
    nome = input('Digite o nome da disciplina: ')
    dcd = {
        'Codigo': codigo_disciplina,
        'Nome': nome
    }
    lista = ler(arquivo)
    lista.append(dcd)
    salvar(lista, arquivo)


def listar_disciplina(arquivo):
    lista = ler(arquivo)
    if len(lista) == 0:
        print('Ainda não há disciplinas cadastradas!')
    else:
        for i in range(len(lista)):
            print(f'{lista[i]}')

    input('\n Pressione ENTER para continuar\n')


def editar_disciplina(codigo, arquivo):
    lista = ler(arquivo)
    for item in lista:
        if item['Codigo'] == codigo:
            item['Nome'] = input('Digite o novo nome da disciplina: ')
            salvar(lista, arquivo)
            return
    print('Código não encontrado!')


def excluir_disciplina(codigo, arquivo):
    lista = ler(arquivo)
    remover = None
    for item in lista:
        if item['Codigo'] == codigo:
            remover = item
            break
    if remover is not None:
        lista.remove(remover)
        salvar(lista, arquivo)
    else:
        print('Código da disciplina não encontrado!')

    input('\n Pressione ENTER para continuar')


def incluir_turma(arquivo):
    lista = ler(arquivo)
    codigo_turma = int(input('Digite o código da turma: '))
    codigo_professor = int(input('Digite o código do professor tutor: '))
    codigo_disciplina = int(input('Digite o código da disciplina: '))
    for item in lista:
        if item['CodigoTurma'] == codigo_turma:
            print(
                '\nCodigo da turma já utilizado!\nTente novamente com OUTRO CÓDIGO DE TURMA!\n')
            break
    else:
        dct = {
            'CodigoTurma': codigo_turma,
            'CodigoProfessor': codigo_professor,
            'CodigoDisciplina': codigo_disciplina
        }
        lista.append(dct)
        salvar(lista, arquivo)


def listar_turma(arquivo):
    lista = ler(arquivo)
    if len(lista) == 0:
        print('\nAinda não há turmas cadastradas!\n')
    else:
        for i in range(len(lista)):
            print(f'{lista[i]}')


def editar_turma(codigo, arquivo):
    lista = ler(arquivo)
    for item in lista:
        if item['CodigoTurma'] == codigo:
            item['CodigoProfessor'] = int(
                input('Digite o novo codigo do professor tutor: '))
            item['CodigoDisciplina'] = int(
                input('Digite o codigo da disciplina da turma: '))
            salvar(lista, arquivo)
            return
    print('Código não encontrado!')


def excluir_turma(codigo, arquivo):
    lista = ler(arquivo)
    remover = None
    for item in lista:
        if item['CodigoTurma'] == codigo:
            remover = item
            break
    if remover is not None:
        lista.remove(remover)
        salvar(lista, arquivo)
    else:
        print('Código da disciplina não encontrado!')

    input('\n Pressione ENTER para continuar')


# Diferença do outros código é que ele não via se havia a existencia de um código de turma existente ou de estudante!
def incluir_matricula(arquivo):
    # Por conta disto enviei dois códigos, já que no PDF de TEMPLATE fiquei em dúvidas de como seria o resultado esperado!
    listaTurma = ler(arquivo_turmas)
    # Enviei as duas formas! Espero que não seja problemas Professor Galbas! Agradeço a Compreensão!
    codigo_turma = int(input('Digite o código da turma: '))
    turma_existente = [registro['CodigoTurma'] for registro in listaTurma]
    if codigo_turma not in turma_existente:
        print('\nNão encotrei este código de turma. Verifique e tente novamente!')
        return

    codigo_estudante = int(input('Digite o código do estudante: '))
    listaEstudante = ler(arquivo_estudantes)
    aluno_existente = [registro['Codigo'] for registro in listaEstudante]
    if codigo_estudante not in aluno_existente:
        print('\nNão encotrei este código de estudante. Verifique e tente novamente!')
        return

    matricula = int(str(codigo_turma) + str(codigo_estudante))
    lista = ler(arquivo)

    matriculas_existentes = [registro['Matricula'] for registro in lista]
    if matricula in matriculas_existentes:
        print('\nCódigo de matricula repetido. Não é permitido.\n')
        return

    dct = {
        'Matricula': matricula
    }

    lista.append(dct)
    salvar(lista, arquivo)


def listar_matricula(arquivo):
    lista = ler(arquivo)
    if len(lista) == 0:
        print('\nAinda não há matriculas cadastradas!\n')
    else:
        for i in range(len(lista)):
            print(f'{lista[i]}')


def excluir_matricula(codigo, arquivo):  # Exclusão
    lista = ler(arquivo)
    remover = None
    for item in lista:
        if item['Matricula'] == codigo:
            remover = item
            break
    if remover is not None:
        lista.remove(remover)
        salvar(lista, arquivo)
    else:
        print('Código não encontrado. ')

    input('\nPressione ENTER para continuar')


# Parte de JSON apresentada na SEMANA 7 RACIOCINIO COMPUTACIONAL.

def salvar(lista, arquivo):  # Salva em arquivo JSON.
    with open(arquivo, 'w') as f:
        json.dump(lista, f)


def ler(arquivo):   # Lê o arquivo salvo, se não existir retorna lista vazia.
    try:
        with open(arquivo, 'r') as f:
            lista = json.load(f)

        return lista
    except:
        return []


arquivo_estudantes = 'estudantes.json'  # Variável do arquivo de estudantes.
arquivo_professores = 'professores.json'  # Varíavel do arquivo professores.
arquivo_disciplinas = 'disciplinas.json'  # Varíavel do arquivo disciplina.
arquivo_turmas = 'turmas.json'  # Varíavel do arquivo turmas.
arquivo_matriculas = 'matricula.json'  # Varíavel do arquivo matriculas.

while True:  # Loop menu principal
    try:
        opcao_menu_principal = menu_principal()
        if opcao_menu_principal == 1:  # Menu ESTUDANTES OK
            print('\nVocê escolheu o menu de ESTUDANTES.\n')
            while True:
                opcao_operacoes = menu_operacoes()
                if not proc_menu_op(opcao_operacoes, arquivo_estudantes):
                    break
        elif opcao_menu_principal == 2:  # Menu Professores OK
            print('\nVocê escolheu o menu de PROFESSORES.\n')
            while True:
                opcao_operacoes = menu_operacoes()
                if not proc_menu_op(opcao_operacoes, arquivo_professores):
                    break
        elif opcao_menu_principal == 3:  # Menu Disciplinas OK
            print('\nVocê escolheu o menu de DISCIPLINAS.\n')
            while True:
                opcao_operacoes = menu_operacoes()
                if not proc_menu_disciplinas(opcao_operacoes, arquivo_disciplinas):
                    break
        elif opcao_menu_principal == 4:  # Menu Turmas OK
            print('Você escolheu o menu TURMAS')
            while True:
                opcao_operacoes = menu_operacoes()
                if proc_menu_turmas(opcao_operacoes, arquivo_turmas):
                    break
        elif opcao_menu_principal == 5:  # Menu Matriculas OK
            while True:
                opcao_operacoes = menu_op_matricula()
                if not proc_menu_mat(opcao_operacoes, arquivo_matriculas):
                    break
        elif opcao_menu_principal == 0:
            print('\nVocê escolheu sair!')
            break
        else:
            print('\nOpção Inválida!\n')
            input('Pressione ENTER para continuar.')
    except ValueError:  # Caso receba um valor fora do que a variavel recebe, aparecerá mensagem de erro
        print('\nOpção Inválida!\n')
