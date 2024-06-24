#https://www.codewars.com/kata/563e320cee5dddcf77000158/train/python

def get_average(marks):
    total = sum(marks)
    average = total // len(marks)
    return average

#https://www.codewars.com/kata/55685cd7ad70877c23000102/train/python

def make_negative( number ):
    if number > 0:
        return number * (-1)
    else:
        return number
    
#https://www.codewars.com/kata/526c7363236867513f0005ca/train/python

def is_leap_year(year):
    if year % 4== 0: 
        return True
    elif year % 400 == 0:
        return True
    else:
        return False