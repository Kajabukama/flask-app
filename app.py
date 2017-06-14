from flask import Flask, render_template, request, flash, url_for, session, redirect, logging
from wtforms import Form, TextAreaField, PasswordField, StringField, validators
from passlib.hash import sha256_crypt
from flask_mysqldb import MySQL

# custom classes
from data import *

class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=4, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=16)])
    email = StringField('Email', [validators.Length(min=10, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message = 'Password do not match')
    ])
    confirm = PasswordField('confirm password')


app = Flask('__name__')

Articles = Articles()

@app.route('/')
def index():
   return render_template('home.html')

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/articles')
def articles():
   return render_template('articles.html', articles = Articles)

@app.route('/article/<string:id>')
def article(id):
    return render_template('article.html', article = findArticle(id))

@app.route('/register', methods = ['GET','POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        pass
    return render_template('register.html', form = form)
    

if __name__ == '__main__':
    app.run(debug = True)