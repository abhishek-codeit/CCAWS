# write a flask app that can run a html file
# and can also run a python file

from flask import Flask, render_template, request
from app import *
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    # how to run a function from algorithm.py
    # and pass the query to it
    # and return the result
    # and display it in the html file

    answer = summarization(query)

    print(answer)
    # write a code to send the string result to html file and also write how to display it in html file 
    # output is a string not tables

    return render_template('output.html', string_value=answer)

    
    
    
    # return 'Code executed'
    
if __name__ == '__main__':
    app.run(host = '0.0.0.0')



# Run the app.py file

