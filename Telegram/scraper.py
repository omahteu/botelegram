from csv import writer
from os import system
from sys import exit
from time import sleep
from configparser import RawConfigParser

from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty

cpass = RawConfigParser()
cpass.read('config.data')  # Buscar em credenciais

try:
    api_id = cpass['cred']['id']
    api_hash = cpass['cred']['hash']
    phone = cpass['cred']['phone']
    client = TelegramClient(phone, int(api_id), api_hash)
except KeyError:
    system('clear')
    print("[!] run python3 setup.py first !!\n")
    exit(1)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    system('clear')
    client.sign_in(phone, input('[+] Enter the code: '))

system('clear')
chats = []
last_date = None
chunk_size = 200
groups = []

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

print('[+] Choose a group to scrape members :')
i = 0
for g in groups:
    print('[' + str(i) + ']' + ' - ' + g.title)
    i += 1

print('')
g_index = input("[+] Enter a Number : ")
target_group = groups[int(g_index)]

print('[+] Fetching Members...')
sleep(1)
all_participants = []
all_participants = client.get_participants(target_group, aggressive=True)

print('[+] Saving In file...')
sleep(1)
with open("members.csv", "w", encoding='UTF-8') as f:
    writer = writer(f, delimiter=",", lineterminator="\n")
    writer.writerow(['username', 'user id', 'access hash', 'name', 'group', 'group id'])
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
        writer.writerow([username, user.id, user.access_hash, name, target_group.title, target_group.id])
print('[+] Members scraped successfully. Subscribe Termux Professor Youtube Channel For Add Members')
