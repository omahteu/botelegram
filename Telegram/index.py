from pathlib import Path, PureWindowsPath, PurePosixPath
from Telegram.setup import configuracoes
from PyQt5 import uic, QtWidgets
from db.inserir import salvar
from db.apagar import deleta
from db.ler import leitura
from os import remove
from Telegram.scraper import Scraper, groups

bolsa = []
ram = []
path = []
cod = []
nomes = []


def autenticacao():
    token = login.token.text()

    if token == '':
        menu.show()
        login.close()

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
    texto = item.text()
    texto_formatado = texto.split('-')[0].strip()
    bolsa.append(texto_formatado)


def remover():
    aexcluir = bolsa[-1]
    local = str(Path.cwd())
    url = PureWindowsPath(local[0:-8] + '/credenciais/' + aexcluir + '.data')
    try:
        remove(url)
        deleta(aexcluir)
        bolsa.clear()
        tela_numeros_telegram.close()

    except FileNotFoundError:
        url = PurePosixPath(local[0:-8] + '/credenciais/' + aexcluir + '.data')
        remove(url)
        deleta(aexcluir)
        bolsa.clear()
        tela_numeros_telegram.close()


def sair():
    tela_numeros_telegram.close()


def exibir_adicionar_contato():
    tela_adicionar_contato.show()


def adicionar_contato():
    numero = tela_adicionar_contato.numero.text()

    if str(numero).isnumeric():
        if len(str(numero)) == 11:
            tela_adicionar_contato.numero.setText('')
        else:
            tela_adicionar_contato.notificacao.setText('Número Inválido')
    else:
        tela_adicionar_contato.notificacao.setText('Formato Inválido')


def exibir_registrar():
    tela_adicionar_numero.show()


def registrar():
    numero_telefone = tela_adicionar_numero.numero.text()

    if str(numero_telefone).isnumeric():
        if len(str(numero_telefone)) == 11:
            tela_adicionar_numero.numero.setText('')
            autenticacao.show()
            autenticacao.numero.setText(f"+55{numero_telefone}")
            autenticacao.telefone.setText(f"+55{numero_telefone}")
            tela_adicionar_numero.close()
        else:
            tela_adicionar_numero.notificacao.setText('Número Inválido')
    else:
        tela_adicionar_numero.notificacao.setText('Formato Inválido')


def enviar_autenticacao():
    idx = autenticacao.id.text()
    hashx = autenticacao.hash.text()
    telefone = autenticacao.telefone.text()

    configuracoes(idx, hashx, telefone)
    salvar(telefone, 'Ativado')
    autenticacao.notificacao.setText('Configuração Realizada')

    autenticacao.id.setText('')
    autenticacao.hash.setText('')
    autenticacao.telefone.setText('')


def exibir_passos():
    transicao_um.show()

    n = []

    dados = leitura()
    for obj in dados:
        number = obj[1]
        n.append(number)

    transicao_um.numerosBox.addItems(n)


def passo_um():
    telefone = transicao_um.numerosBox.currentText()
    transicao_um.numerosBox.setDisabled(True)
    transicao_um.lineEdit.setDisabled(False)

    ram.append(telefone)

    url = '../credenciais/+5585999831355.data'
    path.append(url)

    inicializar = Scraper(url)
    inicializar.autenticar(telefone)
    return inicializar


def passo_dois():
    codigo = transicao_um.lineEdit.text()
    numero = ram[-1]
    cod.append(codigo)

    progresso = passo_um()
    progresso.cfm(numero, codigo)
    for za in groups:
        print(za)
    return progresso


def passo_tres():
    client = passo_dois()

    for gp in groups:
        transicao_um.grupoBox.addItems(gp)
        nomes.append(gp)

    grupo = transicao_um.grupoBox.currentText()
    gpo = nomes.index(grupo)
    numero = ram[-1]
    codi = cod[-1]

    print(gpo, numero, codi)
    print('*******************')
    print(nomes)

    # client.coleta(grupo, numero, codi)


app = QtWidgets.QApplication([])

login = uic.loadUi("../UIs/login.ui")
login.validar.clicked.connect(autenticacao)

menu = uic.loadUi("../UIs/menu.ui")
menu.actionVer_N_meros.triggered.connect(lista_numeros_telegram)
menu.actionInserir.triggered.connect(exibir_adicionar_contato)
menu.actionTransferencia.triggered.connect(exibir_passos)

tela_numeros_telegram = uic.loadUi("../UIs/numeros.ui")
tela_numeros_telegram.adicionar.clicked.connect(exibir_registrar)
tela_numeros_telegram.remover.clicked.connect(remover)
tela_numeros_telegram.sair.clicked.connect(sair)

tela_adicionar_numero = uic.loadUi("../UIs/addNumero.ui")
tela_adicionar_numero.adicionar.clicked.connect(registrar)

tela_adicionar_contato = uic.loadUi("../UIs/addContato.ui")
tela_adicionar_contato.adicionar.clicked.connect(adicionar_contato)

autenticacao = uic.loadUi("../UIs/registro.ui")
autenticacao.registrar.clicked.connect(enviar_autenticacao)

transicao_um = uic.loadUi("../UIs/transacao.ui")
transicao_um.avancar.clicked.connect(passo_um)
transicao_um.pushButton.clicked.connect(passo_dois)

login.show()
app.exec()
