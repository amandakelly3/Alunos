from time import sleep

def adiciona_aluno(turma):
    aluno = input('Digite o nome do aluno: ')
    if aluno in turma:
        print('Aluno já existe')
        sleep(0.5)
    else:
        turma[aluno] = []
        print('aluno adicionado')
        sleep(0.5)


def adiciona_nota(turma):
    aluno = input('Digite o nome do aluno: ')
    if aluno in turma:
        if len(turma[aluno]) == 0:
            n1 = float(input('Digite a primeira nota: '))
            if n1 > 10.0:
                n1 = input('Digite uma nota válida: ')
            else:
                turma[aluno].append(n1)
            n2 = float(input('Digite a segunda nota: '))
            if n2 > 10.0:
                n2 = input('Digite uma nota válida: ')
            else:
                turma[aluno].append(n2)
            n3 = float(input('Digite a terceira nota: '))
            if n3 > 10.0:
                n3 = input('Digite uma nota válida: ')
            else:
                turma[aluno].append(n3)
        print('Notas já adicionadas')
        sleep(0.5)
    else:
        print('Aluno não existe')
        sleep(0.5)


def remove_aluno(turma):
    aluno = input('Digite o nome do aluno: ')
    if aluno in turma:
        del turma[aluno]
        print('Removido com sucesso')
        sleep(0.5)
    else:
        print('Aluno não existe')
        sleep(0.5)


def remove_nota(turma):
    aluno = input('Digite o nome do aluno: ')
    nota = int(input('Qual nota remover? [1,2,3] '))
    if aluno in turma:
        if nota == 1:
            turma[aluno].pop(0)
            print('Remoção concluída')
            sleep(0.5)
        elif nota == 2:
            turma[aluno].pop(1)
            print('Remoção concluída')
            sleep(0.5)
        elif nota == 3:
            turma[aluno].pop(2)
            print('Remoção concluída')
            sleep(0.5)
    else:
        print('Aluno não existe')
        sleep(0.5)


def edita_aluno(turma):
    nome = input('Digite o nome a editar: ')
    novo_nome = input('Digite um novo nome: ')
    if nome in turma:
        turma[novo_nome] = turma[nome]
        del turma[nome]
        print('Edição feita com sucesso')
        sleep(0.5)
    else:
        print('Aluno não existe')
        sleep(0.5)


def edita_nota(turma):
    aluno = input('Digite o nome do aluno: ')
    if aluno in turma:
        pos = int(input('Qual nota editar? [1,2,3] '))
        nota = float(input('Digite a nova nota: '))
        if pos == 1:
            turma[aluno].insert(pos - 1, nota)
            turma[aluno].pop(1)
            print("Nota editada")
            sleep(0.5)
        if pos == 2:
            turma[aluno].insert(pos - 1, nota)
            turma[aluno].pop(2)
            print("Nota editada")
            sleep(0.5)
        if pos == 3:
            turma[aluno].insert(pos - 1, nota)
            turma[aluno].pop(3)
            print('Nota editada')
            sleep(0.5)
    else:
        print('Aluno não existe')
        sleep(0.5)


def busca_aluno(turma):
    aluno = input('Digite um nome a buscar: ')
    for nome in turma:
        if nome.startswith(aluno):
            soma = sum(turma[nome])
            media = soma / 3
            print('%s. Notas: %s. Média: %.1f' % (nome, turma[nome], media))
            sleep(0.5)


def media_turma(turma):
    total = 0
    d = 0
    somar = 0
    dividir = 0
    for nome in turma:
        somar = sum(turma[nome])
        dividir = len(turma[nome])
        total += somar
        dividir += d

    media = somar / dividir
    print('Média da turma: %.1f' % (media))
    sleep(0.5)


def melhor_aluno(turma):
    media_dos_alunos = []
    for nome, notas in turma.items():
        media_dos_alunos.append([nome, *notas, round(sum(notas) / 3, 1)])
    alunos_ordenados = sorted(media_dos_alunos, key=lambda estudante: estudante[-1], reverse=True)

    alunos_ordenados_formatado = []

    for estudante in alunos_ordenados:
        nome, nota1, nota2, nota3, media = estudante
        alunos_ordenados_formatado.append([nome, nota1, nota2, nota3, f'Com média: {media}'])

    print("O melhor aluno: ", alunos_ordenados_formatado[0])
    sleep(0.5)


def alunos_ordemalfa(turma):
    nomes = list(turma.keys())
    nomes.sort()

    for nome in nomes:
        print('%s. Notas: %s. Média: %.1f.' % (nome, turma[nome], sum(turma[nome]) / 3))
        sleep(0.5)


def alunos_ordemnota(turma):
    media_dos_alunos = []
    for nome, notas in turma.items():
        media_dos_alunos.append([nome, *notas, round(sum(notas) / 3, 1)])
    alunos_ordenados = sorted(media_dos_alunos, key=lambda estudante: estudante[-1], reverse=True)

    alunos_ordenados_formatado = []

    for estudante in alunos_ordenados:
        nome, nota1, nota2, nota3, media = estudante
        alunos_ordenados_formatado.append([nome, nota1, nota2, nota3, f'Com média: {media}'])

    print(alunos_ordenados_formatado)
    sleep(0.5)


def alunos_aprovados(turma):
    nomes = list(turma.keys())
    for nome in nomes:
        media = sum(turma[nome]) / 3
        if media >= 7:
            print('%s. Notas: %s. Média: %.1f = Aprovado' % (nome, turma[nome], media))
            sleep(0.5)
        else:
            pass


def alunos_final(turma):
    nomes = list(turma.keys())
    for nome in nomes:
        media = sum(turma[nome]) / 3
        if media >= 5 and media < 6.9:
            print('%s. Notas: %s. Média: %.1f = Na Final' % (nome, turma[nome], media))
            sleep(0.5)
        else:
            pass


def alunos_reprovados(turma):
    nomes = list(turma.keys())
    for nome in nomes:
        media = sum(turma[nome]) / 3
        if media < 5:
            print('%s. Notas: %s. Média: %.1f = Reprovado' % (nome, turma[nome], media))
            sleep(0.5)
        else:
            pass


turma = {}
opcao = int(input('1- Adicionar aluno\n2- Adicionar nota\n3- Remover aluno\n4- Remover nota\n5- Editar nome aluno\n6- Editar nota aluno\n7- Buscar aluno por nome\n8- Calcular média da turma\n9- Exibir melhor aluno\n10- Exibir alunos em ordem alfabética\n11- Exibir aluno por ordenados por nota\n12- Exibir alunos aprovados por média\n13- Exibir alunos na final\n14- Exibir alunos reprovados\n15- Encerrar\n'))
while opcao != 15:
    if opcao == 1:
        adiciona_aluno(turma)
    elif opcao == 2:
        adiciona_nota(turma)
    elif opcao == 3:
        remove_aluno(turma)
    elif opcao == 4:
        remove_nota(turma)
    elif opcao == 5:
        edita_aluno(turma)
    elif opcao == 6:
        edita_nota(turma)
    elif opcao == 7:
        busca_aluno(turma)
    elif opcao == 8:
        media_turma(turma)
    elif opcao == 9:
        melhor_aluno(turma)
    elif opcao == 10:
        alunos_ordemalfa(turma)
    elif opcao == 11:
        alunos_ordemnota(turma)
    elif opcao == 12:
        alunos_aprovados(turma)
    elif opcao == 13:
        alunos_final(turma)
    elif opcao == 14:
        alunos_reprovados(turma)

    opcao = int(input('1- Adicionar aluno\n2- Adicionar nota\n3- Remover aluno\n4- Remover nota\n5- Editar nome aluno\n6- Editar nota aluno\n7- Buscar aluno por nome\n8- Calcular média da turma\n9- Exibir melhor aluno\n10- Exibir alunos em ordem alfabética\n11- Exibir aluno por ordenados por nota\n12- Exibir alunos aprovados por média\n13- Exibir alunos na final\n14- Exibir alunos reprovados\n15- Encerrar\n').center(100))
