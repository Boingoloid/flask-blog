
from flask import (Flask, jsonify, abort, flash, Markup, redirect, render_template,
                   request, Response, session, url_for)
from flask import Flask
from flask_admin import Admin
from flask_mongoengine import MongoEngine
from flask_admin.contrib.mongoengine import ModelView
from flask_mongoengine.wtf import model_form
from flask_admin.model.fields import InlineFormField, InlineFieldList

app = Flask(__name__)
import views

app.config['MONGO_DBNAME'] = "heroku_6r9wd2wt"
app.config['MONGO_URL'] = "mongodb://part_elf_part_man:all_boingo@ds151117.mlab.com:51117/heroku_6r9wd2wt"
app.config['MONGODB_URI'] = "mongodb://part_elf_part_man:all_boingo@ds151117.mlab.com:51117/heroku_6r9wd2wt"

app.config['SECRET_KEY'] = '123456790'

# app.config['MONGODB_SETTINGS'] = {
#     'db': 'heroku_6r9wd2wt',
#     'username':'part_elf_part_man',
#     'password':'all_boingo',
#     'host':'mongodb://part_elf_part_man:all_boingo@ds151117.mlab.com:51117/heroku_6r9wd2wt',
#     'port':51117
# }
app.config.from_object('config')
app.config.from_pyfile('../config.py')

db = MongoEngine(app)
print 'print the database object'
print db.Document

# class UserForm(Form):
#     name = StringField('Name')
#     email = StringField('Email')

class Post(db.Document):
    title = db.StringField(required=True)
    content = db.StringField(required=True)

    def __unicode__(self):
        return self.title

class PostView(ModelView):
    can_delete = True  # disable model deletion
    column_editable_list = ['title', 'content']

admin = Admin(app, MongoEngine)
admin.add_view(PostView(Post))

    # column_filters = ['title']

# PostView = model_form(post)

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

# admin = admin.Admin(app, name='flask-blog-mj', template_mode='bootstrap3')
from flask_admin.contrib.sqla import ModelView





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







# if __name__ == '__main__':




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