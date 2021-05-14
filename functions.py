# TODO(everyone): 더하기, 빼기, 곱하기, 나누기 함수 정의하기

def check_num(n1,n2):

    if n1.isdigit() == False:
        return "Not a num"
    elif n2.isdigit() == False:
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