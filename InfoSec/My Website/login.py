from flask import Flask, render_template_string, request, redirect, url_for, session, flash
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Removed the conflicting redirect route

# Dummy user database
users = {
    'admin': generate_password_hash('password123')
}

login_page = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Login Page</title>
    <link href="https://fonts.googleapis.com/css?family=Montserrat:400,700" rel="stylesheet">
    <style>
        body {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            font-family: 'Montserrat', sans-serif;
            height: 100vh;
            margin: 0;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .login-container {
            background: #fff;
            padding: 2.5rem 2rem;
            border-radius: 15px;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
            width: 350px;
        }
        .login-container h2 {
            text-align: center;
            margin-bottom: 1.5rem;
            color: #764ba2;
        }
        .login-container input[type="text"],
        .login-container input[type="password"] {
            width: 100%;
            padding: 0.75rem;
            margin: 0.5rem 0 1rem 0;
            border: none;
            border-radius: 8px;
            background: #f0f0f0;
            font-size: 1rem;
        }
        .login-container button {
            width: 100%;
            padding: 0.75rem;
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
            border: none;
            border-radius: 8px;
            color: #fff;
            font-size: 1.1rem;
            font-weight: bold;
            cursor: pointer;
            transition: background 0.3s;
        }
        .login-container button:hover {
            background: linear-gradient(90deg, #764ba2 0%, #667eea 100%);
        }
        .flash {
            color: #e74c3c;
            text-align: center;
            margin-bottom: 1rem;
        }
    </style>
</head>
<body>
    <form class="login-container" method="POST">
        <h2>Login</h2>
        {% with messages = get_flashed_messages() %}
          {% if messages %}
            <div class="flash">{{ messages[0] }}</div>
          {% endif %}
        {% endwith %}
        <input type="text" name="username" placeholder="Username" required autofocus>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit">Sign In</button>
    </form>
</body>
</html>
'''

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_hash = users.get(username)
        if user_hash and check_password_hash(user_hash, password):
            session['user'] = username
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password.')
    return render_template_string(login_page)

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    return f"<h1>Welcome, {session['user']}!</h1><a href='/logout'>Logout</a>"

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=False, port=5003)