# CONTROLLER FILE
from flask import render_template, request,redirect,session,flash
from recipes import app

# import from Friend class 
from recipes.models.recipe import Recipe

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app) 
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# instantiate
recipeData = Recipe()

class Recipes():
  def index(self):
    if 'userid' not in session:
      session['userid'] = 0
    return render_template("index.html")

  def logout(self):
    flash('you have been logged out')
    return redirect('/')

  def login(self,formdata):
    print('SESSION ID',session['userid'])
    print('HERE formdata in controller', formdata['login_email'])
    data = {"email":formdata['login_email']}
    result = recipeData.login(data)

    if result:
      print('RESULT INSIDE LOGIN: ',result)
      # if bcrypt.check_password_hash(result[0]['password'],formdata['login_password']):
      session['userid'] = result[0]['id']
      print("result[0]['id'] ", result[0]['id'])
      return redirect('/success')
    else:
      flash("can't log you in")
      print('on controllers page: didnt get anthing')
    return redirect('/')

  def success(self):
    if session['userid']:
      print('logged in success route for userid: ',session['userid'])
      data = {'sessionid':session['userid']}
      storeResults = {
        'userInfoResults':recipeData.queryUser(data),
        'tripPlanResults':recipeData.queryTripPlan(data),
        'tripsIJoinedResults':recipeData.tripsIJoined(data),
        'otherUsersInfoResults':recipeData.otherUsersInfo(data),
      }

      return render_template("welcome.html",storeResults=storeResults)
    else:
      print('please login')
    return redirect('/')

  def registration(self,formdata):
    print('registration formdata', formdata)
    # check blank fields
    if len(formdata['fname']) < 2:
      flash("First name should have at least 2 characters")
    elif len(formdata['email']) < 1:
        flash("Email cannot be blank!")
    else:
      # create password hash
      # pw_hash = bcrypt.generate_password_hash(formdata['password'])
      # look for email in db
      result = recipeData.login(formdata)
      data = {
          "email":formdata['email'],
          "fname":formdata['fname'],
          "lname": formdata['lname'],
          "password": formdata['password'],
          }
        # store the result (an array) from talking to the database in the variable 
      emailQuery = recipeData.checkExistUsers(data)
      print('sent data',emailQuery)
      # store the result (an array) from talking to the database in the variable 
      
      # if there's a match in db, user already exist
      if len(emailQuery) > 0:
        flash("user email already exit")
      # if user/email doesn't exist in db, insert it into the db
      else:
        insertResult = recipeData.registerUser(formdata)
        # get the new user id and place it in session
        print("what is the query result after insert?",insertResult)
        session['userid'] = insertResult
        flash("You have been successfully registered!")
      return redirect('/success')
    
  
 