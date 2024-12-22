#Simply run this file to run the whole app.


from forum import app
from forum import db

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)