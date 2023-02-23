import telebot
from telebot.types import ForceReply, InputFile #para citar un mensaje
from telebot import types

from bot_funciones import solicitar, crear_grafico

token = '6113092305:AAEQFPxaNDtn5JIocQlP1SmEVLKqsNPG35I'
bot = telebot.TeleBot(token)

#variable donde guardamos los datos del usuario
usuarios = {}


#responde al comando /start
@bot.message_handler(commands = ['start','help'])
def start(message):
    '''Da la bienvenida al usuario del bot'''
    bot.reply_to(message,'¡Bienvenido! Soy panel_solar_bot , un bot diseñado para ayudarte con el consumo y la producción de tu sistema fotovoltaico. \n \n Puedes controlarme usando los siguientes comandos disponibles: \n \n /datos Para almacenar tus datos \n/1 Consultar el consumo actual: Permite al usuario ver la cantidad de energía que consumió en la última hora. \n /2 Consultar la producción actual: Permite al usuario ver la cantidad de energía que está produciendo el sistema fotovoltaico en tiempo real. \n /3 Ver el historial de consumo: Muestra al usuario un gráfico con el consumo de energía del panel solar a lo largo del tiempo: (dia, semana, mes, año) \n /4 Ver el historial de consumo: Muestra al usuario un gráfico con la producción de energía del panel solar a lo largo del tiempo: (dia, semana, mes, año) \n /5 Ver la producción prevista: Predice la producción de energía basándose en el clima y otros factores. \n \n ¿En qué puedo ayudarte hoy?')


#Datos del usuario
@bot.message_handler(commands = ['datos'])

def cliente_id(message):
    '''Pregunta al usuario su número de cliente'''
    
    markup = ForceReply()
    msg = bot.send_message(message.chat.id, '¿Cuál es tu número de cliente?', reply_markup=markup)
    id = msg


    
#comando 1
@bot.message_handler(commands = ['1'])
def consumo_actual(message):
    '''Consultar el consumo actual: Permite al usuario ver la cantidad de energía que consumió en la última media hora.'''
    data = solicitar('consumo_now')

    hora = data['Datetime'].split('T')[1]

    mensaje = f'El consumo a las {hora} es de {data["Total"]} Kw.'

    bot.send_message(message.chat.id, mensaje)

#comando 2
@bot.message_handler(commands = ['2'])
def consumo_actual(message):
    '''Consultar la producción actual: Permite al usuario ver la cantidad de energía que está produciendo el sistema fotovoltaico en tiempo real.'''
    data = solicitar('produccion_now')
    
    hora = data['Datetime'].split('T')[1]

    mensaje = f'El producción a las {hora} es de {data["Produccion"]} Kw.'

    bot.send_message(message.chat.id, mensaje)



def grafico_consumo(message):
    respuesta_usuario = message.text.upper()
    if respuesta_usuario == 'D':
        # Lógica para mostrar el consumo diario
        data = solicitar('line/false/1D/30T')
        crear_grafico(data, 'Grafico de consumo diario')
        bot.send_message(message.chat.id, 'Mostrando consumo diario...')
        bot.send_photo(message.chat.id, InputFile('Foto.png'))
        

    elif respuesta_usuario == 'S':
        # Logica para mostrar el consumo semanal
        data = solicitar('line/false/1W/6H')
        grafico = crear_grafico(data, 'Grafico de consumo semanal')
        bot.send_message(message.chat.id, 'Mostrando consumo semanal...')
        bot.send_photo(message.chat.id, InputFile('Foto.png'))
        
    elif respuesta_usuario == 'M':
        # Logica para mostrar el consumo mensual
        
        data = solicitar('line/false/1M/1D')
        grafico = crear_grafico(data, 'Grafico de consumo mensual')
        bot.send_message(message.chat.id, 'Mostrando consumo mensual...')
        bot.send_photo(message.chat.id, InputFile('Foto.png'))

    elif respuesta_usuario == 'A':
        # Lógica para mostrar el consumo anual
        data = solicitar('line/false/1Y/1W')
        grafico = crear_grafico(data, 'Grafico de consumo anual')
        bot.send_message(message.chat.id, 'Mostrando consumo anual')
        bot.send_photo(message.chat.id, InputFile('Foto.png'))

    else:
        bot.send_message(message.chat.id, 'Opción inválida. Por favor, seleccione D, S, M o A.')



#comando 3
@bot.message_handler(commands = ['3'])
def historial_consumo(message):
    '''Ver el historial de consumo: Muestra al usuario un gráfico con el consumo de energía del panel solar a lo largo del tiempo: (dia, semana, mes, año).'''
    bot.send_message(message.chat.id,'Desea ver el consumo de energía D: diario, S: semanal, M: mensual o A: anual?')

    bot.register_next_step_handler(message, grafico_consumo)


     

def grafico_produccion(message):
    respuesta_usuario = message.text.upper()
    if respuesta_usuario == 'D':
        data = solicitar('line/true/1D/30T')
        crear_grafico(data, 'Grafico de producción diario')
        bot.send_message(message.chat.id, 'Mostrando la producción diaria')
        bot.send_photo(message.chat.id, InputFile('Foto.png'))
        
    elif respuesta_usuario == 'S':
        bot.send_message(message.chat.id, 'Mostrando la producción semanal')
        data = solicitar('line/true/1W/6H')
        grafico = crear_grafico(data, 'Grafico de producción semanal')
        bot.send_photo(message.chat.id, InputFile('Foto.png'))

    elif respuesta_usuario == 'M':
        bot.send_message(message.chat.id, 'Mostrando la producción mensual')
        data = solicitar('line/true/1M/1D')
        grafico = crear_grafico(data, 'Grafico de producción mensual')
        bot.send_photo(message.chat.id, InputFile('Foto.png'))

    elif respuesta_usuario == 'A':
        bot.send_message(message.chat.id, 'Mostrando la producción anual')
        data = solicitar('line/true/1Y/1W')
        grafico = crear_grafico(data, 'Grafico de producción anual')
        bot.send_photo(message.chat.id, InputFile('Foto.png'))

    else:
        bot.send_message(message.chat.id, 'Opción inválida. Por favor, seleccione D, S, M o A.')

#comando 4
@bot.message_handler(commands = ['4'])
def historial_produccion(message):
    '''Ver el historial de consumo: Muestra al usuario un gráfico con la producción de energía del panel solar a lo largo del tiempo: (dia, semana, mes, año).'''
    bot.send_message(message.chat.id,'Desea ver la producción de energía D: diaria, S: semanal, M: mensual o A: anual?')
    bot.register_next_step_handler(message, grafico_produccion)

#comando 5
@bot.message_handler(commands = ['5'])
def produccion_prevista(message):
    '''Ver la producción prevista: Predice la producción de energía basándose en el clima y otros factores.'''
    mensaje = 'aca iria la predicción de la producción'
    bot.send_message(message.chat.id, mensaje)
    

#Comandos no válidos      
@bot.message_handler(content_types=['text'])
def mensajes_texto(message):
    '''Gestiona los mensajes de texto recibidos'''
    bot.send_message(message.chat.id,'El comando enviado no realiza ninguna función. Intente nuevamente')

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