from flask import Flask, render_template
from models.models import db, Vacancy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  

with app.app_context():
    db.create_all() 


@app.route('/')
def index():
    dynamic_title = "Это домашнее задание. Урок 22"
    return render_template('index.html', dynamic_title=dynamic_title)


@app.route('/contacts')
def contacts():
    return render_template('contacts.html', email="example@example.com", phone="+123456789")


@app.route('/form')
def form_view():       
    vacancies = Vacancy.query.all()
    return render_template('form.html', vacancies=vacancies)


if __name__ == '__main__':
    app.run(debug=True)