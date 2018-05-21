I have made a catalog that includes a list of different movies. I have a movie table with columns title, title, year (when the movie came out), description, and an actor that is in the movie. I also created an actor table with columns names. An actor can be in multiple movies but a movie can only have one lead actor.

### Database Design
Actor ID |  Name | Age
------------|---------------|-------------
1 | Ryan Gosling | 37
2 | Chris Evans| 36
3 | Jennifer Lawrence| 27

Movie ID | Title | Year | Description | Actor
---------|-------|-------|------|------------|---------
1 | The Notebook | 2004 | This movie is incredibly romantic... | Ryan Gosling
2 | The avengers | 20212 | The Avengers is the best superhero movie ever made.... |  Chris Evans
3 | Red Sparrow | 2018 | The Red Sparrow is definitely not your average movie... | Jennifer Lawrence

### Instructions

In order to run my website, you'll need to follow a few simple steps to get it up and running in your web browser of choice.

- **Mac Instructions**
  1. Go to my github repository https://github.com/julesrules123/JuliasFinalProject and clone the repo so that you can store it locally.

  2. Open the Command Line

  3. Type the following command to open the project directory:
          cd JuliasFinalProject (hit tab)

  4. Type the following command to create Virtualenv so that you can setup a virtual environment:
          sudo pip install virtualenv

  5. Create the venv folder:
          virtualenv venv

  6. Activate the virtual environment:
          venv/bin/activate

  7. Install the requirements for the project:
          pip install -r requirements.txt

  8. Initialize the database:
          python manage.py deploy

  9. Run the server:
          python manage.py runserver -d

  10. View the website in your web browser by typing your IP address into the address bar.
