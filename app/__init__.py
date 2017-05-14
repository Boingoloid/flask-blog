from flask import (Flask, jsonify, abort, flash, Markup, redirect, render_template,
                   request, Response, session, url_for)
from flask_admin import Admin
from flask_mongoengine import MongoEngine
import pymongo
from flask_admin.contrib.mongoengine import ModelView
from flask_mongoengine.wtf import model_form
from flask_admin.model.fields import InlineFormField, InlineFieldList

app = Flask(__name__)
import views

app.config['MONGO_DBNAME'] = "heroku_6r9wd2wt"
app.config['MONGODB_URI'] = "mongodb://part_elf_part_man:all_boingo@ds151117.mlab.com:51117/heroku_6r9wd2wt"

# app.config['MONGO_DBNAME'] = "app"
# app.config['MONGODB_URI'] = 'mongodb://localhost/app'


app.config['SECRET_KEY'] = '38649539871'

app.config.from_object('config')

db = MongoEngine(app)
print 'print the database object'
print db

client = pymongo.MongoClient(app.config['MONGODB_URI'])
db2 = client.get_default_database()

# entry = db2.post.find_one()
# print entry

# class post(db.Document):
#     title = db.StringField(required=True)
#     content = db.StringField(required=True)
#
#     def __unicode__(self):
#         return self.title
#
# # class PostView(ModelView):
# #     pass
#
# admin = Admin(app, MongoEngine)
# admin.add_view(PostView(post))

# Connect to MongoDB and call the connection "my-app".
# connect("mongodb://localhost:27017/myDatabase", alias="my-app")

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