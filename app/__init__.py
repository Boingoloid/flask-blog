
import datetime

from flask import (Flask, jsonify, abort, flash, Markup, redirect, render_template,
                   request, Response, session, url_for)
import pymongo
from flask import Flask
from flask_admin import Admin
import mongoengine as me
from flask_mongoengine import MongoEngine
from flask_admin.form import rules
from flask_admin.contrib.mongoengine import ModelView
from flask_mongoengine.wtf import model_form


app = Flask(__name__)
import views

app.config['MONGO_DBNAME'] = "heroku_6r9wd2wt"
app.config['MONGO_URL'] = "mongodb://part_elf_part_man:all_boingo@ds151117.mlab.com:51117/heroku_6r9wd2wt"
app.config['MONGODB_URI'] = "mongodb://part_elf_part_man:all_boingo@ds151117.mlab.com:51117/heroku_6r9wd2wt"
app.config.from_object('config')
# app.config['MONGODB_SETTINGS'] = {'db': 'heroku_6r9wd2wt',
# 'host': 'mongodb://part_elf_part_man:all_boingo@ds151117.mlab.com:51117/heroku_6r9wd2wt'
# }
# mongo = PyMongo(app)
#
# app.config['MONGODB_DB'] = 'heroku_6r9wd2wt'
# app.config['MONGODB_USERNAME'] = 'part_elf_part_man'
# app.config['MONGODB_PASSWORD'] = 'all_boingo'
# app.config['MONGODB_HOST'] = 'mongodb://part_elf_part_man:all_boingo@ds151117.mlab.com:51117/heroku_6r9wd2wt'
# app.config['MONGODB_PORT'] = 51117

# client = pymongo.MongoClient(app.config['MONGODB_URI'],connect=False)
# db = client.get_default_database()
db = MongoEngine(app)

# client = pymongo.MongoClient(app.config['MONGODB_URI'])
# DEFAULT_CONNECTION_NAME = 'default-mongodb-connection'
# alias=DEFAULT_CONNECTION_NAME
# connection = db.connection

# db = client.get_default_database()

# app.config['MONGODB_SETTINGS'] = {
#     'alias': 'default',
#     'db': 'heroku_6r9wd2wt',
#     'host': 'mongodb://part_elf_part_man:all_boingo@ds151117.mlab.com:51117/heroku_6r9wd2wt',
#     'port': 51117,
# }

# conn = pymongo.Connection()

class post(db.Document):
    title = db.StringField(required=True)
    # title = db.StringField(required=True)
    # content = db.StringField(required=True)

    def __unicode__(self):
        return self.title

class PostView(ModelView):
    pass
    # column_filters = ['title']

# PostView = model_form(post)



# admin = admin.Admin(app, name='flask-blog-mj', template_mode='bootstrap3')
from flask_admin.contrib.sqla import ModelView



# if __name__ == '__main__':
    # Create admin
admin = Admin(app, MongoEngine)
admin.add_view(PostView(post))


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