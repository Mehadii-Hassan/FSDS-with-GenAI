from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__) 

# @app.route("/")
# def home():
#     return "Hello, Flask!"


@app.route("/welcome")
def welcome():
    return "Welcome to the Flask Application!"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/success/<int:score>")
def success(score):
    return f"The person is passed and the score is {score}"


@app.route("/fail/<int:score>")
def fail(score):
    return f"The person is failed and the score is {score}"


@app.route("/calculate", methods=["POST", "GET"])
def calculate():
    if request.method == "GET":
        return render_template("form.html")
    
    else:
        maths = float(request.form["maths"])
        science = float(request.form["science"])
        history = float(request.form["history"])

        average_score = (maths + science + history) / 3 
        
        # result = ""
        # if average_score >= 50:
        #     result = "success"
        # else:
        #     result = "fail"

        # return redirect(url_for(result, score=average_score))

        return render_template("result.html", results=average_score)



@app.route('/api/calculate', methods=['POST'])
def api_calculate():
    data = request.get_json()
    
    maths = float(data['maths'])
    science = float(data['science'])
    history = float(data['history'])
    
    average_marks = (maths + science + history) / 3
    result = "pass" if average_marks >= 50 else "fail"
    
    return jsonify({
        'result': result,
        'average_marks': round(average_marks, 2)
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)




