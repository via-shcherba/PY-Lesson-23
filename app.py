from flask import Flask, render_template
from models.models import Vacancy, init_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload 
from contextlib import contextmanager


app = Flask(__name__)

DATABASE_URL = 'sqlite:///site.db'
engine = create_engine(DATABASE_URL, echo=True)

init_db(engine)

Session = sessionmaker(bind=engine)


@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
    finally:
        session.close()
        

@app.route('/')
def index():
    dynamic_title = "Это домашнее задание. Урок 22"
    return render_template('index.html', dynamic_title=dynamic_title)


@app.route('/contacts')
def contacts():
    return render_template('contacts.html', email="example@example.com", phone="+123456789")


@app.route('/form')
def form_view():       
    with session_scope() as session: 
        vacancies = session.query(Vacancy).options(joinedload(Vacancy.profession), 
                                                    joinedload(Vacancy.city)).all()
    return render_template('form.html', vacancies=vacancies)


if __name__ == '__main__':
    app.run(debug=True)