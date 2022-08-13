from flask import Blueprint, render_template, redirect
from services.home import *


home = Blueprint('home', __name__)

@home.route('/')
def index():
    blog = get_blog()
    return render_template('index.html', blog=blog)

