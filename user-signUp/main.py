from flask import Flask, request, redirect, render_template
import cgi
#  cgi is a module than you can use cgi.escape convert raw string data into html enconded data

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/validate', methods=['POST'])
def validate():
# how you get the info from the form the variables come to str 
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    print(email)
    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

    if len(username) < 3 or len(username) > 20 or " " in username:
        username_error = 'Not a valid username'

    if len(password) < 3 or len(password) > 20 or " " in password:
        password_error = 'Not a valid password'
        password = ''
        # password="" deleted the worng info 

    if verify == "":
        verify_error = 'Not a valid password'

    elif password != verify:
        verify_error = 'Does not match password above'
        verify = ''

    if email != "" and len(email) < 3 or len(email) > 20:
        email_error = 'Not a valid email'
    elif email != "" and ("." not in email or "@" not in email):
        email_error = 'Not a valid email'

    if not username_error and not password_error and not verify_error and not email_error:
        return render_template('welcome.html', username=username)
    else:
        return render_template('index.html', username_error=username_error, password_error=password_error,
            verify_error=verify_error, email_error=email_error, username=username, email=email)

app.run()
