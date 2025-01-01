from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class City(Base):
    __tablename__ = 'city'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    vacancies = relationship("Vacancy", back_populates="city")

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.id}) {self.name}'


class Profession(Base):
    __tablename__ = 'profession'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    vacancies = relationship("Vacancy", back_populates="profession")

    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f'{self.id}) {self.name}'


class Vacancy(Base):
    __tablename__ = 'vacancy'
    
    id = Column(Integer, primary_key=True)
    profession_id = Column(Integer, ForeignKey('profession.id'), nullable=False)
    city_id = Column(Integer, ForeignKey('city.id'), nullable=False)
    salary = Column(Float, nullable=False)

    profession = relationship("Profession", back_populates="vacancies")
    city = relationship("City", back_populates="vacancies")

    def __init__(self, profession, city, salary):
        self.profession = profession
        self.city = city
        self.salary = salary

    def __str__(self):
        return f'{self.id}) {self.profession.name} in {self.city.name}: {self.salary}'


def init_db(engine):
    Base.metadata.create_all(engine)