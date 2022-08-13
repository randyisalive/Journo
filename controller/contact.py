from pydoc import render_doc
from flask import Blueprint, render_template

contact = Blueprint('contact', __name__)

@contact.route('/')
def index():
    return render_template('contact.html')