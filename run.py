#!flask/bin/python
from app import app
from app import views
app.run(debug=True)


# from procfile
# web: gunicorn app.wsgi --log-file -