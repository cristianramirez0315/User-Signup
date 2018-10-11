from flask import Flask, request, render_template

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/", methods=['POST'])
def validate():
    usernameError = ''
    passwordError = ''
    verifyError = ''
    emailError = ''

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        verify = request.form['verify']
        email = request.form['email']

        # check if any required field is empty
        if not username:
            usernameError = 'Username cannot be empty.'
        if not password:
            passwordError = 'Password cannot be empty.'
        if not verify:
            verifyError = 'Verified password cannot be empty.'

        # check if password is the same as verified password
        if password != verify:
            verifyError = 'Verified password does not match password.'

        # check if any fields contain spaces
        if ' ' in username:
            usernameError = 'Username cannot contain any spaces.'
        if ' ' in password:
            passwordError = 'Password cannot contain any spaces.'
        if ' ' in verify:
            verifyError = 'Verified password cannot contain any spaces.'

        # check if the length of any field is less than 3 or greater than 20
        if len(username) > 20:
            usernameError = 'Username cannot be greater than 20 characters.'
        if len(username) < 3:
            usernameError = 'Username cannot be less than 3 characters.'
        if len(password) > 20:
            passwordError = 'Password cannot be greater than 20 characters.'
        if len(password) < 3:
            passwordError = 'Password cannot be less than 3 characters.'
        if len(verify) > 20:
            verifyError = 'Verified password cannot be greater than 20 characters.'
        if len(verify) < 3:
            verifyError = 'Verified password cannot be less than 3 characters.'

        # if an email is submitted, make sure it is a valid email
        if email:
            if '@' and '.' not in email or len(email) > 20 or len(email) < 3 or ' ' not in email:
                emailError = 'Email is not a valid email.'

    # if there are no errors then return the welcome page, otherwise, return the same form with the error messages
    if not usernameError and not passwordError and not verifyError and not emailError:
        return render_template('welcome.html', username=username)
    else:
        return render_template('index.html', usernameError=usernameError, passwordError=passwordError,
                               verifyError=verifyError, emailError=emailError, username=username, email=email)


app.run()
