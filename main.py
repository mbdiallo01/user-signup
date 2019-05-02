from flask import Flask, request, render_template, url_for, redirect
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True


header = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            .error {
                color: red;
            }
        </style>
    </head>
    <body>
    <h1>Signup</h1>
"""
form= """
        <form action="/signup" id="form" method="post">
            <table>
                <tr>
                    <td><label for="username">Username</label></td>
                    <td>
                        <input name="username" type="text" value="">
                        <span class="error" name="usernameError">{0}</span>
                    </td>
                </tr>
                <tr>
                    <td><label for="password">Password</label></td>
                    <td>
                        <input name="password" type="password">
                        <span class="error" name="passwordError">{1}</span>
                    </td>
                </tr>
                <tr>
                    <td><label for="verify">Verify Password</label></td>
                    <td>
                        <input name="verify" type="password">
                        <span class="error">{2}</span>
                    </td>
                </tr>
                <tr>
                    <td><label for="email">Email (optional)</label></td>
                    <td>
                        <input name="email" value="">
                        <span class="error"name="emailError">{3}</span>
                    </td>
                </tr>
            </table>
            <input type="submit">
        </form>
    </body>
</html>
"""

@app.route("/welcome")
def welcome():
    test = request.args.get("user")
    return render_template("/welcome.html", username=test)

@app.route("/signup", methods= ['POST', 'GET'])
def add_user():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify'] 
    email = request.form['email']

    usernameError = ""
    passwordError = ""
    verifyError = ""
    emailError = ""

    if not username:
        usernameError = "username not valid"
        
        #return header + form.format(usernameError, "")
    
    if len(password) < 3:
        
        passwordError = "Password must be more than 3 character."

    elif len(password) > 20:
        
        passwordError = "Password must be less than 20 character."
    
    elif " " in password:
        passwordError = "Password must not contain any space"

    if verify != password:

        verifyError = "Passwords must match"
    
    if len(email) > 0:
        if "@" not in email or "." not in email:
            emailError = "This is not a valid email address"
    
    if len(usernameError) > 0 or len(passwordError) > 0 or len(verifyError) > 0  or len(emailError) > 0:
        content = header + form.format(usernameError, passwordError, verifyError, emailError)
        return content

    return redirect("/welcome?user={0}".format(username))

@app.route("/")
def index():
    return header + form.format("", "", "", "", "")

app.run()