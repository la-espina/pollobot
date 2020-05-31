import telepot 
import json
import os.path
import time
token='1273095502:AAGblLlUtscDMGh3K40rssw3NJbsa705XCg'  
Telegrambot=telepot.Bot(token)

print(os.getcwd())
lastlog='last_data.jl'
curlog='data.jl'
# Compara las diferencias entre los logs

last=[]
current={}

def posttry(msg):
    """ Enviar mensajes al grupo por el id """
    try:
        Telegrambot.sendMessage(-429014316,msg,parse_mode="Markdown")
    except:  
        print('Demasiados request. Esperando 5..')
        time.sleep(5)
        posttry(msg)
        
with open(lastlog) as file:
    for line in file:
        decd  = json.loads(line)
        last.append(decd['chk'])

with open(curlog) as file:
    for line in file:
        decd  = json.loads(line)
        current[decd['chk']]={'product':decd['product'],'place':decd['place'], 'price':decd['price']   }
        



for prod in current.keys():
    if prod not in last:
        msg="{} {}  \n *{}*   ".format(current[prod]['product'],current[prod]['price'],current[prod]['place']  )
        print(msg)
        time.sleep(1)
        posttry(msg)
        # try:
        #     Telegrambot.sendMessage(-429014316,msg,parse_mode="Markdown")  
        # except:
        #     print('Demasiados request. Esperando 5..')
        #     time.sleep(5)
        #     Telegrambot.sendMessage(-429014316,msg,parse_mode="Markdown")

os.system('mv '+curlog+' '+lastlog)