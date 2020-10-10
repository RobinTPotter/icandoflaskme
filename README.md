gunicorn --bind=0.0.0.0 gunicorn-app:app
 
gunicorn --bind=0.0.0.0 flask-app:app
 
gunicorn --bind=0.0.0.0 flask-template-app:app
 
gunicorn testapp:app --bind=0.0.0.0


flask-app and gunicorn-app are self contained
flask-template-app needs templates folder where it is
testapp is same as flask-temate-app but as package

