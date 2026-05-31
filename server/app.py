import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='../resources')    # need to tell Flask where the resources directory is

@app.route('/')
def main():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)