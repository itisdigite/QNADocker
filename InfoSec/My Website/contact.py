from flask import Flask, request, render_template
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Email configuration
        sender = 'your_email@gmail.com'
        receiver = 'xxxx@xxxx.com'
        password = 'your_gmail_app_password'  # Use an app password for Gmail

        subject = f"New Contact Form Submission from {name}"
        body = f"Name: {name}\nEmail: {email}\nMessage:\n{message}"

        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = receiver

        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                server.login(sender, password)
                server.sendmail(sender, receiver, msg.as_string())
            return "<h2>Thank you for contacting us!</h2>"
        except Exception as e:
            return f"<h2>Failed to send message. Error: {e}</h2>"

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=False, port=5005)