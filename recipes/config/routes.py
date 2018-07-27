from flask import session, request

from recipes import app

app.secret_key = "bigIsSecret!"

from recipes.config.mysqlconnection import connectToMySQL
mysql = connectToMySQL('tripplanner')

from recipes.controllers.recipes import Recipes
recipes = Recipes()

@app.route('/')
def index():
    return recipes.index()

@app.route('/logout')
def logout():
    return recipes.logout()

@app.route('/login', methods=['POST'])
def login():
  formdata = request.form
  print('msg from routes.py. login page loaded. ',
  formdata)
  return recipes.login(formdata)

@app.route('/success')
def success():
  print('msg from success route')
  return recipes.success()


@app.route('/register', methods=['POST'])
def register():
   formData = request.form
   return recipes.registration(formData)
