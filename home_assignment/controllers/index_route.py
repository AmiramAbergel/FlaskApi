from flask import render_template, flash, redirect, url_for
from forms import RegistrationForm, LoginForm


def index_route(app):
    @app.route('/')
    @app.route('/home')
    def home():
        return render_template('home.html')

    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/registration', methods=['GET', 'POST'])
    def registration():
        form = RegistrationForm()
        if form.validate_on_submit():
            flash(f'Account created for {form.username.data}!', 'success')
            return redirect(url_for('home'))
        return render_template('registration.html', title='Register', form=form)

    @app.route('/login')
    def login():
        form = LoginForm()
        flash('Login Unsuccessful. Please check email and password', 'danger')
        return render_template('login.html', title='Login', form=form)


