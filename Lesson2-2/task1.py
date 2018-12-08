age = int(input('Сколько вам лет? '))


def get_user_info(age):
        if age < 7:
            user_status = str('Ты учишься в детском саду')
        elif age <= 17:
            user_status = str('Ты учишься в школе')
        elif age <= 22:
            user_status = str('Ты учишься в Вузе')
        elif age < 70:
            user_status = str('Ты работаешь')
        elif age > 70:
            user_status = str('Ты пенсионер')
        return str(user_status)

display_info = get_user_info(age)
print(display_info)