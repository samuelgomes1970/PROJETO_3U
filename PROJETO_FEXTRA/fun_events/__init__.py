import matplotlib.pyplot as plt

def verificar_senha(senha1, senha2):
    return senha1 == senha2


def verificar_user_existente(email, users):
    return email in users

def verificar_email_valido(email):
    return '@' in email

def verificar_titulo_evento(nomeevento, events):
    return nomeevento.lower() in events

def verificar_email_senha(emailcadastrado, senhacadastrada, users):
    emailcadastrado = emailcadastrado.strip()
    senhacadastrada = senhacadastrada.strip()

    if emailcadastrado in users:
        return users[emailcadastrado] == senhacadastrada
    return False

def cadastrar_usuario(users):
    nome = input('Digite seu nome: ').strip()
    if not nome:
        print('Nome não pode ser vazio.')
        return

    email = input('Digite seu e-mail: ').lower().strip()
    while not verificar_email_valido(email):
        print('E-mail inválido. O e-mail deve conter "@"')
        email = input('Digite um e-mail válido: ').lower().strip()

    while verificar_user_existente(email, users):
        print('Este e-mail já existe, digite novamente seu e-mail:')
        email = input('Digite seu e-mail: ').lower().strip()

    senha = input('Digite sua senha: ').strip()
    senha2 = input('Repita sua senha: ').strip()

    while not verificar_senha(senha, senha2):
        print('As senhas não coincidem. Tente novamente.')
        senha = input('Digite sua senha: ').strip()
        senha2 = input('Repita sua senha: ').strip()


    users[email] = senha
    print('=' * 50)
    print('USUÁRIO CADASTRADO COM SUCESSO')
    print(f'BEM-VINDO(A), {nome}')
    print('=' * 50)

def login_usuario(users):
    emailcadastrado = input('Digite o seu e-mail: ').lower().strip()
    senhacadastrada = input('Digite a sua senha: ').strip()

    if verificar_email_senha(emailcadastrado, senhacadastrada, users):
        print('=' * 50)
        print('Usuário logado com sucesso')
        print('=' * 50)
        return emailcadastrado
    else:
        print('=' * 50)
        print('E-mail ou senha incorretos, Tente novamente')
        print('=' * 50)
        return False

def cadastrar_evento(email_logado, events):
    titulo = input('Digite o título do evento: ').lower().strip()
    descricao = input('Digite a descrição do evento: ').strip()
    data = input('Digite a data do evento (DD/MM/AAAA): ').strip()
    local = input('Digite o local do evento: ').strip()

    while True:
        valor = input('Digite o valor do evento: ')
        if valor.isnumeric():
            valor = float(valor)
            break
        else:
            print('Valor inválido. Por favor, insira um número válido.')

    evento = {'criador': email_logado, 'titulo': titulo, 'descricao': descricao, 'data': data, 'local': local, 'valor': valor, 'participantes': []}
    events[titulo] = evento
    print(f'Evento "{titulo}" cadastrado com sucesso!')

def remover_evento(email, titulo, eventos):
    if titulo in eventos and eventos[titulo]['criador'] == email:
        del eventos[titulo]
        print('=' * 50)
        print(f'Evento "{titulo}" removido com sucesso')
        print('=' * 50)
        return True
    print('Evento não encontrado ou você não é o criador')
    return False

def participar_evento(email, titulo, eventos):
    if titulo in eventos:
        evento = eventos[titulo]
        if email not in evento['participantes']:
            evento['participantes'].append(email)
            print('=' * 50)
            print('Inscrição realizada com sucesso')
            print('=' * 50)
        else:
            evento['participantes'].remove(email)
            print('=' * 50)
            print('Inscrição cancelada com sucesso')
            print('=' * 50)
        return True
    print('Evento não encontrado')
    return False

def listar_participantes_evento(email, titulo, eventos):
    if titulo in eventos:
        evento = eventos[titulo]
        if evento['criador'] == email:
            if evento['participantes']:
                print(f'Participantes do evento {titulo}:')
                for participante in evento['participantes']:
                    print(participante)
            else:
                print(f'Não há participantes cadastrados para o evento {titulo}')
            return True
        else:
            print('Voce não é o criador deste evento,Apenas o criador pode listar os participantes')
            return False
    print('Evento não encontrado')
    return False

def verificar_valor_arrecadado(email, titulo, eventos):
    if titulo in eventos and eventos[titulo]['criador'] == email:
        evento = eventos[titulo]
        num_inscritos = len(evento['participantes'])
        valor_por_participante = evento['valor']
        total_arrecadado = num_inscritos * valor_por_participante

        print(f'Número de inscritos: {num_inscritos}')
        print(f'Valor por participante: R${valor_por_participante:.2f}')
        print(f'Total arrecadado: R${total_arrecadado:.2f}')
        return True
    print('Evento não encontrado ou você não é o criador')
    return False

def filtrar_eventos_por_valor(valor_maximo, eventos):
    print(f'Eventos com valor até R${valor_maximo:.2f}:')
    for evento in eventos.values():
        if evento['valor'] <= valor_maximo:
            print(f'{evento["titulo"]} - R${evento["valor"]:.2f}')

def buscar_eventos_por_data(data_inicial, data_final, eventos):
    print(f'Eventos entre {data_inicial} e {data_final}:')
    for evento in eventos.values():
        if data_inicial <= evento['data'] <= data_final:
            print(f'{evento['titulo']} - Data: {evento['data']} - Local: {evento['local']}')


def verificar_usuario_cadastrado(email, users):
    return email in users

def adicionar_participante_diretamente_evento(email_logado, titulo_evento, email_participante, events):
    if titulo_evento in events:
        evento = events[titulo_evento]
        if email_participante not in evento['participantes']:
            evento['participantes'].append(email_participante)
            print(f'Usuário {email_participante} adicionado ao evento {titulo_evento}')
        else:
            print(f'Usuário {email_participante} já está inscrito no evento')
        return True
    print('Evento não encontrado')
    return False

def gerar_grafico_participantes(events):
    nomes_eventos = []
    participantes = []
    for evento in events.values():
        nomes_eventos.append(evento['titulo'])
        participantes.append(len(evento['participantes']))

    plt.bar(nomes_eventos, participantes)
    plt.xlabel('Eventos')
    plt.ylabel('Número de Participantes')
    plt.show()


def listar_participantes_e_salvar_arquivo_txt(email_logado, titulo_evento, eventos):
    if titulo_evento in eventos:
        evento = eventos[titulo_evento]
        if evento['criador'] == email_logado:
            participantes = evento['participantes']
            if participantes:
                with open(f'{titulo_evento}_participantes.txt', "w") as file:
                    file.write(f'Participantes do evento: {titulo_evento}\n\n')
                    for participante in participantes:
                        file.write(f'{participante}\n')
                print(f"Participantes do evento '{titulo_evento}' foram salvos em {titulo_evento}_participantes.txt.")
            else:
                print(f'O evento "{titulo_evento}" não possui participantes')
        else:
            print('apenas o criador do evento pode salvar os arquivos')
    else:
        print('Evento não encontrado')





