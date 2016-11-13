



import datetime
import functools
import os
import re
import urllib

from flask_sqlalchemy import SQLAlchemy


import json


from flask import (Flask, jsonify, abort, flash, Markup, redirect, render_template,
                   request, Response, session, url_for)
from flask_pymongo import PyMongo
import pymongo
import views

from markdown import markdown
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.extra import ExtraExtension
from micawber import bootstrap_basic, parse_html
from micawber.cache import Cache as OEmbedCache
from peewee import *
from playhouse.flask_utils import FlaskDB, get_object_or_404, object_list
from playhouse.sqlite_ext import *


app = Flask(__name__)

app.config['MONGO_DBNAME'] = "heroku_6r9wd2wt"
app.config['MONGO_URL'] = "mongodb://part_elf_part_man:all_boingo@ds151117.mlab.com:51117/heroku_6r9wd2wt"
app.config['MONGODB_URI'] = "mongodb://part_elf_part_man:all_boingo@ds151117.mlab.com:51117/heroku_6r9wd2wt"
app.config.from_object('config')
mongo = PyMongo(app)


from datetime import datetime

oembed_providers = bootstrap_basic(OEmbedCache())


@app.route('/add')
def add():
    # online_users = list(mongo.db.users.find().count())
    client = pymongo.MongoClient(app.config['MONGODB_URI'])
    db = client.get_default_database()

    # result = db.users.insert_one()
    userscount = db.hello_world.find().count()

    print "print some shit"
    print(userscount)

#     title = CharField()
#     slug = CharField(unique=True)
#     content = TextField()
#     published = BooleanField(index=True)
#     timestamp = DateTimeField(default=datetime.datetime.now, index=True)

    result = db.post.insert_one(
    {
        "title": "First Post",
        "content": "The body of the post with image: ![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png \"Logo Title Text 1\")",
        "published": 1,
        "timestamp": datetime.utcnow(),
    }
    )

    print (result)
    return 'Added post'


# script to add a user
    # result = db.user.insert_one(
    # {
    #     "nickname": "Matt",
    #     "username": "matthew.acalin@gmail.com",
    #     "email": "matthew.acalin@gmail.com",
    #     "pw": "m",
    #     "admin": "yes"
    # }
    # )


# app.config.from_object('config')
# db = SQLAlchemy(app)



# ADMIN_PASSWORD = 'secret'
# APP_DIR = os.path.dirname(os.path.realpath(__file__))
# DATABASE = 'sqliteext:///%s' % os.path.join(APP_DIR, 'app.db')
# DEBUG = False
# SECRET_KEY = 'shhh, secret!'  # Used by Flask to encrypt session cookie.
# SITE_WIDTH = 800


# app = Flask(__name__)
# app.config.from_object(__name__)
#
# flask_db = FlaskDB(app)
# database = flask_db.database
#
# oembed_providers = bootstrap_basic(OEmbedCache())


# @app.template_filter('clean_querystring')
# def clean_querystring(request_args, *keys_to_remove, **new_values):
#     querystring = dict((key, value) for key, value in request_args.items())
#     for key in keys_to_remove:
#         querystring.pop(key, None)
#     querystring.update(new_values)
#     return urllib.urlencode(querystring)
#
# @app.errorhandler(404)
# def not_found(exc):
#     return Response('<h3>Not found</h3>'), 404
#
# def main():
#     database.create_tables([Entry, FTSEntry], safe=True)
#     app.run(debug=True)
#
# if __name__ == '__main__':
#     main()