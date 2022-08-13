from db import db_connection


def get_blog_by_id(id):
    db = db_connection()
    cur = db.cursor()
    params = (id)
    sql = 'SELECT * FROM blog WHERE id = %s' % params
    cur.execute(sql)
    blog = cur.fetchone()
    cur.close()
    db.close()
    return blog

