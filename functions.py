# TODO(everyone): 더하기, 빼기, 곱하기, 나누기 함수 정의하기
import math 

def check_num(n1,n2):
    str_n1 = str(n1)
    str_n2 = str(n2)
    if str_n1.isdigit() and str_n2.isdigit():
        return False
    else:
        return "Not a num"

def check_num_one(n1):
    str_n1 = str(n1)
    if str_n1.isdigit():
        return False
    else:
        return "Not a num"

def add(n1, n2):
    err = check_num(n1,n2)
    if err:
        return err

    result = float(n1) + float(n2)
    return result

def sub(n1, n2):
    err = check_num(n1,n2)
    if err:
        return err
        
    result = float(n1) - float(n2)
    return result


def div(n1, n2):
    err = check_num(n1,n2)
    if err:
        return err
    
    if n2 == 0:
        return "#DIV/0!"
    result = float(n1)/float(n2)
    return result

def mul(n1, n2):
    err = check_num(n1,n2)
    if err:
        return err
        
    result = float(n1)*float(n2)
    return result

def sqrt(n1):
    err = check_num_one(n1)
    if err:
        return err
        
    result = math.sqrt(n1)
    return result