from flask import Flask
a=Flask(__name__)
@a.route("/")
def greeting():
    return "Hello My name is Phyo Ei!"
@a.route("/tiide")
def tiide():
    return "Welcome from my first Heroku Page"
if __name__ == "__main__":
    a.run(debug=True)

