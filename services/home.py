from controller.post import *
from db import db_connection


def get_blog():
    db = db_connection()
    cur = db.cursor()
    sql = 'SELECT id,title,subs FROM blog'
    cur.execute(sql)
    blog = cur.fetchall()
    cur.close()
    db.close()
    return blog

def get_blog_title_by_id(id):
    db = db_connection()
    cur = db.cursor()
    params = (id)
    sql = 'SELECT title FROM blog WHERE id = %s' % params
    cur.execute(sql)
    title = cur.fetchone()
    cur.close()
    db.close()
    return id, title

