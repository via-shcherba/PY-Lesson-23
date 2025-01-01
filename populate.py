from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.models import City, Profession, Vacancy, init_db


DATABASE_URL = 'sqlite:///site.db'
engine = create_engine(DATABASE_URL, echo=True)

init_db(engine)

Session = sessionmaker(bind=engine)
session = Session()


def populate_database():
    session.query(Vacancy).delete()
    session.query(City).delete()
    session.query(Profession).delete()
    
    city1 = City('Москва')
    city2 = City('Санкт-Петербург')
    city3 = City('Сочи')

    profession1 = Profession('Программист')
    profession2 = Profession('Дизайнер')
    profession3 = Profession('Токарь')

    session.add_all([city1, city2, city3])
    session.commit()

    session.add_all([profession1, profession2, profession3])
    session.commit()

    vacancy1 = Vacancy(profession=profession1, city=city1, salary=100000)
    vacancy2 = Vacancy(profession=profession2, city=city2, salary=80000)
    vacancy3 = Vacancy(profession=profession3, city=city3, salary=70000)

    session.add_all([vacancy1, vacancy2, vacancy3])
    session.commit()

    print("База данных успешно заполнена!")
    

if __name__ == '__main__':
    populate_database()