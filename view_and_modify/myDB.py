import mysql.connector
from mysql.connector import connect

# Connect to database in sigma server.
# Double underscore declare private variables, meaning it can't be imported in other scripts.
__db = connect(
  host = "sigma.jasoncoding.com",
  user = "alpha",
  password = "bestdatabase",
  database = "CourseDB",       
  port = 5555
)

# Function to reconnect to the database if the previous connection were to be severed.
def getDb():
    if not __db.is_connected():
        __db.reconnect()
    return __db

# Returns the mysql error object to be used in exception handlings.
def getDbError():
    return mysql.connector.Error