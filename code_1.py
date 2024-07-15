from flask import Flask, render_template
import sqlite3
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)   

@app.route('/')
def index():
    return render_template('page.html')

@app.route('/excursions')
def excursions():
    # Получение данных об экскурсиях из базы данных
    conn = sqlite3.connect('instance/travels.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Tourism")
    excursions = c.fetchall()
    conn.close()

    return render_template('excursions.html', excursions=excursions)

class Myform(FlaskForm):
    Экскурсия = StringField('Название', validators=[DataRequired()])
    Продолжительность = IntegerField('Продолжительность (часов)', validators=[DataRequired()])
    Цена = IntegerField('Цена ($)', validators=[DataRequired()])
    submit = SubmitField('Добавить')
 
@app.route('/form', methods=['POST'])
def form():
    form = Myform()
    if form.validate_on_submit():   
        return render_template ('Form.html', form = form)

if __name__ == '__main__':
    app.config["WTF_CSRF_ENABLED"] = False  
    app.run(debug=True)