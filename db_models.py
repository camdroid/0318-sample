from flask import Flask
from flask import render_template
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

@app.route('/get_users')
def get_users():
    users = User.query.all()
    print(users)
    if users:
        return render_template('list_users.html', users=users)
    else:
        return "no users found!"


@app.route('/add_user/<uname>')
def add_user(uname):
    db.session.add(User(username=uname))
    db.session.commit()
    return 'Succesfully added user ' + uname


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))

    def __repr__(self):
        return self.username


db.create_all()

if __name__ == '__main__':
    app.run()
