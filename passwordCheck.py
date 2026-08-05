import random

SpecialSimbols = '!@#$%^&*_'

def register(password):
    flagregister = False
    flagupper = False
    flaglower = False
    flagdigit = False

    for i in password:
        if i.isupper():
            flagupper = True
        if i.islower():
            flaglower = True
        if i.isdigit():
            flagdigit = True

    if not flagdigit:
        print("Пароль должен содержать цифры")

    if flagupper and flaglower and flagdigit:
        return 4
    elif (flagupper and flaglower) or flagdigit:
        return 2
    elif flaglower:
        print("Пароль должен содержать  заглавные буквы")
        return 0
    elif flagupper:
        print("Пароль должен содержать строчные буквы")
        return 0
    else:
        print("Пароль должен содержать буквы разного регистра")
        return 0

def repiat(password):
    flagrepiat = True

    for i in range(len(password)-1):
        if password[i] == password[i+1]:
            flagrepiat = False
    if flagrepiat:
        return 2
    else: 
        print('Пароль не должен содержать повторяющиеся подряд символы')
        return 0
        
def Check(password):
    grade =  0
    flagSimbols = False

    for i in password:
        if i in SpecialSimbols:
            flagSimbols = True
            break
    if not flagSimbols:
        print(f'Добавьте специальные символы (Например: {SpecialSimbols})')

    grade += register(password)

    if len(password) >= 8:
        grade += 2
    else:
        print("Пароль должен состоять минимум из 8 символов")

    if str(password) != str(password[::-1]):
        grade += 2
    else:
        print("Пароль не должен быть палиндромом")

    grade += repiat(password)

    if flagSimbols:
        grade += 2


    return grade


print("Введите ваш пароль")
password = input().rstrip().lstrip()
print(f'Пароль набрал: {Check(password)}/12 баллов)')

