import random
def reference():
    print("1) Не используйте стандартные последовательности цифр или букв \n 2) Не указывайте год, месяц или день рождения в пароле \n 3) Используйте комбинацию из не менее восьми букв, цифр и символов \n 4) Комбинируйте различные несвязанные слова в пароле или парольной фразе")
def rsmdon_pass (length):
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@_-+=#$%&*"
        password = " "
        for k in range (length):
            password += random.choice(chars)
        return password
def complexity():
    warn = 0
    user_print = input("введите ваш пароль для получения оценки \n p.s этот код не собирает данные и не украдёт ваш пароль можите не боятся     ")
    lens = len(user_print)
    def mixer(user_print, warn):
        result = {
        'has_upper' : False,
        'has_lower' : False,
        'has_digit' : False,
        'has_special': False
        }
        for char in user_print:
            if char.isupper():
                result['has_upper'] = True
                warn -= 1
                break
        for char in user_print:
            if char.islower():
                result['has_lower'] = True
                warn -= 1
                break
        for char in user_print:
            if char.isdigit():
                result['has_digit'] = True
                warn -= 1
                break
        for char in user_print:
            if not char.isalnum():
                result['has_special'] = True
                warn -= 1
                break
        return result
    result = mixer(user_print)
    print(f"заглавные: {result['has_upper']}")
    print(f"строчные: {result['has_lower']}")
    print(f"цифры: {result['has_digit']}")
    print(f"специальные символы: {result['has_special']}")
    if lens <= 5:
        warn += 5
    elif lens <= 9:
        warn += 3
    elif lens >= 10:
        warn += 1
    print(f"ваш пароль получил {warn} замечаний")
    if warn >= 4:
        print("ваш пароль очень плохой добавте в него новых типов символов")
    elif warn >= 2:
        print("ваш пароль хороший но лучше сделать его сложней")
    else:
        print("у вас замечательный пароль")
    return warn
while True:
    try:
        a1 = input(f"вы можете сделать... \n 0 - выйти \n 1 - справка  \n 2 - проверить сложность пароля \n 3 - сгенирировать пароль \n ")
    except:
        print("введите цифры")
    if a1 == "0":
        exit("хорошо")
    elif a1 == "1":
        reference()
    elif a1 == "2":
        complexity()
    elif a1 == "3":
        try:
            length = int(input("напишите длинну вашего пароля:    "))
            gen_password = rsmdon_pass(length)
            print("ваш пароль:", gen_password)
        except:
            print("надо вводить цифры!!!")