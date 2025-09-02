from flask import Flask, render_template_string, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash
import re

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this in production!

# In-memory user store (replace with a database in production)
users = {}

# Fancy registration page template
registration_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Registration</title>
    <link href="https://fonts.googleapis.com/css?family=Roboto:400,700&display=swap" rel="stylesheet">
    <style>
        body { background: #f0f4f8; font-family: 'Roboto', sans-serif; }
        .container { max-width: 400px; margin: 60px auto; background: #fff; border-radius: 12px; box-shadow: 0 4px 24px rgba(0,0,0,0.1); padding: 32px; }
        h2 { text-align: center; color: #333; }
        .form-group { margin-bottom: 18px; }
        label { display: block; margin-bottom: 6px; color: #555; }
        input[type="text"], input[type="password"], input[type="email"] {
            width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 6px; font-size: 16px;
        }
        button {
            width: 100%; padding: 12px; background: #007bff; color: #fff; border: none;
            border-radius: 6px; font-size: 18px; font-weight: bold; cursor: pointer; transition: background 0.2s;
        }
        button:hover { background: #0056b3; }
        .flash { color: #d8000c; background: #ffd2d2; padding: 10px; border-radius: 6px; margin-bottom: 12px; }
    </style>
</head>
<body>
    <div class="container">
        <h2>Register</h2>
        {% with messages = get_flashed_messages() %}
          {% if messages %}
            <div class="flash">{{ messages[0] }}</div>
          {% endif %}
        {% endwith %}
        <form method="POST">
            <div class="form-group">
                <label for="username">Username</label>
                <input required type="text" id="username" name="username" minlength="3" maxlength="30" pattern="^[a-zA-Z0-9_]+$" title="Username must be alphanumeric and can include underscores.">
            </div>
            <div class="form-group">
                <label for="email">Email</label>
                <input required type="email" id="email" name="email" maxlength="64">
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input required type="password" id="password" name="password" minlength="8" maxlength="20" pattern="^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,64}$" title="Password must be at least 8 characters long and contain both letters and numbers.">
            </div>
            <button type="submit">Register</button>
        </form>
    </div>
</body>
</html>
"""

def is_valid_email(email):
    # Simple regex for email validation
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username'].strip()
        email = request.form['email'].strip().lower()
        password = request.form['password']

        # Input validation
        if not (3 <= len(username) <= 32):
            flash('Username must be between 3 and 32 characters.')
        elif not is_valid_email(email):
            flash('Invalid email address.')
        elif not (8 <= len(password) <= 64):
            flash('Password must be between 8 and 64 characters.')
        elif username in users:
            flash('Username already exists.')
        elif any(u['email'] == email for u in users.values()):
            flash('Email already registered.')
        else:
            # Securely hash the password
            password_hash = generate_password_hash(password)
            users[username] = {'email': email, 'password_hash': password_hash}
            flash('Registration successful! You can now log in.')
            return redirect(url_for('register'))

    return render_template_string(registration_template)

if __name__ == '__main__':
    app.run(debug=False, port=5004)