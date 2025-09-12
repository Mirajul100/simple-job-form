from flask import Flask , render_template , request

app = Flask(__name__)

@app.route("/" , methods=["GET" , "POST"])
def index():
    
    if request.method == "POST":
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        email = request.form['email']
        phone = request.form['phone']
        position = request.form['position']
        experience = request.form['experience']
        availability = request.form['availability']
        terms = request.form["terms"]
        newsletter = request.form["newsletter"]

    return render_template("index.html")

app.run(debug=(True) , port=5001)