from website.database.models_user import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask import render_template, request, redirect, session, url_for, flash, Blueprint
from flask_login import login_required, logout_user, login_user, current_user
from website import db
from sqlalchemy import exc

auth = Blueprint('auth', __name__, template_folder='../templates/user')


@auth.route('/login', methods=["POST", "GET"])
def login():
    if 'userLogged' in session or current_user.is_authenticated:
        return redirect('base.index')

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username != '' and password != '':
            user = User.query.filter_by(username=username).first()
            if not check_password_hash(user.password, password) or user is None:
                flash('Неправильно')
                return redirect(url_for('auth.login'))
            if request.form.get('save_user'):
                login_user(user, remember=True)
            else:
                login_user(user)

            return redirect(url_for('base.profile'))
        else:
            flash("Ошибка")

    return render_template('user/login.html')


@auth.route('/register', methods=["POST", "GET"])
def registration():
    if request.method == 'POST':
        username = request.form.get('username')
        password_1 = request.form.get('password1')
        password_2 = request.form.get('password2')

        if username != '' and password_1 != '':
            user = User.query.filter_by(username=username).first()
            if user:
                flash('Username already exists.')
            else:
                if password_1 == password_2:
                    pass_hash = generate_password_hash(password_1)
                    try:
                        new_user = User(username=username, password=pass_hash)
                        db.session.add(new_user)
                        db.session.commit()
                        login_user(new_user)
                        flash('Account created!')
                        return redirect(url_for('base.index'))
                    except ValueError or exc.DataError:
                        flash('Ошибка!')
                else:
                    flash('Неверно набраный пароль')
        else:
            flash('Ошибка')

    return render_template('user/registration.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('base.index'))

