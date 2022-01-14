from PyQt5 import uic, QtWidgets
from Telegram.setup import configuracoes
from Telegram.box import salvar, ler, dados


def autenticacao():
    token = inicial.token.text()

    if token == '':
        menu.show()
        inicial.close()

    else:
        print('ERRO 1')


def lista_numeros():
    numero.show()
    dados.clear()

    ler()
    qtd = len(dados)

    numero.listWidget.clear()

    for t in dados[0: qtd]:
        numero.listWidget.addItem(t)


def addicionar():
    add.show()


def salvarnum():
    num = add.numero.text()

    if str(num).isnumeric():
        if len(str(num)) == 11:
            # salvar(str(num).strip())
            # add.notificacao.setText('Número Cadastrado')
            add.numero.setText('')
            telegram.show()
            telegram.numero.setText(f"+55{num}")
            telegram.telefone.setText(f"+55{num}")
            add.close()

        else:
            add.notificacao.setText('Número Inválido')
    else:
        add.notificacao.setText('Formato Inválido')


def lista_inserir_contatos():
    contatos.show()


def telegram():
    telegram.show()
    telegram.listWidget.addItem('1. Acesse o site: https://my.telegram.org/auth, cria sua conta e insira os dados nos '
                                'campos ao lado.\n2. Após preencher todos os campos disponíveis clique em ENVIAR.\n'
                                '3. Ao receber a confirmação o número já está registrado e pronto para uso.')


def printi():
    tex = numero.listWidget.selectedItems()
    for nn in tex:
        nume = nn.text()
        nume_formatado = nume.split('-')[0].strip()


def enviar():
    idx = telegram.id.text()
    hashx = telegram.hash.text()
    telefone = telegram.telefone.text()

    configuracoes(idx, hashx, telefone)
    salvar(telefone)
    telegram.notificacao.setText('Configuração Realizada')

    telegram.id.setText('')
    telegram.hash.setText('')
    telegram.telefone.setText('')


app = QtWidgets.QApplication([])
inicial = uic.loadUi('UIs/inicio.ui')
inicial.validar.clicked.connect(autenticacao)

menu = uic.loadUi('UIs/menu.ui')
menu.actionVer_N_meros.triggered.connect(lista_numeros)
menu.actionInserir.triggered.connect(lista_numeros)
menu.actionTransferir.triggered.connect(telegram)

numero = uic.loadUi('UIs/numeros.ui')
numero.adicionar.clicked.connect(addicionar)
numero.print.clicked.connect(printi)

contatos = uic.loadUi('UIs/contatos.ui')

telegram = uic.loadUi('UIs/transf.ui')
telegram.registrar.clicked.connect(enviar)

add = uic.loadUi('UIs/addnum.ui')
add.adicionar.clicked.connect(salvarnum)


inicial.show()
app.exec()






# import configparser
# config = configparser.ConfigParser()
# config.read('+5585999831355.data')
# print(str(config['cred']['id']).strip())
