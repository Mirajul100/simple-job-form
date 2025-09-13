from flask import Flask , render_template , request , flash , redirect , url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)


app.config["SECRET_KEY"] = "mynameisanik123"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db = SQLAlchemy(app)

class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80)  , nullable=False)
    phone = db.Column(db.String(80))
    position = db.Column(db.String(80))
    experience = db.Column(db.String(50))
    availability = db.Column(db.String(50))
    terms = db.Column(db.Boolean , default=False)
    newsletter = db.Column(db.Boolean , default=False)


@app.route("/" , methods=["GET" , "POST"])
def index():
    try :

        if request.method == "POST":
            first_name=request.form.get("firstName").title()
            last_name=request.form.get("lastName").title()
            email=request.form.get("email")
            phone=request.form.get("phone")
            position=request.form.get("position")
            experience=request.form.get("experience")
            availability=request.form.get("availability")
            terms=True if request.form.get("terms") else False
            newsletter=True if request.form.get("newsletter") else False

            form = Form(first_name = first_name ,
                        last_name = last_name , 
                        email = email , 
                        phone = phone , 
                        position = position ,
                        experience = experience , 
                        availability = availability , 
                        terms = terms , 
                        newsletter = newsletter)
            db.session.add(form)
            db.session.commit()
            flash (f"{first_name} , Your form was submitted successfully" , "success")
            return redirect(url_for("index"))

    except IntegrityError:
        db.session.rollback()
        flash("Email address already exists." , "error")
        return redirect(url_for("index"))

    return render_template("index.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=(True) , port=5001)
