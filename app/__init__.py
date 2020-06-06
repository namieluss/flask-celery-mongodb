__author__ = "Suleiman"

from celery import Celery
from flask import Flask, render_template
from pymongo import MongoClient

from .constants import *

app = Flask(__name__, template_folder="templates")

app.config['CELERY_BROKER_URL'] = MONGODB_CON_STR
app.config['CELERY_RESULT_BACKEND'] = MONGODB_CON_STR

db = MongoClient(MONGODB_URL)[DB_NAME]

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

from .task import check_who_and_where


@app.route('/')
def index_page():
    check_who_and_where(page='index')
    return render_template('index.html')


@app.route('/about')
def about_page():
    check_who_and_where(page='about')
    return render_template('about.html')


@app.route('/contact')
def contact_page():
    return render_template('contact.html')
