import random
import time
#справка
def reference():
    print("1) Не используйте стандартные последовательности цифр или букв \n 2) Не указывайте год, месяц или день рождения в пароле \n 3) Используйте комбинацию из не менее восьми букв, цифр и символов \n 4) Комбинируйте различные несвязанные слова в пароле или парольной фразе")
    time.sleep(1)
#генератор
def rsmdon_pass (length):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@_-+=#$%&*"
    password = ""
    for k in range (length):
        password += random.choice(chars)
    choice = input("хотьте в этот пароль добавить что то своё? да\нет  ")
    if choice == "да":
        a = input("напишите что хотите добавить:   ")
        time.sleep(1)
        b = input(f"куда хотите добавить {a} вперёд или назад?:   ")
        time.sleep(1)
        if b == "вперёд":
            print("ваш пароль с изменениями:", a+password)
        else:
            print("ваш пароль с изменениями:", password+a)
    else:
        print("ладно \n ваш пароль без изменений:", password)
    return password
#начало проверки сложности
def complexity():
    warn = 0
    user_print = input("введите ваш пароль для получения оценки \n p.s этот код не собирает данные и не украдёт ваш пароль можите не боятся     ")
    if not user_print:
        print("вы не чего не ввели")
        return
    lens = len(user_print)
    #проверка сложности
    def mixer(user_print):
        result = {
        'has_upper' : False,
        'has_lower' : False,
        'has_digit' : False,
        'has_special': False
        }
        for char in user_print:
            if char.isupper():
                result['has_upper'] = True
                break
        for char in user_print:
            if char.islower():
                result['has_lower'] = True
                break
        for char in user_print:
            if char.isdigit():
                result['has_digit'] = True
                break
        for char in user_print:
            if not char.isalnum():
                result['has_special'] = True
                break
        return result
    result = mixer(user_print)
    print("длинна пароля: ", len(user_print))
    print(f"заглавные: {result['has_upper']}")
    print(f"строчные: {result['has_lower']}")
    print(f"цифры: {result['has_digit']}")
    print(f"специальные символы: {result['has_special']}")
    if lens >= 12:
        warn += 0
    elif lens >= 9:
        warn += 1
    else:
        warn += 2
    if result['has_upper'] == False:
        warn += 1
    if result['has_lower'] == False:
        warn += 1
    if result['has_digit'] == False:
        warn += 1
    if result['has_special'] == False:
        warn += 1
    if warn >= 5:
        print("ваш пароль очень прохой добавте символы всех типов и добавте длину пароля! \n p.s посмотрите 'справка' чтобы сделать пароль безопасней! \n итог - плохой пароль")
        time.sleep(1)
    elif warn >= 2:
        print("ваш пароль хороший но советую его улутшить и сделать его безопасней с помощью 'справка' \n итог - средний пароль")
        time.sleep(1)
    else:
        print("у вас замечательный пароль \n итог - замечательный пароль")
        time.sleep(1)
    return warn
#меню
while True:
    try:
        a1 = input(f"вы можете сделать... \n 0 - выйти \n 1 - справка  \n 2 - проверить сложность пароля \n 3 - сгенирировать пароль \n ")
    except:
        print("введите цифры")
        time.sleep(1)
    if a1 == "0":
        exit("хорошо")
        time.sleep(1)
    elif a1 == "1":
        reference()
    elif a1 == "2":
        complexity()
    elif a1 == "3":
        try:
            length = int(input("напишите длинну вашего пароля:    "))
            time.sleep(1)
            gen_password = rsmdon_pass(length)
        except ValueError:
            print("надо ввести число")
    else:
        print("этих функций ещё нет")
        time.sleep(1)
