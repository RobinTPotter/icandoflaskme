 2008  gunicorn --bind=0.0.0.0 gunicorn-app:app
 2014  gunicorn --bind=0.0.0.0 flask-app:app
 2019  gunicorn --bind=0.0.0.0 flask-template-app:app
 2045  gunicorn testapp:app --bind=0.0.0.0

flask-app and gunicorn-app are self contained
flask-template-app needs templates folder where it is
testapp is same as flask-temate-app but as package

