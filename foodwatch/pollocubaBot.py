import telepot 
import json

token='1273095502:AAGblLlUtscDMGh3K40rssw3NJbsa705XCg'  
Telegrambot=telepot.Bot(token)



with open('data.jl')as file:
    for line in file:
        