from csv import writer
from os import system
from sys import exit
from configparser import RawConfigParser

from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty


# cpass = RawConfigParser()
# cpass.read(arquivo)
#
# try:
#     api_id = str(cpass['cred']['id']).strip()
#     api_hash = str(cpass['cred']['hash']).strip()
#     phone = str(cpass['cred']['phone']).strip()
#     client = TelegramClient(phone, int(api_id), api_hash)
# except KeyError:
#     system('clear')
#     # print("run python3 setup.py first !!\n")
#     exit(1)
#
# client.connect()
# if not client.is_user_authorized():
#     client.send_code_request(phone)
#     system('clear')
#     client.sign_in(phone, input('Enter the code: '))
#
# system('clear')
# chats = []
# last_date = None
# chunk_size = 200
# groups = []
#
# result = client(GetDialogsRequest(
#     offset_date=last_date,
#     offset_id=0,
#     offset_peer=InputPeerEmpty(),
#     limit=chunk_size,
#     hash=0
# ))
# chats.extend(result.chats)

# for chat in chats:
#     try:
#         if chat.megagroup:
#             groups.append(chat)
#     except:
#         continue
#
# print('Escolha um grupo para raspar os membros :')

# for g in groups:
#     print(g.title)

# g_index = input("Enter a Number : ")
# target_group = groups[int(g_index)]
#
# print('Fetching Members...')
# sleep(1)
# all_participants = []
# all_participants = client.get_participants(target_group, aggressive=True)
#
# print('Saving In file...')
# sleep(1)
# with open("members.csv", "w", encoding='UTF-8') as f:
#     writer = writer(f, delimiter=",", lineterminator="\n")
#     writer.writerow(['username', 'user id', 'access hash', 'name', 'group', 'group id'])
#     for user in all_participants:
#         if user.username:
#             username = user.username
#         else:
#             username = ""
#         if user.first_name:
#             first_name = user.first_name
#         else:
#             first_name = ""
#         if user.last_name:
#             last_name = user.last_name
#         else:
#             last_name = ""
#         name = (first_name + ' ' + last_name).strip()
#         writer.writerow([username, user.id, user.access_hash, name, target_group.title, target_group.id])
# print('Members scraped successfully. Subscribe Termux Professor Youtube Channel For Add Members')
chats = []
groups = []
all_participants = []


class Scraper:
    def __init__(self, arquivo):
        self.codigo = None
        self.phone = None
        self.grupo = None
        self.arquivo = arquivo

    def carregar_arquivo(self):
        cpass = RawConfigParser()
        cpass.read(self.arquivo)

        try:
            api_id = str(cpass['cred']['id']).strip()
            api_hash = str(cpass['cred']['hash']).strip()
            phone = str(cpass['cred']['phone']).strip()
            client = TelegramClient(phone, int(api_id), api_hash)
            client.connect()
            print('caer')
            return client
        except KeyError:
            system('clear')
            # print("run python3 setup.py first !!\n")
            exit(1)

    def autenticar(self, phone):
        self.phone = phone
        client = self.carregar_arquivo()
        if not client.is_user_authorized():
            client.send_code_request(self.phone)
            return client

    def cfm(self, phone, codigo):
        self.phone = phone
        system('clear')
        client = self.autenticar(self.phone)
        client.sign_in(phone, codigo)

        system('clear')

        last_date = None
        chunk_size = 200

        result = client(GetDialogsRequest(
            offset_date=last_date,
            offset_id=0,
            offset_peer=InputPeerEmpty(),
            limit=chunk_size,
            hash=0
        ))
        chats.extend(result.chats)

        for chat in chats:
            try:
                if chat.megagroup:
                    groups.append(chat)
            except:
                continue

        return client

    def coleta(self, grupo, phone, codigo):
        self.grupo = grupo
        self.phone = phone
        self.codigo = codigo
        client = self.cfm(self.phone, self.codigo)

        g_index = grupo
        target_group = groups[int(g_index)]

        all_participants = client.get_participants(target_group, aggressive=True)

        with open("members.csv", "w", encoding='UTF-8') as f:
            write = writer(f, delimiter=",", lineterminator="\n")
            write.writerow(['username', 'user id', 'access hash', 'name', 'group', 'group id'])
            for user in all_participants:
                if user.username:
                    username = user.username
                else:
                    username = ""
                if user.first_name:
                    first_name = user.first_name
                else:
                    first_name = ""
                if user.last_name:
                    last_name = user.last_name
                else:
                    last_name = ""
                name = (first_name + ' ' + last_name).strip()
                write.writerow([username, user.id, user.access_hash, name, target_group.title, target_group.id])
        print('Members scraped successfully.')
