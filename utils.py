#넥센 & 키움 - 0
#두산 - 1
#롯데 - 2
#삼성 - 3
#한화 - 4
#KIA - 5
#KT - 6
#NC - 7
#LG - 8
#SK - 9

def KBO_num(name):
    if(name == "넥센" or name == "키움"):
        return 0
    elif(name == "두산"):
        return 1
    elif(name == "롯데"):
        return 2
    elif(name == "삼성"):
        return 3
    elif(name == "한화"):
        return 4
    elif(name == "KIA"):
        return 5
    elif(name == "KT"):
        return 6
    elif(name == "NC"):
        return 7
    elif(name == "LG"):
        return 8
    elif(name == "SK"):
        return 9
    else:
        return 10


def numtoten(num):
    if(num < 10):
        return '0' + str(num)
    else:
        return str(num)