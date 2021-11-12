import aminofix as amino
import time
from threading import Thread


print("script by @zefil02")


email = 'почта от аккаунта'
passw = 'пароль от аккаунта'
client = amino.Client()
com = [113383312, 252369385, 59791455, 205668103, 252764515, 101322536, 199796406, 7805841,
       177037843, 40132197, 18112698, 139139023, 166804149, 96047705, 50254034, 65740446, 245558723, 104190758,
       263152124,
       7297362, 246856333, 79230968, 75991221, 40485550, 23503347, 158702123, 46776305, 47088259, 172854462, 124600604,
       256405973, 200885262,
       197509629, 238336683, 156542274, 122468660, 253945005, 261468961, 226808465, 202247760, 89775875, 226429472,
       94952774, 204485934, 257597713,
       115523372, 178054750, 76687965, 12003551, 47981125, 235200375, 1305279, 42900916, 253410987, 219915687,
       226388204, 243789609,
       221851906, 105894570, 246856333, 172854462, 197509629, 204485934, 23727781, 48217134, 231094129, 218791022,
       158702123, 124600604]
def zefilCantor():
    try:
        client.join_community(comId=int(i))
    except:
        pass
while True:
    try:
        client.login(email=email, password=passw)
        for i in com:
            Thread(target=zefilCantor).start()
        break
    except amino.exceptions.VerificationRequired as e:
        while True:
            input(f"пройдите капчу и нажмите Enter")
            try:
                for i in com:
                    Thread(target=zefilCantor()).start()
                break
            except amino.exceptions.VerificationRequired:
                continue
time.sleep(2)
community = client.sub_clients(start=0, size=1000)
for number, name in enumerate(community.name, 1):
    print(f"{number}.{name}")
com = community.comId[int(input("номер сообщества: "))-1]
lvl = int(input("максимальный уровень участников, которые будут приглашены в чат:"))
zefil = """
пиар сообщение
"""
client.join_community(comId=com)
sub_client = amino.SubClient(comId=com,
profile=client.profile)
castel = []
users = sub_client.get_all_users(start=0, size=10)
a = 1
for name, id, level, status in zip(users.profile.nickname,
                                   users.profile.userId,
                                   users.profile.level,
                                   users.profile.role):
    if status == 0 and level <= lvl:
        castel.append(id)
try:
    sub_client.start_chat(userId=castel, message=zefil)
except:
    pass
print('чат создан.')
chat = sub_client.get_chat_threads(size=100)
for number_chat, title in enumerate(chat.title, 1):
 print(f"{number_chat}.{title}")
chatid = chat.chatId[int(input("выберите чат: "))-1]
sub_client.edit_chat(viewOnly=False,
                     chatId=chatid,
                     title='@zefilCantor',
                     content=zefil)
def zefil():
    try:
        sub_client.invite_to_chat(userId=id,
                                  chatId=chatid)
    except:
        pass
print('приглашаю онлайн участников.')
for i in range(0, 5000, 100):
    users = sub_client.get_online_users(start=i, size= 100)
    if users:
        for name, id, level, status in zip(users.profile.nickname,
                                           users.profile.userId,
                                           users.profile.level,
                                           users.profile.role):
            if status == 0 and level <= lvl:
                Thread(target=zefil)
                print(f'приглашён участник {name} с уровнем {level} ')
                a+=1
            else:
                pass
    else:
        break
print('приглашаю участников из общего списка.')
for i in range(0, 10000, 100):
    users = sub_client.get_online_users(start=i, size= 100)
    if users:
        for name, id, level, status in zip(users.profile.nickname,
                                           users.profile.userId,
                                           users.profile.level,
                                           users.profile.role):
            if status == 0 and level <= lvl:
                Thread(target=zefil).start()
                print(f'приглашён участник {name} с уровнем {level} ')
                a+=1
            else:
                pass
    else:
        break
print(f'приглашено {a} участников.')
