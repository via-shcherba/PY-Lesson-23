from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class Profession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class Vacancy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    profession_id = db.Column(db.Integer, db.ForeignKey('profession.id'), nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)
    salary = db.Column(db.Float, nullable=False)

    profession = db.relationship('Profession', backref='vacancies')
    city = db.relationship('City', backref='vacancies')