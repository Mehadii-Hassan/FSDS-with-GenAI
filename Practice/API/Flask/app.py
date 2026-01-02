from flask import Flask

app = Flask(__name__) #flask server initialization

@app.route("/")
def home():
    return "Hello flask"

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000, debug = True)