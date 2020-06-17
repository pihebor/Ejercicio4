def leap_year(year):
    res = False
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        res = True
    return res

    
