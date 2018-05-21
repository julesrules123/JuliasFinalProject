from flask_script import Manager
from movie import app, db, Actor, Movie

manager = Manager(app)

@manager.command
def deploy():
    print ("resetting database....")
    db.drop_all()
    db.create_all()

    gosling = Actor(name="Ryan Gosling", age="37")
    evans = Actor(name="Chris Evans", age="36")
    lawrence = Actor(name="Jennifer Lawrence", age="27")

    notebook = Movie(title="The Notebook", year="2004", description="This movie is incredibly romantic. I would reccomend seeing this with a loved one, or if its a girls night and you want to cry. This is such a beautiful movie!", actor=gosling)
    avengers = Movie(title="The Avengers", year="2012", description="The Avengers is the best superhero movie ever made so far. Different superheros come together to fight in an awesome squad to beat aliens and villians.", actor=evans)
    sparrow = Movie(title="Red Sparrow", year="2018", description="The Red Sparrow is definitely not your average movie, it is action packed, bloody and sexual all at the same time.", actor=lawrence)

    db.session.add(gosling)
    db.session.add(evans)
    db.session.add(lawrence)

    db.session.add(notebook)
    db.session.add(avengers)
    db.session.add(sparrow)

    db.session.commit()


if __name__ == '__main__':
    manager.run()
