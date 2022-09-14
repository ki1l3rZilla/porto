# To run site need to run in therse 2 commands in terminal:
# export FLASK_APP=server.py
# python -m flask --debug run


from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('./index.html')


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


def write_to_csv(data):
    with open("database.csv", mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csc_writer = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csc_writer.writerow([email, subject, message])


def write_to_file(data):
    with open("database.txt", mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email}, {subject}, {message}')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    # error = None
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_file(data)
            write_to_csv(data)
            return redirect("/thank_you.html")
        except:
            return 'Unable t save to database'
    else:
        return "Something went wrong. Try again!"

# @app.route("/index.html")
# def my_home():
#     return render_template('./index.html')
#
#
# @app.route("/about.html")
# def about():
#     return render_template('./about.html')
#
#
# @app.route("/works.html")
# def works():
#     return render_template('./works.html')
#
#
# @app.route("/contact.html")
# def contact():
#     return render_template("./contact.html")
#
#
# @app.route("/components.html")
# def components():
#     return render_template("./components.html")
