from datetime import datetime

DB_PATH_LOCAL = "sqlite:///sochi_athletes_local.sqlite3"

def find_date_and_height(db_path):
    session = db.connect_db(db_path)
    id_user = input("Введите идентификатор пользователя: ")
    finded_user = session.query(db.User).filter(db.User.id == id_user).first()
    if finded_user:
        print("Найден пользователь {} {}, дата рождения: {}, рост: {}".format(
            finded_user.first_name, finded_user.last_name, finded_user.birthdate, finded_user.height))
        querry_atheletes = session.query(db.Athelete)
        atheletes = [(ath.id, ath.birthdate, ath.height) for ath in querry_atheletes.all()]
        min_ath_date = abs(datetime.strptime(atheletes[0][1], "%Y-%m-%d")-datetime.strptime(finded_user.birthdate, "%Y-%m-%d"))
        min_ath_height = abs(atheletes[0][2] - finded_user.height)
        for ath in atheletes:
            if ath[2] is not None:
                abs_ath_height = abs(ath[2] - finded_user.height)
                if abs_ath_height < min_ath_height:
                    min_ath_height = abs_ath_height
                    min_id_height = ath[0]
            if ath[1] is not None:
                abs_ath_date = abs(datetime.strptime(ath[1], "%Y-%m-%d")-datetime.strptime(finded_user.birthdate, "%Y-%m-%d"))
                if abs_ath_date < min_ath_date:
                    min_ath_date = abs_ath_date
                    min_id_date = ath[0]
        min_height_athelete = session.query(db.Athelete).filter(db.Athelete.id == min_id_height).first()
        min_date_athelete = session.query(db.Athelete).filter(db.Athelete.id == min_id_date).first()
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
    main()
else:
    from utils import db
