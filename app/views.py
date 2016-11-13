from app import app
from app import mongo
from flask_pymongo import PyMongo
import pymongo

from flask import (Flask, jsonify, abort, flash, Markup, redirect, render_template,
                   request, Response, session, url_for)


from markdown import markdown
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.extra import ExtraExtension
from micawber import bootstrap_basic, parse_html
from micawber.cache import Cache as OEmbedCache
from peewee import *
from playhouse.flask_utils import FlaskDB, get_object_or_404, object_list
from playhouse.sqlite_ext import *
# SITE_WIDTH = 800


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
    oembed_providers = bootstrap_basic(OEmbedCache())

    blog = db.post.find_one()
    blogContent = blog['content']



    def html_content(blog):
        hilite = CodeHiliteExtension(linenums=False, css_class='highlight')
        extras = ExtraExtension()
        markdown_content = markdown(blog['content'], extensions=[hilite, extras])
        oembed_content = parse_html(
            markdown_content,
            oembed_providers,
            urlize_all=True,
            # maxwidth=app.config['SITE_WIDTH']
        )
        return Markup(oembed_content)

    blogEnriched = html_content(blog)



    return render_template("index.html", title='Home', user=user, posts=posts,blogContent=blogContent, blog=blog,
                           blogEnriched=blogEnriched)



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
