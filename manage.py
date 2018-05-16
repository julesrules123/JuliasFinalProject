from flask_script import Manager
from movie import app, db, Movie, Actor

manager = Manager(app)

@manager.command
def deploy():
    print ("resetting database....")
    db.drop_all()
    db.create_all()

    gosling = Actor(name="Ryan Gosling", age="37")
    evans = Actor(name="Chris Evans", age="36")

    notebook = Movie(name="The Notebook", year="2004", description="juLIA PUT THIS IN", actor=gosling)
    avengers = Movie(name="The Avengers", year="2012", description="JULIA", actor=evans)

    db.session.add(gosling)
    db.session.add(evans)

    db.session.add(notebook)
    db.session.add(avengers)

    db.session.commit()


if __name__ == '__main__':
    manager.run()
