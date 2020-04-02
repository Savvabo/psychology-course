from flask import Flask, render_template, request
from email.mime.text import MIMEText
import smtplib
from email_test import format_message

app = Flask(__name__)


@app.route('/')
def webprint():
    return render_template('html/index.html')


@app.route('/feedback')
def about():
    return render_template('html/feedback.html')


@app.route('/submit_form', methods=['POST'])
def submit_form():
    email_from = 'savvabogun@gmail.com'
    email = 'martindevil666666@gmail.com'
    # email = 'reshetnikov.kirill.s@gmail.com '
    # email = 'kiril_1999@ukr.net'
    body = request.get_json()
    body = format_message(body)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_from, 'k.,k.Rbh.ie')
    message = MIMEText(body, 'plain', 'utf-8')
    server.sendmail(email_from, email, message.as_string())
    server.close()
    return '', 200
    # return jsonify_no_content()
    # return '', http.HTTPStatus.NO_CONTENT


if __name__ == '__main__':
    app.run(host='0.0.0.0')
