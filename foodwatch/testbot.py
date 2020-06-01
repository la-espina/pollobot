import telepot 
import json
import os.path
import time
print('Iniciando comunicación')
token='1273095502:AAGblLlUtscDMGh3K40rssw3NJbsa705XCg'  

telepot.api.set_proxy('http://10.0.100.191:3128',('miguel.hinojosa','CoalBitminer'))

Telegrambot=telepot.Bot(token)
print('Conectado a telegram')


def posttry(msg):
    """ Enviar mensajes al grupo por el id """
    Telegrambot.sendMessage(-1001334786762,msg,parse_mode="Markdown")
#    try:
#        Telegrambot.sendMessage(-1001334786762,msg,parse_mode="Markdown")
#    except:  
#        print('Demasiados request. Esperando 5...')
#        time.sleep(5)
#        posttry(msg)
        

posttry("_1 2 3 Probando_")
