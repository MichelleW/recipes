
from simplewall import app
from simplewall.config import routes

 









# now, we may invoke the query_db method
# select the table from the db 
# print("all the users", mysql.query_db("SELECT * FROM messages;"))

 
if __name__=="__main__":
    app.run(debug=True)
