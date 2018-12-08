# def ask_user:
# while True:
 #   user_say = input("Как дела? ")
 #   if user_say == "Хорошо":   
 #       print('И у меня хорошо!')
 #       break
 #   else:
 #       print('Нет, а все-таки как твои дела? ')




answers = {
    "Как дела?": 'Хорошо',
    "Что делаешь?": 'Пишу код',
    "Как погода?": 'Сейчас солнечно',
    "Какой сегодня день?": 'Тот самый',
    "Как тебе янжекс телефон?": 'Ну такое'
}

def ask_user(user_say):
    while True:
        if user_say in answers.keys():   
            print('Программа: ' + answers.get(user_say))
            break
        else:
            print("Программа: " + 'Задай правильный вопрос')
            break

if __name__ == '__main__':
    try:
        say_smth = input("Пользователь: ")
        bot = ask_user(say_smth)
    except KeyboardInterrupt:
        зкште('Пока!')