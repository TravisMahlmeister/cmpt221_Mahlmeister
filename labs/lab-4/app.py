"""app.py: render and route to webpages"""

import os
from dotenv import load_dotenv
from flask import Flask, render_template
from db.server import init_database, get_session
from db.schema import Course, Professor, ProfessorCourse
from db.sql import insert_courses, get_all_courses, update_course, delete_course
from db.orm import insert_professors, get_all_professors, update_professor, delete_professor

# load environment variables from .env
load_dotenv()

# database connection - values set in .env
db_name = os.getenv('db_name')
db_owner = os.getenv('db_owner')
db_pass = os.getenv('db_pass')
db_url = f"postgresql://{db_owner}:{db_pass}@localhost/{db_name}"

def create_app():
    """Create Flask application and connect to your DB"""
    # create flask app
    app = Flask(__name__, 
                template_folder=os.path.join(os.getcwd(), 'templates'), 
                static_folder=os.path.join(os.getcwd(), 'static'))
    
    # connect to db
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url
    
    # Initialize database
    with app.app_context():
        if not init_database():
            print("Failed to initialize database. Exiting.")
            exit(1)

    # ===============================================================
    # routes
    # ===============================================================

    # create a webpage based off of the html in templates/index.html
    @app.route('/')
    def index():
        """Home page"""
        return render_template('index.html')

    @app.route('/sql')
    def sql():
        insert_courses()
        courses = get_all_courses()
        update_course() 
        delete_course()

        # print the table to the console
        courses = get_all_courses()
        for course in courses:
            print(course)

        return "I managed the Courses table using raw SQL!"
    
    @app.route('/orm')
    def orm():
        insert_professors()
        update_professor() 
        delete_professor()

        # print the table to the console
        professors = get_all_professors()
        for professor in professors:
            print(professor)

        return "I managed the Professors table using the SQLAlchemy ORM!"

    return app

if __name__ == "__main__":
    app = create_app()
    # debug refreshes your application with your new changes every time you save
    app.run(debug=True)