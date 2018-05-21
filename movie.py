import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

#setup SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)


class Actor(db.Model):
    __tablename__= 'actors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    age = db.Column(db.Integer)
    movies = db.relationship('Movie', backref='actor', cascade='delete')


class Movie(db.Model):
    __tablename__= 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    year = db.Column(db.Integer)
    description = db.Column(db.Text)
    actor_id = db.Column(db.Integer, db.ForeignKey('actors.id'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/movies')
def show_all_movies():
    movies = Movie.query.all()
    return render_template('movie-all.html', movies=movies)


@app.route('/movies/add', methods=['GET', 'POST'])
def add_movies():
    if request.method == 'GET':
        movies = Movie.query.all()
        return render_template('movie-add.html', movies=movies)
    if request.method == 'POST':
        # get data from the form
        title = request.form['title']
        year = request.form['year']
        description = request.form['description']
        actor_name = request.form['actor']
        actor = Actor.query.filter_by(name=actor_name).first()
        movie = Movie(title=title, year=year, description=description, actor=actor)

        # insert the data into the database
        db.session.add(movie)
        db.session.commit()
        return redirect(url_for('show_all_movies'))


@app.route('/movies/delete/<int:id>', methods=['GET', 'POST'])
def delete_movies(id):
    movie = Movie.query.filter_by(id=id).first()
    movies = Movie.query.all()
    if request.method == 'GET':
        return render_template('movie-delete.html', movie=movie)
    if request.method == 'POST':
        db.session.delete(movie)
        db.session.commit()
        return redirect(url_for('show_all_movies'))


@app.route('/movies/edit/<int:id>', methods=['GET', 'POST'])
def edit_movies(id):
    movie = Movie.query.filter_by(id=id).first()
    actors = Actor.query.all()
    if request.method == 'GET':
        return render_template('movie-edit.html', movie=movie, actors=actors)
    if request.method == 'POST':
        movie.title = request.form['title']
        movie.year = request.form['year']
        movie.description = request.form['description']
        actor_name = request.form['actor']
        actor = Actor.query.filter_by(name=actor_name).first()
        movie.actor = actor
        # update the database
        db.session.commit()
        return redirect(url_for('show_all_movies'))


@app.route('/actors')
def show_all_actors():
    actors = Actor.query.all()
    return render_template('actor-all.html', actors=actors)


@app.route('/actors/add', methods=['GET', 'POST'])
def add_actors():
    if request.method == 'GET':
        return render_template('actor-add.html')
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']

        actor = Actor(name=name, age=age)
        db.session.add(actor)
        db.session.commit()
        return redirect(url_for('show_all_actors'))


@app.route('/actors/delete/<int:id>', methods=['GET', 'POST'])
def delete_actors(id):
    actor = Actor.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('actor-delete.html', actor=actor)
    if request.method == 'POST':
        db.session.delete(actor)
        db.session.commit()
        return redirect(url_for('show_all_actors'))


@app.route('/actors/edit/<int:id>', methods=['GET', 'POST'])
def edit_actor(id):
    actor = Actor.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('actor-edit.html', actor=actor)
    if request.method == 'POST':
        actor.name = request.form['name']
        actor.age = request.form['age']
        db.session.commit()
        return redirect(url_for('show_all_actors'))


if __name__ == '__main__':
    app.run()
