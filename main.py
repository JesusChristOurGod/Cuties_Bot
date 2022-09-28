import telebot
f = open("animals.txt","r+")
a=[]
for line in f:
    a.append(line[:-1])

token='5700729853:AAG2MKzUnvYpmYaeBae1Pi5cAZ1r45qPP7c'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Привет ✌️ ")

@bot.message_handler(content_types=['text'])
def new_message(message, winner):
    bot.send_chat_action()

bot.polling(none_stop = True)