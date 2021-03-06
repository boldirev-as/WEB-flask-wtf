from flask import render_template, Flask, url_for
from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandex_lyceum_secret_key'


@app.route('/index/<title>')
def index(title):
    return render_template("base.html", title=title)


@app.route('/training/<prof>')
def training(prof):
    if "инженер" in prof or "строитель" in prof:
        type_prof = "Научные симуляторы"
        image_dir = url_for('static', filename='img/train.jpg')
    else:
        type_prof = "Тренажеры"
        image_dir = url_for('static', filename='img/train1.jpg')

    return render_template("trainings.html", title=type_prof, type_prof=type_prof,
                           image_dir=image_dir)


@app.route('/list_prof/<type_prof>')
def list_profs(type_prof):
    list_prof = ["Кулинар", "Кулинар_4", "Кулинар_2", "Хлебопечник", "Соусьер", "Повар",
                 "Дигустатор", "Кулинар_3", "Шеф", "Выпекатель", "Едаделатель", "Приготовитель"]
    return render_template("list_prof.html", list_prof=list_prof, types=type_prof)


@app.route('/auto_answer')
@app.route('/answer')
def answer():
    person = {'surname': 'QW', 'name': 'bob', 'education': 'high',
              'profession': 'inhere', 'sex': 'male', 'motivation': 'Want',
              'ready': 'True'}
    return render_template("anwser.html", title="Анкета", person=person,
                           css=url_for('static', filename='css/anwser_style.css'))


class LoginForm(FlaskForm):
    captain_username = StringField('Id капитана', validators=[DataRequired()])
    captain_password = PasswordField('Пароль капитана', validators=[DataRequired()])
    austronavt_username = StringField('Id астронавта', validators=[DataRequired()])
    austronavt_password = PasswordField('Пароль астронавта', validators=[DataRequired()])
    submit = SubmitField('Доступ')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/login')
    return render_template('login.html', title='Авторизация', form=form,
                           css=url_for('static', filename='css/authorization_style.css'),
                           img=url_for('static', filename='img/icon.png'))


@app.route('/distribution')
def distribution():
    user_list = ["Bob", "Gon", "Igor", "Milan", "Boris"]
    return render_template('rooms_order.html', title='Расселение', user_list=user_list)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
