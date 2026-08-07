import random

SpecialSimbols = '!@#$%^&*_'

# Проверки
def register(password):
    flagupper = any(c.isupper() for c in password)
    flaglower = any(c.islower() for c in password)
    flagdigit = any(c.isdigit() for c in password)

    if not flagdigit:
        print("Пароль должен содержать цифры")
    if flagupper and flaglower and flagdigit:
        return 4, improve_register(password, flagupper, flaglower, flagdigit)
    elif flagupper and flaglower:
        return 2, improve_register(password, flagupper, flaglower, flagdigit)
    elif flaglower:
        print("Пароль должен содержать заглавные буквы")
        return 0, improve_register(password, flagupper, flaglower, flagdigit)
    elif flagupper:
        print("Пароль должен содержать строчные буквы")
        return 0, improve_register(password, flagupper, flaglower, flagdigit)
    else:
        print("Пароль должен содержать буквы разного регистра")
        return 0, addlitters(password)
     
def repiat(password, newpass):
    flagrepiat = True
    for i in range(len(password)-1):
        if password[i] == password[i+1]:
            flagrepiat = False
    if flagrepiat:
        return 2, newpass
    else: 
        print('Пароль не должен содержать повторяющиеся подряд символы')
        return 0, repairrepiat(newpass)   

def Check(password):
    password = "".join(password.split())
    newpass = password
    grade = 0

    ball, newpass = repiat(password, newpass)
    grade += ball
    ball, newpass = register(newpass)
    grade += ball

    flagSimbols = any(i in SpecialSimbols for i in newpass)
    
    if not flagSimbols:
        print(f'Добавьте специальные символы (Например: {SpecialSimbols})')
        newpass = addsimbol(newpass)
        flagSimbols = True
    else:
        grade += 2

    if len(newpass) >= 8:
        grade += 2
    else:
        print("Пароль должен состоять минимум из 8 символов")
        newpass = repairlen(newpass)

    if str(newpass) != str(newpass[::-1]):
        grade += 2
    else:
        print("Пароль не должен быть палиндромом")
    
    return grade, newpass

# Новые пароли
def improve_register(newpass, flagupper, flaglower, flagdigit):
    if not flagupper:
        newpass = up(newpass)
    if not flaglower:
        newpass = low(newpass)
    if not flagdigit:
        newpass = digit(newpass)
    return newpass

def up(newpass):
    chars = list(newpass)
    for j in range(2):
        i = random.randint(0, len(chars) - 1)
        chars[i] = chars[i].upper()
    newpass = ''.join(chars)
    return newpass
def low(newpass):
    chars = list(newpass)
    for j in range(2):
        i = random.randint(0, len(chars) - 1)
        chars[i] = chars[i].lower()
    newpass = ''.join(chars)
    return newpass
def digit(newpass):
    chars = list(newpass)
    i = random.randint(0, len(chars) - 1)
    while 1:
        num = random.randint(0, 1000)
        n = str(num)
        if n != n[::-1]:
            break
    chars[i] += n
    newpass = ''.join(chars)
    return newpass

def addlitters(password):
    chars = list(password)
    for j in range(2):
        i = random.randint(0, len(chars) - 1)
        if j == 0:
            l = chr(random.randint(65, 90))
        else:
            l = chr(random.randint(97, 122))
        chars[i] += l
    newpass = ''.join(chars)
    return newpass
def addsimbol(newpass):
    chars = list(newpass)
    i = random.randint(0, len(chars) - 1)
    simbol = random.choice(SpecialSimbols)
    chars[i] += simbol
    newpass = ''.join(chars)
    return newpass

def repairrepiat(newpass):
    chars = list(newpass)
    for i in range(len(newpass)-1):
        num = random.randint(0, 2)
        if chars[i].lower() == chars[i+1].lower():
            if num == 0:
                while 1:
                    chars[i+1] = chr(random.randint(65, 90))
                    if chars[i+1] != chars[-len(chars)+i] and chars[i+1] != chars[i]:
                        break
            elif num == 1:
                while 1:
                    chars[i+1] = chr(random.randint(97, 122))
                    if chars[i+1] != chars[-len(chars)+i] and chars[i+1] != chars[i]:
                        break            
            elif num == 2:
                while 1:
                    chars[i+1] = str(random.randint(10, 1000))
                    n = chars[i+1]
                    if n != n[::-1] and chars[i+1] != chars[-len(chars)+i] and chars[i+1] != chars[i]:
                        break
    newpass = ''.join(chars)
    return newpass
def repairlen(newpass):
    chars = list(newpass)
    while len(chars) < 8:
        i = random.randint(0, len(chars))
        num = random.randint(0, 2)
        if num == 0:
            chars.insert(i, chr(random.randint(65, 90)))  
        elif num == 1:
            chars.insert(i, chr(random.randint(97, 122)))
        else:
            chars.insert(i, str(random.randint(0, 9)))
    newpass = ''.join(chars)
    return newpass

print('Введите ваш пароль')
password = input().strip()
grade, newpass = Check(password)
print(f'Пароль набрал: {grade}/12 баллов')
print(f'Пример надежного пароля - {newpass}')
grade, newpass = Check(newpass)
print(f'Он защищен на {grade}/12 баллов')
