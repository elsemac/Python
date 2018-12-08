def check_stroke(stroke1, stroke2):
    if type(stroke1) == str and type(stroke2) == str:
        if stroke1 == stroke2:
            stroke_stat = 1
        elif stroke1 > stroke2 and stroke2 != "learn":
            stroke_stat = 2
        elif stroke1 != stroke2 and stroke2 == "learn":
            stroke_stat = 3
        else:
            stroke_stat = 'not as described in task'
    else: 
        stroke_stat = 0
    return stroke_stat 

stroke1 = input('Введите строку 1 ')
stroke2 = input('Введите строку 2 ')
dipslay_info = check_stroke(stroke1, stroke2)
print(dipslay_info)