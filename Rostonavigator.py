import socks
from telethon import TelegramClient,sync
import json
import datetime
import time
import random

api_id = 612708
api_hash = 'f62d0ebf0c9a0b582b02464a5bee904c'
host = "t.geekclass.ru"
port = 7777
proxy = (socks.SOCKS5, host, port, True, 'geek', 'socks')
client = TelegramClient('+79080485104', api_id, api_hash, proxy=proxy)
client.start()
entity = client.get_entity(-348553457)
participants = client.get_participants(entity)
t = str(datetime.datetime.now())
t = int(t[11:13])


i = 0
id_users = []
i_users = []
id_teacher = [670564, 86773763]
for partic in client.iter_participants(entity):
    r = random.randint(1, 23)
    id_users.append([int(partic.id), r])
    i += 1
i = 0
print(id_users)
for i in range(len(id_users)):
    i_users.append(0)
print(i_users)
print(t)
while True:
    if t > 6:
        for partic in client.iter_participants(entity):
            lastname = ""
            if partic.last_name:
                lastname = partic.last_name
            s = str(partic.status)
            s = s[10:12]
            if s == 'On':
                if partic.id not in id_teacher:
                    for i in range(len(id_users)):
                        if id_users[i][0] == partic.id:
                            client.send_message(partic.id, 'Чё не спим?')
                            client.send_message(partic.id, 'Ну все, я звоню Росту!')
                            #client.send_message(86773763, str(partic.first_name) +' '+ str(lastname)+' в '+ str(id_users[i][1]) +' доме')

                print(partic.id,partic.first_name +' '+ lastname,'online')
            else:
                print(partic.id, partic.first_name + ' ' + lastname, 'offline')
                for i in range(len(id_users)):
                    if i_users[i] != 0:
                        i_users[i] = 0

        for i in range(len(id_users)):
            print()
    time.sleep(5)

