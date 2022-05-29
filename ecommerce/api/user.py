from unicodedata import name
from flask import render_template, request, redirect, url_for, session, flash
from __main__ import app

from ecommerce.models.user import db_user, User

def save_user(name, email, login, password, address, telephone):
    user = User(name, email, login, password, address, telephone)
    db_user.session.add(user)
    db_user.session.commit()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.permanent = True
        user_login = request.form['login']
        user_password = request.form['password']

        foundUser = User.query.filter_by(login=user_login, password=user_password).first()
        if foundUser:
            session['user'] = user_login
            flash(f'Login successful.', 'info')
            return redirect(url_for('user'))
        else:
            flash(f'Login or password incorrect.', 'info')
            return redirect(url_for('login'))

    else:
        if 'user' in session:
            flash(f'Already logged in.', 'info')
            return redirect(url_for('user'))
        else:
            return render_template('user/login_page.html')

@app.route('/logout')
def logout():
    flash(f'You have been logged out.', 'info')
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/user')
def user():
    if 'user' in session:
        user = User.query.filter_by(login=session['user']).first()
        return render_template('user/user_page.html', user=user)
    else:
        return redirect(url_for('login'))

@app.route('/user/create/', methods=['GET', 'POST'])
def create_user():
    if request.method == 'GET':
        return render_template('user/create_user_page.html')
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        login = request.form['login']
        password = request.form['password']
        address = request.form['address']
        telephone = request.form['telephone']
        save_user(name, email, login, password, address, telephone)
        return redirect('/login')