"""app.py: render and route to webpages with defensive programming"""

import os
import logging
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for
from db.query import get_all, get_one, insert
from db.server import init_database
from db.schema import Users
import bcrypt

# load environment variables from .env
load_dotenv()
# current working directory
CWD = os.getcwd()

# create logs directory if it doesn't exist
# must be done before logger is configured
if not os.path.exists(f"{CWD}/logs"):
    os.makedirs(f"{CWD}/logs")

# configure logging
logging.basicConfig(
    filename="logs/log.txt", 
    level=logging.INFO, 
    filemode="a", 
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

# database connection - values set in .env
db_name = os.getenv('db_name')
db_owner = os.getenv('db_owner')
db_pass = os.getenv('db_pass')
db_url = f"postgresql://{db_owner}:{db_pass}@localhost/{db_name}"

def create_app():
    """Create Flask application and connect to your DB"""
    # create flask app
    app = Flask(__name__, 
                template_folder=os.path.join(CWD, 'templates'), 
                static_folder=os.path.join(CWD, 'static'))
    
    # connect to db
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url
    
    # initialize database
    with app.app_context():
        if not init_database():
            logger.critical("Failed to initialize database")
            print("Failed to initialize database. Exiting.")
            exit(1)
        logger.info("Database initialized successfully")

    # ===============================================================
    # routes
    # ===============================================================

    # create a webpage based off of the html in templates/index.html
    @app.route('/')
    def index():
        """Home page"""
        logger.info("User accessed home page")
        return render_template('index.html')
    
    @app.route('/signup', methods=['GET', 'POST'])
    def signup():
        """Sign up page: enables users to sign up"""
        if request.method == 'POST':
            try:
                # get form data and sanitize (strip whitespace)
                first_name = request.form["FirstName"].strip()
                last_name = request.form["LastName"].strip()
                email = request.form["Email"].strip()
                phone_number = request.form["PhoneNumber"].strip()
                password = request.form["Password"].strip()
                
                # validate first name
                if not first_name.isalpha():
                    error = "First name can only contain letters."
                    logger.warning(f"Invalid first name attempt: {first_name}")
                    return render_template('signup.html', error=error)
                
                # validate last name
                if not last_name.isalpha():
                    error = "Last name can only contain letters."
                    logger.warning(f"Invalid last name attempt: {last_name}")
                    return render_template('signup.html', error=error)
                
                # validate phone number
                if not (phone_number.isnumeric() and len(phone_number) == 10):
                    error = "Phone number must be exactly 10 digits."
                    logger.warning(f"Invalid phone number attempt: {phone_number}")
                    return render_template('signup.html', error=error)
                
                # all validation passed - proceed with signup
                # hash and salt the password using bcrypt
                salt = bcrypt.gensalt()
                hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
                
                # create user object with sanitized data
                user = Users(
                    FirstName=first_name, 
                    LastName=last_name, 
                    Email=email,
                    PhoneNumber=phone_number,
                    Password=hashed_password.decode('utf-8')
                )

                # insert into database
                insert(user)
                logger.info(f"New user registered: {email}")
                
                # return to home page
                return redirect(url_for('index'))
            
            except Exception as e:
                # log the error
                logger.error(f"An error occurred during signup: {e}")
                
                # route user to error page
                user_error_msg = "Something went wrong on our end. Rest assured we are working to solve this problem. Please try again later."
                return render_template('error.html', error=user_error_msg)

        return render_template('signup.html')
    
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        """Log in page: enables users to log in"""
        if request.method == 'POST':
            try:
                # get email & password from form
                submitted_password = request.form["Password"]
                submitted_email = request.form["Email"]

                # get the user with the submitted email from the db 
                user = get_one(Users, Email=submitted_email)

                # generic login failure msg so we don't expose details
                # note: will use more specific msg for logging - helps w/ debugging
                error = f"Failed login attempt for: {submitted_email}"

                if user is None:
                    logger.warning(f"Login attempted with non-existent email: {submitted_email}")
                    return render_template('login.html', error=error)

                # compare the submitted password with the hashed password
                if bcrypt.checkpw(submitted_password.encode('utf-8'), user.Password.encode('utf-8')):
                    # if it's a match, send the user to the success page
                    logger.info(f"Successful login: {submitted_email}")
                    return redirect(url_for('success'))
                else:
                    # if they don't match, stay on the same page
                    logger.warning(f"Login attempted with incorrect password")
                    return render_template('login.html', error=error)
                    
            except Exception as e:
                # log the error
                logger.error(f"An error occurred during login: {e}")
                
                # route user to error page
                user_error_msg = "Something went wrong on our end. Rest assured we are working to solve this problem. Please try again later."
                return render_template('error.html', error=user_error_msg)

        return render_template('login.html')

    @app.route('/users')
    def users():
        """Users page: displays all users in the Users table"""
        try:
            all_users = get_all(Users)
            logger.info("Users page accessed")
            return render_template('users.html', users=all_users)
        except Exception as e:
            logger.error(f"Error accessing users page: {e}")
            user_error_msg = "Unable to load users at this time."
            return render_template('error.html', error=user_error_msg)

    @app.route('/success')
    def success():
        """Success page: displayed upon successful login"""
        logger.info("Success page accessed")
        return render_template('success.html')
    
    @app.route('/error')
    def error():
        """Error page: displayed when something goes wrong"""
        return render_template('error.html')

    return app

if __name__ == "__main__":
    app = create_app()
    # debug refreshes your application with your new changes every time you save
    app.run(debug=True)