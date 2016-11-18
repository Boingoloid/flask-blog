#!flask/bin/python
from app import app

app.run(debug=True)


# from procfile
# web: gunicorn app.wsgi --log-file -