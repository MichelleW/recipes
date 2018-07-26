# MODELS
# import mysql

from recipes.config.routes import mysql

class Recipe():
  def login(self,data):
    # print('logged and query result: ',result)
    query = "SELECT * FROM users WHERE email = %(email)s;"
    result = mysql.query_db(query,data)
    return result

  def logout(self):
    print('session["userid"]')
    return session.clear()

  def queryUser(self, data):
    print('is this session id? ', data)
    query = "select * from tripplanner.users WHERE users.id = %(sessionid)s;"
    result = mysql.query_db(query,data)
    return result
  
  def queryTripPlan(self,data):
    query = "select * from travelplans where user_id= %(sessionid)s;"
    result = mysql.query_db(query,data)
    return result
  
  def tripsIJoined(self,data):
    query = "select * from travelplans join joinTrip on travelPlans.id = joinTrip.travelPlan_id WHERE joinTrip.joiner_id = %(sessionid)s;"
    return mysql.query_db(query,data)

  def otherUsersInfo(self,data):
    query = "select * from travelPlans join joinTrip on travelPlans.id = joinTrip.travelPlan_id WHERE joiner_id not in (%(sessionid)s);"
    return mysql.query_db(query,data)









  