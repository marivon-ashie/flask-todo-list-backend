from flask import Flask,  request, jsonify,Blueprint,redirect,url_for
from app import db
from datetime import timedelta
from werkzeug.security import generate_password_hash,check_password_hash
from app.models import User
from flask_login import login_user, logout_user,login_required,current_user

    


auth=Blueprint('auth',__name__)

@auth.route('/signup', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return jsonify({'message': 'User already exists. Please login.'}), 400

        hashed_password = generate_password_hash(password)
        new_user = User( name=name, email=email, password=hashed_password)

        db.session.add(new_user)
        db.session.commit()

        return "registration success"

    return "Register"



@auth.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()

        if not user or not check_password_hash(user.password, password):
            return jsonify({'message': 'Invalid email or password'}), 401
        login_user(user)

        return 'login successful'
    return 'login failed'   
        # token = jwt.encode({'public_id': user.public_id, 'exp': datetime.now(timezone.now) + timedelta(hours=1)},
        #                    auth.config['SECRET_KEY'], algorithm="HS256")

        # response = make_response(redirect(url_for('dashboard')))
        # response.set_cookie('jwt_token', token)
@auth.route("/logout")
@login_required
def logout():
    logout_user
    return "logout successful"