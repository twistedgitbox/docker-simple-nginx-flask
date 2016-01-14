from datetime import datetime as dt

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def landing_page():
    time_string = str( dt.now() ) 
    return render_template('hello_world.html', time_string = time_string)

if __name__ == "__main__":
    app.run()
