from models.models import db, City, Profession, Vacancy
from app import app

with app.app_context():
    
    city1 = City(name='Москва')
    city2 = City(name='Санкт-Петербург')
    city3 = City(name='Сочи')
    
    profession1 = Profession(name='Программист')
    profession2 = Profession(name='Дизайнер')
    profession3 = Profession(name='Токарь')

    vacancy1 = Vacancy(profession=profession1, city=city1, salary=100000)
    vacancy2 = Vacancy(profession=profession2, city=city2, salary=80000)
    vacancy3 = Vacancy(profession=profession3, city=city3, salary=70000)
    
    db.session.add_all([city1, city2, city3, profession1, profession2, profession3, vacancy1, vacancy2, vacancy3])
    db.session.commit()