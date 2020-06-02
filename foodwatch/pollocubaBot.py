import telepot 
import json
import os.path
import time

configfile=os.path.expanduser('~/.pollobotconfig')
config = json.loads(open(configfile).read())

if config['proxy']['active'] == 'yes':
    telepot.api.set_proxy(config['proxy']['url'],(config['proxy']['user'],config['proxy']['pass']))

token='1273095502:AAGblLlUtscDMGh3K40rssw3NJbsa705XCg'  
Telegrambot=telepot.Bot(token)

print(os.getcwd())
lastlog='last_data.jl'
curlog='data.jl'
# Compara las diferencias entre los logs

last=[]
current={}
tiendas={
    '4caminos':'Cuatro Caminos',
    'carlos3':'Carlos III',
    'tipicaboyeros':'Tipica Boyeros',
    'caribehabana':'Villa Diana',
    '5tay42':'5ta y 42'
}
def posttry(msg):
    """ Enviar mensajes al grupo por el id """
    try:
        Telegrambot.sendMessage(-1001334786762,msg,parse_mode="Markdown")
    except:  
        print('Demasiados request. Esperando 5...')
        time.sleep(5)
        posttry(msg)
        
with open(lastlog) as file:
    for line in file:
        decd  = json.loads(line)
        last.append(decd['chk'])

with open(curlog) as file:
    for line in file:
        decd  = json.loads(line)
        current[decd['chk']]={'product':decd['product'],'place':tiendas[decd['place']], 'price':decd['price'],'url':decd['url']   }
        



for prod in current.keys():
    if prod not in last:
        msg="{}\n_{}_\n[{}]({})   ".format(current[prod]['product'],current[prod]['price'],current[prod]['place'],current[prod]['url']   )
        print(msg)
        time.sleep(1)
        posttry(msg)
        # try:
        #     Telegrambot.sendMessage(-429014316,msg,parse_mode="Markdown")  
        # except:
        #     print('Demasiados request. Esperando 5..')
        #     time.sleep(5)
        #     Telegrambot.sendMessage(-429014316,msg,parse_mode="Markdown")

os.system('cp '+curlog+' '+lastlog)
