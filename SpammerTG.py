from telethon.sync import TelegramClient, events

print("""Telegram: @Termuxtop \n
	 	 Telegram: @Termuxtop \n
		 Telegram: @Termuxtop \n
		 Telegram: @Termuxtop \n
		 Telegram: @Termuxtop \n
	 	 """)

hashtg = input("Xэш аккаунта: ")
iptg = int(input("Собственный идентификатор API: "))
px = int(input("Введите количество сообщений: "))
idp = input("Введите id пользователя Telegram: ")
mes = input("Текст сообщения: ")

api_id = iptg
api_hash = hashtg

for i in range(px):
	with TelegramClient('proxy', api_id, api_hash) as client:
		client.send_message(idp, mes)