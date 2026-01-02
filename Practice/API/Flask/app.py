from flask import Flask

app = Flask(__name__) #flask server initialization

@app.route("/")
def home():
    return "Hello flask"

@app.route("/welcome")
def welcome():
    return "welcome to the Flask Application"

@app.route("/success/<int:score>")
def success(score):
    return f"The person is passed and the score is {score}"

@app.route("/fail/<int:score>")
def fail(score):
    return f"The person is failed and the score is {score}"

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000, debug = True)