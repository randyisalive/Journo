from flask import Blueprint, flash,render_template, request, session, url_for, redirect
from db import db_connection

login = Blueprint('login', __name__)


@login.route('/login/', methods=['POST', 'GET'])
def index():
    error = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = db_connection()
        cur = conn.cursor()
        params = (username, password)
        sql = "SELECT id, username, password FROM user WHERE username = '%s' AND password = '%s'" % params
        cur.execute(sql)
        user = cur.fetchone()
        if user is None:
            error = 'Wrong username or password'
        else:
            session.clear()
            session['id'] = user[0]
            session['username'] = user[1]
            session['password'] = user[2]
            name = session.get('username')
            user_id = session.get('id')
            return redirect(url_for('home.index', name=name, user_id=user_id))
        flash(error)
        cur.close()
        conn.close()
    return render_template('login.html', error=error)

@login.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home.index'))