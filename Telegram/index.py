from PyQt5 import uic, QtWidgets
from Telegram.setup import configuracoes
from db.ler import leitura
from db.inserir import salvar
from db.apagar import deletar
from pathlib import Path, PureWindowsPath, PurePosixPath
from os import remove

apagando = []


def autenticacao():
    token = inicial.token.text()

    if token == '':
        menu.show()
        inicial.close()

    else:
        print('ERRO 1')


def lista_numeros_telegram():
    tela_numeros_telegram.show()
    dados = leitura()
    tela_numeros_telegram.listaNumeros.clear()

    try:
        for t in dados:
            tela_numeros_telegram.listaNumeros.addItem(f"{t[1]} - {t[2]}")
    except TypeError:
        pass

    tela_numeros_telegram.listaNumeros.itemClicked.connect(item)


def item(item):
    text = item.text()
    text_formatado = text.split('-')[0].strip()
    apagando.append(text_formatado)


def excluir():
    aexcluir = apagando[-1]
    local = str(Path.cwd())
    url = PureWindowsPath(local[0:-8] + '/credenciais/' + aexcluir + '.data')
    try:
        remove(url)
        deletar(aexcluir)
        apagando.clear()
        tela_numeros_telegram.close()

    except FileNotFoundError:
        url = PurePosixPath(local[0:-8] + '/credenciais/' + aexcluir + '.data')
        remove(url)
        deletar(aexcluir)
        apagando.clear()
        tela_numeros_telegram.close()


def addicionar():
    add.show()


def salvarnum():
    num = add.tela_numeros_telegram.text()

    if str(num).isnumeric():
        if len(str(num)) == 11:
            # salvar(str(num).strip())
            # add.notificacao.setText('Número Cadastrado')
            add.tela_numeros_telegram.setText('')
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


def enviar():
    idx = telegram.id.text()
    hashx = telegram.hash.text()
    telefone = telegram.telefone.text()

    configuracoes(idx, hashx, telefone)
    salvar(telefone, 'Ativado')
    telegram.notificacao.setText('Configuração Realizada')

    telegram.id.setText('')
    telegram.hash.setText('')
    telegram.telefone.setText('')


app = QtWidgets.QApplication([])
inicial = uic.loadUi('../UIs/inicio.ui')
inicial.validar.clicked.connect(autenticacao)

menu = uic.loadUi('../UIs/menu.ui')
menu.actionVer_N_meros.triggered.connect(lista_numeros_telegram)
# menu.actionInserir.triggered.connect(lista_numeros_telegram)
menu.actionTransferir.triggered.connect(telegram)

tela_numeros_telegram = uic.loadUi('../UIs/numeros.ui')
tela_numeros_telegram.adicionar.clicked.connect(addicionar)
tela_numeros_telegram.remover.clicked.connect(excluir)

contatos = uic.loadUi('../UIs/contatos.ui')

telegram = uic.loadUi('../UIs/transf.ui')
telegram.registrar.clicked.connect(enviar)

add = uic.loadUi('../UIs/addnum.ui')
add.adicionar.clicked.connect(salvarnum)

inicial.show()
app.exec()
