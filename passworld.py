import random
import time
import requests
import hashlib
#недопустимые пароли
kall_password = ["admin123", "123456", "password", "12345678", "qwerty", "123456789", "12345", "1234", "111111", "1234567", "dragon", "123123", "baseball", "abc123", "football", "monkey", "letmein", "696969", "shadow", "master", "666666", "qwertyuiop", "123321", "mustang", "1234567890", "michael", "654321", "pussy", "superman", "1qaz2wsx", "7777777", "fuckyou", "121212", "000000", "qazwsx", "123qwe", "killer", "trustno1", "jordan", "jennifer", "zxcvbnm", "asdfgh", "hunter", "buster", "soccer", "harley", "batman", "andrew", "tigger", "sunshine", "iloveyou", "fuckme", "2000", "charlie", "robert", "thomas", "hockey", "ranger", "daniel", "starwars", "klaster", "112233", "george", "asshole", "computer", "michelle", "jessica", "pepper", "1111", "zxcvbn", "555555", "11111111", "131313", "freedom", "777777", "pass", "fuck", "maggie", "159753", "aaaaaa", "ginger", "princess", "joshua", "cheese", "amanda", "summer", "love", "ashley", "6969", "nicole", "chelsea", "biteme", "matthew", "access", "yankees", "987654321", "dallas", "austin", "thunder", "taylor", "matrix", "minecraft", "walter", "helpme", "fuckoff", "oliver", "merlin", "cookie", "sexy", "chocolate", "guitar", "butthead", "patrick", "richard", "snoopy", "scooby","admin", "welcome", "login", "passw0rd", "master123", "hello123", "loveme", "zaq12wsx", "qwerty123", "asdf1234", "admin123", "123abc", "password123", "letmein1", "monkey123", "football123", "sunshine1", "iloveyou1", "princess1", "ashley1", "bailey", "diamond", "abcd1234", "1q2w3e4r", "1q2w3e", "flower", "password1", "hello", "ninja", "mustang1", "123654", "123456a", "qwerty1", "hello1", "freedom1", "whatever", "hello123", "charlie1", "888888", "q1w2e3r4", "super123", "samsung", "1111111", "123123123", "123456789a", "qazxsw", "66666666", "unknown", "internet", "soccer1", "purple", "fishing", "maverick", "jessica1", "12345678910", "987654", "ferrari", "corvette", "cherokee", "redskins", "jackson", "william", "cameron", "golfer", "benjamin", "tiffany", "patrick1", "cookie1", "chicken", "liverpool", "blahblah", "hello123", "porsche", "guitar1", "hammer", "beaver", "mickey", "coffee", "peanut", "jupiter", "kitten", "panties", "toyota", "zxcvb", "testing", "bond007", "changeme", "david", "michael1", "q1w2e3r4t5", "asdfasdf", "metallica", "sparky", "snickers", "goldfish", "boomer", "cowboy", "firebird", "blizzard", "startrek", "bootsie", "bubba1", "brooklyn", "rangers", "marlboro", "phantom", "strength", "sandwich", "lovely", "sweetie", "panther", "clinton", "brooklyn", "yamaha", "skyline", "eagles", "pikachu", "booboo", "trouble", "topgun", "bigdaddy", "johnson", "alexander", "dolphins", "mother", "parker", "christin", "business", "butter", "cricket", "nathan", "morgan", "rabbit", "tristan", "rainbow", "melissa", "elephant", "nothing", "apple", "orange", "ginger1", "simpson", "banana", "london", "diego", "august", "success", "hannah", "michelle1", "victoria", "happy", "secret", "steelers", "peaches", "genesis", "brandon1", "popcorn", "teresa", "maxwell", "heather1", "christian", "beauty", "stephen", "winter", "john316", "doctor", "freddie", "winner", "harrison", "bonnie", "shelby", "compass", "adidas", "energy", "angel1", "friends", "forever", "sweetheart", "spring", "someone", "sierra", "pretty", "dancing", "hotdog", "teacher", "lifehack", "mountain", "lovelove", "dreamer", "eclipse", "smokey", "pisces", "phoenix", "kingkong", "caroline", "slipknot", "courtney", "goodluck", "crystal", "garfield", "lollipop", "edward", "tequiero", "pumpkin", "playboy", "christina", "badboy", "december", "spiderman", "mitchell", "stella", "scarface", "disney", "rooster", "brenda", "storm", "sherlock", "pentium", "jeremiah", "gordon", "tomcat" ]
#генератор
def rsmdon_pass ():
    try:
        length = int(input("напишите длинну вашего пароля:    "))
        time.sleep(1)
        if length > 50:
            print("слишком длинный пароль максимум 50 \n ")
            return None
        elif length < 4:
            print("слишком коротко максимум 4 \n ")
            return None
    except ValueError:
        print("надо ввести число \n ")
        return None
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
#поиск в утечках HIBP
def hibp_check(user_print):
    hash_full = hashlib.sha1(user_print.encode()).hexdigest().upper()
    prefix = hash_full[:5]
    suffix = hash_full[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)
    for line in response.text.splitlines():
        if line.startswith(suffix):
            count = int(line.split(':')[1])
            print(count)
            return count
    return 0
#оценка
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
    print("длинна пароля: ", len(user_print))
    print(f"заглавные: {result['has_upper']}")
    print(f"строчные: {result['has_lower']}")
    print(f"цифры: {result['has_digit']}")
    print(f"специальные символы: {result['has_special']}")
    return result
#ввывод оценки
def complexity():
    kall_password = ["admin123", "123456", "password", "12345678", "qwerty", "123456789", "12345", "1234", "111111", "1234567", "dragon", "123123", "baseball", "abc123", "football", "monkey", "letmein", "696969", "shadow", "master", "666666", "qwertyuiop", "123321", "mustang", "1234567890", "michael", "654321", "pussy", "superman", "1qaz2wsx", "7777777", "fuckyou", "121212", "000000", "qazwsx", "123qwe", "killer", "trustno1", "jordan", "jennifer", "zxcvbnm", "asdfgh", "hunter", "buster", "soccer", "harley", "batman", "andrew", "tigger", "sunshine", "iloveyou", "fuckme", "2000", "charlie", "robert", "thomas", "hockey", "ranger", "daniel", "starwars", "klaster", "112233", "george", "asshole", "computer", "michelle", "jessica", "pepper", "1111", "zxcvbn", "555555", "11111111", "131313", "freedom", "777777", "pass", "fuck", "maggie", "159753", "aaaaaa", "ginger", "princess", "joshua", "cheese", "amanda", "summer", "love", "ashley", "6969", "nicole", "chelsea", "biteme", "matthew", "access", "yankees", "987654321", "dallas", "austin", "thunder", "taylor", "matrix", "minecraft", "walter", "helpme", "fuckoff", "oliver", "merlin", "cookie", "sexy", "chocolate", "guitar", "butthead", "patrick", "richard", "snoopy", "scooby","admin", "welcome", "login", "passw0rd", "master123", "hello123", "loveme", "zaq12wsx", "qwerty123", "asdf1234", "admin123", "123abc", "password123", "letmein1", "monkey123", "football123", "sunshine1", "iloveyou1", "princess1", "ashley1", "bailey", "diamond", "abcd1234", "1q2w3e4r", "1q2w3e", "flower", "password1", "hello", "ninja", "mustang1", "123654", "123456a", "qwerty1", "hello1", "freedom1", "whatever", "hello123", "charlie1", "888888", "q1w2e3r4", "super123", "samsung", "1111111", "123123123", "123456789a", "qazxsw", "66666666", "unknown", "internet", "soccer1", "purple", "fishing", "maverick", "jessica1", "12345678910", "987654", "ferrari", "corvette", "cherokee", "redskins", "jackson", "william", "cameron", "golfer", "benjamin", "tiffany", "patrick1", "cookie1", "chicken", "liverpool", "blahblah", "hello123", "porsche", "guitar1", "hammer", "beaver", "mickey", "coffee", "peanut", "jupiter", "kitten", "panties", "toyota", "zxcvb", "testing", "bond007", "changeme", "david", "michael1", "q1w2e3r4t5", "asdfasdf", "metallica", "sparky", "snickers", "goldfish", "boomer", "cowboy", "firebird", "blizzard", "startrek", "bootsie", "bubba1", "brooklyn", "rangers", "marlboro", "phantom", "strength", "sandwich", "lovely", "sweetie", "panther", "clinton", "brooklyn", "yamaha", "skyline", "eagles", "pikachu", "booboo", "trouble", "topgun", "bigdaddy", "johnson", "alexander", "dolphins", "mother", "parker", "christin", "business", "butter", "cricket", "nathan", "morgan", "rabbit", "tristan", "rainbow", "melissa", "elephant", "nothing", "apple", "orange", "ginger1", "simpson", "banana", "london", "diego", "august", "success", "hannah", "michelle1", "victoria", "happy", "secret", "steelers", "peaches", "genesis", "brandon1", "popcorn", "teresa", "maxwell", "heather1", "christian", "beauty", "stephen", "winter", "john316", "doctor", "freddie", "winner", "harrison", "bonnie", "shelby", "compass", "adidas", "energy", "angel1", "friends", "forever", "sweetheart", "spring", "someone", "sierra", "pretty", "dancing", "hotdog", "teacher", "lifehack", "mountain", "lovelove", "dreamer", "eclipse", "smokey", "pisces", "phoenix", "kingkong", "caroline", "slipknot", "courtney", "goodluck", "crystal", "garfield", "lollipop", "edward", "tequiero", "pumpkin", "playboy", "christina", "badboy", "december", "spiderman", "mitchell", "stella", "scarface", "disney", "rooster", "brenda", "storm", "sherlock", "pentium", "jeremiah", "gordon", "tomcat" ]
    warn = 0
    user_print = input("введите ваш пароль для получения оценки \n p.s этот код не собирает данные и не украдёт ваш пароль можите не боятся     ")
    if not user_print:
        print("вы не чего не ввели")
        return
    lens = len(user_print)
    result = mixer(user_print)
    #поиск в утечках HIBP
    def hibp_check(user_print):
        hash_full = hashlib.sha1(user_print.encode()).hexdigest().upper()
        prefix = hash_full[:5]
        suffix = hash_full[5:]
        url = f"https://api.pwnedpasswords.com/range/{prefix}"
        response = requests.get(url)
        for line in response.text.splitlines():
            if line.startswith(suffix):
                count = int(line.split(':')[1])
                print(f"ваш пароль слили: {count} раз")
                return count
        return 0
    count = hibp_check(user_print)
    if lens >= 12:
        warn += 0
    elif lens >= 9:
        warn += 1
    else:
        warn += 2
    if user_print in kall_password:
        print("ваш пароль в списке самых популярных срочно замените его он не безопасен! \n оценка -10000000 из 10 срочно замените его")
        return
    if result['has_upper'] == False:
        warn += 1
    if result['has_lower'] == False:
        warn += 1
    if result['has_digit'] == False:
        warn += 1
    if result['has_special'] == False:
        warn += 1
    if count >= 1000:
        warn += 3
        print("_______________________________ \nваш пароль слили очень много раз \nзамените его \n_______________________________ ")
    elif count >= 100:
        warn += 2
        print("ваш пароль слили достатьчно раз чтобы его заменить")
    elif count >= 50:
        warn += 1
        print("ваш пароль слили мало раз но лучше его усложнить")
    elif count <= 10:
        warn += 0
    if warn >= 6:
        print("ваш пароль очень плохой добавте символы всех типов и добавте длину пароля! \n p.s посмотрите 'справка' чтобы сделать пароль безопасней! \n итог - плохой пароль \n ")
        time.sleep(1)
    elif warn >= 3:
        print("ваш пароль хороший но советую его улучшить и сделать его безопасней с помощью 'справка' \n итог - средний пароль \n ")
        time.sleep(1)
    else:
        print("у вас замечательный пароль \n итог - замечательный пароль \n ")
        time.sleep(1)
    return warn
#справка
def reference():
    print("1) Не используйте стандартные последовательности цифр или букв \n 2) Не указывайте год, месяц или день рождения в пароле \n 3) Используйте комбинацию из не менее восьми букв, цифр и символов \n 4) Комбинируйте различные несвязанные слова в пароле или парольной фразе")
    time.sleep(1)
#меню
def menu():
    while True:
        try:
            print("------------------------------------\nМЕНЮ....\n------------------------------------")
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
            rsmdon_pass()
        else:
            print("этих функций ещё нет")
            time.sleep(1)
#запуск кода
menu()
