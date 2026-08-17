# 7. Explore the ‘Flask’ module and create a web server using Flask & Python.

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# app.run()     # This will also helps to run the server
#                        OR 
# flask --app <fileName without extension> run # This is the command to run the flask server  