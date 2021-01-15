DB_PATH_LOCAL = "sqlite:///sochi_athletes_local.sqlite3"

def valid_email(email):
    """Функция проверяет правильность ввода email"""
    if email.count('@') == 1:
        if "." in email.split("@")[1]:
            return True
    print("Введите правильный email")
    return False

def valid_date(date):
    """Функция проверяет правильность ввода даты рождения в формате yyyy-mm-dd"""
    list_date = date.split("-")
    if (len(list_date) == 3) and ((int(list_date[0]) >= 1900) and (int(list_date[0]) <= 2020)) and \
    ((int(list_date[1]) >= 0) and (int(list_date[1])) <= 12) and \
    ((int(list_date[2]) >= 0) and (int(list_date[1])) <= 31):
        return True
    else:
        print("Введите корректную дату")
        return False

def request_data(db_path):
    """Функция подключается к базе данных и запрашивает на ввод данные пользователя, 
    затем сохраняет их в базу данных в таблицу user"""
    session = db.connect_db(db_path)
    print("Введите данные для регистрации:")
    first_name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    gender = input("Введите пол (Male или Female): ")
    email = input("Введите адрес электронной почты: ")
    while not(valid_email(email)):
        email = input()
    birthdate = input("Введите дату рождения в формате yyyy-mm-dd: ")
    while not(valid_date(birthdate)):
        birthdate = input()
    height = input("Введите рост: ")
    user = db.User(
        first_name = first_name,
        last_name = last_name,
        gender = gender,
        email = email,
        birthdate = birthdate,
        height = height
    )
    session.add(user)
    session.commit()
    return user

def main():
    user = request_data(DB_PATH_LOCAL)
    print("Пользователь {} {} добавлен в базу".format(user.first_name, user.last_name))

if __name__ == "__main__":
    import db
    DB_PATH_LOCAL = "sqlite:///./sochi_athletes.sqlite3"
    main()
else:
    from utils import db
