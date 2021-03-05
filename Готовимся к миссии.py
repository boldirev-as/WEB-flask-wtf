from flask import render_template, Flask, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
