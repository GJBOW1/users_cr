from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.models.users import Users


@app.route('/', methods=['GET', 'POST'])
def home():
    users = Users.get_users()
    return render_template('index.html', users = users)


@app.route('/add/user', methods=["GET", "POST"])
def adding_user():
    return render_template("add_user.html")

@app.route('/user/created', methods=["GET", "POST"])
def create_user():
    data = {
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "email":request.form["email"]
        }
    Users.save(data)
    return redirect('/user/display')

@app.route('/user/display', methods=["GET", "POST"])
def displaying():
    users = Users.get_users()
    return render_template('new_user.html', users = users)

@app.route('/display/<int:id>')
def show(id):
    data= {
        "id":id
    }
    user = Users.show_user(data)
    return render_template('display_user.html', user = user)

@app.route("/user/delete/<int:id>")
def delete(id):
    data= {
        "id":id
    }
    Users.delete_user(data)
    return redirect('/')

@app.route("/<int:id>")
def updating(id):
    data= {
        "id":id
    }
    user = Users.show_user(data)
    return render_template("update_user.html", user = user)

@app.route("/update/<int:id>", methods=["POST"])
def update(id):
    data = {
        "id": id,
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "email":request.form["email"]
    }
    Users.update_user(data)
    return redirect('/')