# -*- coding: utf-8 -*-

from app import app
import pymongo
import codecs

from flask import (Flask, jsonify, abort, flash, Markup, redirect, render_template,
                   request, Response, session, url_for)


from markdown import markdown
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.extra import ExtraExtension
import markdown2
from markdown2 import Markdown
markdowner = Markdown()
from micawber import bootstrap_basic, parse_html
from micawber.cache import Cache as OEmbedCache
from peewee import *
from playhouse.flask_utils import FlaskDB, get_object_or_404, object_list
from playhouse.sqlite_ext import *
# SITE_WIDTH = 800

oembed_providers = bootstrap_basic(OEmbedCache())


# encoding=utf8
import sys
reload(sys)
# sys.setdefaultencoding('utf8')


@app.route('/post')
def post():
    return render_template("post.html")

@app.route('/links')
def links():
    query_string = request.query_string  ## There is it
    print "printing query string"
    print query_string
    # return "hello"
    return redirect(query_string,302)


@app.route('/about')
def about():
    return 'about page'

@app.route('/contact', methods=['GET'])
def contact():
    return render_template("contact.html")

@app.route('/send-contact', methods=['GET', 'POST'])
def send_contact():
    print "send contact function!"
    contact_data = request.json['data']
    print contact_data

    client = pymongo.MongoClient(app.config['MONGODB_URI'])
    db = client.get_default_database()
    saveReturn = db.contact_form.save(contact_data)
    print saveReturn

    return ('hello',203)

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]



    blogTitle = "First Post"
    client = pymongo.MongoClient(app.config['MONGODB_URI'])
    db = client.get_default_database()

    blog = db.post.find_one()

    in_file = open("app/static/img/blog-started/text.txt") # open file lorem.txt for reading text
    # data
    # in_file = codecs.open("app/static/img/blog-started/text.txt", "r", "utf8") # open file lorem.txt for reading text
    contents = in_file.read() # read the entire file into a string variable
    in_file.close() # close the file
    contents_unicode = contents.decode('utf-8')
    print "print contents of read method:"
    print(type(contents)) # print contents
    # code = unicode(contents)
    # print (type(code))
    # contents_unicode = contents.decode('utf-8').strip()
    # print (type(contents_unicode))
    # a = contents_unicode
    # b = a.encode('ascii','ignore')
    # print (type(blog["content"]))


    markdowner = Markdown()

    def html_content(contents):
        hilite = CodeHiliteExtension(linenums=False, css_class='highlight')
        extras = ExtraExtension()
        markdown_content = markdown(contents, extensions=[hilite, extras])
        oembed_content = parse_html(
            markdown_content,
            oembed_providers,
            urlize_all=True
            # maxwidth=app.config['SITE_WIDTH']
        )
        return Markup(oembed_content)

    word = markdowner.convert(contents)

    import lxml
    from lxml import html

    # blogEnriched = html_content(contents)
    # blogEnriched = html_content("*boo!*")
    blogEnriched = Markup(word)

    return render_template("index.html", title='Home', user=user, posts=posts, blog=blog, blogEnriched=blogEnriched)

import datetime
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

if __name__ == '__main__':
    app.run(debug=True)



    # @app.route('/login', methods=['GET', 'POST'])
    # def login():
    #     form = LoginForm()
    #     if form.validate_on_submit():
    #         flash('Login requested for OpenID="%s", remember_me=%s' %
    #               (form.openid.data, str(form.remember_me.data)))
    #         return redirect('/index')
    #     return render_template('login.html',
    #                            title='Sign In',
    #                            form=form,
    #                            providers=app.config['OPENID_PROVIDERS'])


    #
    # @app.route('/')
    # def index():
    #     search_query = request.args.get('q')
    #     if search_query:
    #         query = Entry.search(search_query)
    #     else:
    #         query = Entry.public().order_by(Entry.timestamp.desc())
    #     return object_list('index.html', query, search=search_query)






    # '''
    # <html>
    #   <head>
    #     <title>Home Page</title>
    #   </head>
    #   <body>
    #     <h1>Hello, ''' + user['nickname'] + '''</h1>
    #   </body>
    # </html>
    # '''
