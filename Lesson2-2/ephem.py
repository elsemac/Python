import ephem

# Импортируем нужные компоненты
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Настройки прокси
PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

def greet_user(bot, update):
    text = 'Привет, ты нажал /start'
    print(text)
    update.message.reply_text(text)



def e_planet(bot, update):
    text = 'Привет, ты нажал /planet'
    print(text)
    update.message.reply_text(text)



def check(bot, update):
    check = 'Привет, ты нажал /check'
    print(check)
    update.message.reply_text(check)

def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

# Функция, которая соединяется с платформой Telegram, "тело" нашего бота
def main():
    mybot = Updater("722436219:AAFD-5fM3a8KYR7q3z4YByzkk2Y15M06rjk", request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))  
    dp.add_handler(CommandHandler("check", check))  
    dp.add_handler(CommandHandler("planet", e_planet))  
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()
main()
