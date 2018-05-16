import os
from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

#setup SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)


class Movie(db.Model):
    __tablename__= 'movies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    year = db.Column(db.Integer)
    description = db.Column(db.Text)
    actor_id = db.Column(db.Integer, db.ForeignKey('actors.id'))


class Actor(db.Model):
    __tablename__= 'actors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    age = db.Column(db.Integer)
    movies = db.relationship('Movie', backref='actor', cascade='delete')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/movies')
def movies():
    return render_template('movie-all.html')


@app.route('/actors')
def actors():
    return render_template('actor-all.html')


if __name__ == '__main__':
    app.run()
