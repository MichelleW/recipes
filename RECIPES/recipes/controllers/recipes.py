# CONTROLLER FILE


from flask import render_template, request,redirect,session,flash
from recipes import app

# import from Friend class 
from recipes.models.recipe import Recipe

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app) 


# instantiate
recipeData = Recipe()

class Recipes():
  def index(self):
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
      if bcrypt.check_password_hash(result[0]['password'],formdata['login_password']):
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
    
  
 