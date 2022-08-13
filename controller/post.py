from turtle import title
from flask import Blueprint, render_template
from services.post import *


post = Blueprint('post', __name__)


@post.route('/<id>/<title>')
def post_read(title,id):
    blog = get_blog_by_id(id)
    return render_template('post.html', blog=blog, id=id, title=title)