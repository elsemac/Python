def get_summ(one, two, delimiter='&'):
    return str(one) + str(delimiter) + str(two)
var_one=get_summ('Learn', 'Python')
print(var_one.upper())