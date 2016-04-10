import telebot # Importamos las librería
 
TOKEN = '218715849:AAFuiheHtKSb-GqIF-WW88Q446kOHeh5cVY' # Ponemos nuestro Token generado con el @BotFather
 
tb = telebot.TeleBot(TOKEN) # Combinamos la declaración del Token con la función de la API

#tb.send_message(chat_id, 'patata')
#a = tb.get_me()

#print (a)

@tb.message_handler(commands=['start', 'help'])
def send_welcome(message):
    tb.reply_to(message, "Howdy, how are you doing?")

@tb.message_handler(func=lambda message: True)
def echo_all(message):
    tb.reply_to(message, message.text)

tb.polling()
