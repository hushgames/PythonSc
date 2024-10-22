from flask import Flask
from dbhelper import *

app = Flask(__name__)

@app.route("/")
def index()->None:
    users:list = getall_record('users')
    return users
    
if __name__ == "__main__":
    app.run(debug=True,host ="0.0.0.0")