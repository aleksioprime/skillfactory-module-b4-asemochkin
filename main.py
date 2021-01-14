# подклюваем модули из пакета utils
from utils import users, find_athlete, db

# константа, указывающая способ соединения с базой данных
DB_PATH = "sqlite:///sochi_athletes.sqlite3"

def main():

    """Основная функция программы с выбором режима, каждый из которых обращается к конкретному модулю:
    - модуль users.py регистрирует новых пользователей
    - модуль find_athlete.py ищет и выводит ближайщих по дате рождения и росту к пользователю атлетов"""

    mode = input("Выбери режим.\n1 - Зарегистрировать нового пользователя\n2 - Поиск ближайшего к пользователю атлета по дате рождения\n=> ")
    if mode == "1":
        user = users.request_data(DB_PATH)
        print("Пользователь {} {} добавлен в базу".format(user.first_name, user.last_name))
    elif mode == "2":
        is_finded, min_height_athelete, min_date_athelete = find_athlete.find_date_and_height(DB_PATH)
        if is_finded:
            print("Ближайший по росту атлет: {} ({})".format(min_height_athelete.name,  min_height_athelete.height))
            print("Ближайший по дате атлет: {} ({})".format(min_date_athelete.name, min_date_athelete.birthdate))
        else:
            print("Пользователь не найден")
    else:
        print("Некорректный режим")

if __name__ == "__main__":
    main()
