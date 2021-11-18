import random
random.seed(10)


letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
genders = "男女"
i = 0
print("需要產生幾筆資料?")
sets = int(input())


def password_generator():
    password_list = []
    for password in range(5):
        password_list.append(random.choice(letters))
        password_list.append(random.choice(numbers))
        random.shuffle(password_list)
        password = "".join(password_list)
    print("密碼:"+password)
    return password


def user_generator():
    user_list = []
    for user in range(5):
        user_list.append(random.choice(letters))
        user_list.append(random.choice(numbers))
        random.shuffle(user_list)
        user = "".join(user_list)
    print("使用者:"+user)
    return user


def gender_generator():
    gender_list = []
    for gender in range(1):
        gender_list.append(random.choice(genders))
        gender = "".join(gender_list)
    print("性別:"+gender)

    if gender == "男":
        height = random.randint(150, 200)
        weight = random.randint(50, 100)
        print("身高:"+str(height))
        print("體重:"+str(weight))
    else:
        height = random.randint(140, 180)
        weight = random.randint(35, 80)
        print("身高:"+str(height))
        print("體重:"+str(weight))

    return (gender, height, weight)


def birthday():
    year = random.randint(1911, 2011)
    month = random.randint(1, 12)
    if month == (1, 3, 5, 7, 8, 10, 12):
        day = random.randint(1, 32)
    elif month == (2):
        day = random.randint(1, 29)
    else:
        day = random.randint(1, 31)
    birthday = (f"{str(year)}/{str(month)}/{str(day)}")
    print(f"生日:{birthday}")
    return (birthday)


def score():
    score = random.randint(10, 100)
    print("分數:" + str(score))
    return score


for i in range(sets):
    if i <= (sets):
        user_generator()
        password_generator()
        gender_generator()
        birthday()
        score()
        print()
        i += 1
