import telebot
from telebot.types import ForceReply #para citar un mensaje
import requests
import json

token = '6113092305:AAEQFPxaNDtn5JIocQlP1SmEVLKqsNPG35I'
bot = telebot.TeleBot(token)

#responde al comando /start
@bot.message_handler(commands = ['start','help'])
def start(message):
    '''Da la bienvenida al usuario del bot'''
    bot.reply_to(message,'¡Bienvenido! Soy panel_solar_bot , un bot diseñado para ayudarte con el consumo y la producción de tu sistema fotovoltaico. \n \n Puedes controlarme usando los siguientes comandos disponibles: \n \n /datos Para almacenar tus datos \n/1 Consultar el consumo actual: Permite al usuario ver la cantidad de energía que consumió en la última hora. \n /2 Consultar la producción actual: Permite al usuario ver la cantidad de energía que está produciendo el sistema fotovoltaico en tiempo real. \n /3 Ver el historial de consumo: Muestra al usuario un gráfico con el consumo de energía del panel solar a lo largo del tiempo: (dia, semana, mes, año) \n /4 Ver el historial de consumo: Muestra al usuario un gráfico con la producción de energía del panel solar a lo largo del tiempo: (dia, semana, mes, año) \n /5 Ver la producción prevista: Predice la producción de energía basándose en el clima y otros factores. \n \n ¿En qué puedo ayudarte hoy?')


#Datos del usuario
@bot.message_handler(commands = ['datos'])
def datos(message):
    '''Pregunta el nombre de usuario'''
    markup = ForceReply()
    msg = bot.send_message(message.chat.id, '¿Cuál es tu nombre?', reply_markup=markup)
    bot.register_next_step_handler(msg, cliente_id)


def cliente_id(message):
    '''Pregunta al usuario su número de cliente'''
    nombre = message.text
    markup = ForceReply()
    msg = bot.send_message(message.chat.id, '¿Cuál es tu número de cliente?', reply_markup=markup)
        
@bot.message_handler(content_types=['text'])
def mensajes_texto(message):
    '''Gestiona los mensajes de texto recibidos'''
    bot.send_message(message.chat.id,'El comando enviado no realiza ninguna función. Intente nuevamente')
    

#comando 1
@bot.message_handler(content_types= '1')
def consumo_actual(message):
    '''Consultar el consumo actual: Permite al usuario ver la cantidad de energía que consumió en la última media hora.'''
    response = requests.get('http://127.0.0.1:8000/consumo_now')
    print(type(response.text))
    data = json.loads(response.text)
    print(type(data))
    print(data)

    hora = data['Datetime'].split('T')[1]

    mensaje = f'El consumo a las {hora} es de {data["Total"]} Kw.'

    bot.send_message(message.chat.id, mensaje)

#comando 2
@bot.message_handler(content_types= '2')
def consumo_actual(message):
    '''Consultar la producción actual: Permite al usuario ver la cantidad de energía que está produciendo el sistema fotovoltaico en tiempo real.'''

#comando 3
@bot.message_handler(content_types= '3')
def historial(message):
    '''Ver el historial de consumo: Muestra al usuario un gráfico con el consumo de energía del panel solar a lo largo del tiempo: (dia, semana, mes, año).'''
    bot.send_message(message.chat.id,'Desea ver el consumo de energía diario, semanal, mensual o anual?')
    telebot.types.BotCommand('/','/D: Día, /S: Semana, /M: Mes, /A: Año'),

    @bot.message_handler(content_types='D')
    def historial_dia(message):
        '''Muestra al usuario un gráfico con el consumo de energía del panel solar en el día'''

#comando 4
@bot.message_handler(content_types= '4')
def historial(message):
    '''Ver el historial de consumo: Muestra al usuario un gráfico con la producción de energía del panel solar a lo largo del tiempo: (dia, semana, mes, año).'''
    bot.send_message(message.chat.id,'Desea ver la producción de energía diario, semanal, mensual o anual?')
    telebot.types.BotCommand('/','/D: Día, /S: Semana, /M: Mes, /A: Año')

if __name__ == '__main__':
    bot.set_my_commands([
        telebot.types.BotCommand('/start','Dá la bienvenida al usuario'),
        telebot.types.BotCommand('/1','Consultar el consumo actual'),
        telebot.types.BotCommand('/2','Consultar la producción actual'),
        telebot.types.BotCommand('/3','Ver el historial de consumo'),
        telebot.types.BotCommand('/4','Ver el historial de producción'),
        telebot.types.BotCommand('/5','Ver la producción prevista'),
    ])

    print('Iniciando el bot')
    bot.infinity_polling() # es lo mismo q el while true para ver si hay nuevos mensajes