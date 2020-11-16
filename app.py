from flask import Flask,redirect, url_for,render_template,request
import os


secret_key = str(os.urandom(24))

app = Flask(__name__)
app.config['TESTING'] = True
app.config['DEBUG'] = True
app.config['FLASK_ENV'] = 'development'
app.config['SECRET_KEY'] = secret_key
app.config['DEBUG'] = True

# Defining the home page of our site
@app.route("/",methods=['GET', 'POST'])
def home():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('Continue') == 'Continue':
           return render_template("test1.html")
    else:
        # pass # unknown
        return render_template("home.html")

@app.route("/social-distance", methods=['GET', 'POST'])
def index1():
    print(request.method)
    if request.method == 'POST':
            # pass
            return render_template('home.html')
    else:
        # pass # unknown
        os.chdir("distance")
        print(os.getcwd())
        # os.system("python SocialDistancingDetector.py")
        os.chdir("../")
        return render_template('home.html')

@app.route("/mask", methods=['GET', 'POST'])
def index2():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('Start') == 'Start':
            # pass
            return render_template('home.html')
    else:
        # pass # unknown
        os.system("python code_mask.py")
        os.chdir("../")
        return render_template('home.html')

@app.route("/counter", methods=['GET', 'POST'])
def index3():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('Start') == 'Start':
            # pass
            return render_template('home.html')
    else:
        # pass # unknown
        os.chdir("ENTRY_EXIT_COUNT")
        print(os.getcwd())
        os.system("python counter.py")
        os.chdir("../")
        return render_template('home.HTML')



if __name__ == "_main_":
    app.run()
