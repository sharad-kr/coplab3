from flask import Flask, render_template,request

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def hello_world():
    return render_template('home-page.html')


@app.route("/about")
def about():
    return render_template("about-us.html")


@app.route("/contact")
def contact():
    return render_template("contact-us.html")


@app.route("/appointment")
def book():
    return render_template("book-an-appointment.html")


@app.route("/medicine")
def med():
    return render_template("med-shop.html")


@app.route("/profile")
@app.route("/profile/<name>")
def profile(name=None):
    return render_template("profile-page.html", name=name)



@app.route("/login", methods=['GET', 'POST'])
# @app.route("/signup")
# def login():
#     if(request.method=='POST'):
#         """Add entry to the database"""
#         name = request.form.get('Username')
#         password= request.form.get('Pasw')

#     else:
#         return render_template('index.html')
def login():
    if (request.method=='POST'):
        """Add entry to the database"""
        name = request.form.get('Username')
        password = request.form.get('Password')
    return render_template('index.html',Username=name,Password=password)

@app.route("/signup", methods=['POST'])
def signup():
    if (request.method=='POST'):
        name=request.form.get('Name')
        contact=request.form.get('Contact_No')
        email=request.form.get('Email_Id')
        username=request.form.get('Username')
        password=request.form.get('Password')
        verify_password=request.form.get('Verify_Password')
    return render_template('index.html',Name=name,Contact_No=contact,Email_Id=email,Username=username,Password=password,Verify_Password=verify_password)


app.run(debug=True)


