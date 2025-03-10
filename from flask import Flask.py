from flask import Flask,g,render_template
import sqlite3 

app = Flask(__name__)

DATABASE = 'southeys_autoworld_database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/contents")
def index():
    cursor = get_db().cursor()
    sql = "SELECT * FROM car_stock"
    cursor.execute(sql)
    results = cursor.fetchall() 
    return str(results)                                                                           

if __name__ == "__main__":
    app.run(debug=True)

