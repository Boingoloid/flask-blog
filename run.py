#!flask/bin/python
from app import app
if __name__ == "__main__":
    app.run(debug=False)

# from procfile
# web: gunicorn app.wsgi --log-file -