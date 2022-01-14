dados = []


def salvar(numero):
    with open('dados.txt', 'a') as file:
        file.write(f'{numero} - Ativado\n')
        file.close()


def ler():
    try:
        with open('dados.txt', 'r') as file:
            for c in file:
                dados.append(str(c).strip())
            file.close()
    except FileNotFoundError:
        with open('dados.txt', 'a') as file:
            file.close()
