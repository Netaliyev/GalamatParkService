import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Дежурный сантехник', 'Дежурный охранник')

keyboard2 = types.InlineKeyboardMarkup(row_width=2)
item1 = types.InlineKeyboardButton('🚰 Сантехник', callback_data='plumber')
item2 = types.InlineKeyboardButton('👮🏿‍♂️Охранник', callback_data='security')
item3 = types.InlineKeyboardButton('👩🏻‍💼 Менеджер', callback_data='manager')
item4 = types.InlineKeyboardButton('🏥 Поликлиника', callback_data='hospital')
item5 = types.InlineKeyboardButton('👮🏻‍♂️Участковый', callback_data='precinct')
item6 = types.InlineKeyboardButton('📞 Телеком', callback_data='telecom')

keyboard2.add(item1, item2, item3, item4, item5, item6)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я создан помогать жильцам Galamat Park\nВот список моих команд:\n',
                     reply_markup= keyboard2)
    print("Started in {} by {} ".format(message.chat.title, message.from_user.first_name))

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):


    try:
        if call.message:
            print(call.from_user.first_name, call.data, call.message.date)
            if call.data == 'plumber':
                bot.send_message(call.from_user.id, 'Дежурный сантехник 🚰:\n+7 (771) 900 2269')
            elif call.data == 'security':
                bot.send_message(call.from_user.id, 'Дежурный охранник 👮🏿‍♂️:\n+7 (778) 178 3534')
            elif call.data == 'manager':
                bot.send_message(call.from_user.id, 'Менеджер Салия 👩🏻‍💼:\n+7 (775) 310 2630')
            elif call.data == 'hospital':
                bot.send_message(call.from_user.id, 'Полклиника "Шипагер" 🏥\nУлица Сауран, 42\n+7 (771) 900 1146')
            elif call.data == 'precinct':
                bot.send_message(call.from_user.id,'Участковый инспектор полиции 👮🏻‍♂️\nКарабалаев Сабырхан Мамырханулы:\n'
                                                       '+7 (776) 177 4040\n')
            elif call.data == 'telecom':
                bot.send_message(call.from_user.id,'Нурсултан "Телеком"\n+7 (775) 710 13 75')

    except Exception as e:
        print(repr(e))



bot.infinity_polling()