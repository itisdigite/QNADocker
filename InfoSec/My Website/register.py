from flask import Flask, render_template_string, request
import os
import json
from werkzeug.security import generate_password_hash

app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
def register():
    users_file = 'users.json'
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # Load existing users
        users = {}
        if os.path.exists(users_file):
            with open(users_file, 'r') as f:
                try:
                    users = json.load(f)
                except Exception:
                    users = {}
        # Check if username exists
        if username in users:
            return render_template_string('''
                <html><head><title>Registration Failed</title>
                <style>body {background: linear-gradient(135deg, #2c5364, #203a43, #0f2027); color: #fff; font-family: 'Roboto', Arial, sans-serif; min-height: 100vh; margin:0;} .container {max-width: 400px; margin: 80px auto; background: rgba(44,83,100,0.92); border-radius: 18px; box-shadow: 0 8px 32px rgba(0,0,0,0.25); padding: 32px; text-align: center;} h2 {color: #ff4b2b;} a {color: #00c3ff; text-decoration: none;}</style></head><body><div class="container"><h2>Username already exists!</h2><a href="/register">Back to Register</a></div></body></html>
            ''')
        # Hash password and save
        hashed_pw = generate_password_hash(password)
        users[username] = hashed_pw
        with open(users_file, 'w') as f:
            json.dump(users, f)
        return render_template_string('''
            <html><head><title>Registration Success</title>
            <style>
                body {background: linear-gradient(135deg, #2c5364, #203a43, #0f2027); color: #fff; font-family: 'Roboto', Arial, sans-serif; min-height: 100vh; margin:0;}
                .container {max-width: 400px; margin: 80px auto; background: rgba(44,83,100,0.92); border-radius: 18px; box-shadow: 0 8px 32px rgba(0,0,0,0.25); padding: 32px; text-align: center;}
                h2 {color: #00c3ff;}
                a {color: #00c3ff; text-decoration: none;}
            </style></head><body>
            <div class="container">
                <h2>Registration successful for {{username}}</h2>
                <a href="/register">Back to Register</a>
            </div></body></html>
        ''', username=username)
    return render_template_string('''
        <html><head><title>Register</title>
        <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
        <style>
            body {background: linear-gradient(135deg, #2c5364, #203a43, #0f2027); color: #fff; font-family: 'Roboto', Arial, sans-serif; min-height: 100vh; margin:0;}
            .container {max-width: 400px; margin: 80px auto; background: rgba(44,83,100,0.92); border-radius: 18px; box-shadow: 0 8px 32px rgba(0,0,0,0.25); padding: 32px;}
            h2 {text-align:center; color: #00c3ff;}
            form {display:flex; flex-direction:column; gap:18px;}
            input[type=text], input[type=password] {padding:12px; border-radius:8px; border:none; font-size:1rem;}
            input[type=submit] {background: linear-gradient(90deg, #00c3ff 0%, #3a7bd5 100%); color:#fff; border:none; border-radius:8px; padding:12px; font-size:1.1rem; font-weight:700; cursor:pointer; transition: background 0.3s;}
            input[type=submit]:hover {background: linear-gradient(90deg, #3a7bd5 0%, #00c3ff 100%);}
        </style></head><body>
        <div class="container">
            <h2>Register</h2>
            <form method="post">
                <input type="text" name="username" placeholder="Username" required>
                <input type="password" name="password" placeholder="Password" required>
                <input type="submit" value="Register">
            </form>
        </div></body></html>
    ''')

if __name__ == '__main__':
    app.run(debug=False, port=5001)
