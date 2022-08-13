from pydoc import render_doc
from flask import Blueprint, render_template, redirect



admin = Blueprint('admin', __name__)


@admin.route('/')
def index():
    return render_template('admin/index.html')