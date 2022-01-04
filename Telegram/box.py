dados = []


def salvar(numero):
    with open('dados.txt', 'a') as file:
        file.write(f'{numero}\n')
        file.close()


def ler():
    with open('dados.txt', 'r') as file:
        for c in file:
            dados.append(str(c).strip())
        file.close()
