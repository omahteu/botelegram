import configparser
import os


# print("[+] Installing requierments ...")
# os.system('python3 -m pip install telethon')
# os.system('pip3 install telethon')


def configuracoes(xid, xhash, xphone):
    os.system(f"touch ../credenciais/{xphone}.data")
    cpass = configparser.RawConfigParser()
    cpass.add_section('cred')
    xid = xid
    cpass.set('cred', 'id', xid)
    xhash = xhash
    cpass.set('cred', 'hash', xhash)
    xphone = xphone
    cpass.set('cred', 'phone', xphone)
    setup = open(f"../credenciais/{xphone}.data", 'w')
    cpass.write(setup)
    setup.close()
    return print('Configuração Realizada!')
