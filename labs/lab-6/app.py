"""app.py: render and route to webpages"""

import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, session, flash
from db.query import get_all, insert
from db.server import init_database, get_session
from db.schema import Users
from sqlalchemy import func
import logging
import bcrypt


# load environment variables from .env
load_dotenv()
os.makedirs("logs",exist_ok=True)
logging.basicConfig(
    filename="logs/log.txt",
    level=logging.INFO,
    filemode="a",
    format="%(asctime)s | %(levelname)s | %(message)s"
)

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
    app.config["SECRET_KEY"] = "something-random-and-secure"
    
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
    
    @app.route('/signup', methods=['GET', 'POST'])
    def signup():
        """Sign up page: enables users to sign up"""
        if request.method == 'POST':

            firstName = (request.form.get("FirstName") or "" ).strip()
            lastName = (request.form.get("LastName") or "" ).strip()
            email = (request.form.get("Email") or "" ).strip().lower()
            phonenum = (request.form.get("PhoneNumber") or "" ).strip()
            password = (request.form.get("Password") or "" ).strip()

            is_valid = True
            error_msg = None

            if not firstName or not firstName.isalpha():
                is_valid = False
                error_msg = "First Name must contain only letters."
            elif not lastName or not lastName.isalpha():
                is_valid =False
                error_msg = "Last name must only contain letters."
            elif not phonenum.isnumeric() or len(phonenum) != 10:
                is_valid = False
                error_msg = "Phone number must be 10 digits"
            elif not password:
                is_valid = False
                error_msg = "Password is required to have"
            elif ("@" not in email) or ("." not in email.split("@")[-1]):
                is_valid = False
                error_msg = "Please enter a valid email"
            
            if not is_valid:
                logging.warning(f"Signup failed")

            try:
                hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
            except Exception:
                logging.error(f"Password hashing failed ")

            try:
                user = Users(
                    FirstName=firstName,
                    LastName=lastName,
                    Email=email,
                    PhoneNumber=phonenum,
                    Password=hashed_password)

                insert(user)
                return redirect(url_for('index'))
            except Exception as e:
                print("Error adding user", e)
                return redirect(url_for('signup'))
                
            #TODO: implement sign up logic here

        return render_template('signup.html')
    
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        """Log in page: enables users to log in"""
        # TODO: implement login logic here
        if request.method == 'POST':
            email = (request.form.get('Email') or "").strip().lower()
            password = (request.form.get('Password') or "").strip()
                
            if not email or not password:
                logging.warning(f"Loging failed.")
                return render_template('login.html', error = "Please enter both email and password")

            try:
                with get_session() as s:
                    user = s.query(Users).filter(func.lower(Users.Email) == email).first()
                    if user:
                        stored_hash = (user.Password or "").encode("utf-8")
                        if stored_hash and bcrypt.checkpw(password.encode("utf-8"), stored_hash):
                            logging.info(f"Logged In.")
                            return redirect(url_for('index'))
            except Exception:
                logging.error(f"Could not login.")
                return render_template('error.html')
                
        return render_template('login.html')

    @app.route('/users')
    def users():
        """Users page: displays all users in the Users table"""
        all_users = get_all(Users)
        
        return render_template('users.html', users=all_users)

    @app.route('/success')
    def success():
        """Success page: displayed upon successful login"""

        return render_template('success.html')

    return app

if __name__ == "__main__":
    app = create_app()
    # debug refreshes your application with your new changes every time you save
    app.run(debug=True)