## How to flask with gunicorn

# gunicorn --bind=0.0.0.0 gunicorn-app:app

a very basic gunicorn app a single file source

# gunicorn --bind=0.0.0.0 flask-app:app

a very basic flask app can be run by gunicorn

# gunicorn --bind=0.0.0.0 flask-template-app:app

a basic flask app with templates, but templates are not in the right folder

# gunicorn testapp:app --bind=0.0.0.0

the same basic flask app but with a folder and stuff



flask-app and gunicorn-app are self contained
flask-template-app needs templates folder where it is
testapp is same as flask-temate-app but as package

