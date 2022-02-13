from flask import Flask, render_template
from mysql.connector import errorcode

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

dbname = "mpsscqueueflexdb"
username = "flexdbadmin"
password = "DBAdmin!@#"
#Build the connection string
config = {
  'host':f'{dbname}.mysql.database.azure.com',
  'user': username,
  'password': password,
  'database': dbname
}

#Error handling for the MySQL DB connection
try:
   conn = mysql.connector.connect(**config)
   print(f"\nConnection established to the {dbname} database.")
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("\nError! Something is wrong with the user name or password.")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("\nError! Database does not exist.")
  else:
    print(err)
else:
  cursor = conn.cursor()
