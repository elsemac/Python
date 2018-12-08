def get_sum(num_one, num_two):
    try:
        sum = int(num_one) + int(num_two)
        return print(sum)
    except ValueError:
        return print("Неправильный тип данных")

num_1 = input('Введите число 1 ')
num_2 = input('Введите число 2 ')
answer = get_sum(num_1, num_2)
