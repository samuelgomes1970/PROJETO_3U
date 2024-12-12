from fun_events import * 

users = {}
events = {}

op = -1
while op != 0:
    print('=' * 19)
    print('Bem-vindo à EventoX')
    print('=' * 19)
    print('(1) - Cadastrar usuário')
    print('(2) - Login')
    print('(0) - Sair da aba cadastro')

    while True:
        op = input('Digite a opção desejada: ')
        if op.isnumeric():
            op = int(op)
            if op in [0, 1, 2]:
                break
            else:
                print('Opção inválida. Por favor, escolha uma opção válida.')
        else:
            print('Entrada inválida. Por favor, insira um número.')

    if op == 1:
        cadastrar_usuario(users)

    if op == 2:
        email_logado = login_usuario(users)
        if email_logado:
            sub_op = -1
            while sub_op != 0:
                print('3 - Cadastrar evento')
                print('4 - Buscar eventos')
                print('5 - Listar todos os eventos')
                print('6 - Remover evento')
                print('7 - Participar ou cancelar inscrição em evento')
                print('8 - Listar participantes do meu evento')
                print('9 - Verificar valor arrecadado')
                print('10 - Filtrar eventos por valor')
                print('11 - Buscar eventos por data')
                print('12 - Adicionar participante diretamente ao evento')
                print('13 - Listar participantes e salvar em arquivo de texto')
                print('14 - gerar o grafico dos participantes')
                print('0 - Voltar ao menu principal')

                while True:
                    sub_op = input('Digite a opção desejada: ')
                    if sub_op.isnumeric():
                        sub_op = int(sub_op)
                        if sub_op in [0, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]:
                            break
                        else:
                            print('Opção inválida. Por favor, escolha uma opção válida.')
                    else:
                        print('Entrada inválida! Por favor, insira um número.')

                if sub_op == 3:
                    cadastrar_evento(email_logado, events)

                if sub_op == 4:
                    buscarevento = input('Digite o título do evento desejado: ').lower()
                    if buscarevento in events:
                        print('---------------EVENTO ENCONTRADO---------------')
                        print(events[buscarevento])
                    else:
                        print('Evento não encontrado, tente outra vez')

                if sub_op == 5:
                    if not events:
                        print('Nenhum evento cadastrado')
                    else:
                        for titulo, dados in events.items():
                            print(f'Título: {titulo}, Criador: {dados['criador']}, Descrição: {dados['descricao']}, Data: {dados['data']}, Local: {dados['local']}, Valor: {dados['valor']}')

                if sub_op == 6:
                    titulo_remover = input('Digite o título do evento que deseja remover: ').lower()
                    if remover_evento(email_logado, titulo_remover, events):
                        print('Evento removido com sucesso')

                if sub_op == 7:
                    titulo_inscricao = input('Digite o título do evento: ').lower()
                    participar_evento(email_logado, titulo_inscricao, events)

                if sub_op == 8:
                    titulo_evento = input('Digite o título do evento que deseja listar os participantes: ').lower()
                    listar_participantes_evento(email_logado, titulo_evento, events)

                if sub_op == 9:
                    titulo_evento = input('Digite o título do evento para verificar valor arrecadado: ').lower()
                    verificar_valor_arrecadado(email_logado, titulo_evento, events)

                if sub_op == 10:
                    valor_maximo = int(input('Digite o valor máximo para os eventos: '))
                    filtrar_eventos_por_valor(valor_maximo, events)

                if sub_op == 13:
                    titulo_evento = input(
                        'Digite o título do evento para listar os participantes e salvar em arquivo: ').lower()
                    listar_participantes_e_salvar_arquivo_txt(email_logado, titulo_evento, events)

                if sub_op == 11:
                    data_inicial = input('Digite a data inicial (DD/MM/AAAA):')
                    data_final = input('Digite a data final (DD/MM/AAAA):')
                    buscar_eventos_por_data(data_inicial, data_final, events)

                if sub_op == 12:
                    titulo_evento = input('Digite o título do evento que deseja adicionar participante: ').lower()
                    if titulo_evento in events:
                        email_participante = input('Digite o email do usuário a ser adicionado: ').lower()
                        if verificar_usuario_cadastrado(email_participante, users):
                            adicionar_participante_diretamente_evento(email_logado, titulo_evento, email_participante, events)
                        else:
                            print('Usuário não encontrado na plataforma.')
                    else:
                        print('Evento não encontrado.')

                if sub_op == 14:
                    gerar_grafico_participantes(events)

                if sub_op == 0:
                    print('Voltando ao menu principal...')
                    break
