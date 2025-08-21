import functools
import time
from datetime import datetime
import logging, os

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db #flaskr.db???

bp = Blueprint('auth', __name__, url_prefix='/auth')

#logger = logging.getLogger(__name__)
#logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

# Set your custom log directory and file name
log_dir = 'flask-tutorial/logs'
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, 'example.log')

# Remove existing handlers if any
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

# Set up logging to file and console
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s | %(levelname)s | %(message)s',
    datefmt='%Y.%m.%d %H:%M:%S',
    handlers=[
        logging.FileHandler(log_file, encoding='utf-8'),
        logging.StreamHandler()  # Console output
    ]
)

@bp.route('/register', methods=('GET', 'POST'))
def register():
    print("function register started at ", time.time())
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    logger("function login started")
    logging.info("CICA function login started")
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
            logger(f"error username \"{username}\" does not exist")
            logging.warning("CICA")
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'
            logger(f"error Incorrect password for user \"{username}\"")
            logging.warning("CICA")


        if error is None:
            session.clear()
            session['user_id'] = user['id']
            logger(f"succesful login \"{username}\"")
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view

def logger(log):
    print(datetime.now().strftime('%Y.%m.%d %H:%M:%S.%f')[:-3], log)