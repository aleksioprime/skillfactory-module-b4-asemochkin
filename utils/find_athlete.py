from datetime import datetime

def get_min_date_height(athel, fuser):
    """Функция ищет минимальную разницу между датой рождения пользователя (fuser.birthdate) и атлета (второй элемент списка athel), а также
    минимальную разницу между их ростом (fuser.height и третий элемент списка athel). Функция возвращает ID найденных атлетов"""
    min_ath_date = abs(datetime.strptime(athel[0][1], "%Y-%m-%d")-datetime.strptime(fuser.birthdate, "%Y-%m-%d"))
    min_ath_height = abs(athel[0][2] - fuser.height)
    for ath in athel:
        if ath[2] is not None:
            abs_ath_height = abs(ath[2] - fuser.height)
            if abs_ath_height < min_ath_height:
                min_ath_height = abs_ath_height
                min_id_height = ath[0]
        if ath[1] is not None:
            abs_ath_date = abs(datetime.strptime(ath[1], "%Y-%m-%d")-datetime.strptime(fuser.birthdate, "%Y-%m-%d"))
            if abs_ath_date < min_ath_date:
                min_ath_date = abs_ath_date
                min_id_date = ath[0]
    return min_id_height, min_id_date

def find_date_and_height(db_path):
    """Функция подключается к базе данных, делает запрос на получение данных о пользователе из таблицы user 
    и если он найден по ID, то выполняет поиск наиболее близких атлетов по дате рождения и росту. 
    Функция возвращает флаг истинности и данные найденных атлетов и флаг ложности и None, если пользователь не был найден"""
    session = db.connect_db(db_path)
    id_user = input("Введите идентификатор пользователя: ")
    finded_user = session.query(db.User).filter(db.User.id == id_user).first()
    if finded_user:
        print("Найден пользователь {} {}, дата рождения: {}, рост: {}".format(
            finded_user.first_name, finded_user.last_name, finded_user.birthdate, finded_user.height))
        atheletes = [(ath.id, ath.birthdate, ath.height) for ath in session.query(db.Athelete).all()]
        mih, mid = get_min_date_height(atheletes, finded_user)
        min_height_athelete = session.query(db.Athelete).filter(db.Athelete.id == mih).first()
        min_date_athelete = session.query(db.Athelete).filter(db.Athelete.id == mid).first()
        return True, min_height_athelete, min_date_athelete
    else:
        return False, None, None

def main():
    is_finded, min_height_athelete, min_date_athelete = find_date_and_height(DB_PATH_LOCAL)
    if is_finded:
        print("Ближайший по росту атлет: {} ({})".format(min_height_athelete.name,  min_height_athelete.height))
        print("Ближайший по дате атлет: {} ({})".format(min_date_athelete.name, min_date_athelete.birthdate))
    else:
        print("Пользователь не найден")

if __name__ == "__main__":
    import db
    DB_PATH_LOCAL = "sqlite:///./sochi_athletes.sqlite3"
    main()
else:
    from utils import db
